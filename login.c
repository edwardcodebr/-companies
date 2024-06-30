#include <stdio.h>
#include <string.h>

typedef struct
{
    char name[10];
    char lastname[10];
} name;

typedef struct
{
    int pass;
} login;

typedef struct
{
    char fullname[20];
} Fullname;

typedef struct
{
    char booktype[12];
} book;

void createfullname(name *namestruct, Fullname *fullnamestruct) {
    strcpy(fullnamestruct->fullname, namestruct->name);
    strcat(fullnamestruct->fullname, " ");
    strcat(fullnamestruct->fullname, namestruct->lastname);
}

int main() {
    book booki = {""};  // Initialize booktype to an empty string
    login loga;
    name person;
    Fullname completename = {""};  // Initialize fullname to an empty string
    int choose;
    int acpass;

    printf("Enter your name: ");
    scanf("%9s", person.name);  // Limit input to avoid buffer overflow
    printf("Last name: ");
    scanf("%9s", person.lastname);  // Limit input to avoid buffer overflow

    createfullname(&person, &completename);
    printf("Hello %s\n", completename.fullname);

    printf("Enter password (6 digits): ");
    scanf("%6d", &loga.pass);

    while (1) {
        printf("\nMenu:\n1 - Modify code.\n2 - Book.\n3 - Exit\n");
        printf("Actual book: %s\n", booki.booktype);
        printf("Choose an option: ");
        scanf("%d", &choose);

        switch (choose) {
            case 1:
                printf("New password (6 digits): ");
                scanf("%6d", &loga.pass);
                printf("New pass: %d\n", loga.pass);
                break;
            case 2:
                printf("Enter password: ");
                scanf("%6d", &acpass);
                if (acpass == loga.pass) {
                    printf("Success\n");
                    printf("What is your type of book: ");
                    scanf("%11s", booki.booktype);  // Limit input to avoid buffer overflow
                } else {
                    printf("error\n");
                }
                break;
            case 3:
                return 0;  // Exit the program
            default:
                printf("Invalid option, please try again.\n");
                break;
        }
    }

    return 0;
}