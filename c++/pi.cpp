#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>

std::string get_pi(){
    std::string pi_str, line;
    std::ifstream pi_file;
    pi_file.open("../pi.txt");
    if(pi_file.is_open()){
        while(std::getline(pi_file, line)){
            pi_str += line;
        }
        pi_file.close();
    } else {
        printf("unable to open file");
    }
    return pi_str;
}

int main(int argc, char* args[]){
    std::string pi_str = get_pi();
}
