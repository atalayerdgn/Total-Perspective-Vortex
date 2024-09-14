from headers.imports import *

class imp_utils:
    def __init__(self):
        pass
    ## PCA
    @staticmethod
    def normalize(X):
        """ 
        Normalize the given dataset X
        """
        N, D = X.shape #N:Satır sayısı, D:Sütun sayısı
        mu = np.zeros((D,)) #Sütun sayısı kadar sıfırlardan oluşan bir dizi oluşturuldu
        mu = np.mean(X,axis = 0) #X'in sütunları üzerinde ortalama alındı
        Xbar = X - mu #X ve mu çıkarıldı
        return Xbar, mu #Xbar ve mu döndürüldü
    @staticmethod
    def eig(S): # Özdeğer ve özvektörleri hesaplamak için kullanılan fonksiyon
        """
        Compute the eigenvalues and the eigenvectors of a given matrix S
        """
        eigvals, eigvecs = np.linalg.eig(S) # S matrisinin özdeğer ve özvektörleri hesaplandı
        sort_indices = np.argsort(eigvals)[::-1] # Özdeğerlerin büyüklük sırasına göre sıralanması
        return eigvals[sort_indices], eigvecs[:, sort_indices] # Sıralanmış özdeğerler ve özvektörler döndürüldü
    @staticmethod
    def projection_matrix(B):# Yansıtma matrisi oluşturmak için kullanılan fonksiyon
        """
        Compute the projection matrix onto the space spanned by the columns of a given matrix B
        """
        P = B @ np.linalg.inv(B.T @ B) @ B.T # Yansıtma matrisi hesaplandı
        return np.eye(B.shape[0]) @ P # Yansıtma matrisi döndürüldü
    ## SVM Classifier
    @staticmethod
    def find_weight(X, y):
        """
        Find the weight vector w
        """
        w = np.linalg.inv(X.T @ X) @ X.T @ y
        return w
    @staticmethod
    def find_bias(self, X, y, w):
        """
        Find the bias term b
        """
        b = np.mean(y - X @ w)
        return b
    @staticmethod
    def linear_hyperplane(X, w, b):
        """
        Find the linear hyperplane
        """
        return pow(w,X.T) + b
    @staticmethod
    def find_xi(X, y, w, b):
        """
        find the distance of each point from the hyperplane
        """
        xi = []
        for i in range(len(X)):
            xi.append(imp_utils.distance(X[i], w, b))
        return xi
    @staticmethod
    def distance(x_i, w, b):
        """
        find the distance of a point from the hyperplane
        """
        w_norm = np.linalg.norm(w)
        distance = (np.dot(w, x_i) + b) / w_norm
        return distance
    
    
