---
title: 二进制数据编程指南
apple_id: 10000037i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-01-28'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/BinaryData/Tasks/WorkingBinaryData.html
archived_at: '2026-07-15T07:11:18.368416Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [二进制数据编程指南](Introduction%20to%20Binary%20Data%20Programming%20Guide%20for%20Cocoa.md)


[Next](Working%20With%20Mutable%20Binary%20Data.md)[Previous](Data%20Objects.md)

# 使用二进制数据

本文包含适用于不可变和可变数据对象（即 `NSData` 和 `NSMutableData` 对象）的常见任务代码示例。由于 Foundation 中[类簇（class clusters）](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassCluster.html#//apple_ref/doc/uid/TP40008195-CH7)的特性，数据对象并不是 `NSData` 或 `NSMutableData` 类的实际实例，而是它们某个私有子类的实例。尽管数据对象的类是私有的，但其接口是公开的，由这两个抽象超类 `NSData` 和 `NSMutableData` 声明。

通常，你会使用向 [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) 或 [NSMutableData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSMutableData) 类对象发送 `data...` 类消息之一的方式，从原始字节[创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)一个数据对象。这些方法会返回一个包含你所指定字节的数据对象。

通常，创建方法（例如 [dataWithBytes:length:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/clm/NSData/dataWithBytes:length:)）会复制你作为参数传入的字节。在这种情况下，复制得到的字节归数据对象所有，并在该数据对象被释放时一并释放。释放原始字节的责任在于你自己。

然而，如果你使用名称中包含 `NoCopy` 的方法（例如 [dataWithBytesNoCopy:length:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/clm/NSData/dataWithBytesNoCopy:length:)）创建 `NSData` 对象，字节不会被复制。相反，数据对象会取得作为参数传入的字节的所有权，并在该对象被[释放](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27)时释放这些字节。（[NSMutableData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSMutableData) 也响应这些方法，但无论如何都会复制字节，并立即释放传入的缓冲区。）正因如此，传给 `NoCopy` 方法的字节必须是使用 `malloc` 分配的。

如果你希望在对象被释放时字节既不被复制也不被释放，可以使用 [dataWithBytesNoCopy:length:freeWhenDone:](https://developer.apple.com/documentation/foundation/nsdata/1547240-datawithbytesnocopy) 或 [initWithBytesNoCopy:length:freeWhenDone:](https://developer.apple.com/documentation/foundation/nsdata/1416020-init) 方法，并将 `NO` 作为 `freeWhenDone:` 参数传入。

你可以使用 [dataWithContentsOfFile:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/clm/NSData/dataWithContentsOfFile:) 或 [dataWithContentsOfURL:](https://developer.apple.com/documentation/foundation/nsdata/1547245-datawithcontentsofurl) 类方法来创建一个包含文件或 URL 内容的数据对象。下面的代码示例创建了一个数据对象 `myData`，并用 `myFile.txt` 的内容对其进行初始化。路径必须是绝对路径。

```objc
NSString *thePath = @"/u/smith/myFile.txt";
NSData *myData = [NSData dataWithContentsOfFile:thePath];
```


[NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) 的两个原语方法——[bytes](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/bytes) 和 [length](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/length)——为该类中的所有其他方法提供了基础。[bytes](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/bytes) 方法返回一个指向数据对象中所含字节的指针。[length](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/length) 方法返回数据对象中所含的字节数。

[NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) 提供了用于将数据对象中的字节复制到指定缓冲区的访问方法。[getBytes:length:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/getBytes:length:) 方法会将字节复制到缓冲区中。例如，下面的代码片段用字符串 `myString` 初始化了一个数据对象 `myData`，然后使用 [getBytes:length:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/getBytes:length:) 将 `myData` 的内容复制到 `aBuffer` 中。

```objc
unsigned char aBuffer[20];
NSString *myString = @"Test string.";
const char *utfString = [myString UTF8String];
NSData *myData = [NSData dataWithBytes: utfString length: strlen(utfString)];

[myData getBytes:aBuffer length:20];
```

[getBytes:range:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/getBytes:range:) 方法可以从字节本身内部的某个起始点开始，复制一段范围内的字节。

要从另一个数据对象中提取包含其部分字节的数据对象，可以使用 [subdataWithRange:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/subdataWithRange:) 方法。例如，下面的代码片段初始化了一个数据对象 `data2`，使其包含 `data1` 的一个子范围：

```objc
NSString *myString = @"ABCDEFG";
const char *utfString = [myString UTF8String];
NSRange range = {2, 4};
NSData *data1, *data2;

data1 = [NSData dataWithBytes:utfString length:strlen(utfString)];

data2 = [data1 subdataWithRange:range];
```

要判断两个数据对象是否相等，可以使用 [isEqualToData:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/isEqualToData:) 方法，该方法会逐字节进行比较。

你可以复制数据对象来创建只读副本或可变副本。[NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) 和 [NSMutableData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSMutableData) 都采用了 [NSCopying](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSCopying/Description.html#//apple_ref/occ/intf/NSCopying) 和 [NSMutableCopying](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSMutableCopying/Description.html#//apple_ref/occ/intf/NSMutableCopying) 协议，因而可以方便地在高效的只读数据对象与可变数据对象之间转换。你可以使用 [copy](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/copy) 创建只读副本，使用 [mutableCopy](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/mutableCopy) 创建可变副本。

你可以将数据对象保存到本地文件或互联网上。[writeToFile:atomically:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/writeToFile:atomically:) 和 [writeToURL:atomically:](https://developer.apple.com/documentation/foundation/nsdata/1415134-writetourl) 方法可以让你将数据对象的内容写入本地文件。

[Next](Working%20With%20Mutable%20Binary%20Data.md)[Previous](Data%20Objects.md)

