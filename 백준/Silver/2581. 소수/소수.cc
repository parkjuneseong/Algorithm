//
//  main.cpp
//  beakjoonMath
//
//  Created by June on 2022/10/13.
//

#include <iostream>
using namespace std;
int main(){
    int min , max ;
    int count = 0;
    int ncount = 0;
    int result  = 0, minnum = 0 ;
    cin >> min ;
    cin >> max ;
    for(int i = min ; i <= max; i++){
        for(int j = 1; j <= i ; j++){
            if(i%j == 0)
                count++;
        }
        if (count == 2){
            ncount++;
            result  += i;
            if(ncount == 1)
                minnum = i ;
        }
        count = 0;
         
    }
    if (ncount == 0){
        minnum = -1;
    cout << minnum << "\n";

}

else{
    cout << result << "\n" << minnum << "\n";
}
return 0 ;

}
