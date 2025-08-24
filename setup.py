from setuptools import find_packages,setup

setup(name="END TO END BUS BOOKING",
      version="0.0.1",
      author="nithishkumar",
      author_email="mnithish1231234@gmail.com",
      packages=find_packages(),
      install_requires=["langchain-community","langgraph","fastapi","streamlit","langchain-groq"])