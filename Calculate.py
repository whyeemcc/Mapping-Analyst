class Cal:
    
    def __init__(self):
        pass
    
    def mean(self,X):
        return sum(X)/len(X)

    def median(self,X):
        A = sorted(X)
        L = len(A)
        if (L % 2) == 0:
            return ( A[int(L/2)-1] + A[int(L/2)] )/2
        else:
            return A[int((L-1)/2)]

    def standard(self,X):
        mean = sum(X)/len(X)
        B = [(i-mean)**2 for i in X]
        return (sum(B)/len(X))**0.5
        
    def _3sigma(self,X):
        return 3*self.standard(X)

    def sigmaFilter(self,data,die):
        # delete the value that lager the range from 3sigma to median repeatedly
        L = len(data)
        while True:
            X,Y = [],[]
            median = self.median(data)
            spec = self._3sigma(data) 
            # keep the value which is qualified
            for x,y in zip(data,die):
                if abs(x-median) <= spec:
                    X.append(x)
                    Y.append(y)
            data,die = X,Y
            # check the new list length, if it equals the old list, break
            if L == len(X):
                break
            L = len(X)
        return (data,die)