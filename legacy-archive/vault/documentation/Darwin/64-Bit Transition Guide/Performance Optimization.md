---
title: 64-Bit Transition Guide
apple_id: TP40001064
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/64bitPorting/PerformanceOptimization/PerformanceOptimization.html
archived_at: '2026-07-15T07:23:04.083984Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [64-Bit Transition Guide](Introduction%20to%2064-Bit%20Transition%20Guide.md)


[Next](Kernel%20Extensions%20and%20Drivers.md)[Previous](Cross-Architecture%20Plug-in%20Support.md)

# Performance Optimization

When transitioning your application, kernel extension, or other code to 64-bit, you may notice a performance decrease, depending on your code. While in some cases this is caused by simply moving more data around, in many cases, it is caused by fairly minor data structure layout issues and other easily corrected issues. This chapter briefly describes some of these issues and explains how to correct them.

Software compiled as a 64-bit executable is likely to use more memory than its 32-bit counterpart because of the increased size of data and pointers. However, many of these increases are exacerbated by changes in data alignment. Such increases, which can affect performance, are easily avoided.

As noted in [Data Type and Alignment Tips](Making%20Code%2064-Bit%20Clean.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrsgywvgvzy), data structure alignment is different for 64-bit executables. The following snippet shows a small data structure:

```
struct mystruct {
    char member_one[4];
    void *member_two;
    int member_three;
    void *member_four;
    int member_five;
}
```

In a 32-bit executable, this data structure takes 20 bytes. The pointers are 4 bytes long, and are aligned on a 4-byte boundary. If the structure is allocated dynamically, even though you only request 20 bytes, the memory allocator will actually assign it a memory region that is 32 bytes long (the nearest power-of-2 boundary).

In a 64-bit executable, this data structure bloats to a whopping 36 bytes and is padded to 40 bytes (because it must be 8-byte-aligned), which means that if allocated dynamically, it occupies 64 bytes.

To explain why, assume that the variable starts at address zero (0). The variable `member_one` takes 4 bytes, so the next member would normally start at byte 4.

Because `member_two` is a pointer, it must be aligned on an 8-byte boundary. Thus, its address must be divisible by 8. Because 4 is not divisible by 8, the structure must be padded. The result is a 4-byte gap between `member_one` and `member_two`.

The variable `member_three` is not a problem—it needs to be aligned at a 4-byte boundary and would normally begin at offset 16, so it does not generate a gap.

The variable `member_four`, however, must be aligned at an 8-byte boundary. The compiler generates another 4-byte gap, and this variable begins at offset 24. Finally, the variable `member_five` begins at offset 32 and ends at offset 36.

Fortunately, by making small changes to the order of the structure members, you can reduce the size increase dramatically:

```
struct mystruct {
    char member_one[4];
    int member_three;
    void *member_two;
    void *member_four;
    int member_five;
}
```

By shifting the third member up before the second member, the variables `member_two` and `member_three` now naturally fall on 8-byte boundaries. As a result, this structure is reduced to a mere 28 bytes, and is padded to 32 bytes by the compiler to make it 8-byte aligned. It also takes the same 32-byte dynamic memory allocation as it did in the 32-bit version of the code.

The easiest way to guarantee maximum data structure efficiency is to start with the members aligned to the largest byte boundary and work your way down to the members aligned to the smallest. Place the 8-byte-aligned `long` and `pointer` members first, followed by 4-byte-aligned `int` values, followed by two-byte-aligned `short` values, and finally end with byte-aligned `char` values.

```
struct mystruct {
    void *member_two;
    void *member_four;
    int member_five;
    int member_three;
    char member_one[4];
}
```


Changes in data structure alignment can cause differences in cache-line hits and misses. While this usually does not have a significant impact on performance, in certain degenerate cases it can have a devastating impact. Consider the following code:

```
for (i=0; i<columns; i++) {
    for (j=i; j<rows; j++) {
        arr[j][i] = ...
    }
}
```

This code performs a series of operations on an array. However, it iterates through the array in a fairly inefficient way. C stores arrays in row-major order, but this code iterates in a fashion more appropriate for a column-major array—iterating through the first entry in each row, then the second entry in each row, and so on.

If you are particularly unlucky and your stride length is on the same order as the length of a cache line (or longer), you could easily find that every few accesses, you end up invalidating a cache line containing a previously used data row that you will use again on the next pass through the loop. As a result, the CPU cache fails to boost performance.

Where this often comes back to hurt 64-bit application performance is when the size of data structure members changes to be just slightly larger so that the entire data structure no longer fits within the number of cache lines available, and thus on that last row, the first cache line is invalidated, wiping out the cache for the first row. Then, the first row is processed a second time, invalidating the cache for the next row, and so on.

To fix this performance regression, change the code to iterate through the array in the opposite order so that you perform numerous accesses within each row. With that change, most of the accesses within a given row are serviced out of the cache, and you should see a tremendous performance benefit. (In many cases, you may also see some benefit even in the 32-bit version of your application.)

Once you have determined that this is the source of your problems, you should do whatever you can do reduce the cache collisions by reducing the size of the data structures themselves, reducing your stride length when iterating through arrays, or reorganizing your in-memory data structures in a way that increases temporal locality of reference.

If you create data structures with packed alignment, you may see a performance regression caused by unaligned access penalties. For example:

```
#pragma pack(1)
typedef struct
{
        long a;
        int b;
        int b1;
        int b2;
        long double c;
} myStruct;
#pragma options align=reset
```

Ideally, the variable `c` should be aligned on a 16-byte boundary. In a 32-bit environment, it ends up aligned correctly because the variable `a` is 4 bytes long. In a 64-bit environment, this variable ends up offset by 4 bytes from its ideal position because the variable `a` is 8 bytes long.

While a single unaligned access penalty is relatively small, the cumulative effects can be significant. Given a loop that assigns the value zero (`0`) repeatedly to variables `a`, `b`, and `c`, you can improve performance of the loop by more than 20% by simply moving the variable `b2` after the variable `c`. Of course, this wrecks performance in the 32-bit version because variable `c` is then unaligned.

The best solution is to not use packing pragmas except when working with data structures that mandate it (structures that represent hardware registers or are intended to be written to a file, sent across a network connection, shared across address space boundaries, and so on) and let the compiler use natural alignment for all data structures that you work with on a regular basis in your software.

For maximum efficiency, you should also reorder this structure to place the variable `c` first, followed by the variable `a`, followed by the remaining variables (in order from largest alignment size to smallest). This achieves optimal packing efficiency while avoiding alignment penalties regardless of CPU architecture and often obviates the need for packing pragmas.

[Next](Kernel%20Extensions%20and%20Drivers.md)[Previous](Cross-Architecture%20Plug-in%20Support.md)

