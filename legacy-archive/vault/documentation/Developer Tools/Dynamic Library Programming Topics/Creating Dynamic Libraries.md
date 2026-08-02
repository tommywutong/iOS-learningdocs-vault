---
title: Dynamic Library Programming Topics
apple_id: TP40001869
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/CreatingDynamicLibraries.html
archived_at: '2026-07-15T07:24:25.781308Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dynamic Library Programming Topics](Introduction.md)


[Next](Using%20Dynamic%20Libraries.md)[Previous](Dynamic%20Library%20Usage%20Guidelines.md)

# Creating Dynamic Libraries

When you create or update a dynamic library, you should carefully consider how it may be used by developers in their products. It’s also important to give these developers flexibility by allowing their products to work with earlier or later versions of the library without them having to update their products.

This article demonstrates how to write a dynamic library so that it’s easy to use by developers who want to take advantage of it in their own development. This article also describes how to update existing libraries and manage their version information to maximize client compatibility.

When creating a dynamic library, you should perform these tasks:

- Define the library’s purpose: This information provides the focus required to define the library’s public interface.
- Define the library’s interface (header files): This is the interface through which the library’s clients access its functionality.
- Implement the library (implementation files): This is where you define the public functions that the library’s clients use. You may also need to define private variables and functions needed to implement the interface but not required by clients.
- Set the library’s version information: The library’s version information is divided in three parts: major, minor, and compatibility. You specify all the parts of the library’s version information when you create the `.dylib` file. See [Managing Client Compatibility With Dependent Libraries](Dynamic%20Library%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdamjtfvjvomrq) for details.
- Test the library: At the very least, you should define a test for each of the public functions your library exposes, to ensure that they perform the correct action given particular test inputs or after performing a specific set of operations.

The following sections provide an example of the process taken to develop a simple dynamic library, called Ratings. The files mentioned in the following sections are included in `Ratings/1.0` in this document’s companion-file package.

The purpose of the Ratings library is to provide a ratings analyzer to its clients. Ratings are strings made up of asterisks (\*) that represent levels of satisfaction for a particular item. For example, in Apple’s iTunes app, you can specify whether you like a particular song a lot with a five-star rating (\*\*\*\*\*) or not at all with a one-star rating (\*).

The initial release of the library provides a way for clients to add ratings, get a count of the ratings they have added, get the mean rating, and clear the rating set.

Before you implement the library, you must define the interface the library’s clients use to interact with it. You should carefully specify each function’s semantics. A clear definition benefits you because it makes clear the purpose of each public function. It also benefits developers who use your library because it tells them exactly what to expect when they call each function in their code.

This is an example of a list of interface functions with each function’s semantic meaning:

- `void addRating(char *rating)`: Adds a rating value to the set kept by the library. The rating argument is a string; it must not be NULL. Each character in the string represents one rating point. For example, an empty string (`""`) is equivalent to a rating of 0, `"*"` means 1, `"**"` means 2, and so on. The actual characters used in the string are immaterial. Therefore, `" "` means 1 and `"3456"` means 4. Each call to this function increments the value returned by the ratings function.
- `int ratings(void)`: Returns the number of rating values in the set. This function has no side effects.
- `char *meanRatings(void)`: Returns the mean rating in the rating set as a string, using one asterisk per rating point. This function has no side effects.
- `clearRatings(void)`: Clears the rating set. After calling this function (with no subsequent calls to `addRating`), the `ratings` function returns `0`.

[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvomq) shows the header file that the Ratings library’s clients include to access its interface.

__Listing 1__   Interface to Ratings 1.0

```
/* File: Ratings.h
 * Interface to libRatings.A.dylib 1.0.
 *************************************/

/* Adds 'rating' to the set.
 *      rating: Each character adds 1 to the numeric rating
 *              Example: "" = 0, "*" = 1, "**" = 2, "wer " = 4.
 */
void addRating(char *rating);

/* Returns the number of ratings in the set.
 */
int ratings(void);

/* Returns the mean rating of the set.
 */
char *meanRating(void);

/* Clears the set.
 */
void clearRatings(void);
```


The interface declared in [Defining the Library’s Interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvomjx) is implemented in `Ratings.c` , shown in [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvomy).

__Listing 2__  Implementation of Ratings 1.0

```c
/* File: Ratings.c
 * Compile with -fvisibility=hidden.                        // 1
 **********************************/

#include "Ratings.h"
#include <stdio.h>
#include <string.h>

#define EXPORT __attribute__((visibility("default")))
#define MAX_NUMBERS 99

static int _number_list[MAX_NUMBERS];
static int _numbers = 0;

// Initializer.
__attribute__((constructor))
static void initializer(void) {                             // 2
    printf("[%s] initializer()\n", __FILE__);
}

// Finalizer.
__attribute__((destructor))
static void finalizer(void) {                               // 3
    printf("[%s] finalizer()\n", __FILE__);
}

// Used by meanRating, middleRating, frequentRating.
static char *_char_rating(int rating) {
    char result[10] = "";
    int int_rating = rating;
    for (int i = 0; i < int_rating; i++) {
        strncat(result, "*", sizeof(result) - strlen(result) - 1);
    }
    return strdup(result);
}

// Used by addRating.
void _add(int number) {                                     // 4
    if (_numbers < MAX_NUMBERS) {
        _number_list[_numbers++] = number;
    }
}

// Used by meanRating.
int _mean(void) {
    int result = 0;
    if (_numbers) {
        int sum = 0;
        int i;
        for (i = 0; i < _numbers; i++) {
            sum += _number_list[i];
        }
        result = sum / _numbers;
    }
    return result;
}

EXPORT
void addRating(char *rating) {                            // 5
    if (rating != NULL) {
        int numeric_rating = 0;
        int pos = 0;
        while (*rating++ != '\0' && pos++ < 5) {
            numeric_rating++;
        }
        _add(numeric_rating);
    }
}

EXPORT
char *meanRating(void) {
    return _char_rating(_mean());
}

EXPORT
int ratings(void) {
    return _numbers;
}

EXPORT
void clearRatings(void) {
    _numbers = 0;
}
```

The following list describes the tagged lines.

1. This comment is only to remind the library’s developers to compile this file with the compiler `-fvisibility=hidden` option, so that only the symbols with the `visibility("default")` attribute are exported.
2. This initializer is defined only to show at which point of a client’s execution the library’s initializers are called by the dynamic loader.
3. This finalizer is defined only to show at which point of client’s execution the library’s finalizers are called by the dynamic loader.
4. The `_add` function is an example of an internal function. Clients don’t need to know about it and, therefore, it’s not exported. Also, because internal calls are trusted, no validation is performed. However, there’s no requirement that internal-use functions lack validation.
5. The `addRating` function is an example of an exported function. To ensure that only correct ratings are added, the function’s input parameter is validated.

When you compile the library’s source files into a `.dylib` file, you set version information that specifies whether clients can use versions of the library earlier or later than the version they were linked with. When the client is loaded into a process, the dynamic loader looks for the `.dylib` file in the library search paths and, if it finds it, compares the version information of the `.dylib` file with the version information recorded in the client image. If the client is not compatible with the `.dylib` file, the dynamic loader doesn’t load the client into the process. In effect, the client’s load process is aborted because the dynamic loader was unable to locate a compatible dependent library.

[Listing 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvona) shows the command used to generate version 1.0 of the Ratings library.

__Listing 3__  Generating version 1.0 of the Ratings dynamic library

```
[Ratings/1.0]% make dylib
clang -dynamiclib -std=gnu99 Ratings.c -current_version 1.0 -compatibility_version 1.0 -fvisibility=hidden -o libRatings.A.dylib
```

This list indicates where the major version, minor version, and compatibility version are specified:

- The major version number is specified in the library’s filename as “A” in `-o libRatings.A.dylib`.
- The minor version number is specified in `-current_version 1.0`.
- The compatibility version number is specified in `-compatibility_version 1.0`.

Before publishing a dynamic library, you should test its public interface to ensure that it performs as you specified in the interface’s documentation (see [Defining the Library’s Interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvomjx). To provide maximum flexibility to clients, you should make sure that your library can be used as a dependent library (clients link with it, and the library is loaded when the client is loaded) or as a runtime-loaded library (clients don’t link with it and use `dlopen(3) OS X Developer Tools Manual Page` to load it).

[Listing 4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvoni) shows an example of a test client that uses the Ratings library as a dependent library.

__Listing 4__  Testing Ratings 1.0 as a dependent library

```c
/* Dependent.c
 * Tests libRatings.A.dylib 1.0 as a dependent library.
 *****************************************************/

#include <stdio.h>
#include <string.h>
#include "Ratings.h"

#define PASSFAIL "Passed":"Failed"
#define UNTST "Untested"

int main(int argc, char **argv) {
    printf("[start_test]\n");

    // Setup.
    addRating(NULL);
    addRating("");
    addRating("*");
    addRating("**");
    addRating("***");
    addRating("*****");
    addRating("*****");

    // ratings.
    printf("[%s] ratings(): %s\n",
        __FILE__, (ratings() == 6? PASSFAIL));

    // meanRating.
    printf("[%s] meanRating(): %s\n",
        __FILE__, (strcmp(meanRating(), "**") == 0)? PASSFAIL);

    // clearRatings.
    clearRatings();
    printf("[%s] clearRatings(): %s\n",
        __FILE__, (ratings() == 0? PASSFAIL));

    printf("[end_test]\n");
    return 0;
}
```

The following command generates the `Dependent` client program. Note that `libRatings.A.dylib` is included in the compile line.

```
clang Dependent.c libRatings.A.dylib -o Dependent
```

The `Dependent` program produces output that shows whether calling each of the library’s exported functions produces the expected results. In addition, the `initializer` and `finalizer` functions defined in the library produce output lines that indicate when they are invoked in relation to the program’s normal process. This output is shown in [Listing 5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvonq).

__Listing 5__  Test results for Ratings 1.0 as a dependent library

```
> ./Dependent
[Ratings.c] initializer()
[start_test]
[Dependent.c] ratings(): Passed
[Dependent.c] meanRating(): Passed
[Dependent.c] clearRatings(): Passed
[end_test]
[Ratings.c] finalizer()
```

Notice that `initializer` is called before the `main` function. The finalizer function, on the other hand, is called after exiting the `main` function.

Testing the Ratings library as a runtime-loaded library requires another test program, Runtime. [Listing 6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvooa) shows its source file.

__Listing 6__  Testing Ratings 1.0 as a runtime-loaded library

```c
/* Runtime.c
 * Tests libRatings.A.dylib 1.0 as a runtime-loaded library.
 ***********************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>
#include <string.h>
#include "Ratings.h"

#define PASSFAIL "Passed":"Failed"
#define UNTST "Untested"

int main(int argc, char **argv) {
    printf("[start_test]\n");

    // Open the library.
    char *lib_name = "./libRatings.A.dylib";
    void *lib_handle = dlopen(lib_name, RTLD_NOW);
    if (lib_handle) {
        printf("[%s] dlopen(\"%s\", RTLD_NOW): Successful\n", __FILE__, lib_name);
    }
    else {
        printf("[%s] Unable to open library: %s\n",
            __FILE__, dlerror());
        exit(EXIT_FAILURE);
    }

    // Get the symbol addresses.
    void (*addRating)(char*) = dlsym(lib_handle, "addRating");
    if (addRating) {
        printf("[%s] dlsym(lib_handle, \"addRating\"): Successful\n", __FILE__);
    }
    else {
        printf("[%s] Unable to get symbol: %s\n",
            __FILE__, dlerror());
        exit(EXIT_FAILURE);
    }
    char *(*meanRating)(void) = dlsym(lib_handle, "meanRating");
    if (meanRating) {
        printf("[%s] dlsym(lib_handle, \"meanRating\"): Successful\n", __FILE__);
    }
    else {
        printf("[%s] Unable to get symbol: %s\n",
            __FILE__, dlerror());
        exit(EXIT_FAILURE);
    }
    void (*clearRatings)(void) = dlsym(lib_handle, "clearRatings");
    if (clearRatings) {
        printf("[%s] dlsym(lib_handle, \"clearRatings\"): Successful\n", __FILE__);
    }
    else {
        printf("[%s] Unable to get symbol: %s\n",
            __FILE__, dlerror());
        exit(EXIT_FAILURE);
    }
    int (*ratings)(void) = dlsym(lib_handle, "ratings");
    if (ratings) {
        printf("[%s] dlsym(lib_handle, \"ratings\"): Successful\n", __FILE__);
    }
    else {
        printf("[%s] Unable to get symbol: %s\n",
            __FILE__, dlerror());
        exit(EXIT_FAILURE);
    }

    // Setup.
    addRating(NULL);
    addRating("");
    addRating("*");
    addRating("**");
    addRating("***");
    addRating("*****");
    addRating("*****");

    // ratings.
    printf("[%s] ratings(): %s\n", __FILE__, (ratings() == 6? PASSFAIL));

    // meanRating.
    printf("[%s] meanRating(): %s\n", __FILE__, (strcmp(meanRating(), "**") == 0)? PASSFAIL);

    // clearRatings.
    clearRatings();
    printf("[%s] clearRatings(): %s\n", __FILE__, (ratings() == 0? PASSFAIL));

    // Close the library.
    if (dlclose(lib_handle) == 0) {
        printf("[%s] dlclose(lib_handle): Successful\n", __FILE__);
    }
    else {
        printf("[%s] Unable to open close: %s\n",
            __FILE__, dlerror());
    }

    printf("[end_test]\n");
    return 0;
}
```

The `Runtime` program is very similar to the `Dependent` program. However, Runtime must load `libRuntime.A.dylib` using the `dlopen(3) OS X Developer Tools Manual Page` function. After that, it must get the address of each function exported by the library using `dlsym(3) OS X Developer Tools Manual Page` before using it.

The following command generates the `Runtime` client program.

```
[Ratings/1.0]% make runtime
clang Runtime.c -o Runtime
```

[Listing 7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvomjy) shows the output produced by Runtime.

__Listing 7__  Test results for Ratings 1.0 as a runtime-loaded library

```
> ./Runtime
[start_test]
[Ratings.c] initializer()
[Runtime.c] dlopen("./libRatings.A.dylib", RTLD_NOW): Successful
[Runtime.c] dlsym(lib_handle, "addRating"): Successful
[Runtime.c] dlsym(lib_handle, "meanRating"): Successful
[Runtime.c] dlsym(lib_handle, "clearRatings"): Successful
[Runtime.c] dlsym(lib_handle, "ratings"): Successful
[Runtime.c] ratings(): Passed
[Runtime.c] meanRating(): Passed
[Runtime.c] clearRatings(): Passed
[Runtime.c] dlclose(lib_handle): Successful
[end_test]
[Ratings.c] finalizer()
```

Note that the Ratings library’s initializer function is called within the `main` function execution before the call to `dlopen` returns, which differs from its execution point in the `Dependent` program [Listing 5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvonq). The `finalizer` function, however, is called after `main` has exited, the same point at which it’s called in Dependent’s execution. You should consider this when writing dynamic library initializers and finalizers.

Making revisions to a previously published dynamic library is a delicate task. If you want existing clients to be able to use the library (that is, load the new version of the `.dylib` file without recompilation), you must ensure that the API those clients know about is unchanged, including its semantic meaning.

When you can guarantee that the API of the new version of the library is compatible with the API that clients linked with earlier versions know about, you can deem the new version a minor revision. When you want to publish a minor revision of a dynamic library to users of the library’s clients (for example, the users of a program that uses your library) the only version information item you need to change is the library’s current version. The major version (filename) and compatibility version of the library must remain the same. When end users replace the early version of the library with the new version in their computers, the library’s clients use the new version without any problems. [Managing Client Compatibility With Dependent Libraries](Dynamic%20Library%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdamjtfvjvomrq).

From the point of view of a client image, there are two sides to compatibility with the dynamic libraries it uses: compatibility with versions of a library later than the one the client knows about, known as forward compatibility, and compatibility with versions of a library earlier than the one the client is familiar with, known as backward compatibility. You maintain forward compatibility by ensuring that the library’s API remains compatible across revisions. You facilitate backward compatibility by exporting new functions as weak references. In turn, your library’s clients must ensure that weakly imported functions actually exist before using them.

The Ratings library, introduced in [Creating Libraries](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvomjz), has a second version, 1.1. [Listing 8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvony) shows the updated header for the Ratings library.

__Listing 8__  Interface to Ratings 1.1

```
/* File: Ratings.h
 * Interface to libRatings.A.dylib 1.1.
 *************************************/

#define WEAK_IMPORT __attribute__((weak_import))

/* Adds 'rating' to the set.
 *      rating: Each character adds 1 to the numeric rating
 *      Example: "" = 0, "*" = 1, "**" = 2, "wer " = 4.
 */
void addRating(char* rating);

/* Returns the number of ratings in the set.
 */
int ratings(void);

/* Returns the mean rating of the set.
 */
char* meanRating(void);

/* Returns the medianRating of the set.
 */
WEAK_IMPORT
char *medianRating(void);                       // 1

/* Returns the most frequent rating of the set.
 */
WEAK_IMPORT
char *frequentRating(void);                     // 2

/* Clears the set.
 */
void clearRatings(void);
```

The tagged lines declare the new functions. Notice that both declarations include the `weak_import` attribute, informing client developers that the function is weakly linked. Therefore, clients must make sure the function exists before calling it.

[Listing 9](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvomzq) shows the library’s new implementation file.

__Listing 9__  Implementation of Ratings 1.1

```c
/* File: Ratings.c
 * Compile with -fvisibility=hidden.
 **********************************/

#include "Ratings.h"
#include <Averages.h>
#include <stdio.h>
#include <string.h>
#include <float.h>

#define EXPORT __attribute__((visibility("default")))
#define MAX_NUMBERS 99
//#define MAX_NUMERIC_RATING 10               // published in Ratings.h

static char *_char_rating(float rating) {
    char result[10] = "";
    int int_rating = (int)(rating + 0.5);
    for (int i = 0; i < int_rating; i++) {
        strncat(result, "*", sizeof(result) - strlen(result) - 1);
    }
    return strdup(result);
}

EXPORT
void addRating(char *rating) {
    if (rating != NULL) {
        int numeric_rating = 0;
        int pos = 0;
        while (*rating++ != '\0' && pos++ < 5) {
            numeric_rating++;
        }
        add((float)numeric_rating);     // libAverages.A:add()
    }
}

EXPORT
char *meanRating(void) {
    return _char_rating(mean());        // libAverages.A:mean()
}

EXPORT
char *medianRating(void) {
    return _char_rating(median());      // libAverages.A:median()
}

EXPORT
char *frequentRating(void) {
    int lib_mode = mode();                // libAverages.A:mode()
    return _char_rating(lib_mode);
}

EXPORT
int ratings(void) {
    return count();                     // libAverages.A:count()
}

EXPORT
void clearRatings(void) {
    clear();                            // libAverages.A:clear()
}


/* Ratings.c revision history
 * 1. First version.
 * 2. Added medianRating, frequentRating.
 *    Removed initializer, finalizer.
 */
```

Listing 10 shows the updated source code for the Runtime program that tests the Ratings 1.1 library.

__Listing 10__  Testing Ratings 1.1 as a runtime-loaded library

```c
/* Runtime.c
 * Tests libRatings.A.dylib 1.1 as a runtime-loaded library.
 **********************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>
#include <string.h>
#include "Ratings.h"

#define PASSFAIL "Passed":"Failed"
#define UNTST "Untested"

int main(int argc, char** argv) {
    printf("[start_test]\n");

    // Open the library.
    char *lib_name = "./libRatings.A.dylib";
    void *lib_handle = dlopen(lib_name, RTLD_NOW);
    if (lib_handle) {
        printf("[%s] dlopen(\"%s\", RTLD_NOW): Successful\n", __FILE__, lib_name);
    }
    else {
        printf("[%s] Unable to open library: %s\n",
            __FILE__, dlerror());
        exit(EXIT_FAILURE);
    }

    // Get the function addresses.
    void (*addRating)(char*) = dlsym(lib_handle, "addRating");
    if (addRating) {
        printf("[%s] dlsym(lib_handle, \"addRating\"): Successful\n", __FILE__);
    }
    else {
        printf("[%s] Unable to get symbol: %s\n",
            __FILE__, dlerror());
        exit(EXIT_FAILURE);
    }
    char* (*meanRating)(void) = dlsym(lib_handle, "meanRating");
    if (meanRating) {
        printf("[%s] dlsym(lib_handle, \"meanRating\"): Successful\n", __FILE__);
    }
    else {
        printf("[%s] Unable to get symbol: %s\n",
            __FILE__, dlerror());
        exit(EXIT_FAILURE);
    }
    void (*clearRatings)(void) = dlsym(lib_handle, "clearRatings");
    if (clearRatings) {
        printf("[%s] dlsym(lib_handle, \"clearRatings\"): Successful\n", __FILE__);
    }
    else {
        printf("[%s] Unable to get symbol: %s\n",
            __FILE__, dlerror());
        exit(EXIT_FAILURE);
    }
    int (*ratings)(void) = dlsym(lib_handle, "ratings");
    if (ratings) {
        printf("[%s] dlsym(lib_handle, \"ratings\"): Successful\n", __FILE__);
    }
    else {
        printf("[%s] Unable to get symbol: %s\n",
            __FILE__, dlerror());
        exit(EXIT_FAILURE);
    }
    char *(*medianRating)(void) = dlsym(lib_handle, "medianRating");        // weak import
    char *(*frequentRating)(void) = dlsym(lib_handle, "frequentRating");    // weak import

    // Setup.
    addRating(NULL);
    addRating("");
    addRating("*");
    addRating("**");
    addRating("***");
    addRating("*****");
    addRating("*****");

    // ratings.
    printf("[%s] ratings(): %s\n", __FILE__, (ratings() == 6? PASSFAIL));

    // meanRating.
    printf("[%s] meanRating(): %s\n", __FILE__, (strcmp(meanRating(), "**") == 0)? PASSFAIL);

    // medianRating.
    if (medianRating) {
        printf("[%s] medianRating(): %s\n", __FILE__, (strcmp(medianRating(), "**") == 0? PASSFAIL));
    }
    else {
        printf("[%s] medianRating(): %s\n", __FILE__, UNTST);
    }

    // frequentRating.

    if (frequentRating) {
        char* test_rating = "*****";
        int test_rating_size = sizeof(test_rating);
        printf("[%s] frequentRating(): %s\n", __FILE__, strncmp(test_rating, frequentRating(), test_rating_size) == 0? PASSFAIL);
    }
    else {
        printf("[%s] mostFrequentRating(): %s\n", __FILE__, UNTST);
    }

    // clearRatings.
    clearRatings();
    printf("[%s] clearRatings(): %s\n", __FILE__, (ratings() == 0? PASSFAIL));

    // Close the library.
    if (dlclose(lib_handle) == 0) {
        printf("[%s] dlclose(lib_handle): Successful\n", __FILE__);
    }
    else {
        printf("[%s] Unable to open close: %s\n",
            __FILE__, dlerror());
    }

    printf("[end_test]\n");
    return 0;
}
```


[Listing 11](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvomjq) shows the command used to generate version 1.1 of the Ratings library.

__Listing 11__  Generating version 1.1 of the Ratings dynamic library

```
[Ratings/1.1]% make dylib
clang -dynamiclib -std=gnu99 Ratings.c -I<user_home>/include <user_home>/lib/libAverages.dylib -current_version 1.1 -compatibility_version 1.0 -fvisibility=hidden -o libRatings.A.dylib
```

Notice that this time the library’s current version is set to 1.1 but its compatibility version remains 1.0. When a client is linked against version 1.1 of this library, the compatibility version is encoded in the client image. Therefore, the dynamic loader loads the client image whether it finds version 1.1 or 1.0 of `libRatings.A.dylib`. That is, the client is backwards compatible with version 1.0 of the library. For details on why  `/usr/local/lib/libAverages.dylib` was added to the compile line, see [Using Dependent Libraries](Using%20Dynamic%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcobsfvjvomjr).

Similar to creating initial versions of a library, updating libraries require thorough testing. You should at least add tests for each function you added to your test programs. If you used weak references, your test programs should ensure the existence of the new functions before calling them.

The `Ratings/1.1` directory in this document’s companion-file package contains the source files for the Ratings 1.1 library. [Listing 12](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvomjr) shows an updated version of the `Dependent` program. The tagged lines show how to check for the presence of a function before using it.

__Listing 12__  Testing Ratings 1.1 as a dependent library

```c
/* Dependent.c
 * Tests libRatings.A.dylib 1.1 as a dependent library.
 *****************************************************/

#include <stdio.h>
#include <string.h>
#include "Ratings.h"

#define PASSFAIL "Passed":"Failed"
#define UNTST "Untested"

int main(int argc, char **argv) {
    printf("[start_test]\n");

    // Setup.
    addRating(NULL);
    addRating("");
    addRating("*");
    addRating("**");
    addRating("***");
    addRating("*****");
    addRating("*****");

    // ratings.
    printf("[%s] ratings(): %s\n",
        __FILE__, (ratings() == 6? PASSFAIL));

    // meanRating.
    printf("[%s] meanRating(): %s\n",
        __FILE__, (strcmp(meanRating(), "**") == 0)? PASSFAIL);

    // medianRating.
    if (medianRating) {                         // 1
        printf("[%s] medianRating(): %s\n",
            __FILE__, (strcmp(medianRating(), "**") == 0? PASSFAIL));
    }
    else {
        printf("[%s] medianRating(): %s\n", __FILE__, UNTST);
    }

    // frequentRating.
    if (frequentRating) {                         // 2

        char *test_rating = "*****";
        int test_rating_size = sizeof(test_rating);
        printf("[%s] frequentRating(): %s\n",
            __FILE__, strncmp(test_rating, frequentRating(),
            test_rating_size) == 0? PASSFAIL);
    }
    else {
        printf("[%s] mostFrequentRating(): %s\n",
            __FILE__, UNTST);
    }

    // clearRatings.
    clearRatings();
    printf("[%s] clearRatings(): %s\n",
        __FILE__, (ratings() == 0? PASSFAIL));

    printf("[end_test]\n");
    return 0;
}
```

Ratings 1.1 depends on Averages 1.1. Therefore, to build the library as well as the test programs, `libAverages.A.dylib` must be installed in `~/lib`. To accomplish this, run this command after opening this document’s companion-file package:

```
[Avarages/1.1]% make install
```

These are commands needed to compile the library and the test programs from the `Ratings/1.1` directory:

```
[Ratings/1.1]% make
clang -dynamiclib -std=gnu99 Ratings.c -I<user_home>/include <user_home>/lib/libAverages.dylib -current_version 1.1 -compatibility_version 1.0 -fvisibility=hidden -o libRatings.A.dylib
clang Dependent.c libRatings.A.dylib <user_home>/lib/libAverages.dylib -o Dependent
clang Runtime.c -o Runtime
```

The output the program produces is shown in [Listing 13](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvomjs).

__Listing 13__  Test results for Ratings 1.1 used as a dependent library

```
> ./Dependent
[start_test]
[Dependent.c] ratings(): Passed
[Dependent.c] meanRating(): Passed
[Dependent.c] medianRating(): Passed
[Dependent.c] frequentRating(): Passed
[Dependent.c] clearRatings(): Passed
[end_test]
```

Programs that use `dlopen` to load your library should not fail if they are unable to obtain an address for your weakly exported functions with `dlsym`. Therefore, the program that tests your library as a runtime-loaded library, should allow for the absence of weakly imported functions.

[Listing 14](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvomjt) shows an updated version of the `Runtime` program. Notice that it uses dlsym to try get the addresses of the new functions but doesn’t exit with an error if they are unavailable. However, just before the program uses the new functions, it determines whether they actually exists. If they don’t exist, it doesn’t perform the test.

__Listing 14__  Testing Ratings 1.1 as a runtime-loaded library

```c
/* Runtime.c
 * Tests libRatings.A.dylib 1.1 as a runtime-loaded library.
 **********************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>
#include <string.h>
#include "Ratings.h"

#define PASSFAIL "Passed":"Failed"
#define UNTST "Untested"

int main(int argc, char **argv) {
    printf("[start_test]\n");

    // Open the library.
    char* lib_name = "./libRatings.A.dylib";
    void* lib_handle = dlopen(lib_name, RTLD_NOW);
    if (lib_handle) {
        printf("[%s] dlopen(\"%s\", RTLD_NOW): Successful\n", __FILE__, lib_name);
    }
    else {
        printf("[%s] Unable to open library: %s\n",
            __FILE__, dlerror());
        exit(EXIT_FAILURE);
    }

    // Get the function addresses.
    void (*addRating)(char*) = dlsym(lib_handle, "addRating");
    if (addRating) {
        printf("[%s] dlsym(lib_handle, \"addRating\"): Successful\n", __FILE__);
    }
    else {
        printf("[%s] Unable to get symbol: %s\n",
            __FILE__, dlerror());
        exit(EXIT_FAILURE);
    }
    char* (*meanRating)(void) = dlsym(lib_handle, "meanRating");
    if (meanRating) {
        printf("[%s] dlsym(lib_handle, \"meanRating\"): Successful\n", __FILE__);
    }
    else {
        printf("[%s] Unable to get symbol: %s\n",
            __FILE__, dlerror());
        exit(EXIT_FAILURE);
    }
    void (*clearRatings)(void) = dlsym(lib_handle, "clearRatings");
    if (clearRatings) {
        printf("[%s] dlsym(lib_handle, \"clearRatings\"): Successful\n", __FILE__);
    }
    else {
        printf("[%s] Unable to get symbol: %s\n",
            __FILE__, dlerror());
        exit(EXIT_FAILURE);
    }
    int (*ratings)(void) = dlsym(lib_handle, "ratings");
    if (ratings) {
        printf("[%s] dlsym(lib_handle, \"ratings\"): Successful\n", __FILE__);
    }
    else {
        printf("[%s] Unable to get symbol: %s\n",
            __FILE__, dlerror());
        exit(EXIT_FAILURE);
    }
    char* (*medianRating)(void) = dlsym(lib_handle, "medianRating");        // weak import
    char* (*frequentRating)(void) = dlsym(lib_handle, "frequentRating");    // weak import

    // Setup.
    addRating(NULL);
    addRating("");
    addRating("*");
    addRating("**");
    addRating("***");
    addRating("*****");
    addRating("*****");

    // ratings.
    printf("[%s] ratings(): %s\n", __FILE__, (ratings() == 6? PASSFAIL));

    // meanRating.
    printf("[%s] meanRating(): %s\n", __FILE__, (strcmp(meanRating(), "**") == 0)? PASSFAIL);

    // medianRating.
    if (medianRating) {
        printf("[%s] medianRating(): %s\n", __FILE__, (strcmp(medianRating(), "**") == 0? PASSFAIL));
    }
    else {
        printf("[%s] medianRating(): %s\n", __FILE__, UNTST);
    }

    // frequentRating.
    if (frequentRating) {
        char* mfr = "*****";
        printf("[%s] frequentRating(): %s\n", __FILE__, strncmp(mfr, frequentRating(), sizeof(mfr)) == 0? PASSFAIL);
    }
    else {
        printf("[%s] mostFrequentRating(): %s\n", __FILE__, UNTST);
    }

    // clearRatings.
    clearRatings();
    printf("[%s] clearRatings(): %s\n", __FILE__, (ratings() == 0? PASSFAIL));

    // Close the library.
    if (dlclose(lib_handle) == 0) {
        printf("[%s] dlclose(lib_handle): Successful\n", __FILE__);
    }
    else {
        printf("[%s] Unable to open close: %s\n",
            __FILE__, dlerror());
    }

    printf("[end_test]\n");
    return 0;
}
```

[Listing 15](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvomju) shows the output produced by Runtime.

__Listing 15__  Test results for Ratings 1.1 used as a runtime-loaded library

```
[Ratings/1.1]% ./Runtime
[start_test]
[Runtime.c] dlopen("./libRatings.A.dylib", RTLD_NOW): Successful
[Runtime.c] dlsym(lib_handle, "addRating"): Successful
[Runtime.c] dlsym(lib_handle, "meanRating"): Successful
[Runtime.c] dlsym(lib_handle, "clearRatings"): Successful
[Runtime.c] dlsym(lib_handle, "ratings"): Successful
[Runtime.c] ratings(): Passed
[Runtime.c] meanRating(): Passed
[Runtime.c] medianRating(): Passed
[Runtime.c] frequentRating(): Passed
[Runtime.c] clearRatings(): Passed
[Runtime.c] dlclose(lib_handle): Successful
[end_test]
```

To ensure that clients linked with version 1.0 of `libRatings.A.dylib` can use version 1.1 of the library, you can copy `Ratings/1.1/libRatings.A.dylib` to `Ratings/1.0`. When you run the first `Dependent` program, its output is the identical to the output it produced when it used version 1.0 of the library. The first `Dependent` program knows nothing about the functions introduced in version 1.1 of the Ratings library; therefore, it doesn’t call them.

A more interesting test, however, is making sure that clients linked with version 1.1 of the Ratings library can run when their copy of the library is replaced with version 1.0. To test this, execute the following commands in Terminal:

```
[           ]% cd <companion_dir>/Ratings/1.1
[Ratings/1.1]% make
[Ratings/1.1]% cd ../1.0
[Ratings/1.0]% make
[Ratings/1.0]% cp libRatings.A.dylib ../1.1
[Ratings/1.0]% cd ../1.1
```

[Listing 16](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvomjv) shows the output produced by the second version of `Dependent`, linked with Ratings 1.1, when it loads Ratings 1.0 instead of Ratings 1.1. The highlighted lines show where the client program did not find a particular function at runtime because the function does not exist in the version of the Ratings library that it’s using.

__Listing 16__  Test results for Ratings 1.0 used as a dependent library by a client linked against Ratings 1.1

```
[Ratings/1.1]% ./Dependent
[Ratings.c] initializer()
[start_test]
[Dependent.c] ratings(): Passed
[Dependent.c] meanRating(): Passed
[Dependent.c] medianRating(): Untested ```  ``` 
[Dependent.c] mostFrequentRating(): Untested ```  ``` 
[Dependent.c] clearRatings(): Passed
[end_test]
[Ratings.c] finalizer()
```

The second version of the `Runtime` test program produces similar output when using Ratings 1.0, as shown in [Listing 17](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanztfvjvomjw).

__Listing 17__  Test results for Ratings 1.0 used as a runtime-loaded library by a client liked with Ratings 1.1 when using Ratings 1.0

```
[Ratings/1.1]% ./Runtime
[start_test]
[Ratings.c] initializer()
[Runtime.c] dlopen("./libRatings.A.dylib", RTLD_NOW): Successful
[Runtime.c] dlsym(lib_handle, "addRating"): Successful
[Runtime.c] dlsym(lib_handle, "meanRating"): Successful
[Runtime.c] dlsym(lib_handle, "clearRatings"): Successful
[Runtime.c] dlsym(lib_handle, "ratings"): Successful
[Runtime.c] ratings(): Passed
[Runtime.c] meanRating(): Passed
[Runtime.c] medianRating(): Untested ```  ``` 
[Runtime.c] mostFrequentRating(): Untested ```  ``` 
[Runtime.c] clearRatings(): Passed
[Runtime.c] dlclose(lib_handle): Successful
[end_test]
[Ratings.c] finalizer()
```

[Next](Using%20Dynamic%20Libraries.md)[Previous](Dynamic%20Library%20Usage%20Guidelines.md)

