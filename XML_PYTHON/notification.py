from cmath import pi
from bs4 import BeautifulSoup
from matplotlib.style import available

with open("LEF_XML.xml") as fp:
    soup = BeautifulSoup(fp, 'xml')

# print(soup.find_all('metadata'))
# print(soup.find('metadata').value)

# list=soup.find('metadata').get_text()

# print(list)



# FETCHING ALL THE DATA PRESENT IN DATA TAG
#print(soup.find('metadata'))
# list=soup.find("data")
#print(soup.find("data"))

# for data in list:
#     print(data)


# # entity name
# print("Printing the entity name: ")
# print(soup.find("regulated").text)
# entity=soup.find("regulated")


# entity value
entity="State Bank Of India"



# FETCHING THE ENTITIES WHICH ARE COUNTER PARTY
print("printing the counter party values: ")
print(soup.find("counterparties").text)
counterParty=soup.find("counterparties")

for counterParties in counterParty:
    print(counterParties)


# fetching the exposure values
print("Printing the exposure values: ")
expValue=soup.find("exposurevalues").text
print(expValue)

# fetching the available available eligible capital base

print("Printing the available eligible capital base: ")
availableCapita=soup.find("availableeligiblecapitalbase").text
print(availableCapita)


# fetching the group counter parties
print("Printing the group counter parties: ")
groupcounterparty=soup.find("groupcounterparties").text
print(groupcounterparty)



# #If "entity" is Single Counterparty:
print("single counter party")
cParty=soup.find("counterparties")
cpartychild=cParty.findChildren("counterparty")
print(cpartychild)

# If entity is group counterparty
print("Group counter party")
gParty=soup.find("groupcounterparties")
gPartychild=gParty.findChildren("groupcounterparty")
print(gPartychild)




# finding out the single counter party
print("Finding out the single counter party")
for party in cpartychild:
    if entity==party:
        print("Entity is single counter party")
        if int(expValue)<=0.2*availableCapita:
            print("exp value is less than 20% of available capita")         # if exposure value is less than 20%
        else:
            if int(expValue)<=0.25*availableCapita:
                print("exp value is less than 25% of available capita")         # if exposure value is less than 25% (board approval)
            else:
                print("Inform co , RBI")
    else:
        print("inform CO ,RBI")
    

# finding out group counter party

for party in gPartychild:
    if entity==party:

        if int(expValue)<=0.25*availableCapita:
            pass
        else:
            print("Inform CO , RBI")








 





