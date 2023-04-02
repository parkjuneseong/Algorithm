#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int c, n;

// 벡터값들의 합 구하는 함수
int sum(vector<int> v) {
    int returnValue = 0;
    for (int i = 0; i < v.size(); i++) {
        returnValue += v[i];
    }
    
    return returnValue;
}

// 평균을 리턴해주는 함수
double aver(int x, vector<int> v) {
    return sum(v) / x;
}

// 평균보다 높은 학생이 몇명인지 리턴해주는 함수
int studentCount(double average, vector<int> v) {
    int cnt = 0;
    for (int i = 0; i < v.size(); i++) {
        if (average < v[i]) {
            cnt++;
        }
    }
    
    return cnt;
}

int main() {
    cin >> c;
    while(c--) {    // c번 돈다
        int n;
        cin >> n;
        vector<int> v;
        for (int i = 0; i < n; i++) {
            int a;
            cin >> a;
            v.push_back(a);
        }
        double average = aver(n, v);
        int sCnt = studentCount(average, v);
        cout << fixed;
        cout.precision(3);
        double percent = (double(sCnt) / double(n)) * 100;
        
        cout << percent << "%\n";
    }
    
    return 0;
}