---
title: Dynamic Library Programming Topics
apple_id: TP40001869
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/DynamicLibraryUsageGuidelines.html
archived_at: '2026-07-15T07:24:26.958411Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dynamic Library Programming Topics](Introduction.md)


[Next](Creating%20Dynamic%20Libraries.md)[Previous](Dynamic%20Library%20Design%20Guidelines.md)

# Dynamic Library Usage Guidelines

The dynamic loader compatibility functions provide a portable and efficient way to load code at runtime. However, using the functions incorrectly can degrade app performance. This article shows how to correctly load and use dynamic libraries in your apps.

Dynamic libraries help to distribute an app’s functionality into distinct modules that can be loaded as they are needed. Dynamic libraries can be loaded either when the app launches or as it runs. Libraries that are loaded at launch time are called _dependent libraries_. Libraries that are loaded at runtime are called _dynamically loaded libraries_. You specify which dynamic libraries your app depends on by linking your app with them. However, it’s more efficient to use dynamic libraries as dynamically loaded libraries instead of dependent libraries. That is, you should open libraries when you’re about to use symbols they export and close them when you’re done. In some cases, the system unloads dynamically loaded libraries when it determines that they aren’t being used.

This article uses the word _image_ to refer to an app file or a dynamic library. App binaries contain the app’s code and the code from the static libraries the app uses. The dynamic libraries the app loads at launch time or runtime are separate images.

The dynamic loader loads an image’s dependent libraries when the image is opened; that is, when an app is loaded or when a dynamic library is opened. The dynamic loader binds references to symbols exported by dependent libraries lazily. Lazy binding means that the symbol references are bound only when the image actually uses the symbols. As a debugging measure, you can specify that all references to the exported symbols of a library be bound when the dynamic loader opens the library. You use the compiler `-bind_at_load` command-line option when generating the dynamic library.

To use a dynamic library that is not a dependent library of your image, use the `dlopen(3) OS X Developer Tools Manual Page` function. This function tells the dynamic loader to load a specific dynamic library into the address space of the current process. This function also allows you to specify when the dynamic loader binds the library’s references to the corresponding exported symbols in its dependent libraries and whether to place the library’s exported symbols in the current process’s global scope or a local scope. This function returns a handle called _library handle_. This handle represents the dynamically loaded library in calls to `dlsym` (to use an exported symbol) and `dlclose` (to close the library). The library handle provides `dlsym` a limited domain within which to search for a symbol (see [Using Symbols](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsmryfvjvooi) for details). The client must call `dlclose` when it’s finished using the dynamically loaded library (for example, when the module that opened the library has finished its task).

A dynamic library may itself have dependent libraries. To find out which libraries a dynamic library depends on, use the `otool -L <library>` command. Before using the library, you must ensure that all its dependent libraries are present in your computer. Otherwise, the dynamic loader doesn’t load your app or library when requested at launch time or when the library is opened with `dlopen`.

A process can open the same dynamic library several times without closing it. The `dlopen` function returns the same library handle it returned in the first call, but it also increments the reference count associated with the handle. Calls to `dlclose` decrement the library handle’s reference count. Therefore, you must balance every call to `dlopen` with a call to `dlclose`. When the reference count for a library handle reaches 0, the dynamic loader may remove the library from the address space of the app.

The first parameter to `dlopen(3) OS X Developer Tools Manual Page` is the name of the dynamic library to open. This may be a filename or a partially or fully qualified pathname. For example, `libCelsus.dylib` , `lib/libCelsus.dylib` , or `/usr/local/libCelsus.dylib`.

The dynamic loader searches for libraries in the directories specified by a set of environment variables and the process’s current working directory. These variables, when defined, must contain a colon-separated list of pathnames (absolute or relative) in which the dynamic loader searches for libraries. Table 1 lists the variables.

__Table 1__  Environment variables that define dynamic-loader search paths

| Environment variable | Default value |
| `LD_LIBRARY_PATH` | No default value |
| `DYLD_LIBRARY_PATH` | No default value |
| `DYLD_FALLBACK_LIBRARY_PATH` | `$HOME/lib;/usr/local/lib;/usr/lib` |

When the library name is a filename (that is, when it doesn’t include directory names), the dynamic loader searches for the library in several locations until it finds it, in the following order:

1. `$LD_LIBRARY_PATH`
2. `$DYLD_LIBRARY_PATH`
3. The process’s working directory
4. `$DYLD_FALLBACK_LIBRARY_PATH`

When the library name contains at least one directory name, that is, when the name is a pathname (relative or fully qualified), the dynamic loader searches for the library in the following order:

1. `$DYLD_LIBRARY_PATH` using the filename
2. The given pathname
3. `$DYLD_FALLBACK_LIBRARY_PATH` using the filename

For example, say you set the environment variables introduced earlier as shown in the following table.

| Environment variable | Value |
| --- | --- |
| `LD_LIBRARY_PATH` | `./lib` |
| `DYLD_LIBRARY_PATH` | `/usr/local/dylibs` |
| `DYLD_FALLBACK_LIBRARY_PATH` | `/usr/local/lib` |

Assuming your app calls `dlopen` with the filename `libCelsus.dylib`, the dynamic loader would attempt to open the library using the following pathnames, in order:

| Pathname | Description |
| --- | --- |
| `./lib/libCelsus.dylib` | `LD_LIBRARY_PATH` environment variable |
| `/usr/local/dylibs/libCelsus.dylib` | `DYLD_LIBRARY_PATH` environment variable |
| `libCelsus.dylib` | Current working directory |
| `/usr/local/lib/libCelsus.dylib` | `DYLD_FALLBACK_LIBRARY_PATH` environment variable |

If the app calls `dlopen` with the pathname `/libs/libCelsus.dylib`, the dynamic loader tries to find the library using these pathnames, in order:

| Pathname | Description |
| --- | --- |
| `/usr/local/dylibs/libCelsus.dylib` | `DYLD_LIBRARY_PATH` environment variable |
| `/libs/libCelsus.dylib` | Path as given |
| `/usr/local/lib/libCelsus.dylib` | `DYLD_FALLBACK_LIBRARY_PATH` environment variable |

The second parameter of the `dlopen(3) OS X Developer Tools Manual Page` function specifies two properties: the scope of the library's exported symbols in the current process and when to bind the app’s references the those symbols.

Symbol scope directly affects the performance of apps. Therefore, it’s important that you set the appropriate scope for a library your app opens at runtime.

A dynamically loaded library’s exported symbols can be in one of two levels of scope in the current process: global and local. The main difference between the scopes is that the symbols in the global scope are available to all images in the process, including other dynamically loaded libraries. Symbols in the local scope can be used only by the image that opened the library. See [Using Symbols](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsmryfvjvooi) for more information.

When the dynamic loader searches for symbols, it performs string comparisons with every symbol in the search scope. Reducing the number of symbols the dynamic loader has to go through to find the desired symbol improves your app’s performance. Opening all dynamically loaded libraries into the local scope instead of the global scope maximizes symbol search performance.

You should never need to open a dynamic library into the process’s global scope so that all modules in the app have access to its symbols. Instead, each module that uses the library should open it into its local scope. When done, the module should close the library. If you want the symbols exported by the library to be available to all images in the process, consider making the library a dependent library of the app.

The parameter used to specify symbol scope is also used to specify when the undefined external symbols of the dynamically loaded library are resolved (or bound with their definitions in the library’s own dependent libraries). Undefined external symbols of dynamically loaded libraries can be resolved either immediately or lazily. If a client app uses immediate binding when opening a dynamic library with `dlopen` , the dynamic loader binds all the undefined external symbols of the dynamically loaded library before returning control to the client app. For example, Listing 1 shows the log messages the dynamic loader produces when the `DYLD_PRINT_BINDINGS` environment variable is set and a client app loads a dynamic library called `libPerson.dylib` :

__Listing 1__  Bindings resolved during call to `dlopen` using immediate binding

```
dyld: lazy bind: client:0x107575050 = libdyld.dylib:_dlopen, *0x107575050 = 0x7FFF88740922
dyld: bind: libPerson.dylib:0x1075A9000 = libdyld.dylib:dyld_stub_binder, *0x1075A9000 = 0x7FFF887406A0
dyld: bind: libPerson.dylib:0x1075A9220 = libobjc.A.dylib:__objc_empty_cache, *0x1075A9220 = 0x7FFF7890EC10
dyld: bind: libPerson.dylib:0x1075A9248 = libobjc.A.dylib:__objc_empty_cache, *0x1075A9248 = 0x7FFF7890EC10
dyld: bind: libPerson.dylib:0x1075A9228 = libobjc.A.dylib:__objc_empty_vtable, *0x1075A9228 = 0x7FFF7890CF60
dyld: bind: libPerson.dylib:0x1075A9250 = libobjc.A.dylib:__objc_empty_vtable, *0x1075A9250 = 0x7FFF7890CF60
dyld: bind: libPerson.dylib:0x1075A9218 = CoreFoundation:_OBJC_CLASS_$_NSObject, *0x1075A9218 = 0x7FFF77C40BA8
dyld: bind: libPerson.dylib:0x1075A9238 = CoreFoundation:_OBJC_METACLASS_$_NSObject, *0x1075A9238 = 0x7FFF77C40B80
dyld: bind: libPerson.dylib:0x1075A9240 = CoreFoundation:_OBJC_METACLASS_$_NSObject, *0x1075A9240 = 0x7FFF77C40B80
dyld: bind: libPerson.dylib:0x1075A9260 = CoreFoundation:___CFConstantStringClassReference, *0x1075A9260 = 0x7FFF77C72760
dyld: bind: libPerson.dylib:0x1075A9280 = CoreFoundation:___CFConstantStringClassReference, *0x1075A9280 = 0x7FFF77C72760
```

The first log message indicates that the client app’s `_dlopen` undefined symbol was bound. The remaining messages are the bindings the dynamic loader performs on the dynamic library as part of the loading process before returning control to the calling routine. When using lazy binding, the dynamic loader resolves only the client’s reference to the `dlopen` function, returning control to the calling routine much sooner. For more information on dynamic loader logging, see [Logging Dynamic Loader Events](Logging%20Dynamic%20Loader%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanzxfvjvomi).

Once a library has been opened with `dlopen`, the scope defined for it cannot be changed by subsequent calls to `dlopen` to load the same library. For example, if the process opens a library that hasn’t been loaded into the local scope and later opens the same library into the global scope, the opened library retains its local status. That is, the symbols the library exports do not become available in the global scope with the latter call. This is true even if the library is closed before reopening it within the same process.

Immediate binding slows the loading of dynamic libraries, especially when those libraries contain many undefined external symbols. However, immediate binding can help during development and testing of dynamic libraries because when the dynamic loader cannot resolve all the undefined external symbols of a dynamically loaded library, the app terminates with an error. When deploying the app, however, you should use lazy loading because undefined external symbols are bound only when necessary. Loading dynamic libraries this way can help make your app feel more responsive to its users.

The external undefined symbols in dependent libraries are bound when they are first used unless the client image’s compile line includes the `-bind_at_load` option. See the `ld` man page for details.

After opening a dynamic library using `dlopen(3) OS X Developer Tools Manual Page`, an image uses the `dlsym(3) OS X Developer Tools Manual Page` function to get the address of the desired symbol before using it. This function takes two parameters. The first one specifies in which libraries the dynamic loader looks for the symbol. The second parameter specifies the name of the symbol. For example:

```
symbol_pointer = dlsym(library_handle, "my_symbol")
```

This invocation tells the dynamic loader to search for a symbol named `my_symbol` among the symbols exported by the dynamically loaded library represented by the `library_handle` variable.

There are three scopes the dynamic loader can search for a symbol: a specific dynamic library, the current image's dependent libraries, and the global scope of the process:

- __The local scope:__ To search the symbols exported by a particular dynamic library that has been loaded using `dlopen`, you provide `dlsym` with the handle to that library. This is the most efficient usage model.
- __The next scope:__ This search scope is useful only when a module has interposed a symbol exported by a dependent library. For example, you may need to intercept all calls to a system function to perform bookkeeping before calling the real implementation. In that case, in your custom definition of the function, you get the address of the function you interposed by invoking `dlsym` with the `RTLD_NEXT` special handle instead of the handle to a particular library. Such a call returns the address of the function that would have been executed if you hadn’t masked out that implementation with your own. Therefore, only the dependent libraries of the current image are searched; any other libraries, including libraries opened by the image making the `dlsym` call, are not searched. Also, in a flat namespace, the search starts in the first dependent library listed after the current one when the app was linked.
- __The global scope:__ To search the global scope, you call `dlsym` with the `RTLD_DEFAULT` special handle. The dynamic loader searches the dependent libraries (loaded at launch time) and the dynamically loaded libraries (loaded at runtime with `RTLD_GLOBAL` ) for the first match of the symbol name given to `dlsym` . You should avoid performing global symbol searches because they are the most inefficient.

To illustrate the concepts introduced in this section, take the app depicted in Figure 1. It shows that the app has two dependent libraries, `libArt.dylib` and `libBus.dylib`. The `libBus.dylib` library itself has two dependent libraries, `libBus1.dylib` and `libBus2.dylib`. The `libBus1.dylib` library has one dependent library, `libBus1a.dylib`. In addition, there are four dynamic libraries the app doesn’t depend on, `libCar.dylib`, `libCar1.dylib`, `libDot.dylib`, and `libDot1.dylib`. The `libCar1.dylib` library is a dependent library of `libCar.dylib` and `libDot1.dylib` is a dependent library of `libDot.dylib`. All the libraries except `libArt.dylib` export the `dependencies` function. Each library has a unique implementation of the `...name` function.

__Figure 1__  App with dependent library hierarchy

!

The app image can access the exported symbols in `libArt.dylib` and `libBus.dylib` directly, as shown in Listing 2.

__Listing 2__  App image using symbols exported by dependent libraries through undefined external references

```c
#include <stdio.h>
extern char* A_name();          // libArt.dylib
extern char* dependencies();    // libBus.dylib

int main(void) {
    printf("[%s] libArt.A_name() = %s\n", __FILE__, A_name());
    printf("[%s] libBus.dependencies() = %s\n", __FILE__, dependencies());
}
```

The app image, however, cannot directly access the symbols exported by `libBus1.dylib`, `libBus1a.dylib`, and `libBus2.dylib` because those libraries are not dependent libraries of the app image. To gain access to those symbols, the app image has to open the corresponding libraries using `dlopen`, as shown in Listing 3.

__Listing 3__  App image using a symbol exported by a dynamic library loaded at runtime

```c
#include <stdio.h>
#include <dlfcn.h>

int main(void) {
    void* Bus1a_handle = dlopen("libBus1a.dylib", RTLD_LOCAL);
    if (Bus1a_handle) {
        char* (*b1a_name)() = dlsym(Bus1a_handle, "B1a_name");
        if (b1a_name) {
            printf("[%s] libBus1a.B1a_name() = %s\n",
                __FILE__, b1a_name());
        }
    }
    else {
        printf("[%s] Unable to open libBus1a.dylib: %s\n",
            __FILE__, dlerror());
    }
    dlclose(Bus1a_handle);
}
```

So far you have seen how to access symbols either through references to imported symbols or by obtaining the address of the desired symbol by calling `dlsym` with the handle of the corresponding library or with the `RTLD_DEFAULT` special handle. As mentioned earlier, interposed symbols offer the ability to change the definition of a symbol exported by a dependent library.

To access the original definition of interposed symbols, you call `dlsym` with the `RTLD_NEXT` special handle. Listing 4 shows the implementation of the `dependencies` function in the Bus library (the implementation is identical in Bus1 and Bus1a). The function in Bus returns the name of the library (contained in the `k_lib_name` variable) concatenated with a separator string and the text returned by the next definition of `dependencies`, which is found in the Bus1 library. The definition in Bus1 concatenates its name with a separator string and the text returned by the definition in Bus1a. The definition in Bus1a is the last that would’ve been found if none of the client images had defined their own version. Therefore, when Bus1a invokes `dlsym(RTLD_NEXT, "dependencies")` no other definitions for `dependencies` are found. That’s the end of the interposition hierarchy of the `dependencies` function.

__Listing 4__  Library image using an interposed symbol

```c
#include <string.h>
static char* k_lib_name = "libBus";
char* dependencies(void) {
    char _dependencies[50] = "";
    strcpy(_dependencies, k_lib_name);
    char* (*next_dependencies)() =
        dlsym(RTLD_NEXT, "dependencies");// look for next definition
    if (next_dependencies) {
        strncat(_dependencies, ", ",
            sizeof(_dependencies) - strlen(_dependencies) - 1);
        strncat(_dependencies, next_dependencies(),
            sizeof(_dependencies) - strlen(_dependencies) - 1);
    }
    return strdup(_dependencies);
}
```

When the image calls the dependencies function in the Bus library, it obtains the names of all the libraries the Bus library depends on, as shown in Listing 5.

__Listing 5__  App image calling an interposed function

```c
#include <stdio.h>
extern char* dependencies();    // libBus.dylib

int main(void) {
    printf("[%s] libBus.dependencies() = %s\n",
        __FILE__, dependencies());
}
```


To promote compatibility with earlier or later revisions, a dynamic library may export some or all its public symbols as weakly linked symbols. A _weakly linked symbol_ is one for which the compiler generates a weak reference when a client is linked with a library. Weakly linked symbols may have the `weak_import` attribute in their declarations in the library’s header files, or the library’s developer may otherwise document which of the library’s public symbols are weakly linked. A third way to identify weakly linked symbols it by executing the command:

```
nm -m <client_file> | grep weak
```

This command lists the weakly linked symbols imported from dependent libraries.

A weakly linked symbol may or may not be defined by a dependent library. That is, although the symbol is declared in a header file, the corresponding dynamic library file may not contain an implementation of that symbol. Listing 6 shows how a weakly linked symbol may be declared in a header file for a dynamic library. Clients that use this header file as their interface to the corresponding dependent library are guaranteed that `name` and `set_name` are defined. However, `clear_name` may not be implemented. The dependent library loads successfully whether or not it implements `clear_name`. But it doesn’t load if it doesn’t define either `name` or `set_name`. When the library doesn’t implement a weakly linked symbol, the dynamic loader sets to 0 any client references to the symbol.

__Listing 6__  Header file with a weakly linked symbol declaration

```
/* File: Person.h */
#define WEAK_IMPORT __attribute__((weak_import))
char* name(void);
void set_name(char* name);
WEAK_IMPORT
void clear_name(void);
```

Weakly linked symbols are used by library developers to maximize the compatibility of a client with earlier or newer versions of a dependent library. For example, a symbol that was implemented in a particular revision of a library may not be available in a later revision. But a client linked with the first revision also works with the second revision. Client developers, however, must ensure the existence of the symbol in the running process before executing it. This mechanism is also used to provide a standard interface to plug-ins, which may or may not implement the entire interface.

Listing 7 shows code that ensures that a particular function is defined before using it. When the function is not found, the client uses a different function to accomplish the desired task. In this case, the fallback function is not a weakly linked symbol, so no test is required. Other situations may not offer an alternate interface. In such cases the client may not be able to perform the desired task.

__Listing 7__  Using a weakly linked symbol

```
// Clear the 'name' property.
if (clear_name) {
    clear_name();
}
else {
    set_name(" ");
}
```


How client developers use a C++ class depends on whether the dynamic library that implements it is loaded when the client is loaded (dependent library) or at a later point (runtime loaded library). Dependent-library classes can be used directly. That is, clients can create and delete objects with the `new` and `delete` operators. Classes implemented in libraries loaded at runtime with `dlopen(3) OS X Developer Tools Manual Page` are called _runtime loaded classes_.

A runtime loaded class must be instantiated by the client using that class’s factory functions, declared as part of the class’s interface. _Factory functions_ create and destroy instances of a specific class: Constructor functions instantiate objects and destructor functions destroy them. Clients must use factory functions instead of `new` and `delete` because the dynamic loader doesn’t have access to a runtime loaded class’s constructors and destructors. When the client calls a factory function, the library invokes the appropriate constructor and destructor on the client’s behalf. After you create an instance of a runtime loaded class, you invoke its member functions the same way you would call them if the class were defined locally.

The interface for C++ classes implemented in dynamic libraries is made up of at least the class declaration and a set of factory functions. The class interface includes one type definition per constructor function. To use a factory function, you must create an object of the appropriate type and get the address of the function with `dlsym(3) OS X Developer Tools Manual Page`. You can then call the factory function to create or destroy an object of the class.

Listing 8 shows the interface to the `Person` class, implemented in the Person library.

__Listing 8__  C++ class interface

```
/* File: Person.h */
class Person {
    private:
        char _person_name[30];
    public:
        Person();
        Person(char* name);
        virtual void set_name(char person_name[]);
        virtual char* name();
};

// Constructor functions and function types.
extern "C" Person* NewPerson(void);
typedef Person * Person_creator(void);
extern "C" Person* NewPersonWithName(char name[]);
typedef Person * PersonWithName_creator(char name[]);

// Destructor function and function type.
extern "C" void DeletePerson(Person* person);
typedef void Person_disposer(Person*);
```

Listing 9 shows a possible implementation of the `Person` class.

__Listing 9__  Implementation of the `Person` class in the Person library

```c
/* File: Person.cpp */
#include <iostream>
#include "Person.h"

#define EXPORT __attribute__((visibility("default")))

EXPORT
Person::Person() {
    char default_name[] = "<no value>";
    this->set_name(default_name);
}

EXPORT
Person::Person(char *name) {
    this->set_name(name);
}

EXPORT
Person* NewPerson(void) {
    return new Person;
}

EXPORT
Person* NewPersonWithName(char name[]) {
    return new Person(name);
}

EXPORT
void DeletePerson(Person* person) {
    delete person;
}

void Person::set_name(char name[]) {
    strcpy(_person_name, name);
}

char* Person::name(void) {
    return _person_name;
}
```

Note that the `Person` class has two constructor functions, `NewPerson` and `NewPersonWithName`. Each function declaration has a corresponding type, `Person_creator` and `PersonWithName_creator`. Listing 10 and Listing 11 show how a client may use the Person library.

__Listing 10__  Client using a C++ dependent library

```c
/* File: Client.cpp */
#include <iostream>
#include "Person.h"

int main() {
    using std::cout;
    using std::cerr;

    // Create Person objects.
    Person* person1 = new Person();
    char person_name[] = "Cendrine";
    Person* person2 = new Person(person_name);
    cout << "[" << __FILE__ << "] person1->name() = " << person1->name() << "\n";
    cout << "[" << __FILE__ << "] person2->name() = " << person2->name() << "\n";

    // Use Person objects.
    char person1_name[] = "Floriane";
    person1->set_name(person1_name);
    cout << "[" << __FILE__ << "] person1->name() = " << person1->name() << "\n";
    char person2_name[] = "Marcelle";
    person2->set_name(person2_name);
    cout << "[" << __FILE__ << "] person2->name() = " << person2->name() << "\n";

    // Destroy Person objects.
    delete person1;
    delete person2;

    return 0;
}
```


__Listing 11__  Client using a C++ dynamically loaded library

```c
/* File: Client.cpp */
#include <iostream>
#include <dlfcn.h>
#include "Person.h"

int main() {
    using std::cout;
    using std::cerr;

    // Open the library.
    void* lib_handle = dlopen("./libPerson.dylib", RTLD_LOCAL);
    if (!lib_handle) {
        exit(EXIT_FAILURE);
    }

    // Get the NewPerson function.
    Person_creator* NewPerson = (Person_creator*)dlsym(lib_handle, "NewPerson");
    if (!NewPerson) {
        exit(EXIT_FAILURE);
    }

    // Get the NewPersonWithName function.
    PersonWithName_creator* NewPersonWithName = (PersonWithName_creator*)dlsym(lib_handle, "NewPersonWithName");
    if (!NewPersonWithName) {
        exit(EXIT_FAILURE);
    }

    // Get the DeletePerson function.
    Person_disposer* DeletePerson =
        (Person_disposer*)dlsym(lib_handle, "DeletePerson");
    if (!DeletePerson) {
        exit(EXIT_FAILURE);
    }

    // Create Person objects.
    Person* person1 = NewPerson();
    char person_name[] = "Cendrine";
    Person* person2 = NewPersonWithName(person_name);
    cout << "[" << __FILE__ << "] person1->name() = " << person1->name() << "\n";
    cout << "[" << __FILE__ << "] person2->name() = " << person2->name() << "\n";

    // Use Person objects.
    char person1_name[] = "Floriane";
    person1->set_name(person1_name);
    cout << "[" << __FILE__ << "] person1->name() = " << person1->name() << "\n";
    char person2_name[] = "Marcelle";
    person2->set_name(person2_name);
    cout << "[" << __FILE__ << "] person2->name() = " << person2->name() << "\n";

    // Destroy Person objects.
    DeletePerson(person1);
    DeletePerson(person2);

    // Close the library.
    if (dlclose(lib_handle) != 0) {
        exit(EXIT_FAILURE);
    }

    return 0;
}
```


To use an Objective-C class or category implemented in a dynamic library, a client should have an interface to the class or category. With knowledge of the class’s correct interface, the client can create instances of the class that are appropriately typed. Otherwise, the compiler produces warnings for methods with missing declarations.

The interfaces of Objective-C classes and categories are published in the library’s header files as protocols. Instantiating a class implemented in a dependent library is no different from doing the same for a locally defined class. However, when you load a dynamic library at runtime using `dlopen(3) OS X Developer Tools Manual Page`, you must obtain the appropriate class by calling the [objc_getClass](https://developer.apple.com/documentation/objectivec/1418952-objc_getclass) function.

For example, Listing 12 contains the interfaces for the `Person` class and the `Titling` category to that class, which are implemented by the Person dynamic library.

__Listing 12__  Interface to the `Person` class and its `Titling` category

```objc
/* File: Person.h */
#import <Foundation/Foundation.h>

@protocol Person
- (void)setName:(NSString*)name;
- (NSString*)name;
@end

@interface Person : NSObject <Person> {
    @private
    NSString* _person_name;
}
@end

/* File: Titling.h */
#import <Foundation/Foundation.h>
#import "Person.h"

@protocol Titling
- (void)setTitle:(NSString*)title;
@end

@interface Person (Titling) <Titling>
@end
```

A client compiled with these interfaces and linked with the Person library can create objects that implement the interfaces in a very straightforward way, as shown in Listing 13.

__Listing 13__  Example of a client that uses the Person library as a dependent library

```objc
/* File: Client.m */
#import <Foundation/Foundation.h>
#import "Person.h"
#import "Titling.h"

int main() {
    @autoreleasepool {
        // Create an instance of Person.
        Person<Titling>* person = [[Person alloc] init];

        // Use person.
        [person setName:@"Perrine LeVan"];
        [person setTitle:@"Ms."];
        NSLog(@"[%s] main: [person name] = %@", __FILE__, [person name]);
    }
    return(EXIT_SUCCESS);
}
```

When the Person library is a runtime loaded library, however, the client must obtain a reference to the Person class from the Objective-C runtime after loading the library, using `objc_getClass`. It can then use that reference to instantiate a `Person` object. However, the variable that holds the instance must by typed as an `NSObject` that implements the `Person` and `Titling` protocols to avoid compiler warnings. When done, the client closes the library, as shown in Using Weakly Linked Symbols.

__Listing 14__  Example of a client that uses the Person library as a runtime loaded library

```objc
/* File: Client.m */
#import <Foundation/Foundation.h>
#import <objc/runtime.h>
#import <dlfcn.h>
#import "Person.h"
#import "Titling.h"

int main() {
    @autoreleasepool {
        // Open the library.
        void* lib_handle = dlopen("./libPerson.dylib", RTLD_LOCAL);
        if (!lib_handle) {
            NSLog(@"[%s] main: Unable to open library: %s\n",
            __FILE__, dlerror());
            exit(EXIT_FAILURE);
        }

        // Get the Person class (required with runtime-loaded libraries).
        Class Person_class = objc_getClass("Person");
        if (!Person_class) {
            NSLog(@"[%s] main: Unable to get Person class", __FILE__);
            exit(EXIT_FAILURE);
        }

        // Create an instance of Person.
        NSLog(@"[%s] main: Instantiating Person_class", __FILE__);
        NSObject<Person,Titling>* person = [[Person_class alloc] init];

        // Use person.
        [person setName:@"Perrine LeVan"];
        [person setTitle:@"Ms."];
        NSLog(@"[%s] main: [person name] = %@", __FILE__, [person name]);

        // Close the library.
        if (dlclose(lib_handle) != 0) {
            NSLog(@"[%s] Unable to close library: %s\n",
                __FILE__, dlerror());
            exit(EXIT_FAILURE);
        }
    }
    return(EXIT_SUCCESS);
}
```


One of the dynamic loader compatibility (DLC) functions, `dladdr(3) OS X Developer Tools Manual Page`, provides information on the image and nearest symbol that corresponds to an address. You can use this function to obtain information about the library that exports a particular symbol.

The information `dladdr` provides is returned through an output parameter of type `Dl_info`. These are the names of the structure’s fields as well as their descriptions:

- `dli_fname`: The pathname of the image
- `dli_fbase`: The base address of the image within the process
- `dli_sname`: The name of the symbol with an address that is equal to or lower than the address provided to `dladdr`
- `dli_saddr`: The address of the symbol indicated by `dli_sname`

Listing 15 shows how an image can get information about a symbol:

__Listing 15__  Getting information about a symbol

```c
#include <stdio.h>
#include <dlfcn.h>

extern char* dependencies();

int main(void) {
    // Get information on dependencies().
    Dl_info info;
    if (dladdr(dependencies, &info)) {
        printf("[%s] Info on dependencies():\n", __FILE__);
        printf("[%s]    Pathname: %s\n",         __FILE__, info.dli_fname);
        printf("[%s]    Base address: %p\n",     __FILE__, info.dli_fbase);
        printf("[%s]    Nearest symbol: %s\n",   __FILE__, info.dli_sname);
        printf("[%s]    Symbol address: %p\n",   __FILE__, info.dli_saddr);
    }
    else {
        printf("[%s] Unable to find image containing the address %x\n",
    __FILE__, &dependencies);
    }
}
```

[Next](Creating%20Dynamic%20Libraries.md)[Previous](Dynamic%20Library%20Design%20Guidelines.md)

