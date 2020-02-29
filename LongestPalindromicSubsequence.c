#include<stdio.h>
#include<string.h>
int dp[100][100];
void print(int i,int j,char str1[],char str2[],int pos,int len){
    static int count=0;
    if((j<0||i>len-1)){

    }
    else if(dp[i][j]<=-1){
        
    }
    else if(dp[i][j]!=0){
        if(str1[i]==str1[j]){
            str2[pos]=str1[i];
            print(i+1,j-1,str1,str2,pos+1,len);
            dp[i][j]=dp[i][j]*-1;
        }
        else{
            if(dp[i][j-1]<=-1){
                if(dp[i+1][j]>=(dp[i][j-1]*-1))
                print(i+1,j,str1,str2,pos,len);
            }
            else if(dp[i][j-1]>dp[i+1][j]){
                print(i,j-1,str1,str2,pos,len);
                dp[i][j]=dp[i][j]*-1;    
            }
            else if(dp[i+1][j]>dp[i][j-1]){
                print(i+1,j,str1,str2,pos,len);
                dp[i][j]=dp[i][j]*-1;
            }
            else{
                print(i,j-1,str1,str2,pos,len);
                dp[i][j]=-1;
                print(i+1,j,str1,str2,pos,len);
                dp[i][j]=dp[i][j]*-1;
            }
        }
    }
    else{
        count++;
        str2[pos]='\0';
        printf("%s %d\n",str2,count);
    }
}
int main()
{
    char str1[1000],str2[1000];
    scanf("%s",str1);
    int len = strlen(str1);
    for(int i=0;i<len;i++){
        for(int j=0;j<len;j++){
            if(i==j)dp[i][j]=1;
            else dp[i][j]=0;
        }
    }
    int i,j,k=1;
    while(1){
        i=0;
        j=k;
        if(i==0 && j==len){
            break;
        }
        while(j<len){
            if(str1[i]==str1[j]){
                dp[i][j]=dp[i+1][j-1]+2;
            }
            else{
                dp[i][j]=dp[i][j-1]>=dp[i+1][j]?dp[i][j-1]:dp[i+1][j];
            }
            i++;
            j++;

        }
        k++;
    }
   /* for(int i=0;i<len;i++){
        for(int j=0;j<len;j++){
            printf("%d ",dp[i][j]);
        }
        printf("\n");
    }
    */
    i=0;
    j=len-1;
    print(i,j,str1,str2,0,len);
    for(int i=0;i<len;i++){
        for(int j=0;j<len;j++){
            printf("%d ",dp[i][j]);
        }
        printf("\n");
    }
    /*
    k=0;
    while(dp[i][j]!=0){
        if(str1[i]==str1[j]){
            str2[k]=str1[i];
            k++;
            i++;
            j--;
        }
        else{
            if(dp[i][j-1]>=dp[i+1][j]){
                j--;
            }
            else{
                i++;
            }
        }
    }
    int t;
    if(dp[0][len-1]%2==0){
        t=k-1;
    }
    else{
        t=k-2;
    }
        while(t>=0){
            str2[k]=str2[t];
            t--;
            k++;
        }
        str2[k]='\0';
        printf("%s",str2);
    */
}