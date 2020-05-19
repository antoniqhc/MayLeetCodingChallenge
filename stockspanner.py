class StockSpanner(object):

    def __init__(self):
        self.prices = [0]
        self.spanner = [0]
        self.idx = 1

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        
        self.prices.append(price)
        
        if self.prices[self.idx-1] > price:
            self.spanner.append(1)
        else:
            base = self.spanner[self.idx-1]
            
            check_idx = self.idx - base
            while check_idx > 0:
                if price >= self.prices[check_idx]:
                    base += 1
                else:
                    break
                
                check_idx -= 1
            
        
            self.spanner.append(base)
            
        self.idx += 1
        
        return self.spanner[self.idx-1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)