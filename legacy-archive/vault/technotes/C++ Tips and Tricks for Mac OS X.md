---
title: C++ Tips and Tricks for Mac OS X
apple_id: DTS10004200
resource_type: Technical Note
platform: macOS
topic: Xcode
technology: null
published: '2007-05-25'
source_url: https://developer.apple.com/library/archive/technotes/tn2185/_index.html
archived_at: '2026-07-26T19:54:09.035557Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2185

# C++ Tips and Tricks for Mac OS X

Valuable points of interest for the C++ programmer

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjukq2ujfhu4mi)[Choosing Visibility Options](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjukq2ujfhu4mq)[Command Line Options for Visibility](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjvkqstivbviskpjyza)[Setting Visibility With Pragmas](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjvkqstivbviskpjyzq)[Setting Visibility With Attributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjvkqstivbviskpjy2a)[Hiding Symbols With Export Lists](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjvkqstivbviskpjy2q)[Summing Symbol Visibility Up](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjvkqstivbviskpjy3a)[Choosing an Xcode Template](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjukq2ujfhu4oa)[The Application Templates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjvkqstivbviskpjy4a)[Generic C++ Plugin](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjvkqstivbviskpjy4q)[C++ Command Line Tool](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjvkqstivbviskpjyyta)[Dynamic Library](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjvkqstivbviskpjyytc)[Overriding new/delete](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjukq2ujfhu4mjt)[The Strong Attribute for Namespace Using Declarations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjukq2ujfhu4mju)[Using Namespaces to Manage Versions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjukq2ujfhu4mjv)[Which std C++ symbols are set in stone, and which aren't (ABI issues)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjukq2ujfhu4mjw)[How Best to Strip](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjukq2ujfhu4mjx)[Using basic_string Instantiations Other Than string and wstring With libstdc++](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjukq2ujfhu4mjy)[Release-to-Release Version Compatibility of Shared Libraries Using C APIs and C++ Implementations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjukq2ujfhu4mjz)[Release-to-Release Version Compatibility of Shared Libraries Using C++ APIs and C++ Implementations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawugsbrfvjukq2ujfhu4mrq)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrqgawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

This document seeks to ease the task of bringing modern, complex C++ Mach-O applications to Mac OS X. It addresses several issues which commonly arise with some helpful suggestions. While by no means a complete reference, it should get the perplexed C++ developer heading in the right direction, and equipped with the ability to find more in-depth information if necessary.

[Back to Top](#)

## Choosing Visibility Options

In GCC visibility is akin to what other tools refer to as dynamic library import/export. However GCC symbols are either visible or hidden. The visible symbols are your shared library entry points. More detailed information is available at [Controlling Symbol Visibility](https://developer.apple.com/documentation/DeveloperTools/Conceptual/CppRuntimeEnv/Articles/SymbolVisibility.html). Only a brief summary is offered here.

In C, it is relatively simple to decide which symbols need to be visible, and which hidden. The shared library entry points must be visible, and everything else can be hidden. In C++, many more definitions are found in header files instead of source files. C++ header files can contain both interface and private implementation details. Examples include templates (both class and function), class declarations, and inline functions (both member and non-member).

There are four techniques for declaring visibility:

1. Command line options (e.g. `-fvisibility=hidden`)
2. pragmas
3. Attribute declarations on individual types and functions
4. `Export/unexport` lists

It is important to understand the role of each of these techniques and how they interact with each other. The first three techniques declare visibility at compile time. The fourth is a link time operation. Export lists can hide a symbol which the compiler marked visible, but one can not use export lists to make visible a symbol which the compiler has marked hidden.

### Command Line Options for Visibility

The visibility command line options are useful for setting the visibility defaults. This can be especially helpful when dealing with source code which is third party, or otherwise for some reason not practical to decorate with attributes or pragmas. If you do not specify a command line visibility option then symbols will be marked visible (unless overridden by one of the other three techniques). You can make this choice of default visibility explicit by placing the following on your command line:

```
 -fvisibility=default
```

Specifying `-fvisibility=hidden` on the command line marks all symbols as hidden (unless overridden by pragmas or attributes - export lists can not make a hidden symbol visible).

There are two other visibility-related command options one may find useful:

1. Use `-fvisibility-inlines-hidden` to declare that there will be no attempt to compare pointers to inlined member functions where the addresses of the two member functions were taken in different linkage units.

   For many applications, `-fvisibility-inlines-hidden` is a safe and easy way to hide many symbols which in turn improves load time. The dynamic linker (at load time) does much more work for visible symbols than for hidden ones.

   The behavior of this switch is not quite the same as marking the member function as hidden directly, because it does not affect static variables local to the function or cause the compiler to deduce that the function is defined in only one linkage unit. Any local statics will assume whatever visibility setting is in effect independent of this command line switch.

   - `-fvisibility-inlines-hidden` has no effect when `-fvisibility=hidden` is also on the command line.
   - `-fvisibility-inlines-hidden` has no effect on non-member inline functions.
   - Do not use `-fvisibility-inlines-hidden` if you compare pointers to inlined member functions across shared library boundaries.
2. `-fvisibility-ms-compat` sets the default visibility to hidden, except for the `type_info` data associated with types. The impact of this is to emulate the linkage model of Microsoft Visual Studio. Comparing types is important for catching exceptions, `dynamic_cast`, and comparing `type_info`'s obtained by a `typeid` expression.

   - `-fvisibility=hidden` has no effect when `-fvisibility-ms-compat` is also on the command line.
   - `-fvisibility-inlines-hidden` has no effect when `-fvisibility-ms-compat` is also on the command line.
   - Use of `-fvisibility-ms-compat` can cause two implementation detail classes which were independently developed within different shared libraries to accidently be mistaken for the same type.
   - The `-fvisibility-ms-compat` flag will hide any static data members of types, giving each linkage unit private copies (unless said data is otherwise marked visible).

### Setting Visibility With Pragmas

One can control the visibility of individual symbols or groups of symbols with the use of pragmas. Such use will make the visibility of the affected symbols independent of visibility command line options, and thus potentially make the source code more robust from a maintenance point of view.

To set the compiler's default mode to visible:

```
#pragma GCC visibility push(default)
```

To set the compiler's default mode to hidden:

```
 #pragma GCC visibility push(hidden)
```

To undo the last GCC visibility push pragma:

```
 #pragma GCC visibility pop
```

Thus the visibility pragmas form a scope, and one can nest these scopes with the inner most scope providing the dominant effect.

__Note:__ A common error is to misspell one of the pragmas. This will cause it to silently do nothing unless compiled with `-Wunknown-pragmas` (which warns of unknown (misspelled) pragmas).

To control the visibility of the compiler's meta-data for a type (e.g. `type_info`) surround the type declaration:

```
 #pragma GCC visibility push(default)      class MyType     {         // ...     };      #pragma GCC visibility pop
```

### Setting Visibility With Attributes

One can control the visibility of individual symbols of attributes. This links the visibility of the declaration with the declaration itself, making it independent of both command line options, and pragmas. This technique makes it less error prone to move code from place to place with respect to visibility.

For example, to mark a function as visible:

```
 __attribute__((__visibility__("default"))) void MyFunction1() {}
```

And to mark a function as hidden:

```
__attribute__((__visibility__("hidden"))) void MyFunction2() {}
```

You may find it convenient to create macros for your application which encompass these visibility details. Such macros may make it easier to port your code to other environments which either do not have a visibility concept, or where the visibility specification has other syntax. For example:

```
 #define PUBLIC  __attribute__((__visibility__("default")))     #define PRIVATE __attribute__((__visibility__("hidden")))      PUBLIC  void MyFunction1() {}     PRIVATE void MyFunction2() {}
```

One can mark a `class` or `struct` like so:

```swift
 class PUBLIC MyClass {/*...*/};
```

The attribute marks not only the `type_info` data, but also member functions, and static data members. One can also place attributes on the individual member functions of a class (e.g. private members).

### Hiding Symbols With Export Lists

The last tool in our tool chest is the export list. This is simply a list of symbols (which must be in mangled form) which tell the linker which symbols you want hidden. There are two forms:

1. Tell the linker which symbols you want to make visible and hide everything else with `-exported_symbols_list $FILENAME`.

   __Those symbols in the exported_symbols_list must have been marked visible by the compiler or they will be hidden.__
2. Tell the linker which symbols to hide with `-unexported_symbols_list $FILENAME`.

   __Those symbols which were marked visible by the compiler and do not appear in the unexported_symbols_list will be visible.__

### Summing Symbol Visibility Up

It can be convenient to rely on a combination of the above visibility tools. For example if your library has many symbols which should be hidden, with only a few that should be visible, you may wish to use `-fvisibility=hidden` and only decorate the source code of those few symbols which need to be visible.

For those types which you expect to `throw` or `dynamic_cast` across a shared library boundary, these types must be marked as visible by one of the above techniques. Failure to do so will result in run time errors such as a `catch` clause missing a thrown exception. For example.:

```
 // MyException.h      class MyException {};      // shared library:      #include "MyException.h"      void my_func()     {         throw MyException();     }      // Application:      #include "MyException.h"      int main()     {         try         {             my_func();         }         catch (MyException&)         {             // Catch will miss if MyException is hidden             // If hidden, the MyException thrown is a different type, than             //    the MyException referred to in the catch clause.         }     }
```

[Back to Top](#)

## Choosing an Xcode Template

When choosing "New Project..." in Xcode, there are a wide variety of Xcode templates to choose from. For the C++ developer, which template should you start with? One could start with any of the templates and set everything up yourself. However, if you choose the most relevant template from the beginning, your default settings are more likely to do what you want.

There are six Xcode templates especially tailored for the C++ developer, spread throughout four application types:

- Application

  - Carbon C++ Application
  - Carbon C++ Standard Application
- Bundle

  - Generic C++ Plugin
- Command Line Utility

  - C++ Tool
- Dynamic Library

  - C++ Dynamic Library
  - C++ Standard Dynamic Library

### The Application Templates

Choose one of the Carbon Application templates to create a starter C++ application based on the Carbon API. The starter application will display an OS X application window which responds to the usual windowing commands (new, close, minimize, etc.). There is also an example "About" window in this template. The template also demonstrates, in C++ style, how one can catch and customize events, and read from nib files.

The only difference between "Carbon C++ Application" and "Carbon C++ Standard Application" is the default visibility setting. The "Standard" template defaults to visible, while the other template defaults to hidden. When choosing hidden visibility defaults, one must take care when linking to shared libraries that those symbols that must be known across a shared library are explicitly declared visible by using attribute decorations or pragmas. This includes `type_info` data which is used in the implementation of `try/catch` and `dynamic_cast`. Minimization of visible symbols makes ABI stability among linkage units simpler, and also minimizes load time. With the "Standard" template, all of these C++ language features work as expected with no further effort on the part of the developer.

### Generic C++ Plugin

This project builds a generic C++ template that exposes a C interface, uses the static C++ standard library, and uses Dwarf for debugging.

This template creates a sample "plug-in" or bundle. This is a shared library that can be loaded and unloaded dynamically throughout the application's lifetime. The example plug-in, by design, exports only a C interface, and throws no exceptions. However it is implemented internally with C++. It has hidden visibility by default, and links statically to libstdc++. This enables it to throw and catch exceptions internally, but keep its clients blissfully unaware of that fact.

The template demonstrates the use of pragmas to mark its C interface visible. It also demonstrates "private headers" which contain C++ declarations which are meant to be used internally only (and are marked with hidden visibility).

### C++ Command Line Tool

If you would like to write a simple HelloWorld, or a program that has no graphical user interface (limited to standard C++ console and file I/O), then this is the template to start with. It starts you off with a single main.cpp which only prints "Hello, World!\n". When built and launched from Xcode, the console output is visible in Xcode's Run Log. This application can also be run from Terminal.app.

It has visibility set to hidden by default. If you would prefer visible for the default, select "Edit Active Target" under the Project menu, type "vis" into the search box of the dialog that comes up, and uncheck "Symbols Hidden by Default" and "Inline Functions Hidden".

### Dynamic Library

These templates set up an example dynamic (shared) library. The example includes both a public (visible) interface and private (hidden) internal headers. Like the application templates, the "Standard" template defaults to everything visible, while the template without the word "Standard" in the name defaults to hidden visibility.

[Back to Top](#)

## Overriding new/delete

The C++ standard (ISO no. 14882-2003) says that the following 8 signatures can be replaced by client code:

```
 void* operator new(std::size_t size) throw(std::bad_alloc);     void* operator new(std::size_t size, const std::nothrow_t&) throw();     void  operator delete(void* ptr) throw();      void  operator delete(void* ptr, const std::nothrow_t&) throw();      void* operator new[](std::size_t size) throw(std::bad_alloc);     void* operator new[](std::size_t size, const std::nothrow_t&) throw();     void  operator delete[](void* ptr) throw();     void  operator delete[](void* ptr, const std::nothrow_t&) throw();
```

For complete control and portability, if you replace any of these signatures, you should replace all of them. However the default implementation of the array forms simply forward to the non-array forms. If you only replace the four non-array forms, expect the default array forms to forward to your replacements.

Your replacements will be in effect application wide. Even code in other linkage units (shared libraries) will call your custom `new`  and `delete`. Throughout the application (all linkage units), there should be only one definition for the replaced `new`  and `delete`. This will ensure that if memory ownership is transferred across a shared library boundary, it will be deleted correctly.

In general, shared libraries should not override these operators, unless that is the shared library's only job. Otherwise it becomes likely that an application will link to more than one definition of overridden `new/delete`.

In rare circumstances a shared library may find it convenient to have private definitions of these operators. This is done by linking with the -`unexported_symbols_list` filename flag and placing the following symbols in the `unexport file`:

```
 __Znwm     __Znwm.eh     __ZnwmRKSt9nothrow_t     __ZnwmRKSt9nothrow_t.eh     __ZdlPv     __ZdlPv.eh     __ZdlPvRKSt9nothrow_t     __ZdlPvRKSt9nothrow_t.eh      __Znam     __Znam.eh     __ZnamRKSt9nothrow_t     __ZnamRKSt9nothrow_t.eh     __ZdaPv     __ZdaPv.eh     __ZdaPvRKSt9nothrow_t     __ZdaPvRKSt9nothrow_t.eh
```

In doing so, the author must ensure that memory ownership is not transferred into, or out of, this shared library. Note that memory ownership transfer can happen in subtle ways such as passing reference counted objects (e.g. `std::string`), throwing exceptions which contain a heap allocated message (e.g. `std::runtime_error`) or having a resource-allocating constructor inlined, with the corresponding destructor not inlined (or vice-versa).

Our current tool set has a bug whereby if a translation unit replaces these operators and does not contain a symbol with weak linkage (e.g. an inline function or an implicit template instantiation), then the linker will not find the custom operator `new/delete`. Most real-world translation units will have weak symbols so this is usually not a problem. However should you be affected by this bug you can add the following line next to your operator definitions:

```
 __attribute__((__weak__, __visibility__("default"))) int dummy_weak_symbol_for_new;
```

[Back to Top](#)

## The Strong Attribute for Namespace Using Declarations

Consider the following code:

```
 namespace Acme     {      template <class T>     class V     {     };      template <class T>     void func1(T&) {}      template <class T>     void func2(T&) {}      } // Acme      // Acme client      struct MyType {};      namespace Acme     {      template <>     class V<MyType>     {     };      }  // Acme      int main()     {         Acme::V<int> v_int;         func1(v_int);         Acme::func2(v_int);         Acme::V<MyType> v_mytype;         func1(v_mytype);         Acme::func2(v_mytype);     }
```

We have a library named Acme, and a client using it. The client calls functions within the Acme namespace (via argument dependent lookup), and also specializes an Acme template on a client-defined type. All is well.

Now consider that for some reason, Acme wants to put some of its functionality within a nested namespace of Acme, and then import it into the Acme namespace with a using declaration. The intent is to change the ABI of the library in a controlled manner while holding the API stable (i.e. code recompiled against the new library doesn't have to change, but gets new mangling). Why they might want to do this is covered later:

```
// Acme library  namespace Acme {  namespace _1 {  template <class T> class V { };  template <class T> void func1(T&) {}  }  // _1  using namespace _1;  template <class T> void func2(T&) {}   } // Acme
```

This works for most customers, as they can be blissfully ignorant of the nested namespace and continue to just use `Acme::V` and `Acme::func1`. But it breaks the client code we showed earlier.

```
error: specialization of 'template<class T> class Acme::_1::V' in different namespace
```

I.e. the client can no longer specialize `Acme::V<T>`. They must instead specialize `Acme::_1::V<T>`, which is unfortunate because we wanted to make the nested namespace transparent at the API level. However making this change still does not fix everything:

```
error: 'func2' was not declared in this scope
```

This error refers to both of the uses of `func2` in the client's code:

```
func2(v_int); func2(v_mytype);
```

Since `V` now lives in `Acme::_1`, the namespace `Acme` is not searched for `func2`.

The GCC compiler has an extension to make this code work, and without the client having to be aware of the nested namespace:

```
 using namespace _1 __attribute__((__strong__));
```

Now the client's original code, even the specialization of `Acme::V<T>`, just works. And yet, `V` and `func1` are now mangled with the nested namespace `Acme::_1`.

Why would Acme intentionally introduce this potentially confusing situation into their API?

[Back to Top](#)

## Using Namespaces to Manage Versions

If you have not read the section on The Strong Attribute for Namespace Using Declarations, now would be a good time to do so. If you have just come from that section, this section is about answering that final question: Why?

As you may gather from this section's title, one can use the technique described in the previous section to version a library's ABI, without changing the library's API (or at least holding the API changes to backwards compatible ones). In the context of shared libraries, this means that one can simultaneously ship multiple versions of a shared library and a single application can indirectly link to multiple versions without fear of silent run time errors due to incompatible versions being mixed.

Consider the following:

Acme has shared library versions 1 and 2 which they ship: Acme.1.dylib and Acme.2.dylib. Other shared libraries (Lib_A and Lib_B) link with Acme for their valuable services. Lib_B has recompiled against Acme.2.dylib, but Lib_A is still using Acme.1.dylib. Finally, an application links to both Lib_A and Lib_B, effectively mixing both versions of Acme into the same process.

If, for example, Acme changed `Acme::func1` in a non-ABI preserving manner (say just by slightly changing its semantics, but not its signature), then it would be potentially disastrous to have two incompatible versions of `Acme::func1` running around in the same process. What if the main application calls `Acme::func1`? Which version should it get?

Versioning with namespaces addresses the above scenario. Because namespaces are mangled into the names of symbols, the hidden namespaces within namespace Acme are mangled into `func1`. At the object code level, the two different versions of `func1` are literally two distinct functions, with two distinct names. Yet at the source code level, both versions appear to have the name `Acme::func1`. The main application can call `func1` without problems. If it did so using Acme's version 1 headers, it will get `Acme::_1::func1`. If it used Acme's version 2 headers, it will get `Acme::_2::func1`. If it used the version 1 headers, but no longer links (directly or indirectly) against Acme.1.dylib, it will get a link or load time failure as `Acme::_1::func1` will not be found, even if `Acme::_2::func1` has been loaded into the process.

Thus this technique leverages the type-safety of C++ to have the dynamic linker enforce version compliance, even with multiple versions in the same process, and without introducing version numbers into the client's source code.

__Note:__ For further information on versioning with namespaces you can visit the following sites:

- [Versioning with Namespaces](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2006/n2013.html)
- [Proposal to add namespace references to C++](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2003/n1526.txt)
- [Namespaces and Library Versioning](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2002/n1344.pdf)

[Back to Top](#)

## Which std C++ symbols are set in stone, and which aren't (ABI issues)

If you have read The Strong Attribute for Namespace Using Declarations and Using Namespaces to Manage Versions then you may have already surmised that this is Apple's plan for the C++ standard library. As time goes on, and ABI-incompatible changes are made to our C++ standard library, we will version them as described above so that we can simultaneously offer older, ABI-compatible versions and newer, ABI-incompatible versions of the standard library. Clients will be able to choose versions based on their individual needs, and if an application happens to load third party shared libraries, there will be no danger of silently mixing incompatible `std::` components.

You may have also noticed that in our Acme example above, there was one symbol (`func2`)) left outside of the nested versioning namespace. In this example, `func2` represents a symbol which Acme is guaranteeing to be ABI-stable, even across versions.

Likewise, Apple is guaranteeing that a small subset of the C++ standard library will not change ABI, even across new versions of this library. That subset of ABI-stable signatures is:

```
 namespace std {      // rtti      class type_info;      // exceptions      class exception;     class bad_exception;     class bad_cast;     class bad_typeid;     class bad_alloc;     class logic_error;     class domain_error;     class invalid_argument;     class length_error;     class out_of_range;     class runtime_error;     class range_error;     class overflow_error;     class underflow_error;      // handlers      unexpected_handler set_unexpected(unexpected_handler) throw();     void unexpected();     terminate_handler set_terminate(terminate_handler) throw();     void terminate();     uncaught_exception() throw();     struct nothrow_t {};     new_handler set_new_handler(new_handler) throw();      }  // std      // new / delete      void* operator new(std::size_t) throw(std::bad_alloc);     void* operator new(std::size_t, const std::nothrow_t&) throw();     void  operator delete(void*) throw();     void  operator delete(void*, const std::nothrow_t&) throw();     void* operator new[](std::size_t) throw(std::bad_alloc);     void* operator new[](std::size_t, const std::nothrow_t&) throw();     void  operator delete[](void*) throw();     void  operator delete[](void*, const std::nothrow_t&) throw();     void* operator new (std::size_t, void*) throw();     void* operator new[](std::size_t, void*) throw();     void  operator delete (void*, void*) throw();     void  operator delete[](void*, void*) throw();
```

Having ABI-stable exception classes is especially important as it is exceptions that tend to more easily cross shared library boundaries. And it is the exception classes which most often tend to get thrown. With this guarantee of ABI stability, code linked to any version of the standard library will be able to catch the standard exception classes thrown by another linkage unit which uses any other version of the standard library.

[Back to Top](#)

## How Best to Strip

A linked Mach-O binary contains two kinds of symbols: global and local. Global symbols are used by `dyld` to do binding and are searchable at runtime using `dlsym()`. Local symbols are used by debuggers and CrashReporter when presenting symbolic names for addresses. All C++ constructs with visibility hidden become local symbols when linked.

It is very common to strip local symbols out of shipping products to reduce their size. Xcode does this by default in the Release configuration. On the other hand, stripping global symbols is a bit trickier because doing so can change the runtime meaning of a program.

The fastest way to remove local symbols is to have the linker never put them in the output binary. The linker option `-x` will do this. If you want to have two binaries one with and one without local symbols, you can have the linker generate local symbols, make of copy of the program, and use the `strip` tool with the `-x` option to remove the local symbols from the copy.

To control global symbols, you should use the four visibility options discussed in the section on choosing visibility options.

[Back to Top](#)

## Using basic_string Instantiations Other Than string and wstring With libstdc++

When using `std::basic_string`'s other than `string` and `wstring`, combined with hidden visibility, you should include the `string` header wrapped in `#pragma GCC visibility push(default)`. Failure to do so can result in a double delete associated with the empty string. This is considered an Apple bug
(r. [4940079](rdar://problem/4940079))
and will be corrected in a future release.

Example:

```shell
 $ cat library.h          #ifndef LIBRARY_H         #define LIBRARY_H          #include <string>          typedef unsigned short uchar;         typedef std::basic_string<uchar> ustring;          __attribute__ ((visibility("default"))) ustring foo();          #endif  // LIBRARY_H      $ cat library.cpp          #include "library.h"          ustring foo()         {             ustring s;             return s;         }      $ cat main.cpp          #include "library.h"          int main()         {             ustring s;             s = foo();         }      $ export MallocBadFreeAbort=1     $ g++ -fvisibility=hidden -dynamiclib -o library.so library.cpp     $ g++ -fvisibility=hidden -o main main.cpp library.so     $ ./main          main(5585) malloc: ***  Deallocation of a pointer not malloced: 0xc0ac; This         could be a double free(), or free() called with the middle of an allocated         block; Try setting environment variable MallocHelp to see tools to help debug         Abort trap
```

To fix, change `<library.h>` to:

```shell
 $ cat library.h          #ifndef LIBRARY_H         #define LIBRARY_H          #pragma GCC visibility push(default) //added change         #include <string>         #pragma GCC visibility pop                 //added change          typedef unsigned short uchar;         typedef std::basic_string<uchar> ustring;          __attribute__ ((visibility("default"))) ustring foo();          #endif  // LIBRARY_H
```

[Back to Top](#)

## Release-to-Release Version Compatibility of Shared Libraries Using C APIs and C++ Implementations

One can maintain a pure C interface to a shared library while taking advantage of C++ in the shared library's implementation.

- Give all interface functions extern "C" linkage.
- Give all functions which are not part of the interface hidden visibility.
- Keep implementation details out of your interface headers as much as possible.
- Decorate the symbols in your headers so that your symbols have the visibility you intend, rather than relying on the client to use visiblity command line options.
- Monitor your visible symbols with `nm -mg`. You can ignore undefined symbols.
- Do not let exceptions escape from the shared library.
- Do not override new/delete, or if you do, make the overrides private to your library.
- Avoid interface inline functions with local static variables. Give inline functions hidden visibility (even if they are part of your interface).
- Never remove a visible symbol from your library unless you are willing to break ABI.
- Encode the library's major version number into its filename, so that when you do have to break ABI clients can have a choice of library versions.

For more details and good suggestions see the Apple reference documentation on [dynamic library design guidelines](https://developer.apple.com/documentation/DeveloperTools/Conceptual/DynamicLibraries/Articles/DynamicLibraryDesignGuidelines.html).

[Back to Top](#)

## Release-to-Release Version Compatibility of Shared Libraries Using C++ APIs and C++ Implementations

One can also have a C++ interface to a shared library. In addition to following the points listed in the previous section, one should also consider the following to help maintain a stable ABI:

- Except for the symbols detailed in the section on ABI issues, avoid the std C++ library in your interface. However do use it freely in your implementation.
- If you propagate exceptions out of your shared library, or if you have types for which you expect your clients to be able to `dynamic_cast`, make sure these types are marked visible.
- If not accessed by inline functions, consider giving private member functions hidden visibility.
- Consider using the [Pimpl idiom](http://www.gotw.ca/gotw/024.htm) when possible to hide your private data and functions from your client.
- Consider using namespace versioning to make the eventual ABI breakage less painful.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-05-25 | Correcting the section on setting function visibility via attributes: #define PUBLIC __attribute__((__visibility__("hidden"))) #define PRIVATE __attribute__((__visibility__("default"))) PUBLIC void MyFunction1() {} PRIVATE void MyFunction2() {} had the PUBLIC and PRIVATE macros defined backwards. |
| 2007-01-25 | New document that tips and tricks for beginning to advanced C++ programmers on Mac OS X. |

