# aggregator
Aggregate call records
Assumptions - file  dumped in the base directory


#Instructions

##clone github repository to a local directory
##1.create Dockerfile  --vim Dockerfile

FROM python
ARG export_file=Loans.csv
COPY $export_file /
COPY aggregate.py /
CMD ["python", "./aggregate.py"]

##2. Build the Docker image
docker build -t aggregate-loan .

##2. Run the Docker container
docker run aggregate-loan


##3. copy the resultant file from the container to your local directory , to get container_id run

docker ps -a

docker cp container_id:/Output.csv Output.csv
