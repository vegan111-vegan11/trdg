# import os
# import random as rnd
#
# from PIL import Image, ImageFilter, ImageStat
#
# from trdg import computer_text_generator, background_generator, distorsion_generator
# from trdg.utils import mask_to_bboxes, make_filename_valid
#
# try:
#     from trdg import handwritten_text_generator
# except ImportError as e:
#     print("Missing modules for handwritten text generation.")
#
#
# class FakeTextDataGenerator(object):
#     def __init__(self):
#         print(f'!!!!!!!!!!!!!!!!data_generator.py  FakeTextDataGenerator  클래스 object : {self}')
#
#     print(f'!!!!!!!!!!!!!!!!data_generator.py  FakeTextDataGenerator  클래스 object : {object}')
#     @classmethod
#     def generate_from_tuple(cls, t):
#         print(f'!!!!!!!!!!!!!!!!data_generator.py FakeTextDataGenerator  generate_from_tuple : {t}')
#
#         """
#         Same as generate, but takes all parameters as one tuple
#         """
#         print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py FakeTextDataGenerator  generate_from_tuple cls: {cls}')
#         cls.generate(*t)
#
#     @classmethod
#     def generate(
#         cls,
#         index: int,
#         text: str,
#         font: str,
#         out_dir: str,
#         size: int,
#         extension: str,
#         skewing_angle: int,
#         random_skew: bool,
#         blur: int,
#         random_blur: bool,
#         background_type: int,
#         distorsion_type: int,
#         distorsion_orientation: int,
#         is_handwritten: bool,
#         name_format: int,
#         width: int,
#         alignment: int,
#         text_color: str,
#         orientation: int,
#         space_width: int,
#         character_spacing: int,
#         margins: int,
#         fit: bool,
#         output_mask: bool,
#         word_split: bool,
#         image_dir: str,
#         stroke_width: int = 0,
#         stroke_fill: str = "#282828",
#         image_mode: str = "RGB",
#         output_bboxes: int = 0,
#     ) -> Image:
#         image = None
#
#         print(f"data_generator.py Out_dir: {out_dir}")
#         print(f"data_generator.py font: {font}")
#         print(f"data_generator.py margins: {margins}")
#
#         margin_top, margin_left, margin_bottom, margin_right = margins
#         horizontal_margin = margin_left + margin_right
#         vertical_margin = margin_top + margin_bottom
#
#         ##########################
#         # Create picture of text #
#         ##########################
#         if is_handwritten:
#             if orientation == 1:
#                 raise ValueError("Vertical handwritten text is unavailable")
#             image, mask = handwritten_text_generator.generate(text, text_color)
#         else:
#             image, mask = computer_text_generator.generate(
#                 text,
#                 font,
#                 text_color,
#                 size,
#                 orientation,
#                 space_width,
#                 character_spacing,
#                 fit,
#                 word_split,
#                 stroke_width,
#                 stroke_fill,
#             )
#         random_angle = rnd.randint(0 - skewing_angle, skewing_angle)
#
#         rotated_img = image.rotate(
#             skewing_angle if not random_skew else random_angle, expand=1
#         )
#
#         rotated_mask = mask.rotate(
#             skewing_angle if not random_skew else random_angle, expand=1
#         )
#
#         #############################
#         # Apply distorsion to image #
#         #############################
#         if distorsion_type == 0:
#             distorted_img = rotated_img  # Mind = blown
#             distorted_mask = rotated_mask
#         elif distorsion_type == 1:
#             distorted_img, distorted_mask = distorsion_generator.sin(
#                 rotated_img,
#                 rotated_mask,
#                 vertical=(distorsion_orientation == 0 or distorsion_orientation == 2),
#                 horizontal=(distorsion_orientation == 1 or distorsion_orientation == 2),
#             )
#         elif distorsion_type == 2:
#             distorted_img, distorted_mask = distorsion_generator.cos(
#                 rotated_img,
#                 rotated_mask,
#                 vertical=(distorsion_orientation == 0 or distorsion_orientation == 2),
#                 horizontal=(distorsion_orientation == 1 or distorsion_orientation == 2),
#             )
#         else:
#             distorted_img, distorted_mask = distorsion_generator.random(
#                 rotated_img,
#                 rotated_mask,
#                 vertical=(distorsion_orientation == 0 or distorsion_orientation == 2),
#                 horizontal=(distorsion_orientation == 1 or distorsion_orientation == 2),
#             )
#
#         ##################################
#         # Resize image to desired format #
#         ##################################
#
#         # Horizontal text
#         if orientation == 0:
#             new_width = int(
#                 distorted_img.size[0]
#                 * (float(size - vertical_margin) / float(distorted_img.size[1]))
#             )
#             resized_img = distorted_img.resize(
#                 (new_width, size - vertical_margin), Image.Resampling.LANCZOS
#             )
#             resized_mask = distorted_mask.resize(
#                 (new_width, size - vertical_margin), Image.Resampling.NEAREST
#             )
#             background_width = width if width > 0 else new_width + horizontal_margin
#             background_height = size
#         # Vertical text
#         elif orientation == 1:
#             new_height = int(
#                 float(distorted_img.size[1])
#                 * (float(size - horizontal_margin) / float(distorted_img.size[0]))
#             )
#             resized_img = distorted_img.resize(
#                 (size - horizontal_margin, new_height), Image.Resampling.LANCZOS
#             )
#             resized_mask = distorted_mask.resize(
#                 (size - horizontal_margin, new_height), Image.Resampling.NEAREST
#             )
#             background_width = size
#             background_height = new_height + vertical_margin
#         else:
#             raise ValueError("Invalid orientation")
#
#         #############################
#         # Generate background image #
#         #############################
#         if background_type == 0:
#             background_img = background_generator.gaussian_noise(
#                 background_height, background_width
#             )
#         elif background_type == 1:
#             background_img = background_generator.plain_white(
#                 background_height, background_width
#             )
#         elif background_type == 2:
#             background_img = background_generator.quasicrystal(
#                 background_height, background_width
#             )
#         else:
#             background_img = background_generator.image(
#                 background_height, background_width, image_dir
#             )
#         background_mask = Image.new(
#             "RGB", (background_width, background_height), (0, 0, 0)
#         )
#
#         ##############################################################
#         # Comparing average pixel value of text and background image #
#         ##############################################################
#         try:
#             resized_img_st = ImageStat.Stat(resized_img, resized_mask.split()[2])
#             background_img_st = ImageStat.Stat(background_img)
#
#             resized_img_px_mean = sum(resized_img_st.mean[:2]) / 3
#             background_img_px_mean = sum(background_img_st.mean) / 3
#
#             if abs(resized_img_px_mean - background_img_px_mean) < 15:
#                 print("value of mean pixel is too similar. Ignore this image")
#
#                 print("resized_img_st \n {}".format(resized_img_st.mean))
#                 print("background_img_st \n {}".format(background_img_st.mean))
#
#                 return
#         except Exception as err:
#             return
#
#         #############################
#         # Place text with alignment #
#         #############################
#
#         new_text_width, _ = resized_img.size
#
#         if alignment == 0 or width == -1:
#             background_img.paste(resized_img, (margin_left, margin_top), resized_img)
#             background_mask.paste(resized_mask, (margin_left, margin_top))
#         elif alignment == 1:
#             background_img.paste(
#                 resized_img,
#                 (int(background_width / 2 - new_text_width / 2), margin_top),
#                 resized_img,
#             )
#             background_mask.paste(
#                 resized_mask,
#                 (int(background_width / 2 - new_text_width / 2), margin_top),
#             )
#         else:
#             background_img.paste(
#                 resized_img,
#                 (background_width - new_text_width - margin_right, margin_top),
#                 resized_img,
#             )
#             background_mask.paste(
#                 resized_mask,
#                 (background_width - new_text_width - margin_right, margin_top),
#             )
#
#         ############################################
#         # Change image mode (RGB, grayscale, etc.) #
#         ############################################
#
#         background_img = background_img.convert(image_mode)
#         background_mask = background_mask.convert(image_mode)
#
#         #######################
#         # Apply gaussian blur #
#         #######################
#
#         gaussian_filter = ImageFilter.GaussianBlur(
#             radius=blur if not random_blur else rnd.random() * blur
#         )
#         final_image = background_img.filter(gaussian_filter)
#         final_mask = background_mask.filter(gaussian_filter)
#
#         #####################################
#         # Generate name for resulting image #
#         #####################################
#         # We remove spaces if space_width == 0
#         if space_width == 0:
#             text = text.replace(" ", "")
#         if name_format == 0:
#             name = "{}_{}".format(text, str(index))
#         elif name_format == 1:
#             name = "{}_{}".format(str(index), text)
#         elif name_format == 2:
#             name = str(index)
#         else:
#             print("{} is not a valid name format. Using default.".format(name_format))
#             name = "{}_{}".format(text, str(index))
#
#         name = make_filename_valid(name, allow_unicode=True)
#         image_name = "{}.{}".format(name, extension)
#         mask_name = "{}_mask.png".format(name)
#         box_name = "{}_boxes.txt".format(name)
#         tess_box_name = "{}.box".format(name)
#
#         print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py final_image : {final_image}')
#
#
#         # Save the image
#         if out_dir is not None:
#             print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py out_dir : {out_dir}')
#             print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py image_name : {image_name}')
#             out_dir = r'C:/Users/TAMSystech/yjh/ipynb/TextRecognitionDataGenerator/out/th/thfont8'
#             image_path = os.path.join(out_dir, image_name)
#
#             final_image.save(os.path.join(out_dir, image_name))
#             print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py f out_dir is not None image_path : {image_path}')
#             print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py final_image : {final_image}')
#
#             # 이미지 열기
#             image = final_image.open(image_path)
#
#             #final_image.show()  # 이미지 출력
#             print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py final_image 이미지 출력 : {final_image}')
#
#             #image.show()  # 이미지 출력
#             print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py image 오픈하고 이미지 출력 ( final_image ) : {image}')
#
#             if output_mask == 1:
#                 final_mask.save(os.path.join(out_dir, mask_name))
#             if output_bboxes == 1:
#                 bboxes = mask_to_bboxes(final_mask)
#                 with open(os.path.join(out_dir, box_name), "w") as f:
#                     for bbox in bboxes:
#                         f.write(" ".join([str(v) for v in bbox]) + "\n")
#             if output_bboxes == 2:
#                 bboxes = mask_to_bboxes(final_mask, tess=True)
#                 with open(os.path.join(out_dir, tess_box_name), "w") as f:
#                     for bbox, char in zip(bboxes, text):
#                         f.write(
#                             " ".join([char] + [str(v) for v in bbox] + ["0"]) + "\n"
#                         )
#         else:
#             if output_mask == 1:
#                 return final_image, final_mask
#             return final_image
import os
import random as rnd

from PIL import Image, ImageFilter, ImageStat

from trdg import computer_text_generator, background_generator, distorsion_generator
from trdg.utils import mask_to_bboxes, make_filename_valid
print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 파일 들어옴 임포트 하는 단계 mask_to_bboxes :  {mask_to_bboxes}')
print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 파일 들어옴 임포트 하는 단계 make_filename_valid :  {make_filename_valid}')

try:
    print('data_generator.py try ============================================')
    from trdg import handwritten_text_generator

    print(f'data_generator.py try handwritten_text_generator 임포트 완료 : {handwritten_text_generator}')
    #pass
    from trdg.string_generator import (
        create_strings_from_dict,
        create_strings_from_file,
        create_strings_from_wikipedia,
        create_strings_randomly,
    )
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py try create_strings_from_dict : {create_strings_from_dict} ')
except ImportError as e:
    print('============================================')
    print("Missing modules for handwritten text generation.")
    print('============================================ 여기서 끝남>???')
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py except ImportError as e 발생 e : {e} ')
    print('============================================ 에러 발생하고 프린트 하고 여기서 끝남>???')

print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 파일 들어옴 임포트 예외 후 :  ')

class FakeTextDataGenerator(object):
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 파일  FakeTextDataGenerator 클래스 들어옴 __init__ 함수 들어가기 전  object : {object} ')
    def __init__(self):
        print(f'!!!!!!!!!!!!!!!!data_generator.py  FakeTextDataGenerator  클래스 object __init__ 함수 들어와야 함 : {self}')

    print(f'!!!!!!!!!!!!!!!!data_generator.py  FakeTextDataGenerator  클래스 -> __init__  FakeTextDataGenerator(object) : {object}')
    @classmethod
    def generate_from_tuple(cls, t):
        print(f'!!!!!!!!!!!!!!!!data_generator.py FakeTextDataGenerator  generate_from_tuple 함수 ( 튜플 전달 ) t : {t}')

        """
        Same as generate, but takes all parameters as one tuple
        """
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py FakeTextDataGenerator  generate_from_tuple cls: {cls}')
        # 원본
        #cls.generate(*t)
        # 클래스 메서드 내에서 인스턴스 생성
        instance = cls()
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py FakeTextDataGenerator  generate_from_tuple 클래스 메서드 내에서 인스턴스 생성 instance : {instance}')

        # generate 메서드 호출
        instance.generate(*t)
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py FakeTextDataGenerator  generate_from_tuple generate 메서드 호출 instance.generate(*t) : {instance.generate(*t)}')

    @classmethod
    def generate(
        cls,
        index: int,
        text: str,
        font: str,
        out_dir: str,
        size: int,
        extension: str,
        skewing_angle: int,
        random_skew: bool,
        blur: int,
        random_blur: bool,
        background_type: int,
        distorsion_type: int,
        distorsion_orientation: int,
        is_handwritten: bool,
        name_format: int,
        width: int,
        alignment: int,
        text_color: str,
        orientation: int,
        space_width: int,
        character_spacing: int,
        margins: int,
        fit: bool,
        output_mask: bool,
        word_split: bool,
        image_dir: str,
        stroke_width: int = 0,
        stroke_fill: str = "#282828",
        #image_mode: str = "RGB",
        image_mode: str = "L",
        output_bboxes: int = 0,
    ) -> Image:
        image = None

        print(f"data_generator.py Out_dir : {out_dir}")
        print(f"data_generator.py font : {font}")
        print(f"data_generator.py margins : {margins}")
        print(f"data_generator.py size : {size}")

        #size = 81
        print(f"data_generator.py size 처음 전달된 값 : {size}")

        margin_top, margin_left, margin_bottom, margin_right = margins
        print(f"data_generator.py margin_top : {margin_top}")
        print(f"data_generator.py margin_left : {margin_left}")
        print(f"data_generator.py margin_bottom : {margin_bottom}")
        print(f"data_generator.py margin_right : {margin_right}")

        horizontal_margin = margin_left + margin_right
        vertical_margin = margin_top + margin_bottom

        print(f"data_generator.py horizontal_margin : {horizontal_margin}")
        print(f"data_generator.py vertical_margin : {vertical_margin}")

        ##########################
        # Create picture of text #
        ##########################
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py is_handwritten : {is_handwritten}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py orientation : {orientation}')

        if is_handwritten:
            if orientation == 1:
                raise ValueError("Vertical handwritten text is unavailable")
            image, mask = handwritten_text_generator.generate(text, text_color)
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py if orientation == 1 image : {image}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py if orientation == 1 mask = : {mask }')
        else:
            image, mask = computer_text_generator.generate(
                text,
                font,
                text_color,
                size,
                orientation,
                space_width,
                character_spacing,
                fit,
                word_split,
                stroke_width,
                stroke_fill,
            )
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py gaussian_filter if orientation != 1 image : {image}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py gaussian_filter if orientation != 1 mask : {mask}')

        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py image : {image}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py size : {size}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py skewing_angle : {skewing_angle}')
        #image.show()  # 이미지 출력
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 처음 생성한 image 이미지 출력 : {image}')

        # 투명도 조절
        # alpha_value = 0  # 투명도를 나타내는 값 (0에서 255 사이의 값)
        # image.putalpha(alpha_value)

        # 경로 설정
        save_path = fr'{out_dir}/log/'
        if not os.path.exists(save_path):
            os.makedirs(save_path)
            print(f'data_generator.py Directory {save_path} created.')
        else:
            print(f'data_generator.py Directory {save_path} already exists.')
        # save_path = r"C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\out\th_1129_2\NotoSansThaiLooped-Black\\"
        # save_path = out_dir
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py out_dir : {out_dir}')

        # 이미지 저장
        image_save_path = f"{save_path}_computer_text_generator_image_{1}.png"
        image.save(image_save_path)

        # 통계 출력
        print(f"_computer_text_generator image 이미지 저장 완료: {image_save_path}")



        random_angle = rnd.randint(0 - skewing_angle, skewing_angle)

        rotated_img = image.rotate(
            skewing_angle if not random_skew else random_angle, expand=1
        )

        rotated_mask = mask.rotate(
            skewing_angle if not random_skew else random_angle, expand=1
        )

        #############################
        # Apply distorsion to image #
        #############################
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py rotated_mask : {rotated_mask}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py rotated_img : {rotated_img}')

        #rotated_mask.show()  # 이미지 출력
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py rotated_mask 이미지 출력 : {rotated_mask}')
        #rotated_img.show()  # 이미지 출력
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py rotated_img 이미지 출력 : {rotated_img}')

        # 경로 설정
        save_path = fr'{out_dir}/log/'
        # 이미지 저장
        rotated_img_save_path = f"{save_path}_rotated_img_제일 처음 rotated 텍스트 이미지 _{1}.png"
        rotated_img.save(rotated_img_save_path)

        # 통계 출력
        print(f"rotated_img 이미지 저장 완료: {rotated_img_save_path}")

        # 이미지 저장
        rotated_mask_save_path = f"{save_path}_rotated_mask_제일 처음 rotated 텍스트 마스크 _{1}.png"
        rotated_mask.save(rotated_mask_save_path)

        # 통계 출력
        print(f"rotated_mask 이미지 저장 완료: {rotated_mask_save_path}")

        if distorsion_type == 0:
            distorted_img = rotated_img  # Mind = blown
            distorted_mask = rotated_mask
        elif distorsion_type == 1:
            distorted_img, distorted_mask = distorsion_generator.sin(
                rotated_img,
                rotated_mask,
                vertical=(distorsion_orientation == 0 or distorsion_orientation == 2),
                horizontal=(distorsion_orientation == 1 or distorsion_orientation == 2),
            )
        elif distorsion_type == 2:
            distorted_img, distorted_mask = distorsion_generator.cos(
                rotated_img,
                rotated_mask,
                vertical=(distorsion_orientation == 0 or distorsion_orientation == 2),
                horizontal=(distorsion_orientation == 1 or distorsion_orientation == 2),
            )
        else:
            distorted_img, distorted_mask = distorsion_generator.random(
                rotated_img,
                rotated_mask,
                vertical=(distorsion_orientation == 0 or distorsion_orientation == 2),
                horizontal=(distorsion_orientation == 1 or distorsion_orientation == 2),
            )

        ##################################
        # Resize image to desired format #
        ##################################
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py orientation : {orientation}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py distorted_img : {distorted_img}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py distorted_mask : {distorted_mask}')

        #distorted_img.show()  # 이미지 출력
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py distorted_img 이미지 출력 : {distorted_img}')
        #distorted_mask.show()  # 이미지 출력
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py distorted_mask 이미지 출력 : {distorted_mask}')

        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Horizontal text distorted_img.size : {distorted_img.size}')

        # 경로 설정
        save_path = fr'{out_dir}/log/'
        # 이미지 저장
        distorted_img_save_path = f"{save_path}_distorted_img_처음 distorted 텍스트 이미지 _{1}.png"
        distorted_img.save(distorted_img_save_path)

        # 통계 출력
        print(f"distorted_img 이미지 저장 완료: {distorted_img_save_path}")

        # 이미지 저장
        distorted_mask_save_path = f"{save_path}_distorted_mask_처음 distorted 텍스트 마스크 _{1}.png"
        distorted_mask.save(distorted_mask_save_path)

        # 통계 출력
        print(f"distorted_mask 이미지 저장 완료: {distorted_mask_save_path}")

        # Horizontal text
        if orientation == 0:
            new_width = int(
                distorted_img.size[0]
                * (float(size - vertical_margin) / float(distorted_img.size[1]))
            )
            #new_width = 81
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Horizontal text new_width 81 으로 임의로 설정 : {new_width}')
            # resized_img = distorted_img.resize(
            #     (new_width, size - vertical_margin), Image.Resampling.LANCZOS
            # )
            # resized_mask = distorted_mask.resize(
            #     (new_width, size - vertical_margin), Image.Resampling.NEAREST
            # )
            # resized_img = distorted_img.resize(
            #     (new_width, size - vertical_margin), Image.Resampling.LANCZOS
            # )
            # resized_mask = distorted_mask.resize(
            #     (new_width, size - vertical_margin), Image.Resampling.NEAREST
            # )
            # 원래 distorted_img 가로, 세로 길이로 함
            resized_img = distorted_img.resize(
                (distorted_img.size[0] - horizontal_margin * 2, distorted_img.size[1] - vertical_margin * 2), Image.Resampling.LANCZOS
            )
            resized_mask = distorted_mask.resize(
                (distorted_img.size[0] - horizontal_margin * 2, distorted_img.size[1] - vertical_margin * 2), Image.Resampling.NEAREST
            )

            # 경로 설정
            save_path = fr'{out_dir}/log/'
            # 이미지 저장
            resized_img_save_path = f"{save_path}_resized_img_처음 리사이즈드 텍스트 이미지 _{1}.png"
            resized_img.save(resized_img_save_path)

            # 통계 출력
            print(f"resized_img 이미지 저장 완료: {resized_img_save_path}")

            # 배경을 투명하게 만들기
            #resized_img.putalpha(resized_mask)

            # 경로 설정
            save_path = fr'{out_dir}/log/'
            # 이미지 저장
            resized_img_save_path = f"{save_path}_resized_img_처음 리사이즈드 텍스트 이미지_배경을 투명하게_{1}.png"
            resized_img.save(resized_img_save_path)

            # 통계 출력
            print(f"resized_img 이미지 저장 완료: {resized_img_save_path}")

            # resized_img = distorted_img.resize(
            #     (82, 81), Image.Resampling.LANCZOS
            # )
            # resized_mask = distorted_mask.resize(
            #     (82, 81), Image.Resampling.NEAREST
            # )
            # 원본 ( 32 는 yaml 파일에 설정돼 있는 값 )
            # background_width = width if width > 0 else new_width + horizontal_margin
            # background_height = size
            # background_width = width if width > 0 else new_width + horizontal_margin
            # background_height = size
            background_width = width if width > 0 else distorted_img.size[0] - horizontal_margin
            background_height = distorted_img.size[1] - vertical_margin
            #distorted_img.size[0] - horizontal_margin, distorted_img.size[1] - vertical_margin

            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py size : {size}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Horizontal if orientation == 0 text background_width : {background_width}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Horizontal if orientation == 0 text background_height : {background_height}')


            # Vertical text
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Horizontal if orientation == 0 text orientation : {orientation}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Horizontal if orientation == 0 text distorted_img.size[0] : {distorted_img.size[0]}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Horizontal if orientation == 0 text distorted_img.size[1] : {distorted_img.size[1]}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Horizontal if orientation == 0 text distorted_img.size  : {distorted_img.size }')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Horizontal if orientation == 0 text size : {size}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Horizontal if orientation == 0 text horizontal_margin : {horizontal_margin}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Horizontal if orientation == 0 text vertical_margin : {vertical_margin}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Horizontal if orientation == 0 text new_width : {new_width}')

        elif orientation == 1:
            new_height = int(
                float(distorted_img.size[1])
                * (float(size - horizontal_margin) / float(distorted_img.size[0]))
            )

            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Vertical text orientation == 1 resized_img 계산전 size : {size}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Vertical text orientation == 1 resized_img 계산전 new_height : {new_height}')


            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Vertical text orientation == 1 size resized_img 계산전 - horizontal_margin : {size - horizontal_margin}')

            #new_height = 81
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Vertical text orientation == 1 resized_img   new_height 81 로 임의로 설정 : {new_height}')

            # resized_img = distorted_img.resize(
            #     (size - horizontal_margin, new_height), Image.Resampling.LANCZOS
            # )
            resized_img = distorted_img.resize(
                (distorted_img.size[1] - horizontal_margin * 2, distorted_img.size[0]), Image.Resampling.LANCZOS
            )
            # resized_img = distorted_img.resize(
            #     (82, 81), Image.Resampling.LANCZOS
            # )
            # resized_mask = distorted_mask.resize(
            #     (82, 81), Image.Resampling.NEAREST
            # )
            # 원본
            # background_width = size
            # background_height = new_height + vertical_margin
            background_width = width if width > 0 else distorted_img.size[0] - horizontal_margin
            background_height = distorted_img.size[1] - vertical_margin

            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Vertical text orientation == 1 resized_img 최종 orientation == 1 background_width : {background_width}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Vertical text orientation == 1 resized_img 최종 orientation == 1 background_height : {background_height}')


            #background_width = 82
            #background_height = 81
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!background_width 1000 으로 임의로 설정 orientation == 1 background_width : {background_width}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!background_width 1000 으로 임의로 설정 orientation == 1 background_height : {background_height}')

        else:
            raise ValueError("Invalid orientation")


        # background_width = 82
        # background_height = 81

        # 텍스트 크기
        # text_width = 208
        # text_height = 72
        text_width = 208
        text_height = 72

        # 이미지 크기
        #background_width = text_width
        #background_height = text_height

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!수평또는 수직으로 텍스트 변환 background_width 1000 으로 임의로 설정 : {background_width}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!수평또는 수직으로 텍스트 변환 background_width 1000 으로 임의로 설정 background_height : {background_height}')

        #resized_img.show()  # 이미지 출력
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!수평또는 수직으로 텍스트 변환 data_generator.py resized_img 이미지 출력 : {resized_img}')
        #resized_mask.show()  # 이미지 출력
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!수평또는 수직으로 텍스트 변환 data_generator.py resized_mask 이미지 출력 : {resized_mask}')

        # 경로 설정
        save_path = fr'{out_dir}/log/'
        # 이미지 저장
        resized_img_save_path = f"{save_path}_resized_img_처음 리사이즈드 텍스트 이미지 최종_{1}.png"
        resized_img.save(resized_img_save_path)

        # 통계 출력
        print(f"resized_img 이미지 저장 완료: {resized_img_save_path}")

        # 이미지 저장
        resized_mask_save_path = f"{save_path}_resized_mask_처음 리사이즈드 텍스트 마스크 최종_{1}.png"
        resized_mask.save(resized_mask_save_path)

        # 통계 출력
        print(f"resized_mask 이미지 저장 완료: {resized_mask_save_path}")

        print(f"background_type: {background_type}")

        #############################
        # Generate background image #
        #############################
        if background_type == 0:
            background_img = background_generator.gaussian_noise(
                background_height, background_width
            )
        elif background_type == 1:
            background_img = background_generator.plain_white(
                background_height, background_width
            )
        elif background_type == 2:
            background_img = background_generator.quasicrystal(
                background_height, background_width
            )
        else:
            background_img = background_generator.image(
                background_height, background_width, image_dir
            )
        background_mask = Image.new(
            "RGB", (background_width, background_height), (0, 0, 0)
        )

        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 배경생성 background_img paste 한 후 Image : {Image}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 배경생성 background_img paste 한 후 background_width : {background_width}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 배경생성 background_img paste 한 후 background_height : {background_height}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 배경생성 background_img paste 한 후 background_mask : {background_mask}')

        #background_img.show()  # 이미지 출력
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 배경생성 background_img 이미지 출력 : {background_img}')
        #background_mask.show()  # 이미지 출력
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 배경생성 background_mask 이미지 출력 : {background_mask}')

        # 경로 설정
        save_path = fr'{out_dir}/log/'
        # 이미지 저장
        background_img_save_path = f"{save_path}_background_img_처음 배경_{1}.png"
        background_img.save(background_img_save_path)

        # 통계 출력
        print(f"background_img 이미지 저장 완료: {background_img_save_path}")

        # 이미지 저장
        background_mask_save_path = f"{save_path}_background_mask_처음 mask_{1}.png"
        background_mask.save(background_mask_save_path)

        # 통계 출력
        print(f"background_mask 이미지 저장 완료: {background_mask_save_path}")

        ##############################################################
        # Comparing average pixel value of text and background image #
        ##############################################################
        try:
            resized_img_st = ImageStat.Stat(resized_img, resized_mask.split()[2])
            background_img_st = ImageStat.Stat(background_img)

            # 경로 설정
            save_path = fr'{out_dir}/log/'
            # 이미지 저장
            resized_img_save_path = f"{save_path}_resized_img_{ 1}.png"
            resized_img.save(resized_img_save_path)

            # 통계 출력
            print(f"resized_img 이미지 저장 완료: {resized_img_save_path}")

            # 이미지 저장
            background_img_save_path = f"{save_path}_background_img_{1}.png"
            background_img.save(background_img_save_path)

            # 통계 출력
            print(f"background_img 이미지 저장 완료: {background_img_save_path}")

            resized_img_px_mean = sum(resized_img_st.mean[:2]) / 3
            background_img_px_mean = sum(background_img_st.mean) / 3

            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 전경 배경 픽셀값 비교 try resized_img : {resized_img}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 전경 배경 픽셀값 비교 background_img paste 한 후 try resized_mask : {resized_mask}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 전경 배경 픽셀값 비교 background_img paste 한 후 try resized_mask.split() : {resized_mask.split()}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 전경 배경 픽셀값 비교 background_img paste 한 후 try resized_mask.split()[2] : {resized_mask.split()[2]}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 전경 배경 픽셀값 비교 background_img paste 한 후 resized_img_st : {resized_img_st}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 전경 배경 픽셀값 비교 background_img paste 한 후 resized_img_st.mean : {resized_img_st.mean}')

            #resized_img.show()  # 이미지 출력
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 전경 배경 픽셀값 비교 resized_img 이미지 출력 : {resized_img}')
            #resized_mask.show()  # 이미지 출력
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 전경 배경 픽셀값 비교 resized_mask 이미지 출력 : {resized_mask}')

            #resized_mask.split().show()  # 이미지 출력
            #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 전경 배경 픽셀값 비교 resized_mask.split() 이미지 출력 이거 왜 프린트 안됌 : {resized_mask.split()}')
            #resized_img_st.show()  # 이미지 출력
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 전경 배경 픽셀값 비교 resized_img_st 이미지 출력 이거 왜 프린트 안됌 : {resized_img_st}')

            resized_img_save_path = f"{save_path}_resized_img_{2}.png"
            resized_img.save(resized_img_save_path)

            # 통계 출력
            print(f"resized_img 이미지 저장 완료2: {resized_img_save_path}")

            resized_mask_save_path = f"{save_path}_resized_mask_{2}.png"
            resized_mask.save(resized_mask_save_path)

            # 통계 출력
            print(f"resized_mask 이미지 저장 완료2: {resized_mask_save_path}")

            save_path_channel_1 = r"C:\Users\TAMSystech\yjh\ipynb\TextRecognitionDataGenerator\out\th_1129\NotoSansThaiLooped-Black\resized_mask_channel_1.png"
            #resized_mask.split()[1].save(save_path_channel_1)
            #print(f"resized_mask의 채널 1 이미지를 {save_path_channel_1}에 저장했습니다.")

            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 전경 배경 픽셀값 비교 background_img paste 한 후 resized_img_st.mean[:2] : {resized_img_st.mean[:2]}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 전경 배경 픽셀값 비교 background_img paste 한 후 resized_img_px_mean : {resized_img_px_mean}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 전경 배경 픽셀값 비교 background_img paste 한 후 background_img_px_mean : {background_img_px_mean}')

            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 전경 배경 픽셀값 비교 background_img paste 한 후 텍스트 픽셀 평균과 배경 픽셀 평균 차이 절대값 : {abs(resized_img_px_mean - background_img_px_mean)}')

            if abs(resized_img_px_mean - background_img_px_mean) < 15:
                print("value of mean pixel is too similar. Ignore this image")

                print("resized_img_st \n {}".format(resized_img_st.mean))
                print("background_img_st \n {}".format(background_img_st.mean))

                return
        except Exception as err:
            return

        #############################
        # Place text with alignment #
        #############################




        new_text_width, _ = resized_img.size

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Place text with alignment 텍스트를 특정 위치에 배치 resized_img.size : {resized_img.size}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Place text with alignment 텍스트를 특정 위치에 배치 new_text_width : {new_text_width}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Place text with alignment 텍스트를 특정 위치에 배치 alignment : {alignment}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py Place text with alignment 텍스트를 특정 위치에 배치 width : {width}')

        if alignment == 0 or width == -1:

            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py if alignment == 0 or width == -1 이미지를 다른 이미지 위에 붙임 margin_left : {margin_left}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py if alignment == 0 or width == -1 이미지를 다른 이미지 위에 붙임 margin_top : {margin_top}')

            # 원본
            #background_img.paste(resized_img, (margin_left, margin_top), resized_img)
            #background_img.paste(resized_img, (margin_left, margin_top))

            # 배경 이미지에 텍스트 이미지 붙이기 (투명한 영역은 텍스트가 그려진 부분만 남음)
            #background_img.paste(resized_img, (0, 0), mask=resized_img)
            background_img.paste(resized_img, (margin_left, margin_top), resized_img)


            #background_mask.paste(resized_mask, (margin_left, margin_top))

            background_img_save_path = f"{save_path}_background_img_paste_resized_{3}.png"
            background_img.save(background_img_save_path)

            # 통계 출력
            print(f"background_img 이미지 저장 완료3: {background_img_save_path}")

            background_mask_save_path = f"{save_path}_background_mask_paste_resized_{3}.png"
            background_mask.save(background_mask_save_path)

            # 통계 출력
            print(f"background_mask 이미지 저장 완료3: {background_mask_save_path}")

            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py if alignment == 0 or width == -1 background_img: {background_img}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py if alignment == 0 or width == -1 background_mask: {background_mask}')
            #background_img.show()  # 이미지 출력
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py if alignment == 0 or width == -1 background_img 이미지 출력 : {background_img}')
            #background_mask.show()  # 이미지 출력
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py if alignment == 0 or width == -1 background_mask 이미지 출력 : {background_mask}')

        elif alignment == 1:
            background_img.paste(
                resized_img,
                (int(background_width / 2 - new_text_width / 2), margin_top),
                resized_img,
            )
            background_mask.paste(
                resized_mask,
                (int(background_width / 2 - new_text_width / 2), margin_top),
            )

            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py alignment == 1 background_img: {background_img}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py if alignment == 1 background_mask: {background_mask}')
            #background_img.show()  # 이미지 출력
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py alignment == 1 background_img 이미지 출력 : {background_img}')
            #background_mask.show()  # 이미지 출력
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py alignment == 1 background_mask 이미지 출력 : {background_mask}')

            background_img_save_path = f"{save_path}_background_img_{4}.png"
            background_img.save(background_img_save_path)

            # 통계 출력
            print(f"background_img 이미지 저장 완료3: {background_img_save_path}")

            background_mask_save_path = f"{save_path}_background_mask_{4}.png"
            background_mask.save(background_mask_save_path)

            # 통계 출력
            print(f"background_mask 이미지 저장 완료3: {background_mask_save_path}")

        else:
            background_img.paste(
                resized_img,
                (background_width - new_text_width - margin_right, margin_top),
                resized_img,
            )
            background_mask.paste(
                resized_mask,
                (background_width - new_text_width - margin_right, margin_top),
            )

            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py else background_img: {background_img}')
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py else background_mask: {background_mask}')
            #background_img.show()  # 이미지 출력
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py else background_img 이미지 출력 : {background_img}')
            #background_mask.show()  # 이미지 출력
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py else background_mask 이미지 출력 : {background_mask}')

            background_img_save_path = f"{save_path}_background_img_{5}.png"
            background_img.save(background_img_save_path)

            # 통계 출력
            print(f"background_img 이미지 저장 완료3: {background_img_save_path}")

            background_mask_save_path = f"{save_path}_background_mask_{5}.png"
            background_mask.save(background_mask_save_path)

            # 통계 출력
            print(f"background_mask 이미지 저장 완료3: {background_mask_save_path}")


        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py background_img paste 한 후 resized_mask : {resized_mask}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py background_img paste 한 후 background_width : {background_width}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py background_img paste 한 후 new_text_width : {new_text_width}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py background_img paste 한 후 margin_right : {margin_right}')
        print(
            f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py background_img paste 한 후 margin_top : {margin_top}')

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py background_img paste 한 후 background_img : {background_img}')
        #background_img.show()  # 이미지 출력
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py background_img 이미지 출력 : {background_img}')


        ############################################
        # Change image mode (RGB, grayscale, etc.) #
        ############################################
        # 원본
        # background_img = background_img.convert(image_mode)
        # background_mask = background_mask.convert(image_mode)
        # convert 하면 검은 배경으로 돼서 주석처리
        # background_img = background_img.convert(image_mode)
        # background_mask = background_mask.convert(image_mode)

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 색상 모드를 변경  image_mode : {image_mode}')
        #background_img.show()  # 이미지 출력
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 색상 모드를 변경 background_img 이미지 출력 : {background_img}')
        #######################
        # Apply gaussian blur #
        #######################
        # 원본
        # gaussian_filter = ImageFilter.GaussianBlur(
        #     radius=blur if not random_blur else rnd.random() * blur
        # )
        # 블러 정도 설정
        blur = 0.0  # 블러 정도를 조절할 수 있는 값 (0에서 1 사이의 값)
        # gaussian_filter = ImageFilter.GaussianBlur(
        #     radius=blur if not random_blur else rnd.random() * blur
        # )
        # GaussianBlur 필터 생성
        gaussian_filter = ImageFilter.GaussianBlur(radius=blur)


        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py gaussian blur 전 image_mode : {image_mode}')

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py gaussian blur 전 background_img : {background_img}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py gaussian blur 전 background_mask : {background_mask}')

        #background_img.show()  # 이미지 출력
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py gaussian blur 전 background_img 이미지 출력 : {background_img}')
        #background_mask.show()  # 이미지 출력
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py gaussian blur 전 background_mask 이미지 출력 : {background_mask}')

        # 경로 설정
        save_path = fr'{out_dir}/log/'
        # 이미지 저장
        background_img_save_path = f"{save_path}_background_img_convert(image_mode)_{1}.png"
        background_img.save(background_img_save_path)

        # 통계 출력
        print(f"background_img 이미지 저장 완료: {background_img_save_path}")

        # 이미지 저장
        background_img_save_path = f"{save_path}_background_img_convert(image_mode)_{1}.png"
        background_img.save(background_img_save_path)

        # 통계 출력
        print(f"background_img 이미지 저장 완료: {background_img_save_path}")

        # 원본
        # final_image = background_img.filter(gaussian_filter)
        # final_mask = background_mask.filter(gaussian_filter)
        # 가우시안
        final_image = background_img.filter(gaussian_filter)
        final_mask = background_mask.filter(gaussian_filter)
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py gaussian blur gaussian_filter : {gaussian_filter}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py gaussian blur final_image : {final_image}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py gaussian blur final_mask : {final_mask}')

        #gaussian_filter.show()  # 이미지 출력
        #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 가우시안 필터 적용 이미지 출력 : {gaussian_filter}')
        #final_image.show()  # 이미지 출력
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 가우시안 필터 적용 final_image 이미지 출력 : {final_image}')
        #final_mask.show()  # 이미지 출력
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 가우시안 필터 적용 final_mask 이미지 출력 : {final_mask}')

        # 경로 설정
        save_path = fr'{out_dir}/log/'
        # 이미지 저장
        final_image_save_path = f"{save_path}_final_image_convert(image_mode)_가우시안 필터 적용_{1}.png"
        final_image.save(final_image_save_path)

        # 통계 출력
        print(f"final_image 이미지 저장 완료: {final_image_save_path}")



        #####################################
        # Generate name for resulting image #
        #####################################
        # We remove spaces if space_width == 0
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py space_width : {space_width}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py name_format : {name_format}')


        if space_width == 0:
            text = text.replace(" ", "")
        if name_format == 0:
            name = "{}_{}".format(text, str(index))
        elif name_format == 1:
            name = "{}_{}".format(str(index), text)
        elif name_format == 2:
            name = str(index)
        else:
            print("{} is not a valid name format. Using default.".format(name_format))
            name = "{}_{}".format(text, str(index))

        name = make_filename_valid(name, allow_unicode=True)
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py name : {name}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py extension : {extension}')

        image_name = "{}.{}".format(name, extension)
        mask_name = "{}_mask.png".format(name)
        box_name = "{}_boxes.txt".format(name)
        tess_box_name = "{}.box".format(name)

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 이미지 이름 생성 name : {name}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 이미지 이름 생성 image_name : {image_name}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 이미지 이름 생성 mask_name : {mask_name}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 이미지 이름 생성 name_format : {name_format}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 이미지 이름 생성 box_name : {box_name}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 이미지 이름 생성 tess_box_name : {tess_box_name}')

        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 이미지 이름 생성 final_image : {final_image}')

        #final_image.show()  # 이미지 출력
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 이미지 이름 생성 final_image 이미지 출력 : {final_image}')
        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py 이미지 이름 생성 final_image 이미지 출력 out_dir : {out_dir}')

        #out_dir = save_path

        # Save the image
        if out_dir is not None:

            # 경로 설정
            # save_path = fr'{out_dir}/log/'
            save_path = out_dir
            #out_dir = r'C:/Users/TAMSystech/yjh/ipynb/TextRecognitionDataGenerator/out/th_1129_2'
            #save_path = os.path.join(out_dir, 'out')

            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py out_dir 변경전 : {out_dir}')
            # 이미지 저장
            final_image_save_path = f"{out_dir}/{image_name}"
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py out_dir 변경후 : {out_dir}')

            #final_image.convert('RGB')
            final_image.save(final_image_save_path)

            # 통계 출력
            print(f"final_image 이미지 저장 완료: {final_image_save_path}")


            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py out_dir : {out_dir}')
            #out_dir = r'C:/Users/TAMSystech/yjh/ipynb/TextRecognitionDataGenerator/out/th_1129_2'

            # mask, bbox 파일 저장
            mask_bbox_out_dir = os.path.join(out_dir, 'mask_bbox')
            #out_dir = r'C:/Users/TAMSystech/yjh/ipynb/TextRecognitionDataGenerator/out/th_1129_2/out'


            # 디렉토리가 없으면 생성
            if not os.path.exists(mask_bbox_out_dir):
                os.makedirs(mask_bbox_out_dir)

            #final_image.save(os.path.join(out_dir, image_name))
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py out_dir /out 추가해서 변경 ( bbox 파일 등 저장 디렉토리 ) mask_bbox_out_dir : {mask_bbox_out_dir}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py final_image : {final_image}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py output_mask : {output_mask}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py output_bboxes : {output_bboxes}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py final_mask : {final_mask}')
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py box_name : {box_name}')
            #final_image.show()  # 이미지 출력
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py final_image 이미지 출력 : {final_image}')

            #final_image.show()  # 이미지 출력
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py final_image 이미지 출력 : {final_image}')
            #final_mask.show()  # 이미지 출력
            print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py final_mask 이미지 출력 : {final_mask}')

            output_bboxes = 1
            output_mask = 1

            if output_mask == 1:
                final_mask.save(os.path.join(mask_bbox_out_dir, mask_name))
                print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py output_mask == 1: final_mask : {final_mask}')
            if output_bboxes == 1:
                #bboxes = mask_to_bboxes(final_mask)
                print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py output_bboxes == 1 mask_to_bboxes 함수 전달 파라미터 final_image : {final_image}')

                bboxes = mask_to_bboxes(final_image)
                print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py output_bboxes == 1 bboxes : {bboxes}')
                with open(os.path.join(mask_bbox_out_dir, box_name), "w") as f:
                    for bbox in bboxes:
                        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py output_bboxes == 1 bbox : {bbox}')
                        f.write(" ".join([str(v) for v in bbox]) + "\n")
            if output_bboxes == 2:
                bboxes = mask_to_bboxes(final_mask, tess=True)
                print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py output_bboxes == 2 bboxes : {bboxes}')
                print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py output_bboxes == 2 final_mask : {final_mask}')
                print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py output_bboxes == 2 tess_box_name : {tess_box_name}')
                with open(os.path.join(mask_bbox_out_dir, tess_box_name), "w") as f:
                    for bbox, char in zip(bboxes, text):
                        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py bbox : {bbox}')
                        print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py char : {char}')

                        f.write(
                            " ".join([char] + [str(v) for v in bbox] + ["0"]) + "\n"
                        )
        else:
            if output_mask == 1:
                print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py final_image : {final_image}')
                print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py final_mask : {final_mask}')
                #final_image.show()  # 이미지 출력
                print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!data_generator.py final_image 이미지 출력 : {final_image}')

                return final_image, final_mask
            return final_image
