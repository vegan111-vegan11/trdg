"""
Utility functions
"""

import os
import re
import unicodedata
from typing import List, Tuple

import numpy as np
from PIL import Image, ImageDraw, ImageFont


def load_dict(path: str) -> List[str]:
    """Read the dictionnary file and returns all words in it."""

    word_dict = []
    with open(
        path,
        "r",
        encoding="utf8",
        errors="ignore",
    ) as d:
        word_dict = [l for l in d.read().splitlines() if len(l) > 0]

    return word_dict


def load_fonts(lang: str) -> List[str]:
    """Load all fonts in the fonts directories"""

    if lang in os.listdir(os.path.join(os.path.dirname(__file__), "fonts")):
        return [
            os.path.join(os.path.dirname(__file__), "fonts/{}".format(lang), font)
            for font in os.listdir(
                os.path.join(os.path.dirname(__file__), "fonts/{}".format(lang))
            )
        ]
    else:
        return [
            os.path.join(os.path.dirname(__file__), "fonts/latin", font)
            for font in os.listdir(
                os.path.join(os.path.dirname(__file__), "fonts/latin")
            )
        ]


def mask_to_bboxes(mask: List[Tuple[int, int, int, int]], tess: bool = False):
    """Process the mask and turns it into a list of AABB bounding boxes"""

    mask_arr = np.array(mask)
    #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py mask_arr : {mask_arr}')

    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py mask : {mask}')

    bboxes = []

    i = 0
    space_thresh = 1
    while True:
        try:
            # 원본
            color_tuple = ((i + 1) // (255 * 255), (i + 1) // 255, (i + 1) % 255)
            #color_tuple = ((i + 1) // (255 * 255), (i + 1) // 255, (i + 1) % 255, 255)
            #color_tuple = (221, 221, 221, 255)

            #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py color_tuple : {color_tuple}')

            letter = np.where(np.all(mask_arr == color_tuple, axis=-1))
            np_all = np.all(mask_arr == color_tuple, axis=-1)
            np_where = np.where(np_all)

            # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py mask_arr.shape : {mask_arr.shape}')
            # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py letter : {letter}')
            # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py np_all : {np_all}')
            # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py np_where  : {np_where = }')
            #
            # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py space_thresh : {space_thresh}')

            if space_thresh == 0 and letter:
                x1 = min(bboxes[-1][2] + 1, np.min(letter[1]) - 1)
                #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py x1 : {x1}')
                #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py letter[1] : {letter[1]}')

                y1 = (
                    min(bboxes[-1][3] + 1, np.min(letter[0]) - 1)
                    if not tess
                    else min(
                        mask_arr.shape[0] - np.min(letter[0]) + 2, bboxes[-1][1] - 1
                    )
                )
                x2 = max(bboxes[-1][2] + 1, np.min(letter[1]) - 2)
                y2 = (
                    max(bboxes[-1][3] + 1, np.min(letter[0]) - 2)
                    if not tess
                    else max(
                        mask_arr.shape[0] - np.min(letter[0]) + 2, bboxes[-1][1] - 1
                    )
                )
                bboxes.append((x1, y1, x2, y2))
                space_thresh += 1

            #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py bboxes1 : {bboxes}')

            bboxes.append(
                (
                    max(0, np.min(letter[1]) - 1),
                    max(0, np.min(letter[0]) - 1)
                    if not tess
                    else max(0, mask_arr.shape[0] - np.max(letter[0]) - 1),
                    min(mask_arr.shape[1] - 1, np.max(letter[1]) + 1),
                    min(mask_arr.shape[0] - 1, np.max(letter[0]) + 1)
                    if not tess
                    else min(
                        mask_arr.shape[0] - 1, mask_arr.shape[0] - np.min(letter[0]) + 1
                    ),
                )
            )

            #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py bboxes2 : {bboxes}')

            i += 1
        except Exception as ex:
            if space_thresh == 0:
                break
            space_thresh -= 1
            i += 1

    #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py bboxes 최종 : {bboxes}')


    return bboxes


def draw_bounding_boxes(
    img: Image, bboxes: List[Tuple[int, int, int, int]], color: str = "green"
) -> None:
    d = ImageDraw.Draw(img)

    for bbox in bboxes:
        d.rectangle(bbox, outline=color)


def make_filename_valid(value: str, allow_unicode: bool = False) -> str:
    """
    Code adapted from: https://docs.djangoproject.com/en/4.0/_modules/django/utils/text/#slugify

    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    value = re.sub(r"[^\w\s-]", "", value)

    # Image names will be shortened to avoid exceeding the max filename length
    return value[:200]


def get_text_width(image_font: ImageFont, text: str) -> int:
    """
    Get the width of a string when rendered with a given font
    """
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py get_text_width image_font : {image_font}')

    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py get_text_width text : {text}')
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py get_text_width return image_font.getlength(text) : {image_font.getlength(text)}')

    return round(image_font.getlength(text))


def get_text_height(image_font: ImageFont, text: str) -> int:
    """
    Get the width of a string when rendered with a given font
    """
    #return image_font.getsize(text)[1]
    # 변경된 코드
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py image_font.getbbox(text)[3] : {image_font.getbbox(text)[3]}')
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py image_font.getbbox(text)[1] : {image_font.getbbox(text)[1]}')
    print(
        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py get_text_height return : {image_font.getbbox(text)[3] - image_font.getbbox(text)[1]}')
    return image_font.getbbox(text)[3] - image_font.getbbox(text)[1]
"""
Utility functions
"""

import os
import re
import unicodedata
from typing import List, Tuple

import numpy as np
from PIL import Image, ImageDraw, ImageFont


def load_dict(path: str) -> List[str]:
    """Read the dictionnary file and returns all words in it."""

    word_dict = []
    with open(
        path,
        "r",
        encoding="utf8",
        errors="ignore",
    ) as d:
        word_dict = [l for l in d.read().splitlines() if len(l) > 0]

    return word_dict


def load_fonts(lang: str) -> List[str]:
    """Load all fonts in the fonts directories"""

    if lang in os.listdir(os.path.join(os.path.dirname(__file__), "fonts")):
        return [
            os.path.join(os.path.dirname(__file__), "fonts/{}".format(lang), font)
            for font in os.listdir(
                os.path.join(os.path.dirname(__file__), "fonts/{}".format(lang))
            )
        ]
    else:
        return [
            os.path.join(os.path.dirname(__file__), "fonts/latin", font)
            for font in os.listdir(
                os.path.join(os.path.dirname(__file__), "fonts/latin")
            )
        ]


def mask_to_bboxes(mask: List[Tuple[int, int, int, int]], tess: bool = False):
    """Process the mask and turns it into a list of AABB bounding boxes"""

    mask_arr = np.array(mask)
    #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py mask_arr : {mask_arr}')

    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py mask : {mask}')

    bboxes = []

    i = 0
    space_thresh = 1
    while True:
        try:
            # 원본
            color_tuple = ((i + 1) // (255 * 255), (i + 1) // 255, (i + 1) % 255)
            #color_tuple = ((i + 1) // (255 * 255), (i + 1) // 255, (i + 1) % 255, 255)
            #color_tuple = (221, 221, 221, 255)

            #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py color_tuple : {color_tuple}')

            letter = np.where(np.all(mask_arr == color_tuple, axis=-1))
            np_all = np.all(mask_arr == color_tuple, axis=-1)
            np_where = np.where(np_all)

            # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py mask_arr.shape : {mask_arr.shape}')
            # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py letter : {letter}')
            # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py np_all : {np_all}')
            # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py np_where  : {np_where = }')
            #
            # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py space_thresh : {space_thresh}')

            if space_thresh == 0 and letter:
                x1 = min(bboxes[-1][2] + 1, np.min(letter[1]) - 1)
                #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py x1 : {x1}')
                #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py letter[1] : {letter[1]}')

                y1 = (
                    min(bboxes[-1][3] + 1, np.min(letter[0]) - 1)
                    if not tess
                    else min(
                        mask_arr.shape[0] - np.min(letter[0]) + 2, bboxes[-1][1] - 1
                    )
                )
                x2 = max(bboxes[-1][2] + 1, np.min(letter[1]) - 2)
                y2 = (
                    max(bboxes[-1][3] + 1, np.min(letter[0]) - 2)
                    if not tess
                    else max(
                        mask_arr.shape[0] - np.min(letter[0]) + 2, bboxes[-1][1] - 1
                    )
                )
                bboxes.append((x1, y1, x2, y2))
                space_thresh += 1

            #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py bboxes1 : {bboxes}')

            bboxes.append(
                (
                    max(0, np.min(letter[1]) - 1),
                    max(0, np.min(letter[0]) - 1)
                    if not tess
                    else max(0, mask_arr.shape[0] - np.max(letter[0]) - 1),
                    min(mask_arr.shape[1] - 1, np.max(letter[1]) + 1),
                    min(mask_arr.shape[0] - 1, np.max(letter[0]) + 1)
                    if not tess
                    else min(
                        mask_arr.shape[0] - 1, mask_arr.shape[0] - np.min(letter[0]) + 1
                    ),
                )
            )

            #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py bboxes2 : {bboxes}')

            i += 1
        except Exception as ex:
            if space_thresh == 0:
                break
            space_thresh -= 1
            i += 1

    #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py bboxes 최종 : {bboxes}')


    return bboxes


def draw_bounding_boxes(
    img: Image, bboxes: List[Tuple[int, int, int, int]], color: str = "green"
) -> None:
    d = ImageDraw.Draw(img)

    for bbox in bboxes:
        d.rectangle(bbox, outline=color)


def make_filename_valid(value: str, allow_unicode: bool = False) -> str:
    """
    Code adapted from: https://docs.djangoproject.com/en/4.0/_modules/django/utils/text/#slugify

    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    value = re.sub(r"[^\w\s-]", "", value)

    # Image names will be shortened to avoid exceeding the max filename length
    return value[:200]


def get_text_width(image_font: ImageFont, text: str) -> int:
    """
    Get the width of a string when rendered with a given font
    """
    #로그용 주석처리_print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py get_text_width image_font : {image_font}')

    #로그용 주석처리_print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py get_text_width text : {text}')
    #로그용 주석처리_print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py get_text_width return image_font.getlength(text) : {image_font.getlength(text)}')

    return round(image_font.getlength(text))


def get_text_height(image_font: ImageFont, text: str) -> int:
    """
    Get the width of a string when rendered with a given font
    """
    #return image_font.getsize(text)[1]
    # 변경된 코드
    #로그용 주석처리_print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py image_font.getbbox(text)[3] : {image_font.getbbox(text)[3]}')
    #로그용 주석처리_print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py image_font.getbbox(text)[1] : {image_font.getbbox(text)[1]}')
    #로그용 주석처리_print( f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!utils.py get_text_height return : {image_font.getbbox(text)[3] - image_font.getbbox(text)[1]}')
    return image_font.getbbox(text)[3] - image_font.getbbox(text)[1]
