class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        My_list = []
        for number in range(1, n+1):
            if number % 15 == 0:
                My_list.append("FizzBuzz")
            elif number % 5 == 0:
                My_list.append("Buzz")   
            elif number % 3 == 0:
                My_list.append("Fizz")
            else:
                My_list.append(str(number))
        return My_list
