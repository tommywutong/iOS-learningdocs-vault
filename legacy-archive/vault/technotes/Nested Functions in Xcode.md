---
title: Nested Functions in Xcode
apple_id: DTS10003870
resource_type: Technical Note
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2006-01-10'
source_url: https://developer.apple.com/library/archive/technotes/tn2161/_index.html
archived_at: '2026-07-26T19:54:08.748361Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2161

# Nested Functions in Xcode

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

This technote explains how to port code which uses nested functions, a GCC extension to the C language. Nested functions are not supported in Xcode 2.2.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobxgawugsbrfvke4vcbi4yq)[About Nested Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobxgawugsbrfvke4vcbi4za)[Modifying Your Application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobxgawugsbrfvke4vcbi42a)[Another Example](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobxgawugsbrfvke4vcbi44q)[Nested Functions and GNU Autoconf](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobxgawugsbrfvke4vcbi4yte)[Linker Support for Nested Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobxgawugsbrfvke4vcbi4ytk)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobxgawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

This technote explains how to port code which uses nested functions, a GCC extension to the C language which is not supported in Xcode 2.2. A future Xcode release will introduce a compiler switch, -fnested-functions, and a corresponding build setting to enable the feature for backwards compatibility. However, nested functions will continue to be disabled by default. Use of the backwards compatibility mode should be avoided, since it will prevent your application from taking advantage of a security feature in Mac OS X.

This technote is directed at application developers who have discovered that after installing Xcode 2.2, their application fails to build with the error "nested functions are not supported on MacOSX". If you are not getting this error, your code does not use nested functions and you do not need to read this technote (unless your application uses GNU Autoconf; see "Nested Functions and GNU Autoconf" below.)

[Back to Top](#)

## About Nested Functions

Nested functions are a GCC extension to the C language which allows you to declare a function inside another function. For instance:

```
 void x(int a) {         int b;         ...         void y() {             ...         }         ...     }
```

In the example above, the function y() can only be called from inside the function x. It can access any variables which are in scope in x, such as a and b.

Nested functions are not very widely used. In a survey of 2500 open-source applications taken from the Fink project, only 6 made use of the feature.

In order to support nested functions, the compiler needed to generate code in a form which could, in certain scenarios, impact the security of the system by using a technique called stack trampolines. Stack trampolines require stack pages to be executable; this increases an application's vulnerability to buffer overflow attacks. Because it was not feasible to securely provide support for nested functions, this support was removed from the compiler in Xcode 2.2. Furthermore, removing nested functions from your code will often lead to performance improvements.

[Back to Top](#)

## Modifying Your Application

Xcode will flag all nested functions with the nested function error message when you try to build your application. To unnest these functions, take any nested functions and move them outside and above the body of the function they're inside. You may need to change the names of some formerly nested functions to avoid conflicting with other functions in your application. For instance, change:

```
 void x() {         void y() { ... }     }
```

to:

```
 void y() { ... }     void x() { ... }
```

Now try building your application again. If it builds successfully, that's all you need to do. On the other hand, you may get error messages inside your formerly nested functions about variables being undeclared (for instance, "error: 'foo' undeclared (first use in this function.") This will happen when the nested function accessed variables local to its parent function. In that case, add the variables as new parameters to the function. Because the function may modify the values, you'll need to pass them by reference, through pointers. For instance, change:

```
 void x(int a) {         int b;         void y(int c) { ... }         y(1);     }
```

to:

```
 void y(int c, int *a, int *b) { ... }     void x(int a) {         int b;         y(1,  &a, &b);     }
```

Make sure you update your formerly nested functions to take into account that a and b are now pointers to integers instead of simply integers!

If you know certain things about how the two functions act regarding the variables local to the original function which are now parameters of the new function, there are some optimizations you can make. If the outer function doesn't care about any changes in the value of one of these variables which take place within the nested function, it isn't necessary to pass it in to the new function by reference, so in the example above, a or b in y could be type int instead of int \* if we knew this about them. If the inner function never modifies the value at all, you can add the const modifier, e.g. const int a.

[Back to Top](#)

## Another Example

__Listing 1__  Without nested functions

```
 int factorial(int num) {         int total = 1, b;          int multiply() {             return total * b;         }          int updateTotal() {             total = multiply();         }          for(b = 1; b <= num; b++) {             updateTotal();         }          return total;     }
```

__Listing 2__  With nested functions

```
 //multiply doesn't modify either total or b, so     //we don't need to pass them through pointers     //and we can make them const.     int multiply(const int total, const int b) {         return total * b;     }      //updateTotal doesn't modify b, but it does     //modify total.     int updateTotal(int *total, const int b) {         *total = multiply(*total, b);     }      int factorial(int num) {         int total = 1, b;          for(b = 1; b <= num; b++) {             updateTotal(&total, b);         }          return total;     }
```

[Back to Top](#)

## Nested Functions and GNU Autoconf

Applications which use GNU Autoconf, primarily cross-platform UNIX applications, may have accidental usages of nested functions in their configure scripts which are harder to detect. These usages of nested functions may cause configure checks to silently fail, producing an application which builds in an incorrect manner.

If your application uses GNU Autoconf, you should run the configure script after installing Xcode 2.2 and search config.log for the string nested functions are not supported. If you see this string, you have improperly-written configure macros which you should adjust. Problematic macros look like:

```
 AC_TRY_COMPILE([         #include <stdio.h>     ], [         int main(int argc, char *argv[]) {             printf("Hello, world!\n");             return 0;         }     ], ...
```

GNU Autoconf provides its own main function for configure tests, so you should rewrite the macro to look like:

```
 AC_TRY_COMPILE([         #include <stdio.h>     ], [         printf("Hello, world!\n");     ], ...
```

[Back to Top](#)

## Linker Support for Nested Functions

The linker provides a switch, -allow_stack_execute, which forces execution of the stack segment to be enabled, even in configurations where it would otherwise default to being disabled. Compilers which understand -fnested-functions will supply -allow_stack_execute to the linker when -fnested-functions is given.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-01-10 | New document that this technote explains how to port code which uses nested functions in Xcode 2.2. |

