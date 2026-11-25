class Solution:
    def nextHappy(self, n):
        def happy(x, seen):
            if x == 1:
                return True

            if x in seen:
                return False

            seen.add(x)
            s = sum(int(d)**2 for d in str(x))

            return happy(s, seen)

        n += 1
        while not happy(n, set()):
            n += 1

        return n