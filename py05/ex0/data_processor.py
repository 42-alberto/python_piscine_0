import typing
import abc


class DataProcessor(abc.ABC):


    @abc.abstractmethod
    def validate(self, data: any) -> bool:
        #heck whether the input data are appropriate
        ...

    @abc.abstractmethod
    def ingest(self, data: any) -> None:
        #process the input data
        ...

    def output(self) -> tuple[int, str]:
        # The output method will extract the oldest piece of data stored 
        # internally in the data processor.
        # along with the associated processing rank within the data processor.
        # The piece of data is then removed from the data processor.
        ...


class NumericProcessor(DataProcessor):

    values: list [str] = []

    def __init__(self):
        ...

    def validate(self, data: any) -> bool:
        if not isinstance(data, int | float):
            return False
        if isinstance(data, list):
            for d in data if not isinstance(d, int | float):
                return False
        return True

    def ingest(self, data: int | float | list[int | float]):
        try:
            self.values.append(str(data))
        except:
            print(f"Test invalid ingestion of string '{data}' "
                  "without prior validation:")


class TextProcessor(DataProcessor):
    def __init__(self):
        ...

    def validate(self, data: any) -> bool:
        return isinstance(data, str | list[str])

    def ingest(data: str | list[str]):
        #It stores the data internally, extracted using the output method
        ...


class LogProcessor(DataProcessor):
    def __init__(self):
        ...

    def validate(self, data: any) -> bool:
        return isinstance(data, dict[str, str] | list[dict[str, str]])

    def ingest(data: dict[str, str] | list[dict[str, str]]):
        ...


if __name__ == "__main__":

    # Create instances for each specialized class.
    # Test valid and invalid data for each class through the validate method.
    # Test at least one invalid data item with the ingest method without prior
    #   validation,and check that it raises an exception (This will leave you
    #   with a mypy warning, onpurpose.)
    # Ingest various data for each data processor and then extract it using
    #   output.

    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate("hello")}")
    numeric.ingest("foo")

    print("Testing Text Processor...")

    print("Testing Log Processor...")

    pass