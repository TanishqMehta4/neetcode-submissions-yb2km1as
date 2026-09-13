class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for asteroid in asteroids:
            while s and s[-1] > 0 and asteroid < 0:
                diff = asteroid + s[-1]
                if diff<0:
                    s.pop()
                elif diff > 0:
                    asteroid = 0
                else:
                    s.pop()
                    asteroid=0
            if asteroid:
                s.append(asteroid)
        return s
            