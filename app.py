import streamlit as st
import torch
import torch.nn as nn
from sentence_transformers import SentenceTransformer

# Define the model
class News(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(in_features=384, out_features=128)
        self.layer2 = nn.Linear(in_features=128, out_features=64)
        self.layer3 = nn.Linear(in_features=64, out_features=1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.relu(self.layer2(x))
        x = self.layer3(x)
        return x

# Load model weights
modell2 = News()
modell2.load_state_dict(torch.load("Fake_News_Detection.pth", map_location=torch.device("cpu")))
modell2.eval()

# Load sentence transformer
model = SentenceTransformer("all-MiniLM-L6-v2")

# Streamlit UI
st.title("📰 Fake News Detector")

user = st.text_area("Enter a news headline:")

if st.button("Check"):
    if user.strip() == "":
        st.warning("Please enter a valid headline.")
    else:
        user_embed = model.encode([user])
        usse = torch.tensor(user_embed, dtype=torch.float32)

        with torch.inference_mode():
            pred = modell2(usse)
            pred_labels = torch.sigmoid(pred)
            prob=torch.round(pred_labels)
            st.subheader("Prediction:")
            st.write(f"Raw Prediction Value: {pred.item():.4f}")
            st.write(f"Confidence (sigmoid): {torch.sigmoid(pred).item()}%")
            st.write(f"Prediction Value: {prob.item():.4f}")

            if pred_labels.item() < 0.3:
                st.error("❌ Fake News")
            elif 0.3 < pred_labels < 0.7 :
                st.success(f"Maybe, {pred_labels}")
            else:
                st.success("✅ Real News")
