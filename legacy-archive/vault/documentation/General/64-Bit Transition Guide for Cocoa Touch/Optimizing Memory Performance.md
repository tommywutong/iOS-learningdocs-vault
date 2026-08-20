---
title: 64-Bit Transition Guide for Cocoa Touch
apple_id: TP40013501
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaTouch64BitGuide/OptimizingMemoryPerformance/OptimizingMemoryPerformance.html
archived_at: '2026-07-27T06:57:08.826079Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [64-Bit Transition Guide for Cocoa Touch](About%2064-Bit%20Cocoa%20Touch%20Apps.md)


[Next](Document%20Revision%20History.md)[Previous](Converting%20Your%20App%20to%20a%2064-Bit%20Binary.md)

# Optimizing Memory Performance

Because of improvements in 64-bit processors, 64-bit apps have the potential to perform faster than 32-bit apps. At the same time, the 64-bit runtime increases the size of pointers and some scalar data, resulting in a larger memory footprint for your app. A larger memory footprint results in increased pressure on processor caches and virtual memory and can adversely affect performance. When developing a 64-bit app, it is critical to profile and optimize your app’s memory usage.

For a comprehensive discussion on optimizing memory usage, see _[Memory Usage Performance Guidelines](../../Performance/Memory%20Usage%20Performance%20Guidelines/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3da2i)_.

## Profile Your App

Before attempting to optimize your app’s memory usage, you should first create standard tests that you can run against both the 32-bit and 64-bit versions of your app. Standardized tests can measure the penalty for compiling a 64-bit version of your app when compared with the 32-bit version. It also provides a way to measure improvements as you optimize your app’s memory usage. For at least one test, use a minimal footprint—for example, the app has just been opened and shows an empty document. For other tests, include a variety of data sizes, including at least one test with a very large data set. (A complex app may require multiple sets of test data, each covering a subset of the app’s features.) The goal for these tests is to measure whether the memory usage varies as the type or amount of data changes. If a particular kind of data causes the 64-bit version of your app to use dramatically more memory than its 32-bit counterpart, that is a great place to start looking for improvements.

## Common Memory Usage Problems

The potential memory usage problems you may encounter are organized here, along with some guidance for handling them.

### Foundation Objects May Be Expensive for Small Payloads

Many classes in Foundation offer a flexible feature set, but to provide that flexibility, they use more memory than a simpler data structure. For example, using an [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) object to hold a single key-value pair is significantly more expensive than simply allocating a variable to hold the data. Creating thousands of such dictionaries wastes memory. Using Foundation objects when it isn’t appropriate isn’t a new problem, but when running in the 64-bit runtime, those objects use even more memory.

### Choose a Compact Data Representation

Find places where you can use a better data representation than you have. For example, you are storing a calendar date using the following data structure:

```swift
struct date
{
    NSInteger second;
    NSInteger minute;
    NSInteger hour;
    NSInteger day;
    NSInteger month;
    NSInteger year;
};
```

This structure is 24 bytes long; in the 64-bit runtime, it takes 48 bytes, just for a date! A more compact representation simply stores the number of seconds since a particular time, such as the `time_t` data type used by ANSI C. When necessary, you convert this compact representation to the calendar date and time.

```swift
struct date
{
    time_t seconds;
};
```

Note that the `time_t` data type changes size when your app is compiled for the 64-bit runtime.

### Pack Data Structures

To align data structures, compilers sometimes add padding to a structure. For example:

```swift
struct bad
{
    char       a;        // offset 0
    int32_t    b;        // offset 4
    char       c;        // offset 8
    int64_t    d;        // offset 16
};
```

This structure includes 14 bytes of data, but because of padding, it takes up 24 bytes of space.

A better design sorts the fields from largest to smallest alignment.

```swift
struct good
{
    int64_t    d;        // offset 0
    int32_t    b;        // offset 8
    char       a;        // offset 12;
    char       c;        // offset 13;
};
```

This version adds no additional padding.

### Use Fewer Pointers

Avoid overusing pointers in code. Consider the following data structure:

```swift
struct node
{
    node        *previous;
    node        *next;
    uint32_t    value;
};
```

When this structure is compiled for the 32-bit runtime, only 4 bytes out of 12 are used as payload—the rest is used for linking. If you compile that same structure for the 64-bit runtime, the structure takes 20 bytes—the links alone make up 80% of the memory used. Consider using arrays or aggregate types and storing indices instead.

### Memory Allocations Are Padded to Preserve Alignment

When you call the `malloc` function directly (or when it is called indirectly, such as when an Objective-C object is allocated), additional memory may be allocated by the operating system to maintain a specific data alignment. When allocating memory for C structs, it may be more efficient for you to allocate a few large blocks of memory instead of allocating memory for each individual struct.

### Cache Only When You Need To

Caching previously calculated results is a common way to improve an app’s performance. Still, you may want to investigate whether caching is really helping your app. As the previous examples have shown, memory usage is higher on 64-bit systems. If your app relies too much on caching, the pressure it puts on the virtual memory system may actually result in worse performance.

Typical examples of behaviors to avoid include:

- Caching any data that a class can cheaply recompute on the fly
- Caching data or objects that you can easily obtain from another object
- Caching system objects that are inexpensive to re-create
- Caching read-only data that can be accessed via `mmap()`

Always test to ensure that caching improves the performance of your app. And be sure to build hooks into your app so that you can selectively disable caching. In that way, you can test whether disabling a particular cache has a significant effect on the memory usage or the performance of your app. Make sure you test many different data sets for your caching algorithms.

[Next](Document%20Revision%20History.md)[Previous](Converting%20Your%20App%20to%20a%2064-Bit%20Binary.md)
