---
title: Binary Data Programming Guide for Core Foundation
apple_id: 10000144i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2006-01-10'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBinaryData/Tasks/CFWorkingBinaryData.html
archived_at: '2026-07-15T07:22:11.625559Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Binary Data Programming Guide for Core Foundation](Introduction%20to%20Binary%20Data%20Programming%20Guide%20for%20Core%20Foundation.md)


[Next](Working%20With%20Mutable%20Binary%20Data.md)[Previous](Data%20Objects.md)

# Working With Binary Data

This article contains code examples of common tasks that apply to immutable and mutable data objects, `CFData` and `CFMutableData` objects.

Generally, you create a data object from raw bytes using the `CFDataCreate` and `CFDataCreateMutable` functions for immutable and mutable data objects respectively. These functions make a copy of the bytes you pass as an argument. The copied bytes are owned by the data object and are freed when the data object is released. It is your responsibility to free the original bytes.

In contrast, the bytes are not copied when you create a data object using `CFDataCreateWithBytesNoCopy` with a deallocator argument which is not `kCFAllocatorNull`. Instead, the data object takes ownership of the bytes passed in as an argument and frees them when the object is released. For this reason, the bytes you pass to this function must have been allocated using the allocator you provide as the deallocator argument.

If you prefer that the bytes not be copied or freed when the object is released, you can create a no-copy, no-free `CFData` object using the `CFDataCreateWithBytesNoCopy` function and passing `kCFAllocatorNull` as the deallocator argument, as in:

```
CFDataRef dictData = CFDataCreateWithBytesNoCopy(
                            NULL, bytes, length, kCFAllocatorNull);
```


The three basic `CFData` functions are `CFDataGetBytesPtr`, `CFDataGetBytes`, and `CFDataGetLength`. The `CFDataGetBytesPtr` function returns a pointer to the bytes contained in the data object. The `CFDataGetBytes` function puts the bytes in a supplied buffer. The `CFDataGetLength` function returns the number of bytes contained in the data object.

For example, the following code fragment initializes a data object, `myData`, with the string `myString`. It then uses `CFDataGetBytesPtr` to return the bytes as a pointer.

```
const UInt8 *myString = "Test string.";
CFDataRef myData =
        CFDataCreateWithBytesNoCopy(NULL, myString, strlen(myString), kCFAllocatorNull);
const UInt8 *ptr = CFDataGetBytePtr(myData);
```

To create a data object that contains a subset of the bytes in another data object, pass a value for the range when calling the `CFDataGetBytes` function. For example, the following code fragment initializes a data object, `data2`, to contain a subrange of `data1`:

```
unsigned char aBuffer[20];
const UInt8 *strPtr = "ABCDEFG";
CFDataRef data1 =
        CFDataCreateWithBytesNoCopy(NULL, strPtr, strlen(strPtr), kCFAllocatorNull);
CFDataGetBytes(data1, CFRangeMake(2, 4), aBuffer);
CFDataRef data2 = CFDataCreate(NULL, aBuffer, 20);
```

To determine whether two data objects are equal, use the `CFEqual` function, which performs a byte-for-byte comparison.

Data objects make it convenient to convert between efficient, read-only data objects and mutable data objects. You use the `CFDataCreateCopy` and `CFDataCreateMutableCopy` functions to get an immutable and mutable copy of an existing data object respectively.

[Next](Working%20With%20Mutable%20Binary%20Data.md)[Previous](Data%20Objects.md)

