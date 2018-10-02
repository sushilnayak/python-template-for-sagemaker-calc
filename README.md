1. Command to install virtualenv:

    `pip install virtualenv`

2. Steps to create a new virtual environment:

    **For Windows**
    ```
    git clone https://github.com/sushilnayak/python-template-for-sagemaker-calc.git
    cd python-template-for-sagemaker-calc
    virtualenv venv -p c:\ProgramData\Anaconda3\python.exe
    "venv\Scripts\activate.bat"
    ```
    
    **For Linux/Ubuntu**
    ```
    git clone https://github.com/sushilnayak/python-template-for-sagemaker-calc.git
    cd python-template-for-sagemaker-calc
    which python
    virtualenv venv -p /usr/bin/python
    source venv/bin/activate
    ```

3. Save download packages information into requirements.txt file :

    `pip freeze > requirements.txt`

4. To install the packages from requirements.txt :

    `pip install -r requirements.txt`

5. exit virtual environment:

    **For Windows**
    
    `"venv\Scripts\deactivate.bat"`
    
    **For Linux\Ubuntu**
    
    `deactivate`
