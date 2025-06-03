import io
import logging
import os
from typing import List

import fitz
from PIL import Image

log = logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_images(pdf_path: str, output_dir: str, discarded_pages: List[int]):
    doc = fitz.open(pdf_path)
    os.makedirs(output_dir, exist_ok=True)
    image_count = 0

    for page_index, page in enumerate(doc):
        if page_index in discarded_pages:
            continue
        images = page.get_images(full=True)
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image = Image.open(io.BytesIO(image_bytes))

            image_path = os.path.join(output_dir, f"page{page_index + 1}_img{img_index + 1}.{image_ext}")  # noqa: E501
            image.save(image_path)
            image_count += 1

    doc.close()
    return image_count


if __name__ == "__main__":
    pdf_file = "scripts/pdfs/esa2021.pdf"
    output_folder_name = "ESA/2021"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    assets_dir = os.path.join(project_root, "public")
    output_folder = os.path.join(assets_dir, output_folder_name)

    discarded_pages = [0, 24, 25, 26]

    try:
        total = get_images(
            pdf_path=pdf_file,
            output_dir=output_folder,
            discarded_pages=discarded_pages
        )
        logger.info(f"Successfully extracted {total} images")

    except FileNotFoundError:
        logger.error(f"PDF file not found: {pdf_file}")
    except Exception as e:
        logger.error(f"Error extracting images: {e}")
