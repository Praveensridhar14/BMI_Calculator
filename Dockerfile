FROM python:3
RUN python3 -m pip install virtualenv
RUN virtualenv BMI_calculator_env
RUN . /BMI_calculator_env/bin/activate
WORKDIR .

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "bmi_calculator.py" ]
CMD [ "bmi_unit_test.py" ]
ENTRYPOINT ["python3"]