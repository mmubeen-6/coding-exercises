#include <iostream>
#include <vector>
#include <unordered_map>

static std::unordered_map<int, long> m = std::unordered_map<int, long>();

long fib(const int number);
long fib_memo(const int number, std::unordered_map<int, long> &memo = m);

int main(int argc, char const *argv[])
{
    // std::cout << fib(6) << "\n";
    // std::cout << fib(7) << "\n";
    // std::cout << fib(8) << "\n";
    // std::cout << fib(50) << "\n";
    std::cout << fib_memo(6) << "\n";
    std::cout << fib_memo(7) << "\n";
    std::cout << fib_memo(8) << "\n";
    std::cout << fib_memo(50) << "\n";
    return 0;
}

long fib(const int number)
{
    if (number == 1 || number == 2)
        return 1;

    return fib(number - 1) + fib(number - 2);
}

long fib_memo(const int number, std::unordered_map<int, long> &memo)
{
    if (memo.count(number) > 0)
        return memo[number];

    if (number == 1 || number == 2)
        return 1;

    memo[number] = fib_memo(number - 1, memo) + fib_memo(number - 2, memo);
    return memo[number];
}