from abc import ABC, abstractmethod
import logging 
from requests.exceptions import RequestException

class BaseConnector(ABC):

    def __init__(self, source_name: str):
        self.source = source_name