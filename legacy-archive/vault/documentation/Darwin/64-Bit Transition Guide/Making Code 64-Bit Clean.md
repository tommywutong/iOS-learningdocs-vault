---
title: 64-Bit Transition Guide
apple_id: TP40001064
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/64bitPorting/MakingCode64-BitClean/MakingCode64-BitClean.html
archived_at: '2026-07-15T07:23:04.065441Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [64-Bit Transition Guide](Introduction%20to%2064-Bit%20Transition%20Guide.md)


[Next](Compiling%2064-Bit%20Code.md)[Previous](Major%2064-Bit%20Changes.md)

# Making Code 64-Bit Clean

Before you begin to update your code, you should familiarize yourself with the document _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_. After reading that document, the first thing you should do is compile your code with the `-Wall` compiler flag and fix any warnings that occur. In particular, make sure that all function prototypes are in scope, because out-of-scope prototypes can hide many subtle portability problems.

At a high level, to make your code 64-bit clean, you must do the following:

- Avoid assigning 64-bit `long` integers to 32-bit integers.
- Avoid assigning 64-bit pointers to 32-bit integers.
- Fix alignment issues caused by changes in data type sizes.
- Avoid pointer and `long` integer truncation during arithmetic operations.

This section contains some general tips for making your code 64-bit clean.

__Update architecture-specific code.__ If your software contains any architecture-specific code, you must either add extra code for each additional architecture or modify your preprocessor directives so that the same code is included for multiple supported architectures.

Unless you are including inline assembly language code, you should generally test for the presence of architecture-neutral macros such as `__LITTLE_ENDIAN__` or `__LP64__` rather than testing for a specific processor architecture.

The macro `__LP64__` can be used to test for LP64 compilation in an architecture-independent way. For example:

```
#ifdef __LP64__
// 64-bit code
#else
// 32-bit code
#endif
```

For code that is truly architecture-specific (such as assembly language code), you should continue to use architecture-specific tests. Be aware, however, that when compiling for a 64-bit architecture, code wrapped in a test for a 32-bit architecture is _not_ compiled into the executable.

For example, code wrapped with the `#ifdef __i386__` directive will not be included when compiling for the `x86_64` architecture. The following listing (Listing 3-1) gives examples of how to write tests for various architectures.

__Listing 3-1__  Architecture definition changes

```
#ifdef __ppc__
// 32-bit PowerPC code
#else
#ifdef __ppc64__
// 64-bit PowerPC code
#else
#if defined(__i386__) || defined(__x86_64__)
// 32-bit or 64-bit Intel code
#else
#error UNKNOWN ARCHITECTURE
#endif
#endif
#endif
```

Code that looks for only the `__ppc__` or `__i386__` definition will break if you compile for the related 64-bit architecture.

For code specific to OS X (non-cross-platform), the `TargetConditionals.h` header also provides macro support for architecture-specific code. For example:

```c
#include <TargetConditionals.h>

#if TARGET_RT_LITTLE_ENDIAN
    ...
#elif TARGET_RT_BIG_ENDIAN
    ...
#else
    #error Something is very wrong here.
#endif
```

__Avoid casting pointers to non pointers.__ You should generally avoid casting a pointer to a non-pointer type for any reason (particularly when performing address arithmetic). Alternatives are described in [Avoiding Pointer-to-Integer Conversion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsgywvgvzr).

__Update assembly code.__ Any assembly code needs to be rewritten because 64-bit Intel assembly language is significantly different from its 32-bit counterpart. For more information, see [Porting Assembly Language Code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsgywugqkdjjcueqkd).

Any assembly code that directly deals with the structure of the stack (as opposed to simply using pointers to variables on the stack) must be modified to work in a 64-bit environment. For more information, see _OS X ABI Mach-O File Format Reference_.

__Fix format strings.__ Print functions such as `printf` can be tricky when writing code to support 32-bit and 64-bit platforms because of the change in the sizes of pointers. To solve this problem for pointer-sized integers (`uintptr_t`) and other standard types, various macros exist in the `inttypes.h` header file.

The format strings for various data types are described in Table 3-1. These additional types, listed in the `inttypes.h` header file, are described in Table 3-2.

__Table 3-1__  Standard format strings

| Type | Format string |
| `int` | `%d` |
| `long` | `%ld` |
| `long long` | `%lld` |
| `size_t` | `%zu` |
| `ptrdiff_t` | `%td` |
| any pointer | `%p` |

__Table 3-2__  Additional `inttypes.h` format strings (where _N_ is some number)

| Type | Format string |
| `intN_t` (such as `int32_t`) | `PRIdN` |
| `uintN_t` | `PRIuN` |
| `int_leastN_t` | `PRIdLEASTN` |
| `uint_leastN_t` | `PRIuLEASTN` |
| `int_fastN_t` | `PRIdFASTN` |
| `uint_fastN_t` | `PRIuFASTN` |
| `intptr_t` | `PRIdPTR` |
| `uintptr_t` | `PRIuPTR` |
| `intmax_t` | `PRIdMAX` |
| `uintmax_t` | `PRIuMAX` |

For example, to print an `intptr_t` variable (a pointer-sized integer) and a pointer, you write code similar to that in Listing 3-2.

__Listing 3-2__  Architecture-independent printing

```c
#include <inttypes.h>
void *foo;
intptr_t k = (intptr_t) foo;
void *ptr = &k;

printf("The value of k is %" PRIdPTR "\n", k);
printf("The value of ptr is %p\n", ptr);
```


Here are a few tips to help you avoid problems stemming from changes to data type size and alignment.

__Be careful when mixing integers and long integers.__ The size and alignment of `long` integers and pointers have changed from 32-bit to 64-bit.

For the most part, if you always use the `sizeof` function when allocating data structures and avoid assigning pointers to non-pointer types, the size and alignment of pointers should not affect your code, because structures containing pointer members are generally not written to disk or sent across networks between 32-bit and 64-bit applications. This is something to consider when writing kernel extensions that read structures passed in from applications, however.

If you frequently move data between variables of type `int` and `long`, the change in the size of `long` can cause problems. You will see various related problems throughout this section.

__Be sure to control alignment of shared data.__ The alignment of `long long` (64-bit) integers has changed from 32-bit to 64-bit. This alignment change can pose a problem when you are exchanging data between 32-bit and 64-bit code.

In Listing 3-3, the alignment changes even though the data types are the same size.

__Listing 3-3__  Alignment of `long long` integers in structures

```
struct bar {
    int foo0;
    int foo1;
    int foo2;
    long long bar;
};
```

When this code is compiled with a 32-bit compiler, the variable `bar` begins 12 bytes from the start of the structure. When the same code is compiled with a 64-bit compiler, the variable `bar` begins 16 bytes from the start of the structure, and a 4-byte pad is added after `foo2`.

If you must maintain data structure compatibility, to allow a single data structure to be shared, you can use a pragma to force packed alignment mode for each structure, as needed. Then add appropriate pad bytes (if necessary) to obtain the desired alignment. An example is shown in Listing 3-4.

If backwards compatibility with existing structures is not important, you should reorder the data structure so that the largest fields are at the beginning of the structure. That way, the 8-byte fields begin at offset `0` and thus are aligned on 8-byte boundaries without the need to add an alignment pragma.

__Listing 3-4__  Using pragmas to control alignment

```
#pragma pack(4)
struct bar {
    int foo0;
    int foo1;
    int foo2;
    long long bar;
};
#pragma options align=reset
```

You should use this option only when absolutely necessary, because there is a performance penalty for misaligned accesses.

__Use sizeof with malloc.__ Since pointers and long integers are no longer 4 bytes long, never call [malloc](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/malloc.3.html#//apple_ref/doc/man/3/malloc) with an explicit size (for example, `malloc(4)`) to allocate space for them. Always use `sizeof` to obtain the correct size.

Never assume you know the size of any structure (containing a pointer or otherwise); always use `sizeof` to find out for sure. To avoid future portability problems, search your code for any instance of `malloc` that isn't followed by `sizeof`. The `grep` command and regular expressions are your friend, though using Find in the Xcode Edit menu can do the job.

__64-bit sizeof returns size_t.__ Note that `sizeof` returns an integer of type `size_t`. Because the size of `size_t` has changed to 64 bits, do not pass the value to a function in a parameter of size `int` (unless you are certain that the size cannot be that large). If you do, truncation will occur.

__Use explicit (fixed-width) C99 types.__ You should use explicit types where possible. For example, types with names like `int32_t` and `uint32_t` will always be a 32-bit quantity, regardless of future architectural changes.

| 32-bit type | Suggested C99 type |
| --- | --- |
| `char` or `unsigned char` (only when used as a one-byte integer) | `int8_t` or `uint8_t` |
| `short` or `unsigned short` | `int16_t` or `uint16_t` |
| `int` or `unsigned int` | `int32_t` or `uint32_t` |
| `long` or `unsigned long` | `int32_t` or `uint32_t` |
| `long long` or `unsigned long long` | `int64_t` or `uint64_t` |

__Watch for conversion errors.__ Conversion of shorter types to 64-bit longs may yield unexpected results in certain cases. Be sure to read [Sign Extension Rules for C and C-derived Languages](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsgywugsceizcuesse) if you are seeing unexpected values from math that mixes `int` and `long` variables.

__Use 64-bit types for pointer arithmetic results.__ Because the size of pointers is a 64-bit value, the result of pointer arithmetic is also a 64-bit value. You should always store these values in a variable of type `ptrdiff_t` to ensure that the variable is sized appropriately.

__Avoid truncating file positions and offsets.__ Although file operations have always used 64-bit positions and offsets, you should still check for errors in their use. Errors will become more and more important as common file sizes grow. Use `fpos_t` for file position and `off_t` for file offset.

__Be careful with variable argument lists.__ Variable argument lists (`varargs`) do not provide type information for the arguments, and the arguments are not promoted to larger types automatically. If you need to distinguish between different incoming data types, you are expected to use a format string or other similar mechanism to provide that information to the `varargs` function. If the calling function does not correctly provide that information (or if the `varargs` function does not interpret it correctly), you will get incorrect results.

In particular, if your `varargs` function expects a `long` type and you pass in a 32-bit value, the `varargs` function will contain 32 bits of data and 32 bits of garbage from the next argument (which you will lose as a result). Likewise, if your `varargs` function is expecting an `int` type and you pass in a `long`, you will get only half of the data, and the rest will incorrectly appear in the argument that follows.

For example, if you use incorrect [printf](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/printf.3.html#//apple_ref/doc/man/3/printf) format strings, you will get incorrect behavior. Some examples of these format string mistakes are shown in [General Programming Tips](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsgywvgvzx).

You should generally avoid casting a pointer to a non-pointer type for any reason. If possible, rewrite any code that uses these casts, either by changing the data types or by replacing address arithmetic with pointer arithmetic. For example, the following code:

```
int *c = something passed in as an argument....
int *d = (int *)((int)c + 4); // This code is WRONG!
```

results in pointer truncation. Because the resulting value would be correct for sufficiently small pointers, these bugs can be difficult to find. Instead, this code can be replaced with:

```
int *c = something passed in as an argument....
int *d = c + 1;
```

(Of course, this example is somewhat contrived, and such use of pointers is relatively uncommon.)

A more common problem is storing a pointer temporarily in a variable of type `int`. In most cases, the compiler will warn you that a pointer is being assigned to an integer of a different size. However, in a few cases, code containing such an assignment will compile without warning. For example, if the code stores the values in a variable of type `long` and then later copies it to an integer, the pointer itself is not _directly_ truncated, so the compiler may not generate a warning. These problems are particularly hard to spot.

Finally, a common problem is the need to offset a pointer by a specific number of bytes. Instead of casting to an integer and using integer math, you should cast the pointer to a byte-width pointer type such as `char *` or `uint8_t *`. After you do this, the pointer will behave like an integer for arithmetic purposes. For example:

```
int *myptr = getPointerFromSomewhere();
int *shiftbytwobytes = (int *)(((int)myptr) + 2);
```

can be rewritten as:

```
int *myptr = getPointerFromSomewhere();
int *shiftbytwobytes = (int *)(((char *)myptr) + 2);
```

By avoiding assignment of pointers to any non-pointer type, you avoid almost all pointer-related problems, because pointers are rarely stored or exchanged between 32-bit and 64-bit processes. In a few situations, however, there may be no easy way to avoid address-to-integer conversions. The `uintptr_t` type exists for these edge cases.

When working with bits and masks with 64-bit values, you must be careful to avoid getting 32-bit values inadvertently. Here are some tips to help you:

__Shift carefully.__ If you are shifting through the bits stored in a variable of type `long`, don’t assume that the variable is of a particular length. Instead, use the value `LONG_BIT` to determine the number of bits in a `long`. The result of a shift that exceeds the length of a variable is architecture-dependent.

__Use inverted masks if needed.__ Be careful when using bit masks with variables of type `long`, because the width differs between 32-bit and 64-bit architectures. There are two ways to create a mask, depending on whether you want the mask to be zero-extended or one-extended:

- If you want the mask value to contain zeros in the upper 32 bits on a 64-bit architecture, the usual fixed-width mask will work as expected, because it will be extended in an unsigned fashion to a 64-bit quantity.
- If you want the mask value to contain ones in the upper bits, however, you should write the mask as the bitwise inverse of its inverse, as shown in Listing 3-5.

__Listing 3-5__  Using an inverted mask for sign extension

```
function_name(long value)
{
    long mask = ~0x3; // 0xfffffffc or 0xfffffffffffffffc
    return (value & mask);
}
```

In the code, note that the upper bits in the mask are filled with ones in the 64-bit case.

Here are some tips to help you use the compiler more effectively in transitioning your code to 64-bit:

- If data is being inadvertently truncated, to help you find the source, try turning on additional compiler warnings.
- In 64-bit-capable versions of GCC (4.0 and later), the size of a `long double` will be 128 bits instead of 64 bits. This change is not limited to code compiled as a 64-bit executable, but it is a toolchain change you should be aware of.

You can find detailed tips and information about 64-bit tools changes in [Compiling 64-Bit Code](Compiling%2064-Bit%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrqhawviucykjcummjqge).

Occasionally, developers use alignment pragmas to change the way that data structures are laid out in memory. They usually do this for backward compatibility. In many cases, Apple added pragmas to maintain data structure compatibility between 68K-based and PowerPC-based code running on the same machine under Mac OS 9 and earlier. OS X retained these alignment overrides to maintain binary compatibility with existing Carbon data structures between Mac OS 9 and OS X.

There is a performance cost associated with pragmas, however; memory accesses to unaligned data fields result in a performance penalty. Because there are no existing 64-bit OS X GUI applications with which to be compatible, it is not necessary to preserve binary compatibility for these data structures in 64-bit applications. Thus, to improve overall performance, when compiling 64-bit executables, the OS X version of GCC ignores requests for `mac68k` alignment.

If you are using this pragma only to access Apple data structures, you should not need to make any code changes to your code. When compiling 64-bit code, the compiler ignores the pragmas and your code works correctly. If, however, you currently use the `mac68k` alignment pragma in your own data structures that will be shared between 32-bit and 64-bit versions of your application (or if you use the `mac68k` pragma for a data structure that corresponds with the register layout of a physical device), you must rewrite the data structure to use a packed alignment and pad the structure appropriately.

With the exception of Altivec data types, the following code is equivalent to `mac68k` alignment:

```
#pragma pack(2)
...structure declaration goes here...
#pragma options align=reset
```

Similarly, with the exception of some vector data types, the following code is equivalent to the standard 32-bit alignment:

```
#pragma pack(4)
...structure declaration goes here...
#pragma options align=reset
```


C and similar languages use a set of sign extension rules to determine whether to treat the top bit in an integer as a sign bit when the value is assigned to a variable of larger width. The sign extension rules are as follows:

1. The sum of a signed value and an unsigned value of the same size is an unsigned value.
2. Any promotion always results in a signed type unless a signed type cannot hold all values of the original type (that is, unless the resulting type is the same size as the original type).
3. Unsigned values are zero extended (not sign extended) when promoted to a larger type.
4. Signed values are always sign extended when promoted to a larger type, even if the resulting type is unsigned.
5. Constants (unless modified by a suffix, such as `0x8L`) are treated as the smallest size that will hold the value. Numbers written in hexadecimal may be treated by the compiler as `signed` and `unsigned`  `int`, `long`, and `long long` types. Decimal numbers will always be treated as `signed` types.

Listing 3-6 shows an example of unexpected behavior resulting from these rules along with an accompanying explanation.

__Listing 3-6__  Sign extension example 1

```
int a=-2;
unsigned int b=1;
long c = a + b;
long long d=c; // to get a consistent size for printing.

printf("%lld\n", d);
```

_Problem:_ When this code is executed on a 32-bit architecture, the result is `-1` (`0xffffffff`). When the code is run on a 64-bit architecture, the result is `4294967295` (`0x00000000ffffffff`), which is probably not what you were expecting.

_Cause:_ Why does this happen? First, the two numbers are added. A signed value plus an unsigned value results in an unsigned value _(rule 1)_. Next, that value is promoted to a larger type. This promotion does not cause sign extension _(rule 2)_.

_Solution:_ To fix this problem in a 32-bit-compatible way, cast `b` to `long`. This cast forces the non-sign-extended promotion of `b` to a 64-bit type prior to the addition, thus forcing the signed integer to be promoted (in a signed fashion) to match. With that change, the result is the expected `-1`.

Listing 3-7 shows a related example with an accompanying explanation.

__Listing 3-7__  Sign extension example 2

```
unsigned short a=1;
unsigned long b = (a << 31);
unsigned long long c=b;

printf("%llx\n", c);
```

_Problem:_ The expected result (and the result from a 32-bit executable) is `0x80000000`. The result generated by a 64-bit executable, however, is `0xffffffff80000000`.

_Cause:_ Why is this sign extended? First, when the shift operator is invoked, the variable `a` is promoted to a variable of type `int`. Because all values of a `short` can fit into a signed `int`, the result of this promotion is signed _(rule 3)_.

Second when the shift completed, the result was stored into a `long`. Thus, the 32-bit signed value represented by `(a << 31)` was sign extended _(rule 4)_ when it was promoted to a 64-bit value (even though the resulting type is unsigned).

_Solution:_ To fix this problem, you should cast the initial value to a `long` prior to the shift. Thus, the short will be promoted only once—this time, to a 64-bit type (at least when compiled as a 64-bit executable).

Although the SSE and Velocity Engine C and assembly language interfaces have not changed for 64-bit, if you are using these technologies, you should review any code that attempts to align pointers to 16-byte addresses for processing.

For example, the following code contains two errors:

```
TYPE *aligned = (TYPE *) ((int) misalignedPtr & 0xFFFFFFF0); // BAD!
```

First, the pointer is cast to an `int` value, which results in truncation. Even after this problem is fixed, however, the pointer will still be truncated because the constant value `0xFFFFFFF0` is not a 64-bit value.

Instead, this code should be written as:

```c
#include <stdint.h>
TYPE *aligned = (TYPE *) ((intptr_t) misalignedPtr & ~(intptr_t)0xF);
```


This section describes some of the issues involved in porting assembly language code to a 64-bit application. On the Intel architecture, in addition to the issues described in this section, you must considerably modify any assembly language code that deals with the stack directly, because the 64-bit ABI differs significantly from the 32-bit ABI. The subject of stack frames is beyond the scope of this section. For more information, see _OS X ABI Mach-O File Format Reference_.

On Intel-based Macintosh computers, 64-bit code uses the Intel 64 (formerly EM64T) extensions to the Intel assembly language ISA. This section summarizes the differences between Intel 64 code and IA32 code in terms of their impact on registers and instruction sets.

The 64-bit registers on Intel have different names than their 32-bit counterparts do. In addition, there are more of them. These register names are listed in Table 3-3.

__Table 3-3__  Register naming on 32-bit and 64-bit Intel architectures

| IA32 32-bit register | Intel 64 Architecture 64-bit variant | Description |
| `EIP` | `RIP` | Instruction Pointer |
| `EAX` | `RAX` | General Purpose Register A |
| `EBX` | `RBX` | General Purpose Register B |
| `ECX` | `RCX` | General Purpose Register C |
| `EDX` | `RDX` | General Purpose Register D |
| `ESP` | `RSP` | Stack Pointer |
| `EBP` | `RBP` | Frame Pointer |
| `ESI` | `RSI` | Source Index Register |
| `EDI` | `RDI` | Destination Index Register |
| ---- | `R8` \* | Register 8 (new) |
| ---- | `R9` \* | Register 9 (new) |
| ---- | `R10` \* | Register 10 (new) |
| ---- | `R11` \* | Register 11 (new) |
| ---- | `R12` \* | Register 12 (new) |
| ---- | `R13` \* | Register 13 (new) |
| ---- | `R14` \* | Register 14 (new) |
| ---- | `R15` \* | Register 15 (new) |

All of the new registers (`R8` through `R15`) added in the Intel 64 architecture instruction set can also be accessed as 32-bit, 16-bit, and 8-bit registers. For example, register `R8` can be addressed in the following ways:

| Register name | Description |
| --- | --- |
| `R8` | A 64-bit register. |
| `R8d` | A 32-bit register containing the bottom half of `R8`. |
| `R8w` | A 16-bit register containing the bottom half of `R8d`. |
| `R8l` (Lowercase “l”) | An 8-bit register containing the bottom half of `R8w`. |

In addition to adding general-purpose registers, the Intel 64 Architecture instruction set has eight additional vector registers. In the IA32 instruction set, the vector registers are numbered `XMM0` through `XMM7`. The Intel 64 Architecture instruction set extends this by adding `XMM8` through `XMM15`.

Most IA32 instructions can take 64-bit arguments. All IA32 instruction set extensions up through SSE3 are included as part of the Intel 64 Architecture. In addition, a number of new instructions have been added.

A complete list of these changes is beyond the scope of this document. For information on these changes, see the links in [For More Information](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsgywvgvzw).

For more information on porting and optimizing Intel assembly language code for 64-bit, you should also read:

- _OS X ABI Mach-O File Format Reference_—ABI documentation for OS X.
- [http://developer.intel.com/technology/intel64/index.htm](http://developer.intel.com/technology/intel64/index.htm)—Intel 64 Architecture technology page (Intel).
- [http://software.intel.com/en-us/parallel/](http://software.intel.com/en-us/parallel/)—Intel multicore programming documentation site (Intel).
- [http://software.intel.com/en-us/articles/porting-to-64-bit-intel-architecture/](http://software.intel.com/en-us/articles/porting-to-64-bit-intel-architecture/)—Porting to 64-bit Intel architecture (Intel).
- [http://software.intel.com/en-us/articles/porting-code-to-intel-em64t-based-platforms/](http://software.intel.com/en-us/articles/porting-code-to-intel-em64t-based-platforms/)—Information about 64-bit optimization. Note that the ABI information at this location is Windows oriented, so those portions do not apply.
- [http://www.x86-64.org/documentation/assembly.html](http://www.x86-64.org/documentation/assembly.html)—General information on 64-bit Intel assembly (x86-64.org).

[Next](Compiling%2064-Bit%20Code.md)[Previous](Major%2064-Bit%20Changes.md)

