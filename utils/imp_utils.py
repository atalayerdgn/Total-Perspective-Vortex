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
