import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from src.DecisionTreeClassifier import DecisionTreeClassifier


data = pd.read_csv("data/NJ.csv")

X = data.iloc[:,:-1].values
Y = data.iloc[:,-1].values.reshape(-1,1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.2, random_state=41)


dt = DecisionTreeClassifier(100,11)
dt.fit(X_train,Y_train)
Y_pred = dt.predict(X_test)
print(accuracy_score(Y_test, Y_pred))


'''
A tanítás lényegének felfogásával kezdődött a művelet.
Miután felfiteltem az adott csv-t a DecisionTreeClassifier osztályomra, próbálkoztam a lehető legjobb accuracy elérésével. Ezek eredménye lentebb látható. 
Első neki futásra kézzel írogattam be a konstruktorba az értékeket egy tök légből kapott (50,9) párral, innen indultam el felfelé. 
Mivel ez lassúnak bizonyult "autómatizáláson" kezdtem el gondolkodni, de végül maradtam a beirogatós technikánál.
'''

'''
min_samples_split,max_depth  -->  accuracy

50,9    --> 0.7981666666666667
50,11   --> 0.8026666666666666
50,12   --> 0.8
75,11   --> 0.8033333333333333
75,12   --> 0.8010833333333334
90,11   --> 0.803
100,11  --> 0.8035833333333333  (best)
101,11  --> 0.80325
102,11  --> 0.80325
101,12  --> 0.8021666666666667
'''