---
title: C++ Runtime Environment Programming Guide
apple_id: TP40001666
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2009-10-09'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/CppRuntimeEnv/Articles/SymbolVisibility.html
archived_at: '2026-07-15T07:24:22.601241Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [C++ Runtime Environment Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Creating%20Compatible%20Libraries.md)

# Controlling Symbol Visibility

In ordinary C, if you want to limit the visibility of a function or variable to the current file, you apply the `static` keyword to it. In a shared library containing many files, though, if you want a symbol to be available in several files inside the library, but not available outside the library, hiding that symbol is more difficult. Most linkers provide convenient ways to hide or show all symbols in a module, but if you want to be more selective, it takes a lot more work.

Prior to OS X v10.4, there were two mechanisms for controlling symbol visibility. The first technique was to declare individual symbols as private to the library but external to the current file using the `__private_extern__` keyword. This keyword could be used in the same places you would use either the `static` or `extern` keywords. The second technique was to use an export list.

An export list is a file containing the names of symbols you explicitly want to hide or show. Although symbol names in C are easily determined (by prepending an underscore character to the name), determining symbol names in C++ is far more complicated. Because of classes and namespaces, compilers must include more information to identify each symbol uniquely, and so compilers create what is known as a mangled name for each symbol. This mangled name is often compiler-dependent, difficult to deduce, and difficult to find within a large list of symbols defined by your library.

Luckily, GCC 4.0 provides some new ways to change the visibility of symbols. The following sections describe these new techniques along with reasons why this might be important to you.

Beginning with OS X v10.4, hiding C++ symbol names is much easier. The GCC 4.0 compiler supports new options for hiding or showing symbols and also supports a new pragma and compiler attributes for changing the visibility of symbols in your code.

GCC 4.0 supports a new flag for setting the default visibility of symbols in a file. The `-fvisibility=`_vis_ compiler option lets you set the visibility for symbols in the current compilation. The value for this flag can be either `default` or `hidden`. When set to `default`, symbols not explicitly marked as hidden are made visible. When set to `hidden`, symbols not explicitly marked as visible are hidden. If you do not specify the `-fvisibility` flag during compilation, the compiler assumes `default` visibility.

The compiler also supports the `-fvisibility-inlines-hidden` flag for forcing all inline functions to be hidden. You might use this flag in situations where you want to use default visibility for most items but still want to hide all inline functions. For more information why this might be necessary for inline functions, see [Visibility of Inline Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmnzqfu4tqobqg4).

If you are compiling your code with GCC 4.0, you can mark individual symbols as default or hidden using the visibility attribute:

```
__attribute__((visibility("default"))) void MyFunction1() {}
__attribute__((visibility("hidden"))) void MyFunction2() {}
```

Visibility attributes override the value specified with the `-fvisibility` flag at compile-time. Thus, adding the `default` visibility attribute causes a symbol to be exported in all cases, whereas adding the `hidden` visibility attribute hides it.

Visibility attributes may be applied to functions, variables, templates, and C++ classes. If a class is marked as hidden, all of its member functions, static member variables, and compiler-generated metadata, such as virtual function tables and RTTI information, are also hidden.

To demonstrate how these attributes work at compile-time, take a look at the following declarations:

```
int a(int n) {return n;}

__attribute__((visibility("hidden"))) int b(int n) {return n;}

__attribute__((visibility("default"))) int c(int n) {return n;}

class X
{
    public:
        virtual ~X();
};

class __attribute__((visibility("hidden"))) Y
{
    public:
        virtual ~Y();
};

class __attribute__((visibility("default"))) Z
{
    public:
        virtual ~Z();
};

X::~X() { }
Y::~Y() { }
Z::~Z() { }
```

Compiling this code with the `-fvisibility=default` flag would cause the symbols for functions `a` and `c` and classes `X` and `Z` to be exported by the library. Compiling this code with the `-fvisibility=hidden` flag would cause the symbols for the function `c` and the class `Z` to be exported.

Using the visibility attribute to mark symbols as visible or hidden is better practice than using the `__private_extern__` keyword to hide individual symbols. Using the `__private_extern__` keyword takes the approach of exposing all symbols by default and then selectively hiding ones that are private. In a large shared library, the reverse approach is usually better. Thus, it is usually better to hide all symbols and then selectively expose the ones you want clients to use.

To simplify the task of marking symbols for export, you might also want to define a macro with the `default` visibility attribute set, such as in the following example:

```
#define EXPORT __attribute__((visibility("default")))

// Always export the following function.
EXPORT int MyFunction1();
```

The advantage of using a macro is that if your code is also compiled on other platforms, you can change the macro to the appropriate keywords for the compilers on the other platforms.

Another way to mark symbols as default or hidden is with a new pragma in GCC 4.0. The GCC visibility pragma has the advantage of being able to mark a block of functions quickly, without the need to apply the visibility attribute to each one. The use of this pragma is as follows:

```
void f() { }

#pragma GCC visibility push(default)
void g() { }
void h() { }
#pragma GCC visibility pop
```

In this example, the functions `g` and `h` are marked as default, and are therefore exported regardless of the `-fvisibility` flag, while the function `f` conforms to whatever value is set for the `-fvisibility` flag. As the names `push` and `pop` suggest, this pragma can be nested.

It is good practice to export as few symbols as possible from your dynamic shared libraries. Exporting a limited set of symbols improves program modularity and hides implementation details. Reducing the number of symbols in your libraries also decreases the footprint of your library and reduces the amount of work that must be done by the dynamic linker. With fewer symbols to load and resolve, the dynamic linker is able to get your program up and running more quickly.

Although it is likely that most C++ symbols in your shared library do not need to be visible, there are some situations where you do need to export them:

- If your library exports a C++ interface, the symbols associated with that interface must be visible.
- If your symbol uses runtime type identification (RTTI) information, exceptions, or dynamic casts for an object that is defined in another library, your symbol must be visible if it expects to handle requests initiated by the other library. For example, if you define a catch handler for a type in the C++ standard library, and you want to catch exceptions of that type thrown by the C++ standard library, you must make sure that your `typeinfo` object is visible.
- If you expect the address of an inline function used in different code modules to be the same for each module, the function must be exported from each code module.
- If your inline function contains a static object and you expect there to be only one copy of that object, your symbol for that static object must be visible.

You might think that the visibility of inline functions is not an issue, but it is. Inline functions are normally expanded at the call site, and thus never emitted as symbols in the object file at all. In a number of cases, however, the compiler may emit the body of the function, and therefore generate a symbol for it, for some very good reasons. In the most common case, the compiler may decide not to respect the inline optimization if all optimizations are disabled. In more rare cases, the function may be too big to inline or the address of the function might be used elsewhere and thus require a symbol.

Although you can apply the visibility attribute (see [Visibility Attributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmnzqfu4tonbrgu)) to inline functions in C++ just as you can any other symbol, it is usually better to hide all inline functions. Some complex issues arise when you export inline functions from dynamic shared libraries. Because there are several variables involved in the compiler’s decision to emit a function or inline it, you may run into errors when building clients for different builds of your shared library.

It is also important to remember that there are subtle differences between the inline function semantics for C and C++. In C programs, only one source file may provide an out-of-line definition for an inline function. This means that C programmers have precise control over where out-of-line copies reside. So for a C-based dynamic shared library, it is possible to export only one copy of an inline function. For C++, the definition of an inline function must be included in every translation unit that uses the function. So, if the compiler does emit an out-of-line copy, there can potentially be several copies of the function residing in different translation units.

In the end, if you want to hide all inline functions (but not necessarily all of your other code), you can use the `-fvisibility-inlines-hidden` flag when compiling your code. If you are already passing the `-fvisibility=hidden` flag to the compiler, use of the `-fvisibility-inlines-hidden` flag is unnecessary.

Objective-C is a strict superset of C, and Objective-C++ is a strict superset of C++. This means that all of the discussion regarding symbol visibility in C and C++ applies to Objective-C and Objective-C++ too. You can use the compiler flags, visibility attributes, and the visibility pragma to hide C and C++ code in your Objective-C code files.

In a 32-bit OS X project, these visibility controls apply only to the C or C++ subset of your code. They do not apply to Objective-C classes and methods. Objective-C class and message names are bound by the Objective-C runtime, not by the linker, so the notion of visibility does not apply to them. There is no mechanism for hiding an Objective-C class or method defined in a dynamic library from the clients of that library.

When building for x86_64 OS X or for iOS, symbol visibility _does_ affect objective-C classes. Hiding a class is not a security panacea—enterprising developers can access any class with objective-C runtime calls—but if you directly reference a class whose visibility is hidden in a library you link to, you will get a linker error. This means that if a given class is intended to be usable outside the library or executable it's defined in, you need to ensure proper symbol visibility.

[Next](Document%20Revision%20History.md)[Previous](Creating%20Compatible%20Libraries.md)

