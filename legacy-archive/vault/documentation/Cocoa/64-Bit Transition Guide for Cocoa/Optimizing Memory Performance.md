---
title: 64-Bit Transition Guide for Cocoa
apple_id: TP40004247
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Cocoa64BitGuide/OptimizingMemoryPerformance/OptimizingMemoryPerformance.html
archived_at: '2026-07-15T07:11:59.032952Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [64-Bit Transition Guide for Cocoa](Introduction%20to%2064-Bit%20Transition%20Guide%20For%20Cocoa.md)


[Next](Document%20Revision%20History.md)[Previous](Converting%20an%20Existing%20Application%20to%2064-Bit.md)

# Optimizing Memory Performance

64-bit applications have the potential to perform faster than 32-bit applications due to improvements in modern 64-bit processors. However, 64-bit environments increase the size of pointers and some scalar data, resulting in a larger memory footprint for your application. A larger memory footprint results in increased pressure on processor caches and virtual memory and can adversely affect performance. When developing a 64-bit application, it is critical to profile and optimize your application’s memory usage.

For a comprehensive discussion on optimizing memory usage, see the _[Memory Usage Performance Guidelines](../../Performance/Memory%20Usage%20Performance%20Guidelines/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3da2i)_.

Before attempting to optimize your application’s memory usage, you should first create standard tests that you can run against both the 32-bit and 64-bit versions of your application. Standardized tests allow you to measure the penalty for compiling a 64-bit version of your application when compared to the 32-bit version. It also provides a way to measure improvements as you optimize your application’s memory usage. At least one test should use a minimal footprint (e.g. the application has just been opened and shows an empty document). Other tests should include a variety of different data sizes, including at least one test with a very large data set. A complex application may require tests that cover subsets of its features. The goal for these additional tests is to measure whether the memory usage changes significantly as the type or amount of data changes. If a particular kind of data causes the 64-bit version of your application to use dramatically more memory than its 32-bit counterpart, that is a great place to start looking for improvements.

While both the stack and heap usage increases on 64-bit applications, we recommend you focus your efforts on reducing your application’s heap usage; heap usage will typically be much greater than your stack usage. The `heap` tool can be used to discover how much memory your application has allocated on the heap. The `heap` tool will also tell you how many objects of each class that your application has allocated, and the total usage for each class. Focus your efforts on the classes that use the most memory. As in most performance tuning, often a small number of optimizations will result in significant improvements.

OS X v10.6 offers a new tool, `heapdiff` that can generate a report highlighting the differences between two `heap` reports. Although you can use it to compare any two heap reports, the most common use for `heapdiff` is to compare the memory usage of the same scenario on both the 32-bit and 64-bit versions of your application.

To generate a `heapdiff` report, follow the following steps.

1. Identify a memory scenario you want to profile, as described above.
2. Run the 32-bit version of your application and execute your test.
3. Run `heap` to generate a report for the 32-bit version of your application and save it as a text file.

```
sudo heap -sumObjectFields <application name> > test32.txt
```
4. Repeat steps 2 and 3 using the 64-bit version of your application.

```
sudo heap -sumObjectFields <application name> > test64.txt
```
5. Run `heapdiff` to generate and open the report.

```
/Developer/usr/bin/heapdiff.pl test32.txt test64.txt
```

The `heapdiff` report compares the number of objects and total memory allocated for each class, highlighting the differences in memory usage between the two heap reports. Additionally, the report also provides the ratio of memory used in the two reports, highlighting the expansion of each class’s memory usage after compiling your application for 64-bit.

While the html report is the most human readable form, `heapdiff` also offers additional data formats that are more easily processed by a computer, in case you wish to generate your own data reports. Consult `heapdiff`'s help for more information on list of formats.

It is crucial to understand the behavior of `malloc` when you are developing a 64-bit version of your application. In addition to calling `malloc` directly, all objective-C objects are allocated using `malloc`.

Small allocations (less than 512 bytes) are rounded to the next largest multiple of 16 bytes. For example, assume your used the following struct:

```
struct node
{
    node        *previous;
    node        *next;
    uint32_t    value;
};
```

When this structure is compiled for a 32-bit environment, it uses 12 bytes of storage; `malloc` actually allocates 16 bytes. But in a 64-bit environment, this structure takes up 20 bytes, and `malloc` allocates 32! An application that allocates many such nodes would waste a significant amount of memory.

Larger allocations are even more critical. If `malloc` is called to allocate a block larger than 512 bytes, it will round to the next highest multiple of 512 and allocate that much memory. Be particularly cautious with classes or structures that are above 256 bytes of memory in a 32-bit environment. If the process of converting a structure to 64-bit results in something that is just over 512 bytes in size, your application won’t be using twice as much memory, but almost _four_ times as much — most of it wasted.

The `ConvertCocoa64` script described in [Converting an Existing Application to 64-Bit](Converting%20an%20Existing%20Application%20to%2064-Bit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denbxfvbuqnjnknltc) converts most instances of `int` and `unsigned int` to [NSInteger](https://developer.apple.com/documentation/objectivec/nsinteger) and [NSUInteger](https://developer.apple.com/documentation/objectivec/nsuinteger). [NSInteger](https://developer.apple.com/documentation/objectivec/nsinteger) is a 64-bit integer on 64-bit applications, doubling the storage required, but dramatically increasing the range of values.

| Type | Range |
| --- | --- |
| int | -2,147,483,648 to 2,147,483,647 |
| NSInteger | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |

In most cases, your application will not need this larger range of values. Our recommendation is to choose a C99 representation that accurately reflects the range of values your application requires.

| Type | Range |
| --- | --- |
| int8_t | -128 to 127 |
| int16_t | -32,768 to 32,767 |
| int32_t | -2,147,483,648 to 2,147,483,647 |
| int64_t | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| uint8_t | 0 to 255 |
| uint16_t | 0 to 65,535 |
| uint32_t | 0 to 4,294,967,295 |
| uint64_t | 0 to 18,446,744,073,709,551,615 |

Look for situations where you can choose a stronger data representation. For example, assume we stored a calendar date using the following data structure:

```
struct date
{
    int second;
    int minute;
    int hour;
    int day;
    int month;
    int year;
};
```

This structure is 24 bytes long, and when converted to use [NSInteger](https://developer.apple.com/documentation/objectivec/nsinteger), it would take 48 bytes, just for a date! A more compact representation would be to simply store the number of seconds, and convert these as necessary.

```
struct date
{
    uint32_t seconds;
};
```


For performance reasons, compilers typically pad fields of a structure so that they can be quickly accessed. For example, take a look at the following struct:

```
struct bad
{
    char       a;        // offset 0
    int32_t    b;        // offset 4
    char       c;        // offset 8
    int64_t    d;        // offset 16
};
```

While the structure only uses 14 bytes of data, because of padding, it takes up 24 bytes of space. If this structure were allocated using `malloc`, it would take 32 bytes; more space wasted than used for the data.

A better design would be to sort the fields from largest to smallest.

```
struct good
{
    int64_t    d;        // offset 0
    int32_t    b;        // offset 8
    char       a;        // offset 12;
    char       c;        // offset 13;
};
```

Now the structure doesn’t waste any space.

Avoid overusing pointers in code. Let’s look at a previous example again.

```
struct node
{
    node        *previous;
    node        *next;
    uint32_t    value;
};
```

Only one-third of the memory used is payload; the rest is used for linking. If we compile that same structure into a 64-bit application, the links alone are 80% of the total memory used.

For complex data types that fit within a known data size, you may want to replace pointers with an index instead. For example, if we knew that there would never be more than 65535 nodes in the linked list, we could instead use the following definition instead.

```
struct indexed_node
{
    uint32_t    value;
    uint16_t    next;
    uint16_t    previous;
};
node *nodeList; // pointer to an array of nodes;
```

Using a linked list built around indices, we use significantly less space for links compared to our data. More importantly this example only uses a single pointer. When converted from 32-bit to 64-bit, this example only uses four additional bytes, regardless of the size of the list.

Caching previously calculated results is a common way to improve an application’s performance. However, it is worth investigating whether caching is really helping your application. As the previous examples have shown, memory usage is much higher on 64-bit systems. If your application relies too much on caching, the pressure it puts on the virtual memory system may actually result in worse performance.

Typical examples of behaviors to avoid include:

- Caching any data that a class can cheaply recompute on the fly.
- Caching data or objects that you can easily obtain from another object.
- Caching system objects that are inexpensive to recreate.

Always test to ensure that caching improves the performance of your application. We recommend building hooks into your application that allow you to selectively disable caching. You can test whether disabling a particular cache has a significant effect on the memory usage or the performance of your application. This is a good place to test different memory usage scenarios.

Many Cocoa classes offer a flexible feature set, but to do that, they use more memory than a simpler data structure may provide. For example, if you are using an [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) object to hold a single key-value pair, this is significantly more expensive than simply allocating a variable to hold that information. Creating thousands of such dictionaries wastes memory.

[Next](Document%20Revision%20History.md)[Previous](Converting%20an%20Existing%20Application%20to%2064-Bit.md)

