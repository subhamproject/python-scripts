import json
import requests
import time



job_name = "testjob"   #Give your job name here


def jenkins_job_status(job_name):
        
        try:
                url  = "https://your_jenkins_endpoint/job/%s/lastBuild/api/json" %job_name   #Replace 'your_jenkins_endpoint' with your Jenkins URL
                while True:
                        data = requests.get(url).json()
                        if data['building']:
                                time.sleep(60)
                        else:
                                if data['result'] == "SUCCESS":

                                        print "Job is success"
                                        return True
                                else:
                                        print "Job status failed"
                                        return False

                
        except Exception as e:
                print str(e)
                return False




if __name__ == "__main__":

        if jenkins_job_status(job_name):

                print "Put your autmation here for 'job is success' condition"

        else:
                print "Put your autmation here for 'job is failed' condition"                
