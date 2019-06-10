#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 12:14:49 2019

@author: dixon.maina
"""

import csv
from multiprocessing import Process

def run_cpu_tasks_in_parallel(tasks):
    running_tasks = [Process(target=task) for task in tasks]
    for running_task in running_tasks:
        running_task.start()
    for running_task in running_tasks:
        running_task.join()

def import_loans(input_file='Loans.csv'):
        extract = csv.DictReader(open(input_file))
        callrecords = []
        for row in extract:
            callrecords.append(row)
        return callrecords


class CallRecord:
    def __init__(self, callrecord_attributes):
        for k, v in callrecord_attributes.items():
            setattr(self, k, v)
    
       
class CallRecords:
    
    def __init__(self, imported_list):
        self.callrecord_list = []    
        for callrecord in imported_list:
            #self.callrecord_list.append(CallRecord({'msisdn':row[0],'network':row[1],'date':row[2],'product':row[3],'amount':row[4]}))
            self.callrecord_list.append(CallRecord(callrecord))
    def aggregate(self):
        summaries = {}
        
        for row in self.callrecord_list:
            key=(row.Network,row.Product)
            summaries[key] = summaries.setdefault(key, 0)+float(row.Amount)
        
        with open('aggregate.csv','w') as out_file:
            writer = csv.writer(out_file)
            for key, value in sorted(summaries.items()):
                row = list(key)+[value]
                writer.writerow(row)    
    
    def print_callrecords(self):
        for callrecord in self.callrecord_list:
            print(callrecord.__dict__)  
if __name__ == '__main__':
    df_callrecords = CallRecords(import_loans())
    #df_callrecords.aggregate()
    
    run_cpu_tasks_in_parallel([
    lambda: df_callrecords.aggregate(),
    lambda: df_callrecords.aggregate(),
    ])
    #db_callrecords.print_callrecords()
  