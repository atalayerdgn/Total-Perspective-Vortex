from headers.imports import *

class pca(imp_utils,BaseEstimator, TransformerMixin):
    def __init__(self, num_components):
        self.num_components = num_components
    @property
    def num_components(self):
        """
        Get the number of components to keep
        """
        return self._num_components 
    @num_components.setter
    def num_components(self, num_components):
        """
        Set the number of components to keep
        """
        self._num_components = int(num_components)
    def fit(self, X):
        """
        Fit the model with X
        """
        N, D = X.shape
        X_normalized, mean = imp_utils.normalize(X)
        M = np.dot(X_normalized, X_normalized.T) / N
        eig_vals, eig_vecs = imp_utils.eig(M)
        eig_vecs = X_normalized.T @ eig_vecs
        principal_values = eig_vals[:self.num_components]
        principal_components = eig_vecs[:, :self.num_components]
        principal_components = np.real(principal_components)
        self.principal_values = principal_values
        self.principal_components = principal_components
        return self
    def transform(self, X):
        """
        Transform X into the reduced dimension space
        """
        N, D = X.shape
        X_normalized, mean = imp_utils.normalize(X)
        reconst = (imp_utils.projection_matrix(self.principal_components) @ X_normalized.T).T + mean
        return reconst
    def fit_transform(self, X):
        """
        fit the model with X and transform X into the reduced dimension space
        """
        N, D = X.shape
        X_normalized, mean = imp_utils.normalize(X)
        M = np.dot(X_normalized, X_normalized.T) / N
        eig_vals, eig_vecs = imp_utils.eig(M)
        eig_vecs = X_normalized.T @ eig_vecs
        principal_values = eig_vals[:self.num_components]
        principal_components = eig_vecs[:, :self.num_components]
        principal_components = np.real(principal_components)
        reconst = (imp_utils.projection_matrix(principal_components) @ X_normalized.T).T + mean
        return reconst, mean, principal_values, principal_components

# PCA (Temel Bileşen Analizi)
# PCA, boyut azaltma için kullanılan doğrusal bir dönüşüm tekniğidir.
# Verileri daha düşük boyutlu bir alt uzaya yansıtarak bir veri kümesindeki özellik sayısını azaltmak için kullanılır. 
# Temel bileşenler, verilerin en çok değiştiği yönlerdir.
# İlk temel bileşen verinin en çok değiştiği yöndür, ikinci temel bileşen verinin ikinci en çok değiştiği yöndür ve bu böyle devam eder.
# Temel bileşenler birbirlerine ortogonaldir, yani doğrusal olarak bağımsızdırlar. 
# Temel bileşenler ayrıca verilerde açıkladıkları varyans miktarına göre sıralanır.
# Birinci temel bileşen en fazla varyansı açıklar, ikinci temel bileşen ikinci en fazla varyansı açıklar ve bu böyle devam eder. 
# PCA, görüntü sıkıştırma, veri görselleştirme ve anomali tespiti gibi çeşitli uygulamalarda kullanılır.
# PCA, veri setindeki varyansı en çok koruyan doğrusal dönüşümü bulmaya çalışır.
# PCA, veri setindeki kovaryans matrisinin özvektörlerini ve özdeğerlerini hesaplayarak gerçekleştirilir.
# Kovaryans matrisi, veri setindeki özellikler arasındaki kovaryansları içeren bir kare matristir.
# Özvektörler, bir matrisin doğrusal dönüşümdeki yönleri temsil eder.
# Özdeğerler, özvektörlerin ne kadar önemli olduğunu belirten skaler değerlerdir.
# PCA, özdeğerlerin büyüklük sırasına göre sıralanmasıyla gerçekleştirilir.
# PCA, veri setindeki özellikler arasındaki korelasyonu azaltır.
# PCA, veri setindeki boyutu azaltır ve veri setindeki gürültüyü azaltır.
