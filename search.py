import json

file = open('data/dataset.json')
 
json_data= dict(json.load(file))

olvlRes = {
            "B": 5,
            "S": 2,
            "C": 1
        }
alvlRes = {
            "B": 2,
            "A": 1,
            
        }
def calcGrade(result):
    val = 0
    count = 0
    for k in result:
        count+=int(result[k])
        if(k=="A"):
            val+=75*int(result[k])
        elif(k=="B"):
            val+=65*int(result[k])
        elif(k=="D"):
            val+=75*int(result[k])
        elif(k=="C"):
            val+=55*int(result[k])
        elif(k=="S"):
            val+=45*int(result[k])
    return val/count


def searchCourse(result, type="o"):
    grade = calcGrade(result)
    courses = []
    for key in json_data:
        requiredGrade = calcGrade(json_data[key][type+"lvlRes"])
        if(grade>=requiredGrade):
            courses.append(json_data[key])
        else:
            # print(json_data[key][type+"lvlRes"])
            # print(grade)
            # print(requiredGrade)
            pass
    return courses

# print(searchCourse(olvlRes))
# print(searchCourse(alvlRes,"a")
            




