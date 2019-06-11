FROM python
ARG export_file=Loans.csv
COPY $export_file /
COPY aggregate.py /
CMD ["python", "./aggregate.py"]
