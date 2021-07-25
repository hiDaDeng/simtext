from setuptools import setup
import setuptools

setup(
    name='simtext',     # 包名字
    version='1.2',   # 包版本
    description='文本、文档相似性计算',   # 简单描述
    author='大邓',  # 作者
    author_email='thunderhit@qq.com',  # 邮箱
    url='https://github.com/thunderhit/simtext',      # 包的主页
    packages=setuptools.find_packages(),
    install_requires=['scikit-learn', 'jieba'],
    python_requires='>=3.5',
    license="MIT",
    keywords=[
        'text similarity',
        '文本相似性',
        'text mining',
        '文本挖掘'
    ],
    long_description=open('README.md').read(), # 读取的Readme文档内容
    long_description_content_type="text/markdown")  # 指定包文档格式为markdown

