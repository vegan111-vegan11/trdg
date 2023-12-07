import argparse
import errno
import os
import sys

print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!sys.path ( ocr2_2 의 Lib 의 site-packages 추가전 : {sys.path}')

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!os.path.join(os.path.dirname(__file__), "..") 블라블라 : {os.path.join(os.path.dirname(__file__), "..")}')
print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!os.path.dirname(__file__) 블라블라 : {os.path.dirname(__file__)}')
print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!sys.path ( ocr2_2 의 Lib 의 site-packages 추가후 : {sys.path}')

import random as rnd
import string
import sys
from multiprocessing import Pool

from tqdm import tqdm
import os
print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py FakeTextDataGenerator 임포트 전  os: {os}')

from trdg.data_generator import FakeTextDataGenerator

print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py 어디서 임포트 해오는 거임?? FakeTextDataGenerator : {FakeTextDataGenerator}')
print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py os.getcwd()1 : {os.getcwd()}')
print(f'=============================run.py FakeTextDataGenerator 임포트 완료 FakeTextDataGenerator1 : {FakeTextDataGenerator}')

# run.py 파일 내에서
import sys

print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!sys.path ( yjh 의 Lib 의 site-packages 추가전 : {sys.path}')

sys.path.append(r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator')

print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!sys.path ( yjh 의 Lib 의 site-packages 추가후 : {sys.path}')

from trdg.data_generator import FakeTextDataGenerator
print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py run.py 파일 내에서 임포트 하도록 수정함 ( yjh ) FakeTextDataGenerator : {FakeTextDataGenerator}')
print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py run.py 파일 내에서 임포트 하도록 수정함 ( yjh ) os.getcwd()1 : {os.getcwd()}')
print(f'=============================run.py run.py 파일 내에서 임포트 하도록 수정함 ( yjh ) FakeTextDataGenerator 임포트 완료 FakeTextDataGenerator : {FakeTextDataGenerator}')


from trdg.string_generator import (
    create_strings_from_dict,
    create_strings_from_file,
    create_strings_from_wikipedia,
    create_strings_randomly,
)

print(f'string_generator 임포트 완료 create_strings_from_dict 함수1 : {create_strings_from_dict}')

import sys

#print("Python Path:", sys.path)
import sys
sys.path.append(os.getcwd())

print(f'sys 임포트 완료 sys1 : {sys}')
# from trdg.data_generator import FakeTextDataGenerator
# print(f'FakeTextDataGenerator 임포트 완료 FakeTextDataGenerator2 : {FakeTextDataGenerator}')
# print(f'FakeTextDataGenerator 임포트 완료 FakeTextDataGenerator3.generate_from_tuple() : {FakeTextDataGenerator.generate_from_tuple }')
#
# generator_instance = FakeTextDataGenerator()
# print(
#         f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py generator_instance FakeTextDataGenerator 클래스 객체 생성 : {generator_instance}')
# print(
#         f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py generator_instance.generate_from_tuple 함수 호출 : {generator_instance.generate_from_tuple }')



#
# from trdg.data_generator import (
#     generate_from_tuple
# )
#print(f'FakeTextDataGenerator 임포트 완료 generate_from_tuple : {generate_from_tuple}')

from trdg.utils import load_dict, load_fonts
#import os
from datetime import datetime
print(f' 임포트 완료 datetime : {datetime}')

# 현재 환경 변수 출력
print("Current Environment Variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")

# 디버그 모드에서의 환경 변수와 명령줄에서의 환경 변수 비교
debug_mode = os.environ.get('PYCHARM_HOSTED') == '1'

if debug_mode:
    print("Running in PyCharm Debug Mode")
    # 디버그 모드에서 추가로 필요한 작업 수행
else:
    print("Running in Command Line Mode")
    # 명령줄 모드에서 추가로 필요한 작업 수행

import sys
sys.path.append(r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator')
print(f' sys.path 에  TextRecognitionDataGenerator 어펜드 완료 sys.path : {sys.path}')

# class Args:
#     def __init__(self, index: int, text: str, font: str, out_dir: str, size: int,
#                  extension: str, skewing_angle: int, random_skew: bool,
#                  blur: int, random_blur: bool, background_type: int,
#                  distorsion_type: int, distorsion_orientation: int,
#                  is_handwritten: bool, name_format: int, width: int,
#                  alignment: int, text_color: str, orientation: int,
#                  space_width: int, character_spacing: int, margins: int,
#                  fit: bool, output_mask: bool, word_split: bool,
#                  image_dir: str, stroke_width: int = 0,
#                  stroke_fill: str = "#282828", image_mode: str = "RGB",
#                  output_bboxes: int = 0):
#
#         self.index = index
#         self.text = text
#         self.font = font
#         self.out_dir = out_dir
#         self.size = size
#         self.extension = extension
#         self.skewing_angle = skewing_angle
#         self.random_skew = random_skew
#         self.blur = blur
#         self.random_blur = random_blur
#         self.background_type = background_type
#         self.distorsion_type = distorsion_type
#         self.distorsion_orientation = distorsion_orientation
#         self.is_handwritten = is_handwritten
#         self.name_format = name_format
#         self.width = width
#         self.alignment = alignment
#         self.text_color = text_color
#         self.orientation = orientation
#         self.space_width = space_width
#         self.character_spacing = character_spacing
#         self.margins = (margins, margins, margins, margins) if isinstance(margins, int) else margins
#         self.fit = fit
#         self.output_mask = output_mask
#         self.word_split = word_split
#         self.image_dir = image_dir
#         self.stroke_width = stroke_width
#         self.stroke_fill = stroke_fill
#         self.image_mode = image_mode
#         self.output_bboxes = output_bboxes


def margins(margin):
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py  margins 함수 margin : {margin }')
    margins = margin.split(",")
    if len(margins) == 1:
        return [int(margins[0])] * 4
    return [int(m) for m in margins]


def parse_arguments():
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py  parse_arguments 함수  ')
    """
    Parse the command line arguments of the program.
    """

    parser = argparse.ArgumentParser(
        description="Generate synthetic text data for text recognition."
    )
    parser.add_argument(
        "--output_dir", type=str, nargs="?", help="The output directory", default="out/"
    )
    parser.add_argument(
        "-i",
        "--input_file",
        type=str,
        nargs="?",
        help="When set, this argument uses a specified text file as source for the text",
        default="",
    )
    parser.add_argument(
        "-l",
        "--language",
        type=str,
        nargs="?",
        help="The language to use, should be fr (French), en (English), es (Spanish), de (German), ar (Arabic), cn (Chinese), ja (Japanese) or hi (Hindi)",
        default="en",
    )
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        nargs="?",
        help="The number of images to be created.",
        #required=True,
        required=False,
    )
    parser.add_argument(
        "-rs",
        "--random_sequences",
        action="store_true",
        help="Use random sequences as the source text for the generation. Set '-let','-num','-sym' to use letters/numbers/symbols. If none specified, using all three.",
        default=False,
    )
    parser.add_argument(
        "-let",
        "--include_letters",
        action="store_true",
        help="Define if random sequences should contain letters. Only works with -rs",
        default=False,
    )
    parser.add_argument(
        "-num",
        "--include_numbers",
        action="store_true",
        help="Define if random sequences should contain numbers. Only works with -rs",
        default=False,
    )
    parser.add_argument(
        "-sym",
        "--include_symbols",
        action="store_true",
        help="Define if random sequences should contain symbols. Only works with -rs",
        default=False,
    )
    parser.add_argument(
        "-w",
        "--length",
        type=int,
        nargs="?",
        help="Define how many words should be included in each generated sample. If the text source is Wikipedia, this is the MINIMUM length",
        default=1,
    )
    parser.add_argument(
        "-r",
        "--random",
        action="store_true",
        help="Define if the produced string will have variable word count (with --length being the maximum)",
        default=False,
    )
    parser.add_argument(
        "-f",
        "--format",
        type=int,
        nargs="?",
        help="Define the height of the produced images if horizontal, else the width",
        default=32,
    )
    parser.add_argument(
        "-t",
        "--thread_count",
        type=int,
        nargs="?",
        help="Define the number of thread to use for image generation",
        default=1,
    )
    parser.add_argument(
        "-e",
        "--extension",
        type=str,
        nargs="?",
        help="Define the extension to save the image with",
        #default="jpg",
        default="png",
    )
    parser.add_argument(
        "-k",
        "--skew_angle",
        type=int,
        nargs="?",
        help="Define skewing angle of the generated text. In positive degrees",
        default=0,
    )
    parser.add_argument(
        "-rk",
        "--random_skew",
        action="store_true",
        help="When set, the skew angle will be randomized between the value set with -k and it's opposite",
        default=False,
    )
    parser.add_argument(
        "-wk",
        "--use_wikipedia",
        action="store_true",
        help="Use Wikipedia as the source text for the generation, using this paremeter ignores -r, -n, -s",
        default=False,
    )
    parser.add_argument(
        "-bl",
        "--blur",
        type=int,
        nargs="?",
        help="Apply gaussian blur to the resulting sample. Should be an integer defining the blur radius",
        default=0,
    )
    parser.add_argument(
        "-rbl",
        "--random_blur",
        action="store_true",
        help="When set, the blur radius will be randomized between 0 and -bl.",
        default=False,
    )
    parser.add_argument(
        "-b",
        "--background",
        type=int,
        nargs="?",
        help="Define what kind of background to use. 0: Gaussian Noise, 1: Plain white, 2: Quasicrystal, 3: Image",
        default=0,
    )
    parser.add_argument(
        "-hw",
        "--handwritten",
        action="store_true",
        help='Define if the data will be "handwritten" by an RNN',
    )
    parser.add_argument(
        "-na",
        "--name_format",
        type=int,
        help="Define how the produced files will be named. 0: [TEXT]_[ID].[EXT], 1: [ID]_[TEXT].[EXT] 2: [ID].[EXT] + one file labels.txt containing id-to-label mappings",
        default=0,
    )
    parser.add_argument(
        "-om",
        "--output_mask",
        type=int,
        help="Define if the generator will return masks for the text",
        default=0,
    )
    parser.add_argument(
        "-obb",
        "--output_bboxes",
        type=int,
        help="Define if the generator will return bounding boxes for the text, 1: Bounding box file, 2: Tesseract format",
        default=0,
    )
    parser.add_argument(
        "-d",
        "--distorsion",
        type=int,
        nargs="?",
        help="Define a distorsion applied to the resulting image. 0: None (Default), 1: Sine wave, 2: Cosine wave, 3: Random",
        default=0,
    )
    parser.add_argument(
        "-do",
        "--distorsion_orientation",
        type=int,
        nargs="?",
        help="Define the distorsion's orientation. Only used if -d is specified. 0: Vertical (Up and down), 1: Horizontal (Left and Right), 2: Both",
        default=0,
    )
    parser.add_argument(
        "-wd",
        "--width",
        type=int,
        nargs="?",
        help="Define the width of the resulting image. If not set it will be the width of the text + 10. If the width of the generated text is bigger that number will be used",
        default=-1,
    )
    parser.add_argument(
        "-al",
        "--alignment",
        type=int,
        nargs="?",
        help="Define the alignment of the text in the image. Only used if the width parameter is set. 0: left, 1: center, 2: right",
        default=1,
    )
    parser.add_argument(
        "-or",
        "--orientation",
        type=int,
        nargs="?",
        help="Define the orientation of the text. 0: Horizontal, 1: Vertical",
        default=0,
    )
    parser.add_argument(
        "-tc",
        "--text_color",
        type=str,
        nargs="?",
        help="Define the text's color, should be either a single hex color or a range in the ?,? format.",
        default="#282828",
    )
    parser.add_argument(
        "-sw",
        "--space_width",
        type=float,
        nargs="?",
        help="Define the width of the spaces between words. 2.0 means twice the normal space width",
        default=1.0,
    )
    parser.add_argument(
        "-cs",
        "--character_spacing",
        type=int,
        nargs="?",
        help="Define the width of the spaces between characters. 2 means two pixels",
        default=0,
    )
    parser.add_argument(
        "-m",
        "--margins",
        type=margins,
        nargs="?",
        help="Define the margins around the text when rendered. In pixels",
        default=(5, 5, 5, 5),
    )
    parser.add_argument(
        "-fi",
        "--fit",
        action="store_true",
        help="Apply a tight crop around the rendered text",
        default=False,
    )
    parser.add_argument(
        "-ft", "--font", type=str, nargs="?", help="Define font to be used"
    )
    parser.add_argument(
        "-fd",
        "--font_dir",
        type=str,
        nargs="?",
        help="Define a font directory to be used",
    )
    parser.add_argument(
        "-id",
        "--image_dir",
        type=str,
        nargs="?",
        help="Define an image directory to use when background is set to image",
        default=os.path.join(os.path.split(os.path.realpath(__file__))[0], "images"),
    )
    parser.add_argument(
        "-ca",
        "--case",
        type=str,
        nargs="?",
        help="Generate upper or lowercase only. arguments: upper or lower. Example: --case upper",
    )
    parser.add_argument(
        "-dt", "--dict", type=str, nargs="?", help="Define the dictionary to be used"
    )
    parser.add_argument(
        "-ws",
        "--word_split",
        action="store_true",
        help="Split on words instead of on characters (preserves ligatures, no character spacing)",
        default=False,
    )
    parser.add_argument(
        "-stw",
        "--stroke_width",
        type=int,
        nargs="?",
        help="Define the width of the strokes",
        default=0,
    )
    parser.add_argument(
        "-stf",
        "--stroke_fill",
        type=str,
        nargs="?",
        help="Define the color of the contour of the strokes, if stroke_width is bigger than 0",
        default="#282828",
    )
    parser.add_argument(
        "-im",
        "--image_mode",
        type=str,
        nargs="?",
        help="Define the image mode to be used. RGB is default, L means 8-bit grayscale images, 1 means 1-bit binary images stored with one pixel per byte, etc.",
        default="RGB",
    )
    return parser.parse_args()


def main():
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py main 함수 들어옴')
    """
    Description: Main function
    """

    # Argument parsing
    args = parse_arguments()
    args.count = 1


    from trdg.generators import (
        GeneratorFromDict,
        GeneratorFromRandom,
        GeneratorFromStrings,
        GeneratorFromWikipedia,
    )

    # The generators use the same arguments as the CLI, only as parameters
    # generator = GeneratorFromStrings(
    #     ['Test1', 'Test2', 'Test3'],
    #     blur=2,
    #     random_blur=True
    # )

    from trdg.generators import GeneratorFromStrings
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py  GeneratorFromStrings 임포트 완료 : {GeneratorFromStrings}')

    #from .generators import GeneratorFromStrings
    #from generators import GeneratorFromStrings
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py  GeneratorFromStrings 임포트 완료 : {GeneratorFromStrings}')

    # 생성할 텍스트 리스트
    texts = ['Test1' ]

    # Generator 초기화
    generator = GeneratorFromStrings(
        texts,
        blur=2,
        random_blur=True
    )

    # 이미지를 5번 생성하도록 설정
    num_images_to_generate = 1
    # 경로 설정
    save_path = r"C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\out\th_1130\NotoSansThaiLooped-Black\\"
    save_path = r"C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\out\th_1130\NotoSansThaiLooped-Black\\"
    today_date = datetime.today().strftime('%Y-%m-%d')
    today_date = datetime.today().strftime('%m-%d')

    #save_path = fr"C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\out\th_{today_date}\NotoSansThaiLooped-Black\\"
    #save_path = fr"C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\out\th_{today_date}"
    save_path = fr"C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\out3\th\{today_date}"

    if not os.path.exists(save_path):
        os.makedirs(save_path)
        print(f'Directory {save_path} created.')
    else:
        print(f'Directory {save_path} already exists.')

    # 루프를 이용하여 이미지 생성
    # for _ in range(num_images_to_generate):
    #     img, lbl = next(generator)
    #     print(f'img: {img}, lbl: {lbl}')
        # 이미지 저장
        # img_save_path = f"{save_path}_generated_image_{_ + 1}.png"
        # img.save(img_save_path)
        # print(f"이미지 저장 완료: {img_save_path}")

    # for img, lbl in generator:
    #     print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!img : {img}')
    #     print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!lbl : {lbl}')
    # Do something with the pillow images here.

    # Create the directory if it does not exist.
    # try:
    #     os.makedirs(args.output_dir)
    # except OSError as e:
    #     if e.errno != errno.EEXIST:
    #         raise

    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py args.dict : {args.dict}')
    args.dict = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\전체언어텍스트파일\th4.txt'
    font = r"C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\font\th\Athiti-Bold.ttf"
    out_dir = save_path
    #args = Args(index=1, text="Hello", font=font , out_dir=out_dir, size=32, extension="png", margins=5)
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py 변경전 args.margins : {args.margins}')
    #args.margins = margins(args.margins)
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py 변경후 args.margins : {args.margins}')

    #args.input_file = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\dicts\th.txt'

    # Creating word list
    if args.dict:
        lang_dict = []
        if os.path.isfile(args.dict):
            with open(args.dict, "r", encoding="utf8", errors="ignore") as d:
                lang_dict = [l for l in d.read().splitlines() if len(l) > 0]
                print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py lang_dict : { lang_dict}')
        else:
            sys.exit("Cannot open dict")
    else:
        lang_dict = load_dict(
            os.path.join(os.path.dirname(__file__), "dicts", args.language + ".txt")
        )


    args.font = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\fonts\th\Athiti-Bold.ttf'
    args.font = r'C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\fonts\thfont2\NotoSansThaiLooped-Black.ttf'
    args.language = 'th'
    args.input_file = r'C:/Users/TAMSystech/yjh/ipynb/TextRecognitionDataGenerator/trdg/dicts/전체언어텍스트파일/th5.txt'
    args.font_dir = r'C:/Users/TAMSystech/yjh/ipynb/TextRecognitionDataGenerator/trdg/fonts/thfont5'
    args.count = 1
    #"C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\fonts\thfont2\NotoSansThaiLooped-Black.ttf"



    # Create font (path) list
    if args.font_dir:
        fonts = [
            #os.path.join(args.font_dir, p)
            os.path.join(args.font_dir, p).replace("\\", "/")
            for p in os.listdir(args.font_dir)
            if os.path.splitext(p)[1] == ".ttf"
        ]
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!fonts : {fonts}')
    elif args.font:
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!args.font : {args.font}')
        if os.path.isfile(args.font):
            fonts = [args.font]
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!fonts : {fonts}')
        else:
            sys.exit("Cannot open font")
    else:
        fonts = load_fonts(args.language)
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!else args.language : {args.language}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!else fonts : {fonts}')

    # Creating synthetic sentences (or word)
    strings = []
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py args.input_file : {args.input_file}')
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py args.count : {args.count}')
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!args.font_dir : {args.font_dir}')

    if args.use_wikipedia:
        strings = create_strings_from_wikipedia(args.length, args.count, args.language)
    elif args.input_file != "":
        strings = create_strings_from_file(args.input_file, args.count)
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!input_file 있음 strings : {strings}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!input_file 있음 args.count : {args.count}')
    elif args.random_sequences:
        strings = create_strings_randomly(
            args.length,
            args.random,
            args.count,
            args.include_letters,
            args.include_numbers,
            args.include_symbols,
            args.language,
        )
        # Set a name format compatible with special characters automatically if they are used
        if args.include_symbols or True not in (
            args.include_letters,
            args.include_numbers,
            args.include_symbols,
        ):
            args.name_format = 2
    else:
        strings = create_strings_from_dict(
            args.length, args.random, args.count, lang_dict
        )

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py strings : {strings }')

    if args.language == "ar":
        from arabic_reshaper import ArabicReshaper
        from bidi.algorithm import get_display

        arabic_reshaper = ArabicReshaper()
        strings = [
            " ".join(
                [get_display(arabic_reshaper.reshape(w)) for w in s.split(" ")[::-1]]
            )
            for s in strings
        ]
    if args.case == "upper":
        strings = [x.upper() for x in strings]
    if args.case == "lower":
        strings = [x.lower() for x in strings]

    string_count = len(strings)
    args.name_format = 2
    args.name_format = 0
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py string_count : {string_count}')
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py argsblur : {args.blur}')
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py args.name_format : {args.name_format}')
    args.output_dir = save_path
    output_dir = args.output_dir
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py save_path : {save_path}')
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py output_dir : {output_dir}')
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! fonts 블라블라 : {[fonts[rnd.randrange(0, len(fonts))] for _ in range(0, string_count)]}')
    #args.margins = 2

    #p = Pool(args.thread_count)
    #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! p : {p}')
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py args.output_dir : {args.output_dir}')
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py args.thread_count : {args.thread_count}')
    #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FakeTextDataGenerator.generate_from_tuple : {FakeTextDataGenerator.generate_from_tuple}')
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py FakeTextDataGenerator.generate_from_tuple 함수 호출 전 os.getcwd() : {os.getcwd()}')
    #print(f'FakeTextDataGenerator 임포트 하기전 trdg : {trdg}')
    #print(f'FakeTextDataGenerator 임포트 하기전 trdg.data_generator : {trdg.data_generator}')
    from trdg.data_generator import FakeTextDataGenerator
    print(f'FakeTextDataGenerator 임포트 완료 임포트가 안됌 : {FakeTextDataGenerator}')

    print(
        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py FakeTextDataGenerator.generate_from_tuple 함수 호출하라고 함수 호출하라니깐 FakeTextDataGenerator : {FakeTextDataGenerator }')

    print(
        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py FakeTextDataGenerator.generate_from_tuple 함수 호출하라고 함수 호출하라니깐 : {FakeTextDataGenerator.generate_from_tuple}')
    # 클래스 객체 생성
    generator_instance = FakeTextDataGenerator()
    print(
        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py generator_instance FakeTextDataGenerator 클래스 객체 생성2 : {generator_instance}')
    print(
        f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! run.py generator_instance.generate_from_tuple 함수 호출2 : {generator_instance.generate_from_tuple }')


    for font in fonts:
        p = Pool(args.thread_count)
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! p : {p}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py font : {font}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py font : {font}')
        relative_path = os.path.relpath(font, args.font_dir)
        print(f'run.py Relative Path: {relative_path}')
        relative_path, file_extension = os.path.splitext(relative_path)
        print(f'run.py output_dir 확장자 제거 : {relative_path}')

        args.output_dir = fr'{output_dir}\{relative_path}'
        #args.output_dir = fr'{output_dir}\out\{relative_path}'


        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py  args.output_dir font 디렉토리로 변경 : {args.output_dir}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py ! font 로 string_count 만큼 배열 채운다 fonts : {[fonts[fonts.index(font)] for _ in range(0, string_count)]}')
        # 디렉토리가 없으면 생성
        if not os.path.exists(args.output_dir):
            os.makedirs(args.output_dir)
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py  디렉토리가 없으면 생성 : {args.output_dir}')
        #args.extension = 'png'

        #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py  p.imap_unordered 에 전달하는 zip  : {zip}')
        #
        #for _ in tqdm(
        for _ in tqdm(
                p.imap_unordered(
                    FakeTextDataGenerator.generate_from_tuple,
                    #generator_instance.generate_from_tuple,
                    zip(
                        [i for i in range(0, string_count)],
                        strings,
                        # [fonts[rnd.randrange(0, len(fonts))] for _ in range(0, string_count)],
                        [fonts[fonts.index(font)] for _ in range(0, string_count)],
                        [args.output_dir] * string_count,
                        [args.format] * string_count,
                        [args.extension] * string_count,
                        [args.skew_angle] * string_count,
                        [args.random_skew] * string_count,
                        [args.blur] * string_count,
                        [args.random_blur] * string_count,
                        [args.background] * string_count,
                        [args.distorsion] * string_count,
                        [args.distorsion_orientation] * string_count,
                        [args.handwritten] * string_count,
                        [args.name_format] * string_count,
                        [args.width] * string_count,
                        [args.alignment] * string_count,
                        [args.text_color] * string_count,
                        [args.orientation] * string_count,
                        [args.space_width] * string_count,
                        [args.character_spacing] * string_count,
                        [args.margins] * string_count,
                        [args.fit] * string_count,
                        [args.output_mask] * string_count,
                        [args.word_split] * string_count,
                        [args.image_dir] * string_count,
                        [args.stroke_width] * string_count,
                        [args.stroke_fill] * string_count,
                        [args.image_mode] * string_count,
                        [args.output_bboxes] * string_count,
                    ),
                ),
                total=args.count,
        ):
            pass
        p.terminate()
        args.name_format = 2
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py  args.name_format : {args.name_format}')

        if args.name_format == 2:
            # Create file with filename-to-label connections
            # with open(
            #         os.path.join(args.output_dir, "labels.txt"), "w", encoding="utf8"
            # ) as f:
            #out_dir = os.path.join(out_dir, 'label')
            label_dir = fr'{args.output_dir}/label'
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py  out_dir 변경 ( /out 폴더에 labels.txt 생성 ) : {out_dir}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py  args.extension : {args.extension}')

            # 디렉토리가 없으면 생성
            if not os.path.exists(label_dir):
                os.makedirs(label_dir)
            with open(
                    os.path.join(label_dir, "labels.txt"), "w", encoding="utf8"
            ) as f:
                for i in range(string_count):
                    # file_name = str(i) + "." + args.extension
                    file_name = strings[i] + "_" + str(i) + "." + args.extension
                    label = strings[i]

                    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py label : {label}')
                    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py file_name : {file_name}')
                    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py label : {label}')

                    if args.space_width == 0:
                        label = label.replace(" ", "")
                    f.write("{} {}\n".format(file_name, label))
                    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py label.txt 저장 완료 label : {label}')



    # for _ in tqdm(
    #     p.imap_unordered(
    #         FakeTextDataGenerator.generate_from_tuple,
    #         #generator_instance.generate_from_tuple,
    #         zip(
    #             [i for i in range(0, string_count)],
    #             strings,
    #             [fonts[rnd.randrange(0, len(fonts))] for _ in range(0, string_count)],
    #             [args.output_dir] * string_count,
    #             [args.format] * string_count,
    #             [args.extension] * string_count,
    #             [args.skew_angle] * string_count,
    #             [args.random_skew] * string_count,
    #             [args.blur] * string_count,
    #             [args.random_blur] * string_count,
    #             [args.background] * string_count,
    #             [args.distorsion] * string_count,
    #             [args.distorsion_orientation] * string_count,
    #             [args.handwritten] * string_count,
    #             [args.name_format] * string_count,
    #             [args.width] * string_count,
    #             [args.alignment] * string_count,
    #             [args.text_color] * string_count,
    #             [args.orientation] * string_count,
    #             [args.space_width] * string_count,
    #             [args.character_spacing] * string_count,
    #             [args.margins] * string_count,
    #             [args.fit] * string_count,
    #             [args.output_mask] * string_count,
    #             [args.word_split] * string_count,
    #             [args.image_dir] * string_count,
    #             [args.stroke_width] * string_count,
    #             [args.stroke_fill] * string_count,
    #             [args.image_mode] * string_count,
    #             [args.output_bboxes] * string_count,
    #         ),
    #     ),
    #     total=args.count,
    # ):
    #     pass
    # p.terminate()
    # args.name_format = 2
    # if args.name_format == 2:
    #     # Create file with filename-to-label connections
    #     with open(
    #         os.path.join(args.output_dir, "labels.txt"), "w", encoding="utf8"
    #     ) as f:
    #         for i in range(string_count):
    #             #file_name = str(i) + "." + args.extension
    #             file_name = strings[i] + "_" + str(i) + "." + args.extension
    #             label = strings[i]
    #
    #             print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!run.py label : {label}')
    #
    #
    #             if args.space_width == 0:
    #                 label = label.replace(" ", "")
    #             f.write("{} {}\n".format(file_name, label))


if __name__ == "__main__":
	#font_path = r"C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\trdg\fonts\전체 언어 폰트 파일\Athiti-Bold.ttf"
    main()