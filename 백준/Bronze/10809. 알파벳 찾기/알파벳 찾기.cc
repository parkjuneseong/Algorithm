//
//  main.cpp
//  beakjoon
//
//  Created by 박준성 on 2022/12/29.
//ios_base::sync_with_stdio(false);
//cin.tie(NULL);
//int argc, char const *argv[]
//long long sum(std::vector<int> &a){
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
//vector<int> v; //벡터의 값 v;
int main(){
    char a[101];//문자 101 개의 배열생성 하고 입력
    cin >> a;
    char exm[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    //exm의 알파벳 26개를 입력하고
    for(int i =0; i< 26;i++){//포문으로 26개의 결과를 돌려
        int check = -1; // 체크라는 변수를 만들어 -1로 초기화
        int size = strlen(a); //입력받는 문자의 사이즈가 될 변수 선언 strlen을 사용하여 a만큼의 크기를 설정
        for(int j =0; j < size ; j++){ //a의 크기만큼 포문 j로 돌려준뒤
            if(a[j] == exm[i]){ //만약 사이즈j와 exm[i]가 같다면
                check = j; //체크를 j로 입력 예를들어 a[j]의 첫번째는 b <--이게 exm[]에서는 index[1]자리에 있어 1을 출력해야함
                break;
            }
        }
        cout << check <<' '; //출력
    }
    return 0 ;
}
    
