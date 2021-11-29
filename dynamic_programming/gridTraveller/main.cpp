#include <iostream>
#include <string>
#include <unordered_map>

typedef long long ll;

static std::unordered_map<std::string, ll> memo = std::unordered_map<std::string, ll>();

ll gridTraveller(const int m, const int n);
ll gridTraveller_memo(const int m, const int n);

int main(int argc, char const *argv[])
{
    // std::cout << gridTraveller(0, 0) << "\n";
    // std::cout << gridTraveller(0, 1) << "\n";
    // std::cout << gridTraveller(1, 0) << "\n";
    // std::cout << gridTraveller(1, 1) << "\n";
    // std::cout << gridTraveller(2, 3) << "\n";
    // std::cout << gridTraveller(3, 2) << "\n";
    // std::cout << gridTraveller(3, 3) << "\n";
    // std::cout << gridTraveller(18, 18) << "\n";
    std::cout << gridTraveller_memo(0, 0) << "\n";
    std::cout << gridTraveller_memo(0, 1) << "\n";
    std::cout << gridTraveller_memo(1, 0) << "\n";
    std::cout << gridTraveller_memo(1, 1) << "\n";
    std::cout << gridTraveller_memo(2, 3) << "\n";
    std::cout << gridTraveller_memo(3, 2) << "\n";
    std::cout << gridTraveller_memo(3, 3) << "\n";
    std::cout << gridTraveller_memo(18, 18) << "\n";
    return 0;
}

ll gridTraveller(const int m, const int n)
{
    if (m == 1 && n == 1)
        return 1;
    if (m <= 0 || n <= 0)
        return 0;

    return gridTraveller(m - 1, n) + gridTraveller(m, n - 1);
}

ll gridTraveller_memo(const int m, const int n)
{
    std::string key = std::to_string(m) + "," + std::to_string(n);
    if (memo.count(key) > 0)
        return memo[key];

    if (m == 1 && n == 1)
        return 1;
    if (m <= 0 || n <= 0)
        return 0;

    memo[key] = gridTraveller_memo(m - 1, n) + gridTraveller_memo(m, n - 1);
    return memo[key];
}