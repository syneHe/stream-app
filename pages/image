# 导入框架、包和库
import streamlit as st
from PIL import Image
from io import BytesIO
import numpy as np
import cv2 # 计算机视觉

# 将图像转换为水彩素描的功能
def convertto_watercolorsketch(inp_img):
    img_1 = cv2.edgePreservingFilter(inp_img, flags=2, sigma_s=50, sigma_r=0.8)
    img_water_color = cv2.stylization(img_1, sigma_s=100, sigma_r=0.5)
    return(img_water_color)

# 将图像转换为铅笔素描的功能
def pencilsketch(inp_img):
    img_pencil_sketch, pencil_color_sketch = cv2.pencilSketch(
        inp_img, sigma_s=50, sigma_r=0.07, shade_factor=0.0825)
    return(img_pencil_sketch)

# 加载图像的函数
def load_an_image(image):
    img = Image.open(image)
    return img

# 具有 Web 应用程序代码的主函数
def main():
    
    # 基本 heading 和 titles
    st.title('WEB APPLICATION TO CONVERT IMAGE TO SKETCH')
    st.write("This is an application developed for converting\
    your ***image*** to a ***Water Color Sketch*** OR ***Pencil Sketch***")
    st.subheader("Please Upload your image")
    
    # 图片文件上传器
    image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])

    # 如果图像已上传，则执行这些代码行
    if image_file is not None:
        
        # 选择框（下拉选择水彩/铅笔素描）
        option = st.selectbox('How would you like to convert the image',
                            ('Convert to water color sketch',
                            'Convert to pencil sketch'))
        if option == 'Convert to water color sketch':
            image = Image.open(image_file)
            final_sketch = convertto_watercolorsketch(np.array(image))
            im_pil = Image.fromarray(final_sketch)

            # 两列显示原始图像和应用水彩素描效果后的图像
            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image(load_an_image(image_file), width=250)

            with col2:
                st.header("Water Color Sketch")
                st.image(im_pil, width=250)
                buf = BytesIO()
                img = im_pil
                img.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Download image",
                    data=byte_im,
                    file_name="watercolorsketch.png",
                    mime="image/png"
                )

        if option == 'Convert to pencil sketch':
            image = Image.open(image_file)
            final_sketch = pencilsketch(np.array(image))
            im_pil = Image.fromarray(final_sketch)
            
            # 两列显示原始图像和应用铅笔素描效果后的图像
            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image(load_an_image(image_file), width=250)

            with col2:
                st.header("Pencil Sketch")
                st.image(im_pil, width=250)
                buf = BytesIO()
                img = im_pil
                img.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Download image",
                    data=byte_im,
                    file_name="watercolorsketch.png",
                    mime="image/png"
                )


if __name__ == '__main__':
    main()
