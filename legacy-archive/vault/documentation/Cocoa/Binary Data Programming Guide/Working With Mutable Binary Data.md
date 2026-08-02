---
title: 二进制数据编程指南
apple_id: 10000037i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-01-28'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/BinaryData/Tasks/WorkingMutableData.html
archived_at: '2026-07-15T07:11:18.868732Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [二进制数据编程指南](Introduction%20to%20Binary%20Data%20Programming%20Guide%20for%20Cocoa.md)


[Next](Document%20Revision%20History.md)[Previous](Working%20With%20Binary%20Data.md)

# 使用可变二进制数据

本文包含专门适用于[可变数据对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectMutability.html#//apple_ref/doc/uid/TP40008195-CH42)（即 `NSMutableData` 对象）的常见任务代码示例。基本上，你可以通过直接获取字节数组并修改它、向其追加字节，或替换某一范围内的字节，来更改可变二进制数据对象中的字节。

[NSMutableData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSMutableData) 的两个原语方法——[mutableBytes](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSMutableData/mutableBytes) 和 [setLength:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSMutableData/setLength:)——为该类中的所有其他方法提供了基础。[mutableBytes](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSMutableData/mutableBytes) 方法返回一个指针，用于写入可变数据对象中所含的字节。[setLength:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSMutableData/setLength:) 方法允许你截断或扩展可变数据对象的长度。[increaseLengthBy:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSMutableData/increaseLengthBy:) 方法同样也允许你更改可变数据对象的长度。

在[清单 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge2taljrgu2tqmzrfvbeeq2cjfeukqi)中，[mutableBytes](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSMutableData/mutableBytes) 用于返回一个指向 `data2` 中字节的指针。随后，`data2` 中的字节会被 `data1` 的内容覆盖。

__Listing 1__  Modifying bytes

```
NSMutableData *data1, *data2;
NSString *myString = @"string for data1";
NSString *yourString = @"string for data2";
const char *utfMyString = [myString UTF8String];
const char *utfYourString = [yourString UTF8String];
unsigned char *firstBuffer, secondBuffer[20];

/* initialize data1, data2, and secondBuffer... */
data1 = [NSMutableData dataWithBytes:utfMyString length:strlen(utfMyString)+1];
data2 = [NSMutableData dataWithBytes:utfYourString length:strlen(utfYourString)+1];

[data2 getBytes:secondBuffer length:20];
NSLog(@"data2 before: \"%s\"\n", (char *)secondBuffer);

firstBuffer = [data2 mutableBytes];
[data1 getBytes:firstBuffer length:[data2 length]];
NSLog(@"data1: \"%s\"\n", (char *)firstBuffer);

[data2 getBytes:secondBuffer length:20];
NSLog(@"data2 after: \"%s\"\n", (char *)secondBuffer);
```

以下是[清单 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge2taljrgu2tqmzrfvbeeq2cjfeukqi)的输出：

```text
Oct  3 15:59:51 [1113] data2 before: "string for data2"
Oct  3 15:59:51 [1113] data1: "string for data1"
Oct  3 15:59:51 [1113] data2 after: "string for data1"
```


[appendBytes:length:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSMutableData/appendBytes:length:) 和 [appendData:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSMutableData/appendData:) 方法可以让你将字节或另一个数据对象的内容追加到可变数据对象中。例如，[清单 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge2taljrgu2tqnbxfvbeeq2gjfcukry) 将 `data2` 中的字节复制到 `aBuffer` 中，然后将 `aBuffer` 追加到 `data1`：

__Listing 2__  Appending bytes

```
NSMutableData *data1, *data2;
NSString *firstString  = @"ABCD";
NSString *secondString = @"EFGH";
const char *utfFirstString = [firstString UTF8String];
const char *utfSecondString = [secondString UTF8String];
unsigned char *aBuffer;
unsigned len;

data1 = [NSMutableData dataWithBytes:utfFirstString length:strlen(utfFirstString)];
data2 = [NSMutableData dataWithBytes:utfSecondString length:strlen(utfSecondString)];

len = [data2 length];
aBuffer = malloc(len);

[data2 getBytes:aBuffer length:[data2 length]];
[data1 appendBytes:aBuffer length:len];
```

`data1` 的最终值是一系列 ASCII 字符 `"ABCDEFGH"`。

你可以使用 [resetBytesInRange:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSMutableData/resetBytesInRange:) 方法将可变数据对象中某一范围内的字节替换为零，也可以使用 [replaceBytesInRange:withBytes:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSMutableData/replaceBytesInRange:withBytes:) 方法将其替换为不同的字节。在[清单 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge2taljrgu2tqnzrfvbeeq2gijducrq)中，`data1` 中的一段字节被 `data2` 中的字节替换，`data1` 的内容从 “Liz and John” 变为 “Liz and Larry”：

__Listing 3__  Replacing bytes

```
NSMutableData *data1, *data2;
NSString *myString = @"Liz and John";
NSString *yourString = @"Larry";
const char *utfMyString = [myString UTF8String];
const char *utfYourString = [yourString UTF8String];
unsigned len;
unsigned char *aBuffer;
NSRange range = {8, strlen(utfYourString)};

data1 = [NSMutableData dataWithBytes:utfMyString length:strlen(utfMyString)];
data2 = [NSMutableData dataWithBytes:utfYourString length:strlen(utfYourString)];

len = [data2 length];
aBuffer = malloc(len);
[data2 getBytes:aBuffer length:len];
[data1 replaceBytesInRange:range withBytes:aBuffer];
```

[Next](Document%20Revision%20History.md)[Previous](Working%20With%20Binary%20Data.md)

