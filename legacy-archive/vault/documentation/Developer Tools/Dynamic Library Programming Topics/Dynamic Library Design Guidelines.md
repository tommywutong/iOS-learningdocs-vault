---
title: Dynamic Library Programming Topics
apple_id: TP40001869
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/DynamicLibraryDesignGuidelines.html
archived_at: '2026-07-15T07:24:25.822942Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dynamic Library Programming Topics](Introduction.md)


[Next](Dynamic%20Library%20Usage%20Guidelines.md)[Previous](Overview%20of%20Dynamic%20Libraries.md)

# Dynamic Library Design Guidelines

Dynamic libraries, in addition to grouping common functionality, help reduce an app’s launch time. However, when designed improperly, dynamic libraries can degrade the performance of their clients. (A dynamic library _client_ is an app or a library that either is linked with the library or loads the library at runtime. This document also uses the word _image_ to refer to dynamic-library clients.) Therefore, before creating a dynamic library, you must define its purpose and its intended use. Devising a small and effective interface to the library’s functionality goes a long way towards facilitating its adoption in other libraries or apps.

This article addresses the main issues dynamic library developers face when designing and implementing dynamic libraries. The focus of this article is to show you how to design libraries in a way that facilitates their improvement through revisions and makes it easy for the libraries’ users to correctly interact with the library.

Dynamic libraries contain code that can be shared by multiple apps in a user’s computer. Therefore, they should contain code that several apps can use. They should not contain code specific to one app. These are the attributes of an optimal dynamic library:

- __Focused:__ The library should focus on few, highly related goals. A highly focused library is easier to implement and use than a multi-purpose library.
- __Easy to use:__ The library’s interface, the symbols that the clients of the library use to interact with it, should be few and easy to understand. A simple interface allows a library’s users to understand its functionality faster than they could understand a large interface.
- __Easy to maintain:__ The library’s developers must be able to make changes to the library that improve its performance and add features. A clear separation between a library’s private and public interfaces gives library developers freedom to make profound changes to the library’s inner workings with minimal impact to its clients. When designed properly, a client created with an early version of a library can use the latest version of the library unchanged and benefit from the improvements it provides.

The client of a dynamic library can use the library in two ways: as a dependent library or as a runtime-loaded library. A _dependent library_, from the client’s point of view, is a dynamic library the client is linked with. Dependent libraries are loaded into the same process the client is being loaded into as part of its load process. For example, when an app is launched, its dependent libraries are loaded as part of the launch process, before the main function is executed. When a dynamic library is loaded into a running process, its dependent libraries are loaded into the process before control is passed to the routine that opened the library.

A _runtime loaded library_ is a dynamic library the client opens with the `dlopen(3) OS X Developer Tools Manual Page` function. Clients do not include runtime loaded libraries in their link line. The dynamic loader, therefore, doesn’t open these libraries when the client is loaded. Clients open a runtime loaded library when they’re about to use a symbol it exports. Clients don’t have any undefined external references to symbols in runtime loaded libraries. Clients get the address of all the symbols they need from runtime loaded libraries by calling the `dlsym(3) OS X Developer Tools Manual Page` function with the symbol name.

A client must always be compatible with its dependent libraries. Otherwise, an app doesn’t launch or a runtime loaded library fails to load.

When you design a dynamic library, you may have to consider its ongoing maintenance. Sometime you may have to make changes to the library to implement new features or to correct problems. But you also have to think about the library’s existing clients. There are two types of revisions you can make to a library: revisions that are compatible with current clients and require no client-developer intervention and revisions that require that clients be linked with the new revision. The former are _minor revisions_ and the latter are _major revisions_.

The following sections explore compatibility issues to consider before implementing a library that may need to be updated at a later time.

As a library upon which existing clients depend is revised, changes to it may affect the clients’ ability to use new versions of the library. The degree to which a client can use earlier or later versions of a dependent library than the one it is linked with is called _client compatibility_.

Some changes are minor; these include adding symbols that are unknown to clients. Other changes are major; such changes include removing a symbol, changing a symbol’s size or visibility, and changing the semantics of a function. All the symbols a library exposes to clients make up the library’s ABI (app binary interface). The library’s API (app programming interface) comprises only the functions that a library makes available to its clients. The degree to which a library’s ABI remains the same from the point of view of the clients that were developed using an earlier version of the library determines the library’s stability. Ensuring that a library’s ABI remains stable guarantees that clients can use newer versions of the library unchanged. That is, users of an app that depends on a library that’s updated regularly can see their app’s performance improve as they update the library (think of the OS X Software Update mechanism) without obtaining a new version of the app.

For example, assume an app is linked with the first version of a dynamic library and released to end users. Later, the library’s developer makes minor changes to the library and releases it. When end users install the new version of the library on their computers, the app can use the new version without requiring the end users to get an updated app binary from the developer. The app may benefit from efficiency improvements made to the library’s implementation. And, depending on how the library was written, the app might be able to take advantage of features introduced by the new version. However, these features are accessed by the app only through the API available in the first version of the library. Any interfaces introduced in the new version of the library go unused by the app.

[Figure 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdamjtfvjvomi) illustrates the life cycle of the Draw dynamic library and one of its clients.

__Figure 1__  The life cycle of a dynamic library and a client

!!

This list describes the versions of the library and the client:

- Draw 1.0 is the initial version of the library. It exports two functions, `draw_line` and `draw_square`.
- Client 1.0 is linked with Draw 1.0. Therefore, it can use the two symbols the library exports.
- Draw 1.1 has faster versions of `draw_line` and `draw_square` , but their semantics are unchanged, maintaining client compatibility. This is a compatible, minor revision because Client 1.0 can use Draw 1.1.
- Draw 1.2 introduces the `draw_polygon` function. The API of the new revision of the library is a superset of the previous version’s API. The Draw 1.1 API subset of the 1.2 version is unchanged. Therefore, Client 1.0 can use Draw 1.2. However, Client 1.0 doesn't know of the existence of `draw_polygon` and, therefore, it doesn’t use it. This is a minor revision because the API Client 1.0 knows about is unchanged in Draw 1.2. But this is also an incompatible revision because the API changed. Clients linked with this version of the library cannot use earlier versions.
- Client 1.1 is linked with Draw 1.2 and uses `draw_polygon`. Client 1.1 cannot use earlier versions of the library because it uses `draw_polygon`, a function that isn’t exported by those versions. However, if the library’s developer adds the `weak_import` attribute to the symbol’s definition, Client 1.1 would be able to use earlier versions of the library by ensuring that `draw_polygon` exists in its namespace before using it. If the symbol isn’t defined, the client may use other means of performing the desired task, or it may not perform the task. See [Symbol Exporting Strategies](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdamjtfvjvomjy) for details.
- Draw 2.0 doesn’t export `draw_square`. This is a major revision because a symbol exported in the previous version of the library is not exported in this version. Clients linked with this version of the library cannot use earlier versions.

Clients should be able to use all the minor revisions to the library they’re linked with without relinking. In general, to use a major revision of a library, the client must be linked with the new version. The client may also need to be changed to take advantage of new symbols, to adapt its use of symbols that have been modified, or to not use symbols that are not exported by the new revision.

The filename of a dynamic library normally contains the library’s name with the `lib` prefix and the `.dylib` extension. For example, a library called Dynamo would have the filename `libDynamo.dylib`. However, if a library may go through one or more revisions after it’s released, its filename must include the major version number of the revision. Clients linked with libraries whose filename includes the major version number of the revision never use a new major revision of the library because major revisions are published under different filenames. This versioning model prevents clients from using library revisions whose API is incompatible with the API known to the clients.

When you publish a dynamic library intended to have future revisions, you must disclose the library’s major version number in its filename. For example, the filename for the first version of the Draw library, introduced in [Defining Client Compatibility](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdamjtfvjvomq), could be `libDraw.A.dylib`. The letter A specifies the major version number for the initial release. You can use any nomenclature for the major version. For example, the Draw library could also be named `libDraw.1.dylib`, or `libDraw.I.dylib`. The important thing is that the filenames of subsequent major revisions of the library have different (and preferably incremental) major version numbers. Continuing the Draw library example, a major revision to the library could be named `libDraw.B.dylib` , `libDraw.2.dylib`, or `libDraw.II.dylib`. Minor revisions to the library are released under the same filename used by the previous major revision.

In addition to the major version number, a library has a minor version number. The minor version number is an incremental number using the format `X[.Y[.Z]]` , where X is a number between 0 and 65535, and Y and Z are numbers between 0 and 255. For example, the minor version number for the first release of the Draw library could be 1.0. To set the minor version number of a dynamic library, use the `clang -current_version <version_number>` option.

The compatibility version number is similar to the minor version number; it’s set through the compiler `-compatibility_version` command-line option. The compatibility version number of a library release specifies the earliest minor version of the clients linked with that release can use. For instance, the example in [Defining Client Compatibility](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdamjtfvjvomq) indicates that Client 1.1 cannot use versions of the Draw library earlier than 1.2 because they don’t export the `draw_polygon` function. To view a library’s current and compatibility versions, use the `otool -L <library>` command.

Before loading a dynamic library, the dynamic loader compares the current version of the `.dylib` file in the user’s file system with the compatibility version of the `.dylib` file the client was linked with in the developer’s file system. If the current version is earlier (less) than the compatibility version, the dependent library is not loaded. Therefore, the launch process (for client apps) or the load process (for client libraries) is aborted.

The most important aspect to define before implementing a dynamic library is its interface to its clients. The public interface affects several areas in the use of the library by its clients, the library’s development and maintenance, and the performance of the apps in which the library is used:

- __Ease of use:__ A library with a few but easily understandable public symbols is far easier to use than one that exports all the symbols it defines.
- __Ease of maintenance:__ A library that has a small set of public symbols and an adequate set of private symbols, is far easier to maintain because there are few client entry points to test. Also, developers can change the private symbols to improve the library in newer versions without impacting the functionality of clients that were linked with an earlier version.
- __Performance:__ Designing a dynamic library so that it exports the minimum number of symbols optimizes the amount of time the dynamic loader takes to load the library into a process. The fewer exported symbols a library has, the faster the dynamic loader loads it.

The following sections show how to determine which of the library’s symbols to export, how to name them, and how to export them.

Reducing the set of symbols your library exports makes the library easy to use and easy to maintain. With a reduced symbol set, the users of your library are exposed only to the symbols that are relevant to them. And with few public symbols, you are free to make substantial changes to the internal interfaces, such as adding or removing internal symbols that do not affect clients of your library.

Global variables should never be exported. Providing uncontrolled access to a library’s global variables leaves the library open to problems caused by clients assigning inappropriate values to those variables. It’s also difficult to make changes to global variables from one version of your library to another without making newer revisions incompatible with clients that were not linked with them. One of the main features of dynamic libraries is the fact that, when implemented correctly, clients can use newer versions of them without relinking. If clients need to access a value stored in a global variable, your library should export accessor functions but not the global variable itself. Adhering to this guideline allows library developers to change the definitions of global variables between versions of the library, without introducing incompatible revisions.

If your library needs the functionality implemented by functions it exports, you should consider implementing internal versions of the functions, adding wrapper functions to them, and exporting the wrappers. For example, your library may have a function whose arguments must be validated, but you’re certain that the library always provides valid values when invoking the function. The internal version of the function could be optimized by removing validation code from it, making internal use more efficient. The validation code can then be placed in the wrapper function, maintaining the validation process for clients. In addition, you can further change the internal implementation of the function to include more parameters, for example, while maintaining the external version the same.

Having wrapper functions call internal versions reduces the performance of an app, especially if the function is called repeatedly by clients. However, the advantages of flexible maintenance for you and a stable interface for your clients greatly outweigh this negligible performance impact.

The dynamic loader doesn’t detect naming conflicts between the symbols exported by the dynamic libraries it loads. When a client contains a reference to a symbol that two or more of its dependent libraries export, the dynamic loader binds the reference to the first dependent library that exports the symbol in the client’s dependent library list. The _dependent library list_ is a list of the client’s dependent libraries in the order they were specified when the client was linked with them. Also, when the `dlsym(3) OS X Developer Tools Manual Page` function is invoked, the dynamic loader returns the address of the first symbol it finds in the specified scope (global, local, or next) with a matching name. For details on symbol-search scope, see [Using Symbols](Dynamic%20Library%20Usage%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsmryfvjvooi).

To ensure that your library’s clients always have access to the symbols your library exports, the symbols must have unique names in a process’s namespace. One way is for apps to use two-level namespaces. Another is to add prefixes to every exported symbol. This is the convention used by most of the OS X frameworks, such as Carbon and Cocoa. For more information on two-level namespace, see [Executing Mach-O Files](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/MachOTopics/1-Articles/executing_files.html#//apple_ref/doc/uid/TP40001829) in _[Mach-O Programming Topics](../Mach-O%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjz)_.

After you have identified the symbols you want to expose to your library’s users, you must devise a strategy for exporting them or for not exporting the rest of the symbols. This process is also known as setting the _visibility_ of the symbols—that is, whether they are accessible to clients. Public or exported symbols are accessible to clients; private, hidden, or unexported symbols are not accessible to clients. In OS X, there are several ways of specifying the visibility of a library’s symbols:

- The `static` storage class: This is the easiest way to indicate that you don’t want to export a symbol.
- The exported symbols list or the unexported symbols list: The list is a file with the names of symbols to export or a list of symbols to keep private. The symbol names must include the underscore (`_`) prefix. You can use only one type of list when generating the dynamic library file.
- The `visibility` attribute: You place this attribute in the definition of symbols in implementation files to set the visibility of symbols individually. It gives you more granular control over which symbols are public or private.
- The compiler `-fvisibility` command-line option: This option specifies at compilation time the visibility of symbols with unspecified visibility in implementation files. This option, combined with the `visibility` attribute, is the most safe and convenient way of identifying public symbols.
- The `weak_import` attribute: Placing this attribute in the declaration of a symbol in a header file tells the compiler to generate a weak reference to the symbol. This feature is called _weak linking_; symbols with the `weak_import` attribute are called _weakly linked symbols_. With weak linking, clients do not fail to launch when the version of the dependent library found at launch time or load time doesn’t export a weakly linked symbol referenced by the client. It’s important to place the `weak_import` attribute in the header files that the source files of the library’s clients use, so that the client developers know that they must ensure the existence of the symbol before using it. Otherwise, the client would crash or function incorrectly when it attempts to use the symbol. See [Using Weakly Linked Symbols](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/DynamicLibraryUsageGuidelines.html#//apple_ref/doc/uid/TP40001928-SW20) for further details on weakly linked symbols. For more information on symbol definitions, see [Executing Mach-O Files](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/MachOTopics/1-Articles/executing_files.html#//apple_ref/doc/uid/TP40001829) in _[Mach-O Programming Topics](../Mach-O%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjz)_.
- The compiler `-weak_library` command-line option: This option tells the compiler to treat all the library’s exported symbols as weakly linked symbols.

To illustrate how to set the visibility of a library’s symbols, let’s start with a dynamic library that allows its clients to set a value kept in a global variable in the library, and to retrieve the value. Listing 1 shows the code that makes up the library.

__Listing 1__  A simple dynamic library

```c
/* File: Person.h */
char* name(void);
void set_name(char* name);

/* File: Person.c */
#include "Person.h"
#include <string.h>
char _person_name[30] = {'\0'};
char* name(void) {
    return _person_name;
}

void _set_name(char* name) {
   strcpy(_person_name, name);
}

void set_name(char* name) {
    if (name == NULL) {
        _set_name("");
    }
    else {
        _set_name(name);
    }
}
```

The intent of the library’s developer is to provide clients the ability to set the value of `_person_name` with the `set_name` function and to let them obtain the value of the variable with the `name` function. However, the library exports more than the `name` and `set_name` functions, as shown by the output of the `nm` command-line tool:

```shell
% clang -dynamiclib Person.c -o libPerson.dylib
% nm -gm libPerson.dylib
                 (undefined) external ___strcpy_chk (from libSystem)
0000000000001020 (__DATA,__common) external __person_name     // Inadvertently exported
0000000000000e80 (__TEXT,__text) external __set_name          // Inadvertently exported
0000000000000e70 (__TEXT,__text) external _name
0000000000000ec0 (__TEXT,__text) external _set_name
                 (undefined) external dyld_stub_binder (from libSystem)
```

Note that the `_person_name` global variable and the `_set_name` function are exported along with the `name` and `set_name` functions. There are many options to remove `_person_name` and `_set_name` from the symbols exported by the library. This section explores a few.

The first option is to add the static storage class to the definition of `_person_name` and `_set_name` in `Person.c` , as shown in Listing 2.

__Listing 2__  Person module hiding a symbol with the static storage class

```c
/* File: Person.c */
#include "Person.h"
#include <string.h>

static char _person_name[30] = {'\0'};        // Added 'static' storage class
char* name(void) {
    return _person_name;
}

static void _set_name(char* name) {           // Added 'static' storage class
   strcpy(_person_name, name);
}

void set_name(char* name) {
    if (name == NULL) {
        _set_name("");
    }
    else {
        _set_name(name);
    }
}
```

Now, the `nm` output, looks like this:

```
                 (undefined) external ___strcpy_chk (from libSystem)
0000000000000e80 (__TEXT,__text) external _name
0000000000000e90 (__TEXT,__text) external _set_name
                 (undefined) external dyld_stub_binder (from libSystem)
```

This means that the library exports only `name` and `set_name`. Actually, the library also exports some undefined symbols, including `strcpy`. They are references to symbols the library obtains from its dependent libraries.

The problem with this approach is that it hides the internal `_set_name` function from other modules in the library. If the library’s developer trusts that any internal call to `_set_name` doesn’t need to be validated but wants to validate all client calls, the symbol must be visible to other modules within the library but not to the library’s client. Therefore, the `static` storage class is not appropriate to hide symbols from the client but disclose them to all the library’s modules.

A second option for exposing only the symbols intended for client use is to have an exported symbols file that lists the symbols to export; all other symbols are hidden. Listing 3 shows the `export_list` file.

__Listing 3__  File listing the names of the symbols to export

```
# File: export_list
_name
_set_name
```

To compile the library, you use the `clang -exported_symbols_list` option to specify the file containing the names of the symbols to export, as shown here:

```
clang -dynamiclib Person.c -exported_symbols_list export_list -o libPerson.dylib
```

The third and most convenient option for exposing only `name` and `set_name` is to set the visibility attribute in their implementations to `"default"` and set the `-fvisibility` compiler command-line option to hidden when compiling the library’s source files. Listing 4 shows how the `Person.c` file looks after setting the `visibility` attribute for the symbols to be exported.

__Listing 4__  Person module using visibility attribute to export symbols

```c
/* File: Person.c */
#include "Person.h"
#include <string.h>

// Symbolic name for visibility("default") attribute.
#define EXPORT __attribute__((visibility("default")))

char _person_name[30] = {'\0'};

EXPORT                        // Symbol to export
char* name(void) {
    return _person_name;
}

void _set_name(char* name) {
   strcpy(_person_name, name);
}

EXPORT                        // Symbol to export
void set_name(char* name) {
    if (name == NULL) {
        _set_name("");
    }
    else {
        _set_name(name);
    }
}
```

The library would then be compiled using the following command:

```
% clang -dynamiclib Person.c -fvisibility=hidden -o libPerson.dylib
```

The `-fvisibility=hidden` command-line option tells the compiler to set the visibility of any symbols without a visibility attribute to hidden, thereby hiding them from the library’s clients. For details on the `visibility` attribute and the `-fvisibility` command-line option, see [http://gcc.gnu.org/onlinedocs/gcc](http://gcc.gnu.org/onlinedocs/gcc) and the `clang` man page.

Following these symbol-exporting guidelines ensures that libraries export only the symbols you want to make available to your clients, simplifying the use of the library by its clients and facilitating its maintenance by its developers. The document _How to Write Shared Libraries_ provides an in-depth analysis of symbol exporting strategies. This document is available at [http://people.redhat.com/drepper/dsohowto.pdf](http://people.redhat.com/drepper/dsohowto.pdf).

When you need to locate resources your library or program needs at runtime—such as frameworks, images, and so on—you can use either of the following methods:

- __Executable-relative location.__ To specify a file path relative to the location of the main executable, not the referencing library, place the `@executable_path` macro at the beginning of the path. For example, in an app package that contains private frameworks (which, in turn, contain shared libraries), any of the libraries can locate an app resource called `MyImage.tiff` inside the package by specifying the path `@executable_path/../Resources/MyImage.tiff`. Because `@executable_path` resolves to the binary inside the `MacOS` directory in the app bundle, the resource file path must specify the `Resources` directory as a subdirectory of the `MacOS` parent directory (the `Contents` directory). For a detailed discussion of directory bundles, see _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_.
- __Library-relative location.__ To specify a file path relative to the location of the library itself, place the `@loader_path` macro at the beginning of the pathname. Library-relative location allows you to locate library resources within a directory hierarchy regardless of where the main executable is located.

When you develop a dynamic library, you specify its dependent libraries by linking your source code with them. When a client of your library tries to load it, your library’s dependent libraries must be present in the file system for your library to load successfully. (See [Run-Path Dependent Libraries](Run-Path%20Dependent%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmbwfvjvomi) to learn about installing dependent libraries in a relocatable directory.) Depending on how the client loads your library, some or all of your library’s references to symbols exported by its dependent libraries are resolved. You should consider using the `dlsym(3) OS X Developer Tools Manual Page` function to get the address of symbols when they are needed instead of having references that may always have to be resolved at load time. See [Using Symbols](Dynamic%20Library%20Usage%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsmryfvjvooi) for details.

The more dependent libraries your library has, the longer it takes for your library to load. Therefore, you should link your library only with those dynamic libraries required at load time. After you compile your library, you can view its dependent libraries in a shell editor with the `otool -L` command.

Any dynamic libraries your library seldom uses or whose functionality is needed only when performing specific tasks should be used as runtime loaded libraries; that is, they should be opened with the `dlopen(3) OS X Developer Tools Manual Page` function. For example, when a module in your library needs to perform a task that requires the use of a nondependent library, the module should use `dlopen` to load the library, use the library to perform its task, and close the library with `dlclose(3) OS X Developer Tools Manual Page` when finished. For additional information on loading libraries at runtime, see [Opening Dynamic Libraries](Dynamic%20Library%20Usage%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsmryfvjvomjs).

You should also keep to a minimum the number of external references to symbols in dependent libraries. This practice optimizes further your library’s load time.

You must disclose to your library’s users all the libraries your library uses and whether they are dependent libraries. When users of your dynamic library link their images, the static linker must be able to find all your library’s dependent libraries, either through the link line or symbolic links. Also, because your dynamic library loads successfully even when some or all the libraries it opens at runtime are not present at load time, users of your library must know which dynamic libraries your library opens at runtime and under which circumstances. Your library’s users can use that information when investigating unexpected behavior by your library.

When dynamic libraries are loaded, they may need to prepare resources or perform special initialization before doing anything else. Conversely, when the libraries are unloaded, they may need to perform some finalization processes. These tasks are performed by _initializer functions_ and _finalizer functions_, also called constructors and destructors.

Initializers can safely use symbols from dependent libraries because the dynamic loader executes the static initializers of an image’s dependent libraries before invoking the image’s static initializers.

You indicate that a function is an initializer by adding the `constructor` attribute to its definition. The `destructor` attribute identifies finalizer functions. Initializers and finalizers must not be exported. A dynamic library’s initializers are executed in the order they are encountered by the compiler. It’s finalizers, on the other hand, are executed in the reverse order as encountered by the compiler.

For example, Listing 5 shows a set of initializers and finalizers defined identically in two files `File1.c` and `File2.c` in a dynamic library called Inifi.

__Listing 5__  Inifi initializer and finalizer definitions

```c
/* Files: File1.c, File2.c */
#include <stdio.h>
__attribute__((constructor))
static void initializer1() {
    printf("[%s] [%s]\n", __FILE__, __FUNCTION__);
}

__attribute__((constructor))
static void initializer2() {
    printf("[%s] [%s]\n", __FILE__, __FUNCTION__);
}

__attribute__((constructor))
static void initializer3() {
    printf("[%s] [%s]\n", __FILE__, __FUNCTION__);
}

__attribute__((destructor))
static void finalizer1() {
    printf("[%s] [%s]\n", __FILE__, __FUNCTION__);
}

__attribute__((destructor))
static void finalizer2() {
    printf("[%s] [%s]\n", __FILE__, __FUNCTION__);
}

__attribute__((destructor))
static void finalizer3() {
    printf("[%s] [%s]\n", __FILE__, __FUNCTION__);
}
```

Continuing the example, the Inifi dynamic library is the sole dependent library of the Trial program, generated from the `Trial.c` file, shown in Listing 6.

__Listing 6__  The `Trial.c` file

```c
/* Trial.c */
#include <stdio.h>
int main(int argc, char** argv) {
    printf("[%s] [%s] Finished loading. Now quitting.\n", __FILE__, __FUNCTION__);
    return 0;
}
```

Listing 7 shows the output produced by the Trial app.

__Listing 7__  Execution order of a dynamic library’s initializers and finalizers

```shell
% clang -dynamiclib File1.c File2.c -fvisibility=hidden -o libInifi.dylib
% clang Trial.c libInifi.dylib -o trial
% ./trial
[File1.c] [initializer1]
[File1.c] [initializer2]
[File1.c] [initializer3]
[File2.c] [initializer1]
[File2.c] [initializer2]
[File2.c] [initializer3]
[Trial.c] [main] Finished loading. Now quitting.
[File2.c] [finalizer3]
[File2.c] [finalizer2]
[File2.c] [finalizer1]
[File1.c] [finalizer3]
[File1.c] [finalizer2]
[File1.c] [finalizer1]
```

Although you can have as many static initializers and finalizers in an image as you want, you should consolidate your initialization and finalization code into one initializer and one finalizer per module, as needed. You may also choose to have one initializer and one finalizer per library.

In OS X v10.4 and later, static initializers can access the arguments given to the current program. By defining the initializer’s parameters as you would define the parameters to an program’s main function, you can get the number of arguments given, the arguments themselves, and the process’s environment variables. In addition, to guard against an initializer or finalizer being called twice, you should conditionalize your initialization and finalization code inside the function. Listing 8 shows the definition of a static initializer that has access to the program’s arguments and conditionalizes its initialization code.

__Listing 8__  Definition of a static initializer

```
__attribute__((constructor))
static void initializer(int argc, char** argv, char** envp) {
    static initialized = 0;
    if (!initialized) {
        // Initialization code.
        initialized = 1;
    }
}
```


Using C++ to implement a dynamic library presents a couple of challenges—mainly exporting symbol names and creating and destroying objects. The following sections detail how to export symbols from a C++–based dynamic library and how to provide clients with functions that create and destroy instances of a class.

C++ uses _name mangling_ to encode size and type information in a symbol name. Name mangling in C++ makes exporting symbols in a standard way across different platforms impossible. When a dynamic library is compiled, each symbol is renamed to include that information, but the encoding used is not standard between platforms. The dynamic loader uses string matching to locate symbols at runtime; the name of the symbol searched must match exactly the name of the target. When the symbol names have been mangled, the dynamic loader has no way of knowing how the name of the symbol it’s searching for has been encoded.

To export nonmember symbols from a C++–based dynamic library so that the dynamic loader can find it, you must add the `extern "C"` directive to the symbols’ declarations. This keyword tells the compiler not to mangle the symbol name. For example, the following declaration makes the `NewPerson` function available to the library’s clients:

```
extern "C" Person* NewPerson(void);
```

Without this directive, the function name could be changed to `_Z9NewPersonv` , which would make it impossible for the dynamic loader to find the `NewPerson` symbol at runtime.

The only nonmember functions that must be exported are constructors and destructors, especially in dynamic libraries that can be used by clients as dependent libraries instead of runtime-loaded libraries. This is because clients must have access to a class’s constructors and destructors so that they can use the `new` and `delete` operators on the class.

A dynamic library should always publish its public interface to clients through header files. (Although clients can use dynamic libraries without their header files, doing so is very difficult and is prone to error.) The header file for a class that’s available to clients must include the declarations of its public methods. Dynamic libraries that make a class available to its clients must include the virtual keyword in the declaration of all the class’s methods, except for its constructors and destructors. For example, Listing 9 shows the declaration for the Person class.

__Listing 9__  Declaration for the Person class

```
class Person {
    private:
        char _person_name[30];
    public:
        Person();
        virtual void set_name(char person_name[]);
        virtual char* name();
};
```


When a C++–based dynamic library is a dependent library of its client, the client can use the `new` and `delete` operators to create and destroy instances of a class the library defines. However, clients that open a C++–based library at runtime through `dlopen(3) OS X Developer Tools Manual Page` do not have access to the library’s constructors because the constructors are exported with their names mangled, preventing the dynamic loader from locating them. See [Listing 11](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdamjtfvjvomjs) for details about name mangling.

Clients that load a library at runtime to use a class must have a way to create and destroy a class’s objects without using the `new` and `delete` operators. A library provides this functionality to its clients by exporting at least two class factory functions. _Class factory functions_ create and destroy objects of a class on behalf of a class’s user. Creator functions create an object of the class and return a pointer to it. Destructor functions dispose of an object created by a creator function for the same class. In addition to the factory functions, the library must define a data type for each exported factory function.

For example, Listing 10 shows the header and implementation files of the `Person` class, exported by the Person library. The header file includes the declaration and type definition of a pair of factory functions, `NewPerson`, and `DeletePerson`:

__Listing 10__  Interface and implementation of a C++ class in a dynamic library

```c
/* File: Person.h */
class Person {
    private:
        char _person_name[30];
    public:
        Person();
        virtual void set_name(char person_name[]);
        virtual char* name();
};

// Constructor function and function type.
extern "C" Person *NewPerson(void);
typedef Person *Person_creator(void);

// Destructor function and function type.
extern "C" void DeletePerson(Person *person);
typedef void Person_disposer(Person *);

/* File: Person.cpp */
include <iostream>
#include "Person.h"

#define EXPORT __attribute__((visibility("default")))

EXPORT
Person::Person() {
    char default_name[] = "<no value>";
    this->set_name(default_name);
}

EXPORT
Person* NewPerson(void) {
    return new Person;
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

Listing 11 shows how a client might use the Person library.

__Listing 11__  Client using a C++ class implemented in a runtime-loaded library

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
        cerr << "[" << __FILE__ << "] main: Unable to open library: "
             << dlerror() << "\n";
        exit(EXIT_FAILURE);
    }

    // Get the NewPerson function.
    Person_creator* NewPerson = (Person_creator*)dlsym(lib_handle, "NewPerson");
    if (!NewPerson) {
        cerr << "[" << __FILE__ << "] main: Unable to find NewPerson method: "
             << dlerror() << "\n";
        exit(EXIT_FAILURE);
    }

    // Get the DeletePerson function.
    Person_disposer* DeletePerson =
        (Person_disposer*)dlsym(lib_handle, "DeletePerson");
    if (!DeletePerson) {
        cerr << "[" << __FILE__
             << "] main: Unable to find DeletePerson method: "
             << dlerror() << "\n";
        exit(EXIT_FAILURE);
    }

    // Create Person object.
    Person* person = (Person*)NewPerson();

    // Use Person object.
    cout << "[" << __FILE__ << "] person->name() = " << person->name() << "\n";
    char new_name[] = "Floriane";
    person->set_name(new_name);
    cout << "[" << __FILE__ << "] person->name() = " << person->name() << "\n";

    // Destroy Person object.
    DeletePerson(person);

    // Close the library.
    if (dlclose(lib_handle) != 0) {
        cerr << "[" << __FILE__ << "] main: Unable to close library: "
             << dlerror() << "\n";
    }

    return 0;
}
```

The following commands compile the library and the client program:

```shell
% clang++ -dynamiclib Person.cpp -fvisibility=hidden -o libPerson.dylib
% clang++ Client.cpp -o client
```

For further details on how clients use C++ classes implemented in dynamic libraries, see [Using C++ Classes](Dynamic%20Library%20Usage%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsmryfvjvomjr).

There are a few issues to consider while designing or updating an Objective-C–based dynamic library:

- Publishing the public interface of an Objective-C class or category is different from the way symbols are exported in C.

  In Objective-C every method of every class is available at runtime. Clients can introspect classes to find out which methods are available. However, so that client developers don’t receive a flurry of warnings about missing method implementations, library developers should publish the interface to their classes and categories as protocols to client developers.
- Objective-C–based libraries have access to more initialization facilities than those available to C-based libraries.
- Objective-C has an class-alias facility that allows library developers to rename classes in a revision but allow clients to link with that revision to continue using the names used in earlier revisions.

The following sections explore these areas in detail.

Because client developers generally don’t have access to the implementation of Objective-C classes and categories defined in dynamic libraries, library developers must publish the public interfaces of classes and categories as protocols in header files. Client developers compile their products using those header files and are able to instantiate the classes correctly by adding the necessary protocol names to variable definitions. Listing 12 shows the header and implementation files of the `Person` class in an Objective-C–based library. Listing 13 shows the header and implementation files of the `Titling` category in the same library, which adds the `-setTitle` method to the `Person` class.

__Listing 12__  Header and implementation files of the `Person` class

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

/* File: Person.m */
#import <Foundation/Foundation.h>
#import "Person.h"

@implementation Person
- (id)init {
    if (self = [super init]) {
        _person_name = @"";
    }
    return self;
}

- (void)setName:(NSString*)name {
    _person_name = name;
}

- (NSString*)name {
    return _person_name;
}
@end
```


__Listing 13__  Header and implementation files of the `Titling` category to the `Person` class

```objc
/* File: Titling.h */
#import <Foundation/Foundation.h>
#import "Person.h"

@protocol Titling
- (void)setTitle:(NSString*)title;
@end

@interface Person (Titling) <Titling>
@end

/* File: Titling.m */
#import <Foundation/Foundation.h>
#import "Titling.h"

@implementation Person (Titling)
- (void)setTitle:(NSString*)title {
    [self setName:[[title stringByAppendingString:@" "]
        stringByAppendingString:[self name]]];
}
@end
```

Listing 14 shows how a client might use the library.

__Listing 14__  Client using the Person library

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
        NSObject<Person,Titling>* person = [Person_class new];

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

The following commands compile the library and the client program:

```
clang -framework Foundation -dynamiclib Person.m Titling.m -o libPerson.dylib
clang -framework Foundation Client.m -o client
```


Objective-C–based dynamic libraries provide several initialization facilities for modules, classes, and categories. The following list describes those facilities in the order they are executed.

1. The `+load` method: Initializes resources needed by a class or a category. The Objective-C runtime sends the `load` message to every class a library implements; it then sends the `load` message to every category the library implements. The order in which sibling classes are sent the `load` message is undetermined. Implement the `+load` method to initialize resources needed by a class or category. Note that there’s no corresponding “unload” method.
2. Module initializers: Initializes a module. The dynamic loader calls all the initializer functions (defined with the `constructor` attribute) in each of a library’s modules. See [Module Initializers and Finalizers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdamjtfvjvomjx) for more information on module initializers.
3. The `+initialize` method: Initializes resources needed by instances of a class before any instances are created. The Objective-C runtime sends the `initialize` message to a class just before creating an instance of the class. Note that there’s no corresponding “finalize” message sent to a class when the library is unloaded or the process terminates.

When you rename a class in a revision of a dynamic library, you can reduce the adoption burden to client developers by adding an alias to the new name in the library’s header file. This practice allows client developers to release clients that take advantage of the new version of the library quickly. Client developers can later update references to the class at their leisure.

This list provides a summary of the guidelines for improving specific aspects of a dynamic library:

- Ease of use

  - Reduce the number of symbols a library exports.
  - Provide unique names to public interfaces.
- Ease of maintenance

  - Export accessor functions to variables. Don’t export variables.
  - Implement public interfaces as wrappers to internal, private interfaces.
- Performance

  - Minimize the number of references to symbols in dependent libraries. Use `dlsym(RTLD_GLOBAL, <symbol_name>)` to obtain the address of symbols exported by dependent libraries when they are needed.
  - Minimize the number of dependent libraries. Consider loading libraries with `dlopen` when absolutely necessary. Remember to close the library with `dlclose` when done.
  - Implement public interfaces as wrappers to internal, private interfaces.
- Compatibility

  - Export symbols as weakly linked symbols.
  - Encode a library’s major version number in its filename.

[Next](Dynamic%20Library%20Usage%20Guidelines.md)[Previous](Overview%20of%20Dynamic%20Libraries.md)

