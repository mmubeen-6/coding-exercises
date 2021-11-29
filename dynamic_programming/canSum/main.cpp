#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

static std::unordered_map<int, bool> m = std::unordered_map<int, bool>();

bool canSum(std::vector<int>, int);
bool canSum_memo(std::vector<int>, int, std::unordered_map<int, bool> &memo = m);

int main(int argc, char const *argv[])
{
    // std::cout << canSum(std::vector<int>{2, 3}, 7) << "\n";
    // std::cout << canSum(std::vector<int>{5, 3, 4, 7}, 7) << "\n";
    // std::cout << canSum(std::vector<int>{2, 4}, 7) << "\n";
    // std::cout << canSum(std::vector<int>{2, 3, 5}, 8) << "\n";
    // std::cout << canSum(std::vector<int>{7, 14}, 300) << "\n";
    std::cout << canSum_memo(std::vector<int>{2, 3}, 7) << "\n";
    m.clear();
    std::cout << canSum_memo(std::vector<int>{5, 3, 4, 7}, 7) << "\n";
    m.clear();
    std::cout << canSum_memo(std::vector<int>{2, 4}, 7) << "\n";
    m.clear();
    std::cout << canSum_memo(std::vector<int>{2, 3, 5}, 8) << "\n";
    m.clear();
    std::cout << canSum_memo(std::vector<int>{7, 14}, 300) << "\n";
    m.clear();
    return 0;
}

bool canSum(std::vector<int> numbers, int targetSum)
{
    bool ret{false};

    if (targetSum == 0)
        ret = true;
    else if (targetSum < 0)
        ret = false;
    else
    {
        for (const auto &n : numbers)
            ret = ret || canSum(numbers, targetSum - n);
    }

    return ret;
}

bool canSum_memo(std::vector<int> numbers, int targetSum, std::unordered_map<int, bool> &memo)
{
    if (memo.count(targetSum) > 0)
        return memo[targetSum];

    bool ret{false};

    if (targetSum == 0)
        ret = true;
    else if (targetSum < 0)
        ret = false;
    else
    {
        for (const auto &n : numbers)
            ret = ret || canSum_memo(numbers, targetSum - n, memo);
    }

    memo[targetSum] = ret;
    return memo[targetSum];
}