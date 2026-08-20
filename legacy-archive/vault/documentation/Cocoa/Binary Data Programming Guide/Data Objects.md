---
title: 二进制数据编程指南
apple_id: 10000037i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-01-28'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/BinaryData/Concepts/DataObjects.html
archived_at: '2026-07-15T07:11:17.541468Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [二进制数据编程指南](Introduction%20to%20Binary%20Data%20Programming%20Guide%20for%20Cocoa.md)


[下一页](Working%20With%20Binary%20Data.md)[上一页](Introduction%20to%20Binary%20Data%20Programming%20Guide%20for%20Cocoa.md)

# 数据对象

数据对象是字节缓冲区的面向对象封装。在这些数据对象中，简单分配的缓冲区（即不包含内嵌指针的数据）具备了其他对象的行为——也就是说，它们封装数据并提供操作该数据的方法。数据对象通常用于存储数据。它们在互联网和内联网应用中也很有用，因为数据对象中包含的数据可以在应用程序之间复制或移动。

[NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) 或 [NSMutableData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSMutableData) 实例所能封装的数据大小受平台相关限制的约束——参见 _[NSData Class Reference](https://developer.apple.com/documentation/foundation/nsdata)_。当数据大小超过几个内存页时，该对象会使用虚拟内存管理。数据对象也可以封装已存在的数据，无论该数据是如何分配的。该对象不包含关于数据本身的任何信息（例如其类型）；如何使用数据的决定权在于客户端。特别是，当数据在大端序（big-endian）和小端序（little-endian）机器之间分发时，它不会处理字节序的交换。对于带类型的数据，应改用 [NSValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/cl/NSValue)。

数据对象提供了一种与操作系统无关的方式，来利用写时复制（copy-on-write）内存机制。写时复制技术意味着，当数据通过虚拟内存复制的方式被复制时，实际的数据副本并不会立即生成，而是要等到有修改尝试发生时才会生成。

通常，在创建数据对象时，你需要指定存储在其中的字节及字节长度。你也可以从数据对象中提取给定范围内的字节、比较两个数据对象中存储的数据，以及将数据写入 URL。当你需要在创建之后修改数据时，可以使用可变数据对象。你可以对可变数据对象进行截断、扩展长度、追加数据以及替换某一范围内的字节。

[下一页](Working%20With%20Binary%20Data.md)[上一页](Introduction%20to%20Binary%20Data%20Programming%20Guide%20for%20Cocoa.md)

