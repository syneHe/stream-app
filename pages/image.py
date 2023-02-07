import cv2
import numpy as np
import streamlit as st

# 设置标题
st.title('XXXX演示')

# 上传图片并展示
uploaded_file = st.file_uploader("上传一张图片", type="jpg")

if uploaded_file is not None:
    # 将传入的文件转为Opencv格式
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    # 展示图片
    st.image(opencv_image, channels="BGR")
  	# 保存图片
    cv2.imwrite('test.jpg',opencv_image)
# 然后就可以用这个图片进行一些操作了
