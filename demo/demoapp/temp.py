# class Solution:
#     def __init__(self, days):
#         if type(days) == 'int':
#             raise TypeError("Days argument should be of integer type")
#         self.days = days
#         self.ways_to_attend = self._ways_to_attend_classes()
    
#     def number_of_ways_to_attend_classes(self):
#         return len(self.ways_to_attend)

#     def probability_to_miss_gradution_ceremony(self):
#         ineligible_ways = self._ineligible_ways_to_attend_classes()
#         return len(ineligible_ways) / self.number_of_ways_to_attend_classes()

#     def _ways_to_attend_classes(self):
#         arr = []
#         pattern = ""
#         self._util(self.days, pattern, arr)
#         return arr
    
#     def _util(self, days, pattern, arr):
#         if days == 0:
#             arr.append(pattern)
#         else:
#             # At any given day there are only two possibalities
#             self._util(days - 1, pattern + 'A', arr)  # absent in class
#             self._util(days - 1, pattern + 'P', arr)  # present in class
    
#     def _ineligible_ways_to_attend_classes(self):
#         # Filter out ways where 4 or more consective days classes are missed
#         return list(filter(lambda way: "AAAA" in way, self.ways_to_attend))
    
# xyz = Solution(5)
# print(xyz.number_of_ways_to_attend_classes())
# print(xyz.probability_to_miss_gradution_ceremony())




# def fact(n):

#     if n == 0:

#         return 1

#     else:

#         n = n * fact(n-1)

#     return n

# n = 10

# i = int(n/2)

# w = 0

# p = 0


 

# while i <= n:

#     w = w + int(fact(i+1) / (fact(n-i) * fact(2*i-n+1)))

#     if i < n:

#         p = p + int(fact(i) / (fact(n-i-1) * fact(2*i-n+1)))

#     i = i + 1

# print(w)

# print(str(p) + "/" + str(w))




def count_no_ways_toattend(n):
    dp = [[0]*4 for _ in range(n+1)]
    print(dp)
    dp[0][0] = 1
    for i in range(1, n+1):
        # attended on day i
        dp[i][0] = sum(dp[i-1][:4])
        for j in range(1, 4):
            dp[i][j] = dp[i-1][j-1]
        print(dp)
        
    return str(sum(dp[n][1:])) + '/' + str(sum(dp[n]))

print(count_no_ways_toattend(5))