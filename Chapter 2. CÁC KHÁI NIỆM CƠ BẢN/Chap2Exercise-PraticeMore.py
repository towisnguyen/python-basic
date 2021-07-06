"""
EXERCISE 1: Cho các biến với giá trị: i1 = 2, i2 = 5, i3 = -3, d1 = 2.0, d2= 5.0, d3 = -0.5
            Cho biết kq của các lệnh sau:
            a. i1 + (i2 * i3)     b. i1 * (i2 * i3)       c. i1 / (i2 + i3)       d. i1 // (i2 + i3)
            e. i1 / i2 + i3       f. i1 // i2 + i3        g. 3 + 4 + 5 / 3        h. 3 + 4 + 5 // 3
            i. (3 + 4 + 5) / 3    j. (3 + 4 + 5) // 3     k. d1 + (d2 * d3)       l. d1 + d2 * d3
            m. d1 / d2 - d3       n. d1 / (d2 - d3)       o. d1 + d2 + d3 / 3     p. (d1 + d2 + d3) / 3
            q. d1 + d2 + (d3 / 3) r. 3 * (d1 + d2) * (d1 - d3)
**SOLVE:
a. -13     e. -2.6     i. 4.0        m. 0.9      q. 6.833
b. -30     f. -3       j. 4        n. 0.36     r. 52.5
c. 1.0       g. 8.67     k. -0.5     o. 6.833
d. 1       h. 8        l. -0.5     p. 2.167
"""
i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2= 5.0
d3 = -0.5

print("a. ",i1 + (i2 * i3), "       b. ", i1 * (i2 * i3),"      c. ",i1 / (i2 + i3),
      "   d. ",i1 // (i2 + i3), "       e. ", i1 / i2 + i3,"     f. ",i1 // i2 + i3)
print("g. ", 3 + 4 + 5 / 3,"        h. ", 3 + 4 + 5 // 3,"        i. ",(3 + 4 + 5) / 3,
      "     j. ",(3 + 4 + 5) // 3, "        k. ",d1 + (d2 * d3),"         l. ",d1 + d2 * d3)
print("m. ",d1 / d2 - d3,"      n. ",d1 / (d2 - d3),"       o. ",d1 + d2 + d3 / 3,
      "     p. ",(d1 + d2 + d3) / 3,"       q. ",d1 + d2 + (d3 / 3),"       r. ",3 * (d1 + d2) * (d1 - d3))

"""
EXERCISE2: Viết ngắn gọn lại các lệnh dưới đây:
           a. x = x + 1 
           --> x += 1
           b. x = x / 2
           --> x /= 2
           c. x = x - 1
           --> x -= 1
           d. x = x + y
           --> x += y
           e. x = x - (y + 7)
           --> x -= (y + 7)
           f. x = 2 * x
           --> x *= 2
           g. number_of_closed_cases = number_of_closed_cases + 2 * ncc
           --> number_of_closed_cases += 2 * ncc
"""