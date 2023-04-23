%load_ext autoreload
%autoreload 2
from LinearRegressionSkeleton import LinearRegression

X = df['petal width (cm)'].values
y = df['sepal length (cm)'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

ln = LinearRegression()
ln.fit(X_train, y_train)
pred = ln.predict(X_test)