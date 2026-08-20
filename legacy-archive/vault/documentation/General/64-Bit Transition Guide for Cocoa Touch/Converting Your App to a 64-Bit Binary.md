---
title: 64-Bit Transition Guide for Cocoa Touch
apple_id: TP40013501
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaTouch64BitGuide/ConvertingYourAppto64-Bit/ConvertingYourAppto64-Bit.html
archived_at: '2026-07-27T06:57:08.817615Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [64-Bit Transition Guide for Cocoa Touch](About%2064-Bit%20Cocoa%20Touch%20Apps.md)


[Next](Optimizing%20Memory%20Performance.md)[Previous](Major%2064-Bit%20Changes.md)

# Converting Your App to a 64-Bit Binary

At a high level, here are the steps to create an app that targets both the 32-bit and the 64-bit runtime environments:

1. __Install the latest Xcode.__
2. __Open your project.__ Xcode prompts you to modernize your project. Modernizing the project adds new warnings and errors that are important when compiling your app for 64-bit.
3. __Update your project settings to support iOS 5.1.1 or later.__ You can’t build a 64-bit project if it targets an iOS version earlier than iOS 5.1.
4. __Change the Architectures build setting in your project to “Standard Architectures (including 64-bit).”__
5. __Update your app to support the 64-bit runtime environment.__ The new compiler warnings and errors will help guide you through this process. However, the compiler doesn’t do all of the work for you; use the information in this document to help guide you through investigating your own code.
6. __Test your app on actual 64-bit hardware.__ iOS Simulator can also be helpful during development, but some changes, such as the function calling conventions, are visible only when your app is running on a device.
7. __Use Instruments to tune your app’s memory performance.__
8. __Submit an app that includes both architectures for approval.__

The remainder of this chapter describes problems that frequently occur when porting a Cocoa Touch app to the 64-bit runtime environment. Use these sections to guide your own efforts to investigate your code.

## Do Not Cast Pointers to Integers

There are few reasons to cast pointers to an integer type. By consistently using pointer types, you ensure that all of your variables are sized large enough to hold an address.

For example, the code in Listing 2-1 casts a pointer to an `int` type because it wants to perform arithmetic on the address. In the 32-bit runtime, this code works because an `int` type and a pointer are the same size. However, in the 64-bit runtime, a pointer is larger than an `int` type, so the assignment loses some of the pointer’s data. Here, because the pointer is being advanced by its native size, you can simply increment the pointer.

__Listing 2-1__  Casting a pointer to `int`

```
int *c = something passed in as an argument....
int *d = (int *)((int)c + 4); // Incorrect.
int *d = c + 1;               // Correct!
```

If you must convert a pointer to an integer type, always use the `uintptr_t` type to avoid truncation. Note that modifying pointer values via integer math and then converting it back into a pointer can violate basic type aliasing rules. This can lead to unexpected behavior from the compiler as well as processor faults when a misaligned pointer is accessed.

## Use Data Types Consistently

Many common programming errors result when you don’t use data types consistently throughout your code. Even though the compiler warns you of many problems that result from using data type inconsistently, it’s also useful to see a few variations of these patterns so that you can recognize them in your code.

When calling a function, always match the variable that receives the results to the function’s return type. If the return type is a larger integer than the receiving variable, the value is truncated. Listing 2-2 shows a simple pattern that exhibits this problem. The `PerformCalculation` function returns a `long` integer. In the 32-bit runtime, both `int` and `long` are 32 bits, so the assignment to an `int` type works, even though the code is incorrect. In the 64-bit runtime, the upper 32 bits of the result are lost when the assignment is made. Instead, the result should be assigned to a `long` integer; this approach works consistently in both runtimes.

__Listing 2-2__  Truncation when assigning a return value to a variable

```
long PerformCalculation(void);

    int  x = PerformCalculation(); // incorrect
    long y = PerformCalculation(); // correct!
```

The same problem occurs when you pass in a value as a parameter. For example, in Listing 2-3 the input parameter is truncated when executed in the 64-bit runtime.

__Listing 2-3__  Truncation of an input parameter

```
int PerformAnotherCalculation(int input);
    long i = LONG_MAX;
    int x = PerformCalculation(i);
```

In Listing 2-4, the return value is also truncated in the 64-bit runtime, because the value returned exceeds the range of the function’s return type.

__Listing 2-4__  Truncation when returning a value

```
int ReturnMax()
{
    return LONG_MAX;
}
```

All of these examples result from code that assumes that `int` and `long` are identical. The ANSI C standard does not make this assumption, and it is explicitly incorrect when working in the 64-bit runtime. By default, if you modernized your project, the `-Wshorten-64-to-32` compiler option was automatically enabled, so the compiler automatically warns you about many cases where a value is truncated. If you did not modernize your project, you should explicitly enable that compiler option. Optionally, you may want to include the `-Wconversion` option, which is more verbose, but finds more potential errors.

In a Cocoa Touch app, look for the following integer types and make sure you are using them correctly:

- `long`
- `NSInteger`
- `CFIndex`
- `size_t` (the result of calling the `sizeof` intrinsic operation)

And in both runtime environments, the `fpos_t` and `off_t` types are 64 bits in size, so never assign them to an `int` type.

### Enumerations Are Also Typed

In the LLVM compiler, enumerated types can define the size of the enumeration. This means that some enumerated types may also have a size that is larger than you expect. The solution, as in all the other cases, is to make no assumptions about a data type’s size. Instead, assign any enumerated values to a variable with the proper data type.

### Common Type-Conversion Problems in Cocoa Touch

Cocoa Touch, notably Core Foundation and Foundation, add additional situations to look for, because they offer ways to serialize a C data type or to capture it inside an Objective-C object.

__NSInteger changes size in 64-bit code.__ The [NSInteger](https://developer.apple.com/documentation/objectivec/nsinteger) type is used throughout Cocoa Touch; it is a 32-bit integer in the 32-bit runtime and a 64-bit integer in the 64-bit runtime. So when receiving information from a framework method that takes an `NSInteger` type, use the `NSInteger` type to hold the result.

Although you should never make the assumption that an [NSInteger](https://developer.apple.com/documentation/objectivec/nsinteger) type is the same size as an `int` type, here are a few critical examples to look for:

- Converting to or from an [NSNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/cl/NSNumber) object.
- Encoding and decoding data using the [NSCoder](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCoder/Description.html#//apple_ref/occ/cl/NSCoder) class. In particular, if you encode an `NSInteger` on a 64-bit device and later decode it on a 32-bit device, the decode method throws an exception if the value exceeds the range of a 32-bit integer. You may want to use an explicit integer type instead (see [Use Explicit Integer Data Types](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkmbrfvbuqmznknlto)).
- Working with constants defined in the framework as `NSInteger`. Of particular note is the [NSNotFound](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSNotFound) constant. In the 64-bit runtime, its value is larger than the maximum range of an `int` type, so truncating its value often causes errors in your app.

__CGFloat changes size in 64-bit code.__ The [CGFloat](https://developer.apple.com/documentation/coregraphics/cgfloat) type changes to a 64-bit floating point number. As with the `NSInteger` type, you cannot assume that `CGFloat` is a `float` or a `double`. So use `CGFloat` consistently. [Listing 2-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkmbrfvbuqmznknltcny) shows an example that uses Core Foundation to create a `CFNumber`. But the code assumes that a `CGFloat` is the same size as a `float`, which is incorrect.

__Listing 2-5__  Use `CGFloat` types consistently

```
// Incorrect.
CGFloat value = 200.0;
CFNumberCreate(kCFAllocatorDefault, kCFNumberFloatType, &value);

// Correct!
CGFloat value = 200.0;
CFNumberCreate(kCFAllocatorDefault, kCFNumberCGFloatType, &value);
```

## Be Careful When Performing Integer Computations

Although truncation is the most common problem, you may also run into other problems related to the integer change. This section includes some additional guidance you can use to update your code.

### Sign Extension Rules for C and C-derived Languages

C and similar languages use a set of sign extension rules to determine whether to treat the top bit in an integer as a sign bit when the value is assigned to a variable of larger width. The sign extension rules are as follows:

1. Unsigned values are zero extended (not sign extended) when promoted to a larger type.
2. Signed values are always sign extended when promoted to a larger type, even if the resulting type is unsigned.
3. Constants (unless modified by a suffix, such as `0x8L`) are treated as the smallest size that will hold the value. Numbers written in hexadecimal may be treated by the compiler as `int`, `long`, and `long long` types and may be either `signed` or `unsigned` types. Decimal numbers are always treated as `signed` types.
4. The sum of a signed value and an unsigned value of the same size is an unsigned value.

Listing 2-6 shows an example of unexpected behavior resulting from these rules along with an accompanying explanation.

__Listing 2-6__  Sign extension example 1

```
int a=-2;
unsigned int b=1;
long c = a + b;
long long d=c; // to get a consistent size for printing.

printf("%lld\n", d);
```

_Problem:_ When this code is executed in the 32-bit runtime, the result is `-1` (`0xffffffff`). When the code is run in the 64-bit runtime, the result is `4294967295` (`0x00000000ffffffff`), which is probably not what you were expecting.

_Cause:_ Why does this happen? First, the two numbers are added. A signed value plus an unsigned value results in an unsigned value _(rule 4)_. Next, that value is promoted to a larger type. This promotion does not cause sign extension.

_Solution:_ To fix this problem in a 32-bit-compatible way, cast `b` to a `long` integer. This cast forces the non-sign-extended promotion of `b` to a 64-bit type prior to the addition, thus forcing the signed integer to be promoted (in a signed fashion) to match. With that change, the result is the expected `-1`.

Listing 2-7 shows a related example with an accompanying explanation.

__Listing 2-7__  Sign extension example 2

```
unsigned short a=1;
unsigned long b = (a << 31);
unsigned long long c=b;

printf("%llx\n", c);
```

_Problem:_ The expected result (and the result from a 32-bit executable) is `0x80000000`. The result generated by a 64-bit executable, however, is `0xffffffff80000000`.

_Cause:_ Why is this sign extended? First, when the shift operator is invoked, the variable `a` is promoted to a variable of type `int`. Because all values of a `short` integer can fit into a signed `int` type, the result of this promotion is signed.

Second, when the shift completed, the result was stored into a `long` integer. Thus, the 32-bit signed value represented by `(a << 31)` was sign extended _(rule 2)_ when it was promoted to a 64-bit value (even though the resulting type is unsigned).

_Solution:_ Cast the initial value to a `long` integer prior to the shift. The short is promoted only once—this time, to a 64-bit type (at least when compiled as a 64-bit executable).

### Working with Bits and Bitmasks

When working with bits and masks with 64-bit values, you want to avoid getting 32-bit values inadvertently. Here are some tips to help you.

__Don’t assume that a data type has a particular length.__ If you are shifting through the bits stored in a variable of type `long` integer, use the `LONG_BIT` value to determine the number of bits in a `long` integer. The result of a shift that exceeds the length of a variable is architecture dependent.

__Use inverted masks if needed.__ Be careful when using bit masks with `long` integers, because the width differs between 32-bit and 64-bit runtimes. There are two ways to create a mask, depending on whether you want the mask to be zero extended or one extended:

- If you want the mask value to contain zeros in the upper 32 bits in the 64-bit runtime, the usual fixed-width mask works as expected, because it will be extended in an unsigned fashion to a 64-bit quantity.
- If you want the mask value to contain ones in the upper bits, write the mask as the bitwise inverse of its inverse, as shown in Listing 2-8.

__Listing 2-8__  Using an inverted mask for sign extension

```
function_name(long value)
{
    long mask = ~0x3; // 0xfffffffc or 0xfffffffffffffffc
    return (value & mask);
}
```

In the code, note that the upper bits in the mask are filled with ones in the 64-bit case.

## Create Data Structures with Fixed Size and Alignment

When data is shared between the 32-bit and 64-bit versions of your app, you may need to create data structures whose 32-bit and 64-bit representations are identical, mostly when the data is stored to a file or transmitted across a network to a device that may have the opposite runtime environment. But also keep in mind that a user might back up their data stored on a 32-bit device and then restore that data to a 64-bit device. So interoperability of data is a problem you must solve.

### Use Explicit Integer Data Types

The C99 standard provides built-in data types that are guaranteed to be a specific size, regardless of the underlying hardware architecture. You should use these data types when your data must be a fixed size or when you know that a particular variable has a limited range of possible values. By choosing a proper data type, you get a fixed-width type you can store in memory and you also avoid wasting memory by allocating a variable whose range is much larger than you need.

Table 2-1 lists the C99 types along with the ranges of allowed values for each.

__Table 2-1__  C99 explicit integer types

| Type | Range |
| int8_t | -128 to 127 |
| int16_t | -32,768 to 32,767 |
| int32_t | -2,147,483,648 to 2,147,483,647 |
| int64_t | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| uint8_t | 0 to 255 |
| uint16_t | 0 to 65,535 |
| uint32_t | 0 to 4,294,967,295 |
| uint64_t | 0 to 18,446,744,073,709,551,615 |

### Be Careful When Aligning 64-Bit Integer types

In the 64-bit runtime, the alignment of all 64-bit integer types changes from 4 bytes to 8 bytes. Even if you specify each integer type explicitly, the two structures may still not be identical in both runtimes. In Listing 2-9, the alignment changes even though the fields are declared with explicit integer types.

__Listing 2-9__  Alignment of 64-bit integers in structures

```swift
struct bar {
    int32_t foo0;
    int32_t foo1;
    int32_t foo2;
    int64_t bar;
};
```

When this code is compiled with a 32-bit compiler, the field `bar` begins 12 bytes from the start of the structure. When the same code is compiled with a 64-bit compiler, the field `bar` begins 16 bytes from the start of the structure. Four bytes of padding are added after `foo2` so that `bar` is aligned to an 8-byte boundary.

If you are defining a new data structure, organize the elements with the largest alignment values first and the smallest elements last. This structure organization eliminates the need for most padding bytes. If you are working with an existing structure that includes misaligned 64-bit integers, you can use a pragma to force the proper alignment. Listing 2-10 shows the same data structure, but here the structure is forced to use the 32-bit alignment rules.

__Listing 2-10__  Using pragmas to control alignment

```swift
#pragma pack(4)
struct bar {
    int32_t foo0;
    int32_t foo1;
    int32_t foo2;
    int64_t bar;
};
#pragma options align=reset
```

Use this option only when necessary, because there is a performance penalty for misaligned accesses. For example, you might use this option to maintain backward compatibility with data structures already in use in a 32-bit version of your app.

## Allocate Memory Using sizeof

Never call [malloc](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/malloc.3.html#//apple_ref/doc/man/3/malloc) with an explicit size (for example, `malloc(4)`) to allocate space for a variable. Always use `sizeof` to obtain the correct size for any structure or variable you allocate. Search your code for any instance of `malloc` that isn’t followed by `sizeof`.

## Update Format Strings to Support Both Runtimes

Print functions such as `printf` can be tricky when you are writing code to support both runtimes, because of the data type changes. To solve this problem for pointer-sized integers (`uintptr_t`) and other standard types, use the various macros defined in the `inttypes.h` header file.

The format strings for various data types are described in Table 2-2. These additional types, listed in the `inttypes.h` header file, are described in Table 2-3.

__Table 2-2__  Standard format strings

| Type | Format string |
| `int` | `%d` |
| `long` | `%ld` |
| `long long` | `%lld` |
| `size_t` | `%zu` |
| `ptrdiff_t` | `%td` |
| any pointer | `%p` |

__Table 2-3__  Additional `inttypes.h` format strings (where `N` is some number)

| Type | Format string |
| `int[N]_t` (such as `int32_t`) | `PRId[N]` (such as `PRId32` |
| `uint[N]_t` | `PRIu[N]` |
| `int_least[N]_t` | `PRIdLEAST[N]` |
| `uint_least[N]_t` | `PRIuLEAST[N]` |
| `int_fast[N]_t` | `PRIdFAST[N]` |
| `uint_fast[N]_t` | `PRIuFAST[N]` |
| `intptr_t` | `PRIdPTR` |
| `uintptr_t` | `PRIuPTR` |
| `intmax_t` | `PRIdMAX` |
| `uintmax_t` | `PRIuMAX` |

For example, to print an `intptr_t` variable (a pointer-sized integer) and a pointer, you write code similar to that in Listing 2-11.

__Listing 2-11__  Architecture-independent printing

```c
#include <inttypes.h>
void *foo;
intptr_t k = (intptr_t) foo;
void *ptr = &k;

printf("The value of k is %" PRIdPTR "\n", k);
printf("The value of ptr is %p\n", ptr);
```

## Take Care with Functions and Function Pointers

Function calls in the 64-bit runtime are handled differently than functions in the 32-bit runtime. The critical difference is that function calls with variadic prototypes use a different sequence of instructions to read their parameters than functions that take a fixed list of parameters. Listing 2-12 shows the prototypes for two functions. The first function (`fixedFunction`) always takes a pair of integers. The second function takes a variable number of parameters (but at least two). In the 32-bit runtime, both of the function calls in Listing 2-12 use a similar sequence of instructions to read the parameter data. In the 64-bit runtime, the two functions are compiled using conventions that are completely different.

__Listing 2-12__  64-bit calling conventions vary by function type

```
int fixedFunction(int a, int b);
int variadicFunction(int a, ...);

int main
{
    int value2 = fixedFunction(5,5);
    int value1 = variadicFunction(5,5);
}
```

Because the calling conventions are much more precise in the 64-bit runtime, you need to make sure that a function is always called correctly, so that the callee always finds the parameters that the caller provided.

### Always Define Function Prototypes

When compiling using the modernized project settings, the compiler generates errors if you attempt to make a function call to a function that does not have an explicit prototype. You must provide a function prototype so that the compiler can determine whether the function is a variadic function or not.

### Function Pointers Must Use the Correct Prototype

If you pass a function pointer in your code, its calling conventions must stay consistent. It should always take the same set of parameters. Never cast a variadic function to a function that takes a fixed number of parameters (or vice versa). Listing 2-13 is an example of a problematic piece function call. Because the function pointer was cast to use a different set of calling conventions, a caller is going to place the parameters in a place that the called function is not expecting. This mismatch may cause your app to crash or to exhibit other unpredictable behaviors.

__Listing 2-13__  Casting between variadic and nonvariadic functions results in an error

```
int MyFunction(int a, int b, ...);

int (*action)(int, int, int) = (int (*)(int, int, int)) MyFunction;
action(1,2,3); // Error!
```

__Important:__ If you cast a function in this way, the compiler does not generate an error or warning and its unpredictable behavior is not visible in iOS Simulator. Always test on a real device before shipping your app.

### Dispatch Objective-C Messages Using the Method Function’s Prototype

An exception to the casting rule described above is when you are calling the [objc_msgSend](https://developer.apple.com/documentation/objectivec/1456712-objc_msgsend) function or any other similar functions in the Objective-C runtime that send messages. Although the prototype for the message functions has a variadic form, the method function that is called by the Objective-C runtime does not share the same prototype. The Objective-C runtime directly dispatches to the function that implements the method, so the calling conventions are mismatched, as described previously. Therefore you must cast the [objc_msgSend](https://developer.apple.com/documentation/objectivec/1456712-objc_msgsend) function to a prototype that matches the method function being called.

Listing 2-14 shows the proper form for dispatching a message to an object using the low-level message functions. In this example, the `doSomething:` method takes a single parameter and does not have a variadic form. It casts the [objc_msgSend](https://developer.apple.com/documentation/objectivec/1456712-objc_msgsend) function using the prototype of the method function. Note that a method function always takes an `id` variable and a selector as its first two parameters. After the [objc_msgSend](https://developer.apple.com/documentation/objectivec/1456712-objc_msgsend) function is cast to a function pointer, the call is dispatched through that same function pointer.

__Listing 2-14__  Using a cast to call the Objective-C message sending functions

```objc
- (int) doSomething:(int) x { ... }
- (void) doSomethingElse {
    int (*action)(id, SEL, int) = (int (*)(id, SEL, int)) objc_msgSend;
    action(self, @selector(doSomething:), 0);
}
```

### Be Careful When Calling Variadic Functions

Variable argument lists (`varargs`) do not provide type information for the arguments, and the arguments are not automatically promoted to larger types. If you need to distinguish between different incoming data types, you are expected to use a format string or other similar mechanism to provide that information to the `varargs` function. If the calling function does not correctly provide that information (or if the `varargs` function does not interpret it correctly), you get incorrect results.

In particular, if your `varargs` function expects a `long` integer and you pass in a 32-bit value, the `varargs` function contains 32 bits of data and 32 bits of garbage from the next argument (which you lose as a result). Likewise, if your `varargs` function is expecting an `int` type and you pass in a `long` integer, you get only half of the data, and the rest incorrectly appears in the argument that follows. (One example of this occurs if you use an incorrect [printf](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/printf.3.html#//apple_ref/doc/man/3/printf) format strings.)

## Never Access the Objective-C Pointer Directly

If you have code that directly accesses an object’s `isa` field, that code fails when executing in the 64-bit runtime. The `isa` field no longer holds a pointer. Instead, it includes some pointer data and uses the remaining bits to hold other runtime information. This optimization improves both memory usage and performance.

To read an object’s `isa` field, use the [class](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/class) property or call the [object_getClass](https://developer.apple.com/documentation/objectivec/1418629-object_getclass) function instead. To write to an object’s `isa` field, call the [object_setClass](https://developer.apple.com/documentation/objectivec/1418905-object_setclass).

__Important:__ Because these errors aren’t detected by iOS Simulator, always test your app on actual hardware.

## Use the Built-in Synchronization Primitives

Sometimes, apps implement their own synchronization primitives to improve performance. The iOS runtime environment provides a full complement of primitives that are optimized and correct for each CPU on which they are running. This runtime library is updated as new architectural features are added. Existing 32-bit apps that rely on the runtime library automatically take advantage of new CPU features introduced in the 64-bit world. If you implemented custom primitives in a previous version of your app, now you might be relying on instructions or paths that are orders of magnitude slower than the built-in primitives. Instead, always use the built-in primitives.

## Never Hard-Code the Virtual Memory Page Size

Most apps do not need to know the size of a virtual memory page, but some use it for buffer allocations and some framework calls. Starting with iOS 7, the page size may vary between devices in both the 32-bit and 64-bit runtimes. Therefore, always use the `getpagesize()` function to get the size of the page.

## Go Position Independent

The 64-bit runtime environment supports only Position-Independent Executables (PIE). By default most modern apps are built as position independent. If you have something that is preventing your app from building as a position independent code, such as a statically linked library or assembly code, you need to update this code when porting your app to the 64-bit runtime. Position-independence is also highly recommended for 32-bit apps.

For more information, see _[Building a Position Independent Executable](../../../qa/Building%20a%20Position%20Independent%20Executable.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmzvgq)_.

## Make Your App Run Well in the 32-Bit Runtime

Currently, an app that is written for the 64-bit runtime environment must also support the 32-bit runtime. So you need to make apps that work well when running in either environment. Usually this means creating a single design that works well in both environments. Occasionally, you may need to design specific solutions for each runtime environment.

For example, you might be tempted to use 64-bit integers throughout your code; both environments support 64-bit integer types, and using only a single integer type everywhere simplifies your app’s design. If you use 64-bit integers everywhere, your app will run more slowly in the 32-bit runtime. A 64-bit processor can perform 64-bit integer operations just as quickly as 32-bit integer operations, but a 32-bit processor performs 64-bit calculations much more slowly. And in both environments, the variable may use more memory than is necessary. Instead, a variable should use an integer type that matches the range of values you expect it to hold. If a calculation always fits in a 32-bit integer, use a 32-bit integer. See [Use Explicit Integer Data Types](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkmbrfvbuqmznknlto).

[Next](Optimizing%20Memory%20Performance.md)[Previous](Major%2064-Bit%20Changes.md)
