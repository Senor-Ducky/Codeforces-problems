#include <iostream>
#include <string>
using namespace std;

int main() {
   int n;
   string op;
   cin >> n;
   int count = 0;
   
   for(int i = 0 ; i<n; i++) {
      
           cin >> op;
           
           if(op[1] == '+') {
               count += 1;
           } else {
               count -= 1;
           }
       
   }
   
   
   
   cout << count;
}