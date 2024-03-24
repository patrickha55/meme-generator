import os
import random
from GeneratorInterface import GeneratorInterface
from PIL import Image, ImageOps, ImageDraw
from GeneratorException import GeneratorException


class ImageCaptioner(GeneratorInterface):

    def __init__(self, out_file: str):
        self.out_file = out_file

    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
        try:
            if not os.path.isfile(img_path):
                raise GeneratorException('Invalid image path.')
            if width > 500:
                raise GeneratorException(
                    'Image width exceeded. Maximum width of 500 is allowed.')

            size = tuple([500, width])

            with Image.open(img_path) as im:
                resized_im = ImageOps.contain(im, size)

                text_size = tuple(
                    [resized_im.height/random.randint(2, 4), resized_im.width/random.randint(2, 4)])

                draw = ImageDraw.Draw(resized_im)
                draw.text(text_size,
                          f'{text} \n- {author}',
                          align='center',
                          anchor='ms',
                          fill='white',
                          stroke_width=2,
                          stroke_fill='black',
                          font_size=20
                          )

                resized_im.save(f'{self.out_file}.jpeg')
        except OSError as err:
            print('Unable to open the image using the provided path.')
            print(err)
            raise
        except Exception as err:
            print(err)
            print('An exception occurred')
            raise
