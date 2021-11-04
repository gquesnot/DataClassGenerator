import re

import os

from os import path


def ownCapitalize(string):
    return re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), string, 1)


class DataClassGenerator:
    baseDataClassStr = \
        "@dataclass\n" + \
        "class {}:\n\n"
    headStr = "from dataclasses import dataclass, field, asdict\nfrom typing import Any, Union, List, Dict\nfrom dacite import from_dict\n"
    postStr = "    @classmethod\n" \
              "    def from_dict(cls, data: Dict[str, Any]) -> \"{}\":\n" \
              "        return from_dict(cls, data=data)\n\n" \
              "    def to_dict(self) -> Dict[str, Any]:\n" \
              "        return asdict(self)\n"
    numberStr = [str(i) for i in range(0, 10)]

    def __init__(self, basePath):
        self.basePath = basePath
        self.dataClassSet = set()
        if not path.exists(self.basePath):
            os.mkdir(self.basePath)



    @staticmethod
    def nameToClass(name):
        if name[-1] == "s":
            name = name[:-1]
        return name

    def generateDataClass(self, name, datas):
        nameWS = self.nameToClass(name)

        if nameWS not in self.dataClassSet:
            newClass = True
        else:
            newClass = False
        newClassStr = self.baseDataClassStr.format(ownCapitalize(nameWS))
        newBaseStr = []
        newDefaultStr = []
        newHeadStr = self.headStr
        self.dataClassSet.add(name)
        if isinstance(datas, dict):

            for k, v in datas.items():
                if isinstance(v, dict):
                    if "1" in v.keys():
                        isFake = True
                        v = v["1"]
                    else:
                        isFake = False

                    className = self.nameToClass(k)
                    attrType = ownCapitalize(className) if not isFake else f"Dict[str, {ownCapitalize(className)}]"
                    classPath = f'{self.basePath}.{className}'
                    newHeadStr += f"from {classPath} import {ownCapitalize(className)}\n"

                    self.generateDataClass(k, v)
                    newBaseStr.append(f"    {k}: {attrType}")
                elif isinstance(v, list):
                    if len(v) > 0:
                        v = v[0]
                        if not isinstance(v, str) and not isinstance(v, int) and not isinstance(v,
                                                                                                float) and not isinstance(
                            v, bool):

                            className = self.nameToClass(k)
                            attrType = f"List[{ownCapitalize(className)}]"
                            if isinstance(v, dict):
                                classPath = f'{self.basePath}.{className}'
                                newHeadStr += f"from {classPath} import {ownCapitalize(className)}\n"

                                self.generateDataClass(k, v)
                            if k not in self.dataClassSet:
                                if isinstance(v, list) and len(v) > 0:
                                    val = v[0]
                                    if not isinstance(val, str) or \
                                            not isinstance(val, int) or \
                                            not isinstance(val, float) or \
                                            not isinstance(val, bool):
                                        self.generateDataClass(k, val)
                        else:
                            if isinstance(v, str):
                                className = "str"
                            elif isinstance(v, int):
                                className = "int"
                            elif isinstance(v, float):
                                className = "float"
                            else:
                                className = "bool"
                            attrType = f"List[{className}]"
                    newBaseStr.append(f"    {k}: {attrType}")
                else:
                    if isinstance(v, str):
                        attrType = "str"
                        defaultVal = f"\"{v}\""
                    elif isinstance(v, int):
                        attrType = "int"
                        defaultVal = v
                    elif isinstance(v, float):
                        attrType = float
                        defaultVal = v
                    else:
                        attrType = "bool"
                        defaultVal = "True" if v else "False"

                    newDefaultStr.append(f"    {k}: {attrType} = field(default=None)")

            if len(newBaseStr):
                newClassStr += "\n".join(newBaseStr) + "\n"
            if len(newDefaultStr):
                newClassStr += "\n".join(newDefaultStr) + "\n"

            with open(self.basePath + f"/{nameWS}.py", "w+") as f:
                f.write(f"{newHeadStr}\n{newClassStr}\n{self.postStr.format(ownCapitalize(nameWS))}")

