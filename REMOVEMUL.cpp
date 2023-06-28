#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        long long n,m;
        cin>>n>>m;
        long long a[m];
        long long sum=0;
        long long add=n*(n+1)/2;
        for(int i=0;i<m;i++){
            long long input;
            cin>>input;
            sum+=input;
            
        }
        cout<<add-sum<<endl;
    }
}