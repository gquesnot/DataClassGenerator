
import json

from DataClassGenerator import DataClassGenerator
from created_data_class.datasFrame import DatasFrame

if __name__ == '__main__':

    with open("matchtimeline2.json", "r") as f:
        jsonDatas = json.load(f)

    # instantiate the DataClassGenerator with the path to the folder you want to create them
    dcg = DataClassGenerator("created_data_class")
    # generate dataclass in the folder with "DatasFrame"  as Top Class  and json datas as input
    dcg.generateDataClass("datasFrame", jsonDatas)
    # get your nested Obj
    obj = DatasFrame.from_dict(jsonDatas)
    print(obj)
    print(json.dumps(obj.to_dict(), indent=4))
