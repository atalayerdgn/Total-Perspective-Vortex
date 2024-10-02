from headers.imports import *

class Pipeline(pipeline_utils, BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    @staticmethod
    def create_pipeline():
        pipeline = Pipeline([
    ('playback', DataPlayback(file_path='.')),
    ('dim_reduction', pca(n_components=10)),
    ('classifier', Iclassifier())
])
        return pipeline
    def execute_pipeline(self, pipeline, X_train, y_train, X_test, y_test):
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy
