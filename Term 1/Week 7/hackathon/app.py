
import os
import tempfile

import streamlit as st
from PIL import Image, ImageOps
from inference_sdk import InferenceHTTPClient, InferenceConfiguration


# CONFIGURATION
MODEL_ID = (
    "joels-workspace-pbln3/"
    "bird-species-classification-jomnp-rj55n-1-"
    "vit_small_patch16_dinov3.lvd1689m-t1"
)

API_KEY = os.getenv("ROBOFLOW_API_KEY")

st.set_page_config(
    page_title="BirdID",
    page_icon="🐦",
    layout="centered",
)

st.title("🐦 BirdID")
st.subheader("AI-powered bird species identification")
st.write(
    "Upload a bird photo and let our AI model "
    "predict its species."
)

if not API_KEY:
    st.error(
        "Roboflow API key not found. Please configure "
        "the ROBOFLOW_API_KEY environment variable "
        "and restart the app."
    )
    st.stop()

uploaded_file = st.file_uploader(
    "Upload a bird photo",
    type=["jpg", "jpeg", "png", "webp"],
)

if uploaded_file is not None:
    try:
        image = ImageOps.exif_transpose(
            Image.open(uploaded_file)
        ).convert("RGB")

        st.image(
            image,
            caption="Selected image",
            use_container_width=True,
        )

        if st.button("🔍 Identify Bird", type="primary"):
            with st.spinner("Analyzing image..."):
                client = InferenceHTTPClient(
                    api_url="https://serverless.roboflow.com",
                    api_key=API_KEY,
                )

                with tempfile.NamedTemporaryFile(
                    suffix=".jpg", delete=False
                ) as temp_file:
                    image.save(temp_file.name, format="JPEG")
                    image_path = temp_file.name

                try:
                    with client.use_configuration(
                        InferenceConfiguration(
                            confidence_threshold=0.0,
                            api_key_transport="header",
                        )
                    ):
                        result = client.infer(
                            image_path,
                            model_id=MODEL_ID,
                        )
                finally:
                    if os.path.exists(image_path):
                        os.remove(image_path)

            predictions = result.get("predictions", [])

            if not predictions:
                st.warning(
                    "No predictions were returned. "
                    "Please try another photo."
                )
            else:
                predictions = sorted(
                    predictions,
                    key=lambda item: item.get("confidence", 0),
                    reverse=True,
                )

                best = predictions[0]
                species = best.get("class", "Unknown species")
                confidence = best.get("confidence", 0) * 100

                st.success("Analysis complete")
                st.markdown("### Identification result")
                st.subheader(f"🐦 {species}")
                st.progress(min(int(confidence), 100))
                st.write(f"Model confidence: **{confidence:.2f}%**")

                if confidence < 30:
                    st.warning(
                        "The model has low confidence in this "
                        "prediction. The identification may be incorrect."
                    )
                elif confidence < 60:
                    st.info(
                        "This identification is only a prediction. "
                        "Please verify it with another source."
                    )

                st.markdown("### Other possible species")

                for prediction in predictions[1:5]:
                    name = prediction.get("class", "Unknown")
                    score = prediction.get("confidence", 0) * 100
                    st.write(f"**{name}** — {score:.2f}%")

    except Exception as error:
        st.error("An error occurred while analyzing the image.")
        st.code(str(error))

st.divider()
st.caption(
    "BirdID · An educational AI project for bird species identification."
)
