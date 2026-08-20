---
title: Universal Binary Programming Guidelines, Second Edition
apple_id: TP40002217
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/universal_binary/universal_binary_diffs/universal_binary_diffs.html
archived_at: '2026-07-15T08:16:36.677366Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Universal Binary Programming Guidelines, Second Edition](Introduction.md)


[Next](Swapping%20Bytes.md)[Previous](Building%20a%20Universal%20Binary.md)

# Architectural Differences

The PowerPC and the x86 architectures have some fundamental differences that can prevent code written for one architecture from running properly on the other architecture. The extent to which you need to change your PowerPC code so that it runs natively on an Intel-based Macintosh computer depends on how much of your code is processor specific. This chapter describes the major differences between architectures, organized alphabetically by topic. You can use the information to identify the parts of your code that are likely to be problematic.

All PowerPC instructions are 4 bytes in size and must be 4-byte aligned. x86 instructions are variable in size (from 1 to >10 bytes), and as a consequence do not need to be aligned.

The value of a signed, 1-bit bit field is either `0`, `1`, or `–1`, depending on the compiler, architecture, optimization level, and so forth. Code that compares the value of a bit field to 1 may not work if the bit field is signed, so you will want to use unsigned 1-bit bit fields. Keep in mind that the order of bit fields in memory can be reversed between architectures.

For more information on issues related to endian format, see [Swapping Bytes](Swapping%20Bytes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugmwviucykjcummjqge). See also [Archived Bit Fields](Guidelines%20for%20Specific%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrthewteojrha3di) and [Structures and Unions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugawteobsg42ti).

Microprocessor architectures commonly use two different byte-ordering methods (little-endian and big-endian) to store the individual bytes of multibyte data formats in memory. This difference becomes critically important if you try to read data from files that were created on a computer that uses a different byte ordering than yours. You also need to consider byte ordering when you send and receive data through a network connection and handle networking data. The difference in byte ordering can produce incorrect results if you do not account for this difference. For example, the order of bytes in memory of a scalar type is architecture-dependent, as shown in [Listing 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugawteobsga2te).

__Listing 2-1__  Code that illustrates byte-ordering differences

```
unsigned char charVal;
unsigned long value = 0x12345678;
unsigned long *ptr = &value;
charVal = *(unsigned char*)ptr;
```

On a processor that uses little-endian addressing the variable `charVal` takes on the value 0x78. On a processor that uses big-endian addressing the variable `charVal` takes on the value 0x12. To make this code architecture-independent, change the last line in Listing 2-1 to the following:

`charVal = (unsigned char)*ptr;`

For a detailed discussion of byte ordering and strategies that you can use to account for byte-ordering differences, see [Swapping Bytes](Swapping%20Bytes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugmwviucykjcummjqge).

The x86 C-language calling convention (application binary interface, or ABI) specifies that arguments to functions are passed on the stack. The PowerPC ABI specifies that arguments to functions are passed in registers. Also, x86 has far fewer registers, so many local variables use the stack for their storage. Thus, programming errors, or other operations that access past the end of a local variable array or otherwise incorrectly manipulate values on the stack may be more likely to crash applications on x86 systems than on PowerPC.

For detailed information about the IA-32 ABI, see _[OS X ABI Function Call Guide](../../Developer%20Tools/OS%20X%20ABI%20Function%20Call%20Guide/Introduction%20to%20OS%20X%20ABI%20Function%20Call%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkmrr)_. This document describes the function-calling conventions used in all the architectures supported by Mac OS X. See also [32-Bit Application Binary Interface](32-Bit%20Application%20Binary%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugywviucykjcummjqge).

Intel processors include a bit that prevents code from being executed on the stack. On Intel-based Macintosh computers, this bit is always set to `On`.

For some data type conversions, such as casting a string to a long and converting a floating-point type to an integer type, the PowerPC and x86 architectures perform differently. When the microprocessor converts a floating-point type to an integer type, it discards the fractional part of the value. The behavior is undefined if the value of the integral part cannot be represented by the integer type.

Listing 2-2 shows an example of the sort of code that is architecture-dependent. You would need to modify this code to make it architecture-independent. On a PowerPC microprocessor, the variable `x` shown in the listing is equal to `7fffffff` or `INTMAX`. On an x86 microprocessor, the variable `x` is equal to `80000000` or `INTMIN`.

__Listing 2-2__  Architecture-dependent code

```
int main (int argc, const char * argv[])
{
    double  a;
    int     x;

    a = 5000000.0 * 6709000.5;  // or any really big value
    x = a;
    printf("x = %08x \n",x);
    return 0;
}
```


A `long double` is 16 bytes on both architectures, but only 80 bits are significant in `long double` data types on Intel-based Macintosh computers.

A `bool` data type is a single byte on an x86 system, but four bytes on a PowerPC architecture. This size difference can cause alignment problems. You should use fixed-size data types to avoid alignment problems. (The `bool` data type is not the Carbon `Boolean` type, which is a fixed size of 1 byte.)

Existing document formats that include the `bool` data type as part of a data structure that is written directly to disk can be problematic because the data structure might not be laid out the same on both architectures. If you update the data structure definition to use the `UInt32` data type or another fixed-size four-byte data type, the structure should then be portable, although you must swap bytes appropriately.

An integer divide-by-zero operation is fatal on an x86 system but the operation continues on a PowerPC system, where it returns zero. (A floating point divide-by-zero behaves the same on both architectures.) If you get a crash log that mentions `EXC_I386_DIV (divide by zero)`, your program divided by zero. Mod operations perform a divide, so a mod-by-zero operation produces a divide-by-zero exception. To fix a divide-by-zero exception, find the place in your program corresponding to that operation. Then add code that checks for a denominator of zero before performing the divide operation.

For example, change this:

```
 int a = b % c;    // Divide by zero can happen here;
```

to this:

```
int a;
if (c != 0) {
     a = b % c;
 } else {
     a = 0;
}
```


Intel-based Macintosh computers use extensible firmware interface (EFI). EFI provides a flexible and adaptable interface between Mac OS X and the platform firmware. This change should be transparent to most developers, but may affect some, such as those who write boot drivers.

For more information on the EFI specification, see [http://www.intel.com/technology/efi/](http://www.intel.com/technology/efi/)

The results of a floating-point equality comparison are architecture-dependent. Whether the comparison works depends on a number of things, including the compiler, the surrounding code, all compiler flags in use (particularly optimization flags), and the current floating-point mode for the thread. If your floating-point comparison is currently working on PowerPC, you may need to inspect it on an Intel-based Macintosh computer.

You can use the GCC flag `-Wfloat-equal` to receive a warning for floating-point equality comparisons. For details on this option, see Section 3.8 of the _GNU C/C++/Objective-C 4.0.1 Compiler User Guide_

The fields in a structure can be sensitive to their defined order. Structures must either be properly ordered or accessed by the field name directly.

When a union has components that could be affected by byte order, use a form similar to that shown in Listing 2-3. Code that sets `wch` and then reads `hi` and `lo` as the high and low bytes of `wch` will work correctly. The same is true for the reverse direction. Code that sets `hi` and `lo` and then reads `wch` will get the same value on both architectures. For another example, see the `WideChar` union that’s defined in the `IntlResources.h` header file.

__Listing 2-3__  A union whose components can be affected by byte order

```
union WChar{
    unsigned short wch;
    struct {
#if __BIG_ENDIAN__
        unsigned char hi;
        unsigned char lo;
#else
        unsigned char lo;
        unsigned char hi;
#endif
    } s;
}
```


The ISO standard for the C programming language—ISO/IEC 9899—is a valuable reference that you can use to investigate code portability issues, many of which may not be immediately obvious. You can find this reference in a number of locations on the web, including:

[http://www.iso.org/](http://www.iso.org/)

[Next](Swapping%20Bytes.md)[Previous](Building%20a%20Universal%20Binary.md)

