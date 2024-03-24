import datetime
import io
import os
import random
from MemeGenerator.GeneratorInterface import GeneratorInterface
from PIL import Image, ImageOps, ImageDraw
from MemeGenerator.GeneratorException import GeneratorException


class MemeEngine(GeneratorInterface):
    """TODO: add doc

    Args:
        GeneratorInterface (_type_): _description_
    """

    datetime_format = '%d-%m-%y-%H-%M-%S'

    def __init__(self, output_dir: str):
        self.output_dir = output_dir

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

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
                    [resized_im.height/random.randint(2, 3), resized_im.width/random.randint(2, 3)])

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

                file, _ = os.path.splitext(img_path)

                meme_out_file = f'{self.output_dir}/{file.split(
                    '/')[-1]}-{datetime.datetime.now().strftime(self.datetime_format)}.jpeg'

                resized_im.save(meme_out_file)

                return meme_out_file
        except OSError as err:
            print('Unable to open the image using the provided path.')
            print(err)
            raise
        except Exception as err:
            print(err)
            print('An exception occurred')
            raise

    @staticmethod
    def reading_from_binary(file) -> str | None:
        """Reads an image from a binary format file and save as an Jpeg image file.

        Returns:
            str: Saved image's path.
        """
        try:
            img_path = f'{datetime.datetime.now().strftime(
                '%d-%m-%y-%H-%M-%S')}.jpeg'

            with Image.open(io.BytesIO(file)) as im:
                im.save(img_path)

            return img_path
        except Exception as err:
            print(err)

        return None
