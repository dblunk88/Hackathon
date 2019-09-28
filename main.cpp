#include <iostream>
#include <thread>
#include <chrono>
using namespace std;

char password[6];

bool passCheck(char something[]){
    return strcmp(something, password) == 0;
}

// Average with no threads: 10726440 nanoseconds
void fiveLetter(char beginChar, char endChar){

    char pwdCrack[6] = "\0";
    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();

    for(pwdCrack[0]=beginChar; pwdCrack[0] <= endChar; pwdCrack[0]++)
        for(pwdCrack[1]='A'; pwdCrack[1] <= 'Z'; pwdCrack[1]++)
            for(pwdCrack[2]='A'; pwdCrack[2] <= 'Z'; pwdCrack[2]++)
                for(pwdCrack[3]='A'; pwdCrack[3] <= 'Z'; pwdCrack[3]++)
                    for(pwdCrack[4]='A'; pwdCrack[4] <= 'Z'; pwdCrack[4]++)

                        if(passCheck(pwdCrack)) {
                            printf("%s -> %s\n", pwdCrack, password);
                            std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
                            std::cout << "Time difference = " << std::chrono::duration_cast<std::chrono::microseconds>(end - begin).count() << "[µs]" << std::endl;

                            exit(0);
                        }
}

// 11370420 nanoseconds
void launchMany(){
    char letters[26] = {'A','B','C','D','E','F','G','H','I','J','K',
                        'L','M','N','O','P','Q','R','S','T','U',
                        'V','W','X','Y','Z'};
    for (int i = 0; i < 27; ++i) {
        thread th1(fiveLetter, letters[i], letters[25-i]);
    }
}

// 10726440 nanoseconds
void launchThreads(){
    thread th1(fiveLetter, 'A', 'Z');
    thread th2(fiveLetter, 'Z', 'A');
}


int main() {

    char word[6];
    cin >> word;

    strcpy_s(password, word);

    fiveLetter('A', 'Z');

    std::cout << "Done" << std::endl;
    return 0;
}