---
title: Binary Data Programming Guide for Core Foundation
apple_id: 10000144i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2006-01-10'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBinaryData/Tasks/CFWorkingMutableData.html
archived_at: '2026-07-15T07:22:12.130455Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Binary Data Programming Guide for Core Foundation](Introduction%20to%20Binary%20Data%20Programming%20Guide%20for%20Core%20Foundation.md)


[Next](Document%20Revision%20History.md)[Previous](Working%20With%20Binary%20Data.md)

# Working With Mutable Binary Data

This article contains code examples of common tasks that apply specifically to mutable data objects, `CFMutableData` objects.

The three basic `CFMutableData` functions are `CFDataGetMutableBytePtr`, `CFDataGetLength` and `CFDataSetLength`. The `CFDataGetMutableBytePtr` function returns a pointer for writing into the bytes contained in the mutable data object. The `CFDataGetLength` function returns the number of bytes contained in the data object. The `CFDataSetLength` function allows you to truncate or extend the length of a mutable data object. The `CFDataIncreaseLength` function also allows you to change the length of a mutable data object.

In [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgezdcljrgyydsmzrfvbuuqscjjcugsa), `CFDataGetMutableBytePtr` is used to return a pointer to the bytes in `data2`. The bytes in `data2` are then overwritten with the contents of `data1` using the `CFDataGetBytes` function.

__Listing 1__  Modifying bytes

```
 // Create some strings.
const UInt8 *myString = "string for data1";
const UInt8 *yourString = "string for data2";

// Declare buffers used later.
const UInt8 *data1Bytes, *data2Bytes;

// Create mutable data objects, data1 and data2.
CFMutableDataRef data1 = CFDataCreateMutable(NULL, 0);
CFMutableDataRef data2 = CFDataCreateMutable(NULL, 0);
CFDataAppendBytes(data1, myString, strlen(myString));
CFDataAppendBytes(data2, yourString, strlen(yourString));

// Get and print the data1 bytes.
data1Bytes = CFDataGetBytePtr(data1);
fprintf(stdout, "data1 before: \"%s\"\n", data1Bytes);

// Get and print the data2 bytes.
data2Bytes = CFDataGetMutableBytePtr(data2);
fprintf(stdout, "data2 before: \"%s\"\n", data2Bytes);

// Copy the bytes from data1 into the mutable bytes from data2.
CFDataGetBytes(data1,
               CFRangeMake(0, CFDataGetLength(data1)),
               data2Bytes);

// Get and print the data2 bytes again.
fprintf(stdout, "data2 after: \"%s\"\n", CFDataGetBytePtr(data2));
```

This is the output from [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgezdcljrgyydsmzrfvbuuqscjjcugsa):

```
data1 before: "string for data1"
data2 before: "string for data2"
data2 after: "string for data1"
```


The `CFDataAppendBytes` function lets you append bytes of the specified length to a mutable data object. For example, [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgezdcljrgyydsnzvfvbuuqsdjjbeora) copies the bytes in `data2` into `aBuffer` and then appends `aBuffer` to `data1`:

__Listing 2__  Appending bytes

```
 // Create mutable data objects, data1 and data2.
CFMutableDataRef data1 = CFDataCreateMutable(NULL, 0);
CFDataAppendBytes(data1, "ABCD", strlen("ABCD"));
CFMutableDataRef data2 = CFDataCreateMutable(NULL, 0);
CFDataAppendBytes(data2, "EFGH", strlen("EFGH"));

// Get the data2 bytes.
const UInt8 *aBuffer = CFDataGetBytePtr(data2);

// Append the bytes from data2 to data1.
CFDataAppendBytes(data1, aBuffer, CFDataGetLength(data2));
```


You can delete a range of bytes in a mutable data object (using the `CFDataDeleteBytes` function) or replace a range of bytes with other bytes (using the `CFDataReplaceBytes` function).

In [Listing 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgezdcljrgyytaobxfvbuuqsdjbeecrq), a range of bytes in `data1` is replaced by the bytes in `data2` using `CFDataReplaceBytes` (the content of `data1` changes from “Liz and John” to “Liz and Larry”):

__Listing 3__  Replacing bytes

```
// Create mutable data objects, data1 and data2.
CFMutableDataRef data1 = CFDataCreateMutable(NULL, 0);
CFDataAppendBytes(data1, "Liz and John", strlen("Liz and John"));
CFMutableDataRef data2 = CFDataCreateMutable(NULL, 0);
CFDataAppendBytes(data2, "Larry", strlen("Larry"));

// Allocate a buffer the length of data2.
unsigned len = CFDataGetLength(data2);
unsigned char *aBuffer = malloc(len);

// Put the data2 bytes into the buffer.
CFDataGetBytes(data2, CFRangeMake(0, len), aBuffer);

// Replace John with Larry.
CFDataReplaceBytes(data1, CFRangeMake(8, CFDataGetLength(data1) - 8), aBuffer, len);
```

[Next](Document%20Revision%20History.md)[Previous](Working%20With%20Binary%20Data.md)

