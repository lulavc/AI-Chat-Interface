from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ai_chat_interface",
    version="1.0.0",
    author="lulzactive",
    author_email="your.email@example.com",
    description="Uma interface de chat IA com sistema multi-agente e modelos customizados",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lulzactive/ai-chat-interface",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "ai-chat=ai_chat_interface.app:main",
        ],
    },
)
