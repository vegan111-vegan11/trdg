import random as rnd
from typing import Tuple
from PIL import Image, ImageColor, ImageDraw, ImageFilter, ImageFont

from trdg.utils import get_text_width, get_text_height

# Thai Unicode reference: https://jrgraphix.net/r/Unicode/0E00-0E7F
TH_TONE_MARKS = [
    "0xe47",
    "0xe48",
    "0xe49",
    "0xe4a",
    "0xe4b",
    "0xe4c",
    "0xe4d",
    "0xe4e",
]
TH_UNDER_VOWELS = ["0xe38", "0xe39", "\0xe3A"]
TH_UPPER_VOWELS = ["0xe31", "0xe34", "0xe35", "0xe36", "0xe37"]


def generate(
    text: str,
    font: str,
    text_color: str,
    font_size: int,
    orientation: int,
    space_width: int,
    character_spacing: int,
    fit: bool,
    word_split: bool,
    stroke_width: int = 0,
    stroke_fill: str = "#282828",
) -> Tuple:
    #stroke_width = 1
    if orientation == 0:

        # print(f'computer_text_generator.py text : {text}')
        # print(f'computer_text_generator.py font_size : {font_size}')
        # print(f'computer_text_generator.py space_width : {space_width}')
        # print(f'computer_text_generator.py character_spacing : {character_spacing}')
        #
        # print(f'computer_text_generator.py fit : {fit}')
        # print(f'computer_text_generator.py word_split : {word_split}')
        # print(f'computer_text_generator.py stroke_width : {stroke_width}')
        # print(f'computer_text_generator.py stroke_fill : {stroke_fill}')

        return _generate_horizontal_text(
            text,
            font,
            text_color,
            font_size,
            space_width,
            character_spacing,
            fit,
            word_split,
            stroke_width,
            stroke_fill,
        )
    elif orientation == 1:
        return _generate_vertical_text(
            text,
            font,
            text_color,
            font_size,
            space_width,
            character_spacing,
            fit,
            stroke_width,
            stroke_fill,
        )
    else:
        raise ValueError("Unknown orientation " + str(orientation))


def _compute_character_width(image_font: ImageFont, character: str) -> int:
    if len(character) == 1 and (
        "{0:#x}".format(ord(character))
        in TH_TONE_MARKS + TH_UNDER_VOWELS + TH_UNDER_VOWELS + TH_UPPER_VOWELS
    ):
        return 0
    # Casting as int to preserve the old behavior
    return round(image_font.getlength(character))


def _generate_horizontal_text(
    text: str,
    font: str,
    text_color: str,
    font_size: int,
    space_width: int,
    character_spacing: int,
    fit: bool,
    word_split: bool,
    stroke_width: int = 0,
    stroke_fill: str = "#282828",
) -> Tuple:
    image_font = ImageFont.truetype(font=font, size=font_size)
    # print(f'computer_text_generator.py _generate_horizontal_text image_font : {image_font}')
    # print(
    #     f'computer_text_generator.py _generate_horizontal_text font_size : {font_size}')
    # print(
    #     f'computer_text_generator.py _generate_horizontal_text space_width : {space_width}')

    space_width = int(get_text_width(image_font, " ") * space_width)
    # print(
    #     f'computer_text_generator.py _generate_horizontal_text space_width 변경후 : {space_width}')


    if word_split:
        splitted_text = []
        for w in text.split(" "):
            splitted_text.append(w)
            splitted_text.append(" ")
        splitted_text.pop()
    else:
        splitted_text = text

    #print(f'computer_text_generator.py splitted_text : {splitted_text}')

    piece_widths = [
        _compute_character_width(image_font, p) if p != " " else space_width
        for p in splitted_text
    ]
    text_width = sum(piece_widths)
    #print(f'computer_text_generator.py text_width : {text_width}')

    if not word_split:
        text_width += character_spacing * (len(text) - 1)

    #text_height = max([get_text_height(image_font, p) for p in splitted_text])
    # 수정된 코드
    #text_height = max([image_font.getsize(p)[1] for p in splitted_text])
    # 변경된 코드


    for p in splitted_text:
        pass
        # bottom_y = image_font.getbbox(p)[3]
        # print(
        #     f'computer_text_generator.py image_font.getbbox(p)[3] : {image_font.getbbox(p)[3]}')
        # print(
        #     f'computer_text_generator.py image_font.getbbox(p)[2] : {image_font.getbbox(p)[2]}')
        # print(
        #     f'computer_text_generator.py image_font.getbbox(p)[1] : {image_font.getbbox(p)[1]}')



    #로그용_주석처리_print(f'computer_text_generator.py text_width : {text_width}')

    #text_height = max([image_font.getbbox(p)[3] - image_font.getbbox(p)[1] for p in splitted_text])
    text_height = max([image_font.getbbox(p)[3] - image_font.getbbox(p)[1] + 50 for p in splitted_text])
    #로그용_주석처리_print(f'computer_text_generator.py text_height : {text_height}')

    # 여분의 여백 추가
    top_padding = 50  # 상단 여백 크기를 조절하십시오 (원하는 크기로 변경 가능)
    top_padding = 10  # 상단 여백 크기를 조절하십시오 (원하는 크기로 변경 가능)
    text_height += top_padding

    txt_img = Image.new("RGBA", (text_width, text_height), (0, 0, 0, 0))
    txt_mask = Image.new("RGB", (text_width, text_height), (0, 0, 0))
    # 알파채널 추가
    #txt_mask = Image.new("RGBA", (text_width, text_height), (0, 0, 0, 0))

    txt_img_draw = ImageDraw.Draw(txt_img)
    txt_mask_draw = ImageDraw.Draw(txt_mask, mode="RGB")
    txt_mask_draw.fontmode = "1"

    colors = [ImageColor.getrgb(c) for c in text_color.split(",")]
    c1, c2 = colors[0], colors[-1]

    #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!computer_text_generator.py  colors : {colors}')


    fill = (
        rnd.randint(min(c1[0], c2[0]), max(c1[0], c2[0])),
        rnd.randint(min(c1[1], c2[1]), max(c1[1], c2[1])),
        rnd.randint(min(c1[2], c2[2]), max(c1[2], c2[2])),
    )

    stroke_colors = [ImageColor.getrgb(c) for c in stroke_fill.split(",")]
    stroke_c1, stroke_c2 = stroke_colors[0], stroke_colors[-1]
    #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!computer_text_generator.py  stroke_colors : {stroke_colors}')
    #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!computer_text_generator.py  stroke_c1 : {stroke_c1}')

    stroke_fill = (
        rnd.randint(min(stroke_c1[0], stroke_c2[0]), max(stroke_c1[0], stroke_c2[0])),
        rnd.randint(min(stroke_c1[1], stroke_c2[1]), max(stroke_c1[1], stroke_c2[1])),
        rnd.randint(min(stroke_c1[2], stroke_c2[2]), max(stroke_c1[2], stroke_c2[2])),
    )


   #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!computer_text_generator.py  stroke_fill : {stroke_fill}')

    for i, p in enumerate(splitted_text):
        # print(f'computer_text_generator.py i : {i}')
        # print(f'computer_text_generator.py p : {p}')

        # 글자 색상 (하얀색)
        text_color = (255, 255, 255)

        txt_img_draw.text(
            (sum(piece_widths[0:i]) + i * character_spacing * int(not word_split), 0),
            p,
            #fill=fill,
            fill=text_color,
            font=image_font,
            stroke_width=stroke_width,
            stroke_fill=stroke_fill,
        )
        txt_mask_draw.text(
            (sum(piece_widths[0:i]) + i * character_spacing * int(not word_split), 0),
            p,
            fill=((i + 1) // (255 * 255), (i + 1) // 255, (i + 1) % 255),
            font=image_font,
            stroke_width=stroke_width,
            stroke_fill=stroke_fill,
        )


    # #경로 설정
    # save_path = r"C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\out3\th\12-01\NotoSansThaiLooped-Black\\"
    # # 이미지 저장
    # txt_img_save_path = f"{save_path}_generate_horizontal_text_{1}.png"
    # txt_img.save(txt_img_save_path)
    #
    # # 통계 출력
    # print(f"computer_text_generator.py txt_img 이미지 저장 완료: {txt_img_save_path}")
    #
    # print(f"computer_text_generator.py txt_img.getbbox(): {txt_img.getbbox()}")
    #
    # txt_img_crop = txt_img.crop(txt_img.getbbox())
    # txt_mask_crop = txt_mask.crop(txt_img.getbbox())
    #
    # # 경로 설정
    # save_path = r"C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\out3\th\12-01\NotoSansThaiLooped-Black\\"
    # # 이미지 저장
    # txt_img_crop_save_path = f"{save_path}_txt_img_crop_{1}.png"
    # txt_img_crop.save(txt_img_crop_save_path)
    #
    # # 통계 출력
    # print(f"computer_text_generator.py txt_img 이미지 저장 완료: {txt_img_crop_save_path}")
    #
    # # 경로 설정
    # save_path = r"C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\out3\th\12-01\NotoSansThaiLooped-Black\\"
    # # 이미지 저장
    # txt_mask_crop_save_path = f"{save_path}_txt_mask_crop_{1}.png"
    # txt_mask_crop.save(txt_mask_crop_save_path)
    #
    # # 통계 출력
    # print(f"computer_text_generator.py txt_mask 이미지 저장 완료: {txt_mask_crop_save_path}")

    #print(f'computer_text_generator.py fit : {fit}')
    fit = True
    #print(f'computer_text_generator.py fit True 로 변경후 : {fit}')

    if fit:
        return txt_img.crop(txt_img.getbbox()), txt_mask.crop(txt_img.getbbox())
    else:
        return txt_img, txt_mask


def _generate_vertical_text(
    text: str,
    font: str,
    text_color: str,
    font_size: int,
    space_width: int,
    character_spacing: int,
    fit: bool,
    stroke_width: int = 0,
    stroke_fill: str = "#282828",
) -> Tuple:
    image_font = ImageFont.truetype(font=font, size=font_size)
    # 수정된 코드
    #image_font = ImageFont.truetype(args.font, size=text_size)
    #로그용_주석처리_print( f'computer_text_generator.py _generate_vertical_text image_font : {image_font}')
    #로그용_주석처리_print(  f'computer_text_generator.py _generate_vertical_text font : {font}')

    space_height = int(get_text_height(image_font, " ") * space_width)

    char_heights = [
        get_text_height(image_font, c) if c != " " else space_height for c in text
    ]
    text_width = max([get_text_width(image_font, c) for c in text])
    text_height = sum(char_heights) + character_spacing * len(text)

    txt_img = Image.new("RGBA", (text_width, text_height), (0, 0, 0, 0))
    txt_mask = Image.new("RGBA", (text_width, text_height), (0, 0, 0, 0))

    txt_img_draw = ImageDraw.Draw(txt_img)
    txt_mask_draw = ImageDraw.Draw(txt_mask)
    txt_mask_draw.fontmode = "1"

    colors = [ImageColor.getrgb(c) for c in text_color.split(",")]
    c1, c2 = colors[0], colors[-1]

    fill = (
        rnd.randint(c1[0], c2[0]),
        rnd.randint(c1[1], c2[1]),
        rnd.randint(c1[2], c2[2]),
    )

    stroke_colors = [ImageColor.getrgb(c) for c in stroke_fill.split(",")]
    stroke_c1, stroke_c2 = stroke_colors[0], stroke_colors[-1]

    stroke_fill = (
        rnd.randint(stroke_c1[0], stroke_c2[0]),
        rnd.randint(stroke_c1[1], stroke_c2[1]),
        rnd.randint(stroke_c1[2], stroke_c2[2]),
    )

    for i, c in enumerate(text):
        txt_img_draw.text(
            (0, sum(char_heights[0:i]) + i * character_spacing),
            c,
            fill=fill,
            font=image_font,
            stroke_width=stroke_width,
            stroke_fill=stroke_fill,
        )
        txt_mask_draw.text(
            (0, sum(char_heights[0:i]) + i * character_spacing),
            c,
            fill=((i + 1) // (255 * 255), (i + 1) // 255, (i + 1) % 255),
            font=image_font,
            stroke_width=stroke_width,
            stroke_fill=stroke_fill,
        )

    if fit:
        return txt_img.crop(txt_img.getbbox()), txt_mask.crop(txt_img.getbbox())
    else:
        return txt_img, txt_mask
