---
title: 64-Bit Transition Guide for Cocoa Touch
apple_id: TP40013501
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaTouch64BitGuide/Major64-BitChanges/Major64-BitChanges.html
archived_at: '2026-07-27T06:57:08.783258Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [64-Bit Transition Guide for Cocoa Touch](About%2064-Bit%20Cocoa%20Touch%20Apps.md)


[Next](Converting%20Your%20App%20to%20a%2064-Bit%20Binary.md)[Previous](About%2064-Bit%20Cocoa%20Touch%20Apps.md)

# Major 64-Bit Changes

When different pieces of code must work together, they must follow standard agreed-upon conventions about how code should act. Conventions include the size and format of common data types, as well as the instructions used when one piece of code calls another. Compilers are implemented based on these conventions so that they can emit binary code that works together. Collectively, these conventions are referred to as an _application binary interface (ABI)_.

iOS apps rely on a low-level application binary interface and coding conventions established by the Objective-C language and the system frameworks. Starting with iOS 7, some iOS devices use 64-bit processors and offer both a 32-bit and a 64-bit runtime environment. For most apps, the 64-bit runtime environment differs from the 32-bit runtime environment in two significant ways:

- In the 64-bit runtime, many data types used by Cocoa Touch frameworks (as well as the Objective-C language itself) have increased in size or have stricter memory alignment rules. See [Changes to Data Types](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkmbrfvbuqmrnkrifqusfiyytamy).
- The 64-bit runtime requires proper function prototypes to be used when making function calls. See [Changes to Function Calling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkmbrfvbuqmrnknltk).

## Changes to Data Types

In the C and Objective-C languages, the built-in data types do not have a predefined size or alignment in memory. Instead, each platform defines the characteristics of the built-in types. This means that, within the restrictions defined in the language standard, a platform can use values that best match the underlying hardware and operating system. The 64-bit runtime on iOS changes the sizes of many built-in data types. At a higher level, many data types used by Cocoa Touch frameworks have also changed. This section describes the changes to the data types commonly used in Objective-C code.

### Two Conventions: ILP32 and LP64

The 32-bit runtime uses a convention called ILP32, in which integers, `long` integers, and pointers are 32-bit quantities. The 64-bit runtime uses the LP64 convention; integers are 32-bit quantities, and `long` integers and pointers are 64-bit quantities. These conventions match the ABI for apps running on OS X (and similarly, the Cocoa Touch conventions match the data types used in Cocoa), making it easy to write interoperable code between the two operating systems.

Table 1-1 describes all of the integer types commonly used in Objective-C code. Each entry includes the size of the data type and its expected alignment in memory. The highlighted table entries indicate places where the LP64 convention differs from the ILP32 convention. These size differences indicate places where your code’s behavior changes when compiled for the 64-bit runtime. The compiler defines the `__LP64__` macro when compiling for the 64-bit runtime.

__Table 1-1__  Size and alignment of integer data types in OS X and iOS

| Integer data type | ILP32 size | ILP32 alignment | LP64 size | LP64 alignment |
| `char` | 1 byte | 1 byte | 1 byte | 1 byte |
| `BOOL`, `bool` | 1 byte | 1 byte | 1 byte | 1 byte |
| `short` | 2 bytes | 2 bytes | 2 bytes | 2 bytes |
| `int` | 4 bytes | 4 bytes | 4 bytes | 4 bytes |
| `long` | 4 bytes | 4 bytes | __8 bytes__ | __8 bytes__ |
| `long long` | 8 bytes | 4 bytes | 8 bytes | __8 bytes__ |
| pointer | 4 bytes | 4 bytes | __8 bytes__ | __8 bytes__ |
| `size_t` | 4 bytes | 4 bytes | __8 bytes__ | __8 bytes__ |
| `time_t` | 4 bytes | 4 bytes | __8 bytes__ | __8 bytes__ |
| `NSInteger` | 4 bytes | 4 bytes | __8 bytes__ | __8 bytes__ |
| `CFIndex` | 4 bytes | 4 bytes | __8 bytes__ | __8 bytes__ |
| `fpos_t` | 8 bytes | 4 bytes | 8 bytes | __8 bytes__ |
| `off_t` | 8 bytes | 4 bytes | 8 bytes | __8 bytes__ |

To summarize the changes:

- The size of pointers increased from 4 bytes to 8 bytes.
- The size of `long` integers increased from 4 bytes to 8 bytes. The `size_t`, [CFIndex](https://developer.apple.com/documentation/corefoundation/cfindex), and [NSInteger](https://developer.apple.com/documentation/objectivec/nsinteger) types also increased from 4 bytes to 8 bytes.
- The alignment of `long long` integers and the data types based on it (`fpos_t`, `off_t`) has increased from 4 bytes to 8 bytes. All other types use the natural alignment, meaning that data elements within a structure are aligned at intervals corresponding to the width of the underlying data type.

Table 1-2 shows the floating-point types commonly used in iOS and OS X. Although the built-in data types do not change in size, in the 64-bit runtime the [CGFloat](https://developer.apple.com/documentation/coregraphics/cgfloat) type changes from a `float` to a `double`, providing a larger range and accuracy for these values in Quartz and in other frameworks that use the Core Graphics types. (Floating-point types always use natural alignment.)

__Table 1-2__  Size of floating-point data types in OS X and iOS

| Floating-point type | ILP32 size | LP64 size |
| `float` | 4 bytes | 4 bytes |
| `double` | 8 bytes | 8 bytes |
| [CGFloat](https://developer.apple.com/documentation/coregraphics/cgfloat) | 4 bytes | __8 bytes__ |

The 64-bit ARM environment uses a little-endian environment; this matches the 32-bit iOS runtime used by devices with ARM processors that support the ARMv7 architecture.

### Impact of Data Type Changes on Your App

When you compile your app for both the 32-bit and 64-bit runtime environments, keep in mind that your app’s behavior differs according to the environment it runs in and can result in performance differences or severe compatibility problems. Here are some of the things you need to consider:

- Increased memory pressure

  Because so many fundamental types have increased in size, the 64-bit version of your app uses more memory than the 32-bit version does. For example, even something as simple as a linked list is more expensive when compiled for the 64-bit runtime. Expect to spend more time optimizing the performance of the 64-bit version of your app. You may also need to consider different strategies when designing your app’s data structures, including the instance variables used in your Objective-C classes. For some examples, see [Optimizing Memory Performance](Optimizing%20Memory%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkmbrfvbuqnbnknltc).
- Exchanging data between 64-bit and 32-bit software

  If you ship both 32-bit and 64-bit software, sometimes both versions need to interoperate on the same data. For example, a user might access a file stored in iCloud from both 32-bit and 64-bit devices. Or you might be creating a game that sends network data between devices. In both runtimes, make sure that the data being read or written uses a common memory layout, meaning that the sizes and offsets of every data element are identical.
- Calculations might produce different results

  A 64-bit integer supports a vastly larger range of possible values than a 32-bit integer supports. If your app uses an integer type that changed from 32 bits to 64 bits, the results might be different in the 64-bit version of your app. Specifically, a calculation that exceeds the maximum value of a 32-bit integer overflows on a 32-bit integer but not on a 64-bit integer. Other such edge cases exist.
- Values may be truncated when data is copied from a larger data type to a smaller data type

  Some apps assume that two data types are the same rather than safely converting between them. In the 64-bit runtime, previous assumptions about data types may no longer be correct. For example, assigning an `NSInteger` value to an `int` type works in the 32-bit runtime because both types are 32-bit integers. But in the 64-bit runtime, the two are not the same type and so data may be lost.

## Changes to Function Calling

When a function call is made, the compiler emits code to pass the parameters from the caller to the callee. For example, an ABI might specify that the caller places its parameters into registers, or it might specify that the caller pushes the values onto a stack in memory. Normally, if you aren’t writing assembly language, the calling conventions are rarely important. But in the 64-bit runtime, sometimes you need to be aware of how functions are called. Functions that accept a variable number of parameters (variadic functions) are called using a different set of conventions than calls to functions that accept a fixed set of parameters.

### Impact of Function Call Changes on Your App

When coding an app that targets the 64-bit runtime, your app must always call a function using its exact definition. As a result:

- Every function must have a prototype.
- When you cast a function, you must be careful that the cast version of the function has the same signature as the original function. In particular, avoid casting a a function to a form that takes a different set of parameters (such as casting a function pointer that takes a variadic pattern to one that takes a fixed number of parameters). Additional rules apply if your code directly calls message passing functions in the Objective-C runtime. (See [Dispatch Objective-C Messages Using the Method Function’s Prototype](Converting%20Your%20App%20to%20a%2064-Bit%20Binary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkmbrfvbuqmznknltenq).)

## Changes to Objective-C

If you are writing low-level code that targets the Objective-C runtime directly, you can no longer access an object’s `isa` pointer directly. Instead, you need to use the runtime functions to access that information.

## Other Changes to the 64-Bit Runtime

The 64-bit ARM instruction set is significantly different from the 32-bit instruction set. If your app includes any assembly language code, you need to rewrite it to use the new instruction set. You also need a more detailed description of the 64-bit calling conventions in iOS, because the conventions do not exactly match the ARM standard. For more information, see _[iOS ABI Function Call Guide](../../Xcode/iOS%20ABI%20Function%20Call%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tamrt)_.

## Summary

At a high level, to make your code 64-bit clean, you must do the following:

- Avoid assigning 64-bit `long` integers to 32-bit integers.
- Avoid assigning 64-bit pointers to 32-bit integers.
- Avoid pointer and `long` integer truncation during arithmetic operations (or other arithmetic problems caused by the change in integer types).
- Fix alignment issues caused by changes in data type sizes.
- Ensure that memory structures that are shared between the 32-bit and 64-bit runtimes share a similar layout.
- Rewrite any assembly language code so that your code uses the new 64-bit opcodes and runtime.
- Avoid casting variadic functions to functions that take a fixed number of parameters, or vice versa.

[Next](Converting%20Your%20App%20to%20a%2064-Bit%20Binary.md)[Previous](About%2064-Bit%20Cocoa%20Touch%20Apps.md)
