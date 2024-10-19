# %% [markdown]
# int(model.predict(np.reshape(symptoms, (1, -1)))[0])
# symptoms = [1, 2, 4, mainScript.NULLINDEX] 
# #IMPORTS

# %%
import mainScript
import numpy as np
import os

os.system("cls")

1

# %% [markdown]
# #CODE

# %%
model = mainScript.lg_model


# %%
# print("\ndiseases\n")

# for x in mainScript.diseaseNames.items():
#     print(x)

# print("\nsymptoms\n")

# for x in mainScript.symptNames.items():
#     print(x)

# %%
def MainMenu():
    mode = int()

    print("""
        MEDICAL DIAGNOSIS TESTING
        
        choose mode:
        0 - EXIT
        1 - Diagnose
        2 - Quiz(for Medical Students)

        """)

    while True:
        try:
            mode = int(input()) - 1
            if mode not in [-1, 0, 1]:
                raise Exception
            break
        except:
            print("invalid entry")
    if mode == -1:
        return None
    if mode == 0:
        Diagnose()
    else:
        Quiz()

# %%
def Diagnose():
    symptoms = []
    mode = int()
    print(
        '''
        DIAGNOSIS

        1 - add symptom
        2 - back
        
'''
    )    

    while True:
            try:
                mode = int(input()) - 1
                if mode not in [0, 1]:
                    raise Exception
                break
            except:
                print("invalid entry")

    if mode == 1:
        MainMenu()
    print("0 - Finish")
    for name, i in mainScript.symptNames.items():
        print(f"{name}")

    for i in range(17):
        while True:
            try:
                mode = int(input()) - 1
                if mode not in range(-1, len(mainScript.symptCount)):
                    raise Exception
                break
            except:
                print("invalid entry")

        if mode == -1:
            symptoms.append(mainScript.NULLINDEX)
            continue        

        symptoms.append(mode)

    if [mainScript.NULLINDEX]*mainScript.symptCount == symptoms:
        print("\n NO SYMPTOMS GIVEN\n")
        MainMenu()

    diagnosed = int(model.predict(np.reshape(symptoms, (1, -1)))[0])
    print(f"You Have {diagnosed}")
    return diagnosed

# if [mainScript.NULLINDEX]*mainScript.diseaseCount == 

# %%
def Quiz():
    MainMenu()

# %%
MainMenu()


