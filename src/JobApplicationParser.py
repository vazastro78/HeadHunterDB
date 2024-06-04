
from abc import ABC, abstractmethod


class JobApplicationParser(ABC):
    def __init__(self, json_filename):
        self.json_filename = json_filename

    @abstractmethod
    def load_vacancies(self, keyword):
        pass

    @abstractmethod
    def save_to_file(self):
        pass

    @abstractmethod
    def load_from_file(self):
        pass

    @abstractmethod
    def parse_and_verify(self):
        pass
