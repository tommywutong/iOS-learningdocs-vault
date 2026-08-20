---
title: Dynamic Library Programming Topics
apple_id: TP40001869
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/UsingDynamicLibraries.html
archived_at: '2026-07-15T07:24:28.204167Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dynamic Library Programming Topics](Introduction.md)


[Next](Run-Path%20Dependent%20Libraries.md)[Previous](Creating%20Dynamic%20Libraries.md)

# Using Dynamic Libraries

When you need to use a dynamic library in your product, you have to install the library in your computer. You may use dynamic libraries as dependent libraries (by specifying them in your product’s link line) or as runtime loaded libraries (by loading them when they are needed, using `dlopen(3) OS X Developer Tools Manual Page`).

This article describes the process of installing and using dynamic libraries. It’s based on the Ratings dynamic library and the `StarMeals`, `StarMeals2`, and `Grades` programs, which are included in this document’s companion-file package. This article also shows how to use dynamic libraries as dependent libraries or as runtime-loaded libraries. Finally, this article demonstrates how to interpose the functions exported by a dynamic library.

Before you can use a dynamic library as a dependent library, the library and its header files must be installed on your computer. The standard locations for header files are `~/include`, `/usr/local/include` and `/usr/include`. The standard locations for dynamic libraries are `~/lib`, `/usr/local/lib`, and `/usr/lib`.

You may also place the `.dylib` file at a nonstandard location in your file system, but you must add that location to one of these environment variables:

- `LD_LIBRARY_PATH`
- `DYLD_LIBRARY_PATH`
- `DYLD_FALLBACK_LIBRARY_PATH`

For details on how to add paths to these environment variables, see [Opening Dynamic Libraries](Dynamic%20Library%20Usage%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsmryfvjvomjs). To learn about installing dependent libraries in a relocatable directory, see [Run-Path Dependent Libraries](Run-Path%20Dependent%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmbwfvjvomi).

If you don’t want to change the environment variables and you want to place the dynamic library in a nonstandard location, you must specify where in your file system you placed the library when you link your image. See the description of the compiler `-dylib_file` option in [http://gcc.gnu.org/onlinedocs/gcc/Darwin-Options.html#Darwin-Options](http://gcc.gnu.org/onlinedocs/gcc/Darwin-Options.html#Darwin-Options) for details.

For example, in OS X the executable code of apps can be packaged together with frameworks containing libraries created specifically for a particular app. These frameworks are known as _private embedded frameworks_. Applications that use private embedded frameworks, as well as the frameworks themselves, must be specially built. See “[Creating a Framework](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Tasks/CreatingFrameworks.html#//apple_ref/doc/uid/20002258)” in _[Framework Programming Guide](../../Mac%20OSX/Framework%20Programming%20Guide/Introduction%20to%20Framework%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dg2i)_ and “[Loading Code at Runtime](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/MachOTopics/1-Articles/loading_code.html#//apple_ref/doc/uid/TP40001830)” in _[Mach-O Programming Topics](../Mach-O%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjz)_ for details.

[Using Dependent Libraries](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcobsfvjvomjr) requires that the Averages 1.1 and Ratings 1.1 dynamic libraries be installed on your computer. To install these libraries:

1. Open this document’s companion-file package.
2. In Terminal, execute these commands:

```
[Averages/1.1]% make install
[Ratings/1.1]% make install
```


Using dynamic libraries as dependent libraries by linking your image with them provides several benefits, including producing smaller executable files and not having to get the address of the libraries’ exported symbols before using them in your code. However, you still have to make sure a weakly imported symbol exists before using it.

All you need to do to use a dynamic library as a dependent library is include the library’s headers in your source code and link the library with your program or library. The library’s headers describe the symbols you can use. You should not use any other symbols to access the library’s functionality. Otherwise, you may get unexpected results, or your image may stop working for its users when they update the dependent library in their computers.

Listing 1 shows the source code of a small program that uses Ratings 1.1, developed in [Creating Dynamic Libraries](Creating%20Dynamic%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvomi).

__Listing 1__  Using Ratings 1.1 as a dependent library

```c
/* File: StarMeals.c
 * Uses functions in libRatings.A.dylib.
 **************************************/

#include <stdio.h>
#include <string.h>
#include <Ratings.h>

#define MAX_NAMES 100
#define MAX_NAME_LENGTH 30
#define MAX_RATING_LENGTH 5

static char* name_list[MAX_NAMES];
static char* rating_list[MAX_NAMES];
static int names = 0;

void addNameAndRating(char* name, char* rating) {
    name_list[names] = strdup(name);
    rating_list[names] = (strlen(rating) > MAX_RATING_LENGTH)? "*****" : strdup(rating);
    names++;
}

void test_data(void) {
    addNameAndRating("Spinach", "*");
    addNameAndRating("Cake", "****");
    addNameAndRating("Steak", "****");
    addNameAndRating("Caviar", "*");
    addNameAndRating("Broccoli", "****");
    addNameAndRating("Gagh", "*****");
    addNameAndRating("Chicken", "*****");
}

int main(int argc, char* argv[]) {
    int test_mode = 0;
    if (argc == 2) {
        if (strcmp(argv[1], "test") == 0) {
            test_mode = 1;
            printf("[start_test]\n");
            test_data();
        }
    }
    else {
        printf("Enter meal names and ratings in the form <name> <rating>.\n");
        printf("No spaces are allowed in the name and the rating.\n");
        printf("The rating can be * through *****.\n");
        printf("To finish, enter \"end\" for a meal name.\n");
        while (names < MAX_NAMES) {
            char name[MAX_NAME_LENGTH];
            char rating[MAX_RATING_LENGTH + 1];
            printf("\nName and rating: ");
            scanf("%s", &name);
            if (strcmp(name, "end") == 0) {
                break;
            }
            scanf("%s", rating);
            addNameAndRating(name, rating);
        }
        printf("\n");
    }

    if (names) {
        // Print data entered and call libRatings.addRating().
        printf("This is the data you entered:\n");
        for (int i = 0; i < names; i++) {
            printf("%s (%s)\n", name_list[i], rating_list[i]);
            addRating(rating_list[i]);
        }

        // Print statistical information.
        printf("\nThe mean rating is %s\n", meanRating()); // 1 ```  ``` 
        if (medianRating) {                                // 2 ```  ``` 
            printf("The median rating is %s\n", medianRating());
        }
        if (frequentRating) {                              // 3 ```  ``` 
            printf("The most frequent rating is %s\n", frequentRating());
        }

        //printf("\n");
    }

    if (test_mode) {
        printf("[end_test]\n");
    }
    return 0;
}
```

This list describes the highlighted lines:

- Line 1: The `meanRating` function is guaranteed to exist in all versions of `libRating.A.dylib`. Therefore, no existence test is required.
- Lines 2 and 3: The functions `medianRating` and `frequentRating` are available in Ratings 1.1 but not Ratings 1.0. Since StarMeals is to be backwards compatible with Ratings 1.0, it has to check for the existence of these functions before using them. Otherwise, StarMeals may crash.

To compile the `StarMeals.c` file, use the command shown in [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcobsfvjvomq).

__Listing 2__  Compiling and linking StarMeals

```
[StarMeals]% make
clang -std=gnu99 StarMeals.c <user_home>/lib/libRatings.dylib <user_home>/lib/libAverages.dylib -o StarMeals
```

Notice that the exact location of the library `StarMeals` directly depends on (`libRatings.dylib`) is provided at the link line. The pathname `<user_home>/lib/libRatings.dylib` is actually a symbolic link to `<user_home>/lib/libRatings.A.dylib`. At link time, the static linker resolves the link and stores the library’s actual filename in the image it generates. With this approach, the dynamic linker always uses the library’s complete name when it looks for an image’s dependent libraries.

Listing 3 shows the output StarMeals produces when run in test mode:

__Listing 3__  Test output of the `StarMeals` program

```
> ./StarMeals test
start_test
This is the data you entered:
Spinach (*)
Cake (****)
Steak (****)
Caviar (*)
Broccoli (****)
Gagh (*****)
Chicken (*****)

The mean rating is ***
The medianRating is ****
The most frequent rating is ****
[end_test]
```


An image that uses dynamic libraries as runtime-loaded libraries is smaller and loads faster than the image using the same libraries as dependent libraries. The static linker doesn’t add information about the runtime-loaded libraries to the image. And the dynamic loader doesn’t have to load the library’s dependent libraries when the image is loaded. However, this flexibility comes at a price. Before an image can use a dynamic library that is not one of its dependent libraries, it must load the library with `dlopen(3) OS X Developer Tools Manual Page` and get the address of each symbol it needs with `dlsym(3) OS X Developer Tools Manual Page`. The image must also call `dlclose(3) OS X Developer Tools Manual Page` when it’s done using the library.

The StarMeals2 program provides the same functionality that StarMeals provides. But StarMeals2 uses the Ratings 1.1 dynamic library as a runtime loaded library. [Listing 4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcobsfvjvoni) shows the program’s source code.

__Listing 4__  Using Ratings 1.1 as a runtime-loaded library

```c
/* File: StarMeals2.c
 * Uses functions in libRatings.A.dylib.
 **************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dlfcn.h>
#include <Ratings.h>

#define MAX_NAMES 100
#define MAX_NAME_LENGTH 30
#define MAX_RATING_LENGTH 5

static char *name_list[MAX_NAMES];
static char *rating_list[MAX_NAMES];
static int names = 0;

void addNameAndRating(char *name, char *rating) {
    name_list[names] = strdup(name);
    rating_list[names] =
        (strlen(rating) > MAX_RATING_LENGTH)?
        "*****" : strdup(rating);
    names++;
}

void test_data(void) {
    addNameAndRating("Spinach", "*");
    addNameAndRating("Cake", "****");
    addNameAndRating("Steak", "****");
    addNameAndRating("Caviar", "*");
    addNameAndRating("Broccoli", "****");
    addNameAndRating("Gagh", "*****");
    addNameAndRating("Chicken", "*****");
}

int main(int argc, char *argv[]) {
    int test_mode = 0;
    if (argc == 2) {
        if (strcmp(argv[1], "test") == 0) {
            test_mode = 1;
            printf("[start_test]\n");
            test_data();
        }
    }
    else {
        printf("Enter restaurant names and ratings in the form <name> <rating>.\n");
        printf("No spaces are allowed in the name and the rating.\n");
        printf("The rating can be * through *****.\n");
        printf("To finish, enter \"end\" for a restaurant name.\n");
        while (names < MAX_NAMES) {
            char name[MAX_NAME_LENGTH];
            char rating[MAX_RATING_LENGTH + 1];
            printf("\nName and rating: ");
            scanf("%s", &name);
            if (strcmp(name, "end") == 0) {
                break;
            }
            scanf("%s", rating);
            addNameAndRating(name, rating);
        }
        printf("\n");
    }

    if (names) {
        // Open Ratings library.
        void* lib_handle = dlopen("libRatings.A.dylib", RTLD_LOCAL|RTLD_LAZY);
        if (!lib_handle) {
            printf("[%s] Unable to load library: %s\n", __FILE__, dlerror());
            exit(EXIT_FAILURE);
        }

        // Print data entered and call libRatings.A:addRating().
        void (*addRating)(char*) = dlsym(lib_handle, "addRating");
        if (!addRating) {       // addRating is guaranteed to exist in libRatings.A.dylib
            printf("[%s] Unable to get symbol: %s\n", __FILE__, dlerror());
            exit(EXIT_FAILURE);
        }
        printf("This is the data you entered:\n");
        for (int i = 0; i < names; i++) {
            printf("%s (%s)\n", name_list[i], rating_list[i]);
            addRating(rating_list[i]);
        }

        // Print statistical information.
        char *(*meanRating)(void) = dlsym(lib_handle, "meanRating");
        if (!meanRating) {      // meanRating is guaranteed to exist in libRatings.A.dylib
            printf("[%s] Unable to get symbol: %s\n", __FILE__, dlerror());
            exit(EXIT_FAILURE);
        }
        printf("\nThe mean rating is %s\n", meanRating());

        char *(*medianRating)(void) = dlsym(lib_handle, "medianRating");
        if (medianRating) {     // Backwards compatibility with Ratings 1.0
            printf("The median rating is %s\n", medianRating());
        }
        char *(*frequentRating)(void) = dlsym(lib_handle, "frequentRating");
        if (frequentRating) {   // Backwards compatibility with Ratings 1.0
            printf("The most frequent rating is %s\n", frequentRating());
        }

        // Close Ratings library
        if (dlclose(lib_handle) != 0) {
            printf("[%s] Problem closing library: %s", __FILE__, dlerror());
        }
    }

    if (test_mode) {
        printf("[end_test]\n");
    }
    return 0;
}
```

[Listing 5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcobsfvjvonq) shows to compile the `StarMeals2` program.

__Listing 5__  Compiling and linking StarMeals2

```
[StarMeals2]% make
clang -std=gnu99 StarMeals2.c -I<user_home>/include -o StarMeals2
```

The static linker doesn’t complain about the unresolved external references in `libRatings.A.dylib` because it’s not included at the link line. The dynamic linker resolves these references when StarMeals2 uses `dlopen(3) OS X Developer Tools Manual Page` to load `libRatings.A.dylib`.

Sometimes you need to perform operations before or after a function is called to gather statistical data or to modify its inputs our outputs. For example, you may want to find out how many times a program calls a specific function to determine whether an algorithm should be optimized. However, you may not always have access to the function’s source code to make the modifications. Interposition is a mechanism through which you can define your own version of a function that’s defined in an image’s dependent libraries. In your version, you may or may not call the original function.

To call an interposed function from a custom definition, you use the `dlsym(RTLD_NEXT, "<function_name>")` call to get the address of the “real” function. For example, Listing 6 shows how you may write a custom version of a function defined in a dynamic library.

__Listing 6__  Interposing a function

```
char *name(void) {
    static int name_calls = 0;
    printf("[STATS] name() has been called %i times\n", name_calls);
    char *(*next_name)(void) = dlsym(RTLD_NEXT, "name");
    return next_name();
}
```

You may use interposition to adapt an existing dynamic library to your particular needs without changing its API. For example, this document’s companion package includes the implementations of two dynamic libraries called Ratings and RatingsAsGrades. The Ratings library implements a star-based rating system (it can be used to tally restaurant and hotel ratings; for example, \*\*\* and \*\*\*\*\*). The RatingsAsGrades library implements a letter-based grading system, which can be used to tally student grades; for example A and C. Instead of writing a new algorithm to manage letter grades, the RatingsAsGrades library leverages the functionality of the Ratings library. Listing 7 shows the interface and implementation of the RatingsAsGrades library.

__Listing 7__  RatingsAsGrades Interposing Ratings

```c
/* File: RatingsInterposed.h
 * Interface to the RatingsAsGrages dynamic library.
 **************************************************/

/* Adds 'grade' to the set.
 *      grade: Non-NULL string. Contains zero or
 *             one of these characters:
 *             A, B, C, D, F.
 *             Examples: "", "A", "B".
 */
void addRating(char* grade);

/* Returns the median grade.
 */
char *medianRating(void);

/* Returns the most frequent grade.
 */
char *frequentRating(void);

/* File: RatingsAsGrades.c
 * Compile with -fvisibility=hidden.
 ***********************************/

#include "RatingsAsGrades.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

#define EXPORT __attribute__((visibility("default")))
#define MAX_STAR_RATING_LEN 6

static char *_ratingAsGrade(char *rating) {
    int rating_length = strlen(rating);
    if (rating_length > MAX_STAR_RATING_LEN - 1) {
        rating_length = MAX_STAR_RATING_LEN - 1;
    }
    char grade;
    switch (rating_length) {
        case 5:
            grade = 'A';
            break;
        case 4:
            grade = 'B';
            break;
        case 3:
            grade = 'C';
            break;
        case 2:
            grade = 'D';
            break;
        case 1:
            grade = 'F';
            break;
        default:
            grade = '\0';
    }
    char char_grade[2] = { grade, '\0' };
    return strdup(char_grade);
}

// Interpose libRatings.B.dylib:addRating.
EXPORT
void addRating(char* grade) {
    char rating[MAX_STAR_RATING_LEN] = { '\0' };
    switch (*grade) {
        case 'A':
            strcat(rating, "*");
        case 'B':
            strcat(rating, "*");
        case 'C':
            strcat(rating, "*");
        case 'D':
            strcat(rating, "*");
        case 'F':
            strcat(rating, "*");
        default:
            ;
    }
    void (*next_addRating)(char *) =
dlsym(RTLD_NEXT, "addRating");
    if (next_addRating) {
        next_addRating(rating);
    }
    else {
        printf("[%s] Fatal problem: %s", __FILE__, dlerror());
    }
}

// Interpose libRatings.B.dylib:medianRating.
EXPORT
char *medianRating(void) {
    char medianGrade[2] = { '\0' };
    char *(*next_medianRating)(void) =
dlsym(RTLD_NEXT, "medianRating");
    if (next_medianRating) {
        strcpy(medianGrade,
_ratingAsGrade(next_medianRating()));
    }
    else {
        printf("[%s] Fatal problem: %s", __FILE__, dlerror());
        exit(EXIT_FAILURE);
    }
    return strdup(medianGrade);
}

// Interpose libRatings.B.dylib:frequentRating.
EXPORT
char *frequentRating(void) {
    char frequentGrade[2] = { '\0' };
    char *(*next_frequentRating)(void) =
        dlsym(RTLD_NEXT, "frequentRating");
    if (next_frequentRating) {
        strcpy(frequentGrade,
            _ratingAsGrade(next_frequentRating()));
    }
    else {
        printf("[%s] Fatal problem: %s", __FILE__, dlerror());
        exit(EXIT_FAILURE);
    }
    return strdup(frequentGrade);

}
```

Notice how the `addRating`, `medianRating`, and `frequentRating` functions, modify the input and output of the definitions they shadow.

The companion-files package includes the source code of the `Grades` program. This program uses the RatingsAsGrades library to tally the grades of students.

Follow these instructions to build and run the `Grades` program:

1. Open this document’s companion-files package.
2. In Terminal, perform these commands:

```
[Ratings/1.1]% make install
[Grades]% make
```

[Listing 8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcobsfvjvooi) shows the output of the `Grades` program when ran in test mode.

__Listing 8__  Test output of the `Grades` program

```
[Grades]% ./Grades test
[start_test]
This is the data you entered:
Eloise  (F)
Karla   (B)
Iva     (B)
Hilaire (F)
Jewel   (B)
Simone  (A)
Yvette  (A)
Renee   (A)
Mimi    (A)

The median grade is B
The most frequent grade is A
[end_test]
```

[Next](Run-Path%20Dependent%20Libraries.md)[Previous](Creating%20Dynamic%20Libraries.md)

