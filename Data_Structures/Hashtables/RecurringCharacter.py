class RecurringCharacter:

    def lookup_bruteforce(self, arrayList):
        temp_list=[]
        length = len(arrayList)
        for i in range(length):
            if arrayList[i] in temp_list:
                return arrayList[i]
            else:
                temp_list.append(arrayList[i])
        return None

    def lookup_bruteforce2(self,arrayList):
        length = len(arrayList)
        for i in range(length):
            for j in range(i+1,length):
                if arrayList[i] == arrayList[j]:
                    return arrayList[j]
        return None

    def lookup_non_bruteforce(self,arrayList):
        dictionary = dict()
        for i in range (len(arrayList)):
            if arrayList[i] in dictionary:
                return arrayList[i]
            dictionary[arrayList[i]]=i # this can be anything
        return None
        

if __name__ == '__main__':

    rec_obj = RecurringCharacter()
    arrayList = [1, 2, 3, 10, 4, 7, 8, 9, 10]
    print(rec_obj.lookup_bruteforce(arrayList))
    print(rec_obj.lookup_bruteforce2(arrayList))
    print(rec_obj.lookup_non_bruteforce(arrayList))