---
title: Binary Data Programming Guide for Core Foundation
apple_id: 10000144i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2006-01-10'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBinaryData/DataObjects.html
archived_at: '2026-07-15T07:22:10.626115Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Binary Data Programming Guide for Core Foundation](Introduction%20to%20Binary%20Data%20Programming%20Guide%20for%20Core%20Foundation.md)


[Next](Working%20With%20Binary%20Data.md)[Previous](Introduction%20to%20Binary%20Data%20Programming%20Guide%20for%20Core%20Foundation.md)

# Data Objects

Data objects are object-oriented wrappers for byte buffers. In these data objects, simple allocated buffers (that is, data with no embedded pointers) take on the behavior of other objects—that is, they encapsulate data and provide operations to manipulate that data. Data objects are typically used to store data. They are also useful in internet and intranet applications because the data contained in data objects can be copied or moved between applications.

The size of the data that an instance of [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) or [NSMutableData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSMutableData) can wrap is subject to platform-dependent limitations—see _[NSData Class Reference](https://developer.apple.com/documentation/foundation/nsdata)_. When the data size is more than a few memory pages, the object uses virtual memory management. A data object can also wrap preexisting data, regardless of how the data was allocated. The object contains no information about the data itself (such as its type); the responsibility for deciding how to use the data lies with the client. In particular, it will not handle byte-order swapping when distributed between big-endian and little-endian machines. Instead, use [NSValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/cl/NSValue) for typed data.

Data objects provide an operating system–independent way to benefit from copy-on-write memory. The copy-on-write technique means that when data is copied through a virtual memory copy, an actual copy of the data is not made until there is an attempt to modify it.

Typically, you specify the bytes and the length of the bytes stored in a data object when creating that object. You can also extract bytes of a given range from a data object, compare data stored in two data objects, and write data to a URL. You use mutable data objects when you need to modify the data after creation. You can truncate, extend the length of, append data to, and replace a range of bytes in a mutable data object.

[Next](Working%20With%20Binary%20Data.md)[Previous](Introduction%20to%20Binary%20Data%20Programming%20Guide%20for%20Core%20Foundation.md)

