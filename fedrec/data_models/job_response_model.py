from typing import Dict

from fedrec.data_models.messages import Message
from dataclasses import dataclass


@dataclass
class JobResponseMessage(Message):
    '''
    Creates message objects for job response message

    Attributes:
    -----------
        job_type : str
            type of job (train/test)
        senderid : str
            id of sender
        receiverid : str
            id of receiver
        results : dict
            dict of results obtained from job completion
        errors : null
    '''
    __type__ = "JobResponseMessage"

    def __init__(self, job_type, senderid, receiverid):
        super().__init__(senderid, receiverid)
        self.job_type: str = job_type
        self.results = {}
        self.errors = None

    @property
    def status(self):
        '''
        Check if errors is None and returns response
        message status accordingly
        '''
        if self.errors is None:
            return True
        else:
            return False

    def serialize(self, obj):
        response_dict = {}
        response_dict["job_type"] = obj.job_type
        response_dict["senderid"] = obj.senderid
        response_dict["receiverid"] = obj.receiverid
        response_dict["results"] = self.serialize_attribute(
            obj.results)

        # return self.serialization_strategy.unparse(response_dict)
        return response_dict

    def deserialize(self, obj: Dict):
        obj = self.serialization_strategy.parse(obj)

        return JobResponseMessage(obj["job_type"],
                                  obj["senderid"],
                                  obj["receiverid"])
