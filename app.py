
# Image convertion
import cairosvg

# Image combiner
from PIL import Image # 

images_url = [""] # insert the images url that you want to combine

class PDFCombiner:
    def __init__(self, url) -> None:    
        pass

    # 2nd step: converting received images into png
    def convert_png(self):
        for image_url in images_url:
            cairosvg.svg2png(url=f'./result/{image_url}.svg', write_to=f'./result/{image_url}.png')

    # 3rd step: combining converted images into pdf
    def combine_pdf(self):
        images = []
        for image_url in images_url:
            image = Image.open(f'./result/{image_url}.png')
            image = image.convert('RGB')
            images.append(image)
        # Remember to add images[1:] to exclude first image. Otherwise 1st image duplicates.
        images[0].save(f'./result/file.pdf', save_all=True, append_images=images[1:])

def main():
    pdf_combiner = PDFCombiner()
    pdf_combiner.convert_png()
    pdf_combiner.combine_pdf()
    pass

if __name__ == '__main__':
    main()