---
title: 数值与值编程主题
apple_id: 10000038i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/Articles/Values.html
archived_at: '2026-07-15T07:17:18.997606Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [数值与值编程主题](Introduction%20to%20Numbers%20and%20Other%20Values.md)


[下一页](Using%20Numbers.md)[上一页](Introduction%20to%20Numbers%20and%20Other%20Values.md)

# 使用值

[NSValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/cl/NSValue) 对象是单个 C 或 Objective-C 数据项的简单容器。它可以容纳 `int`、`float`、`char` 等任意标量类型，以及指针、结构体和对象 `id`。该类的目的是让这类数据项能够被添加到集合对象中，例如 [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray) 或 [NSSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSSet) 的实例——这些集合要求其元素必须是对象。[NSValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/cl/NSValue) 对象始终是不可变的。

要用特定的数据项创建一个 [NSValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/cl/NSValue) 对象，你需要提供指向该数据项的指针，以及一个以 Objective-C 类型编码描述该项类型的 C 字符串。这个字符串通过 `@encode()` 编译器指令获得，它返回给定类型在特定平台上的编码（关于 `@encode()` 的更多信息及类型编码列表，请参阅[类型编码](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html#//apple_ref/doc/uid/TP40008048-CH100)）。例如，下面的代码片段创建了包含一个 [NSRange](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSRange) 的 _theValue_：

```objc
NSRange myRange = {4, 10};
NSValue *theValue = [NSValue valueWithBytes:&myRange objCType:@encode(NSRange)];
```

下面的示例演示了对自定义 C 结构体的编码。

```objc
// 假设 ImaginaryNumber 已定义：
typedef struct {
    float real;
    float imaginary;
} ImaginaryNumber;


ImaginaryNumber miNumber;
miNumber.real = 1.1;
miNumber.imaginary = 1.41;

NSValue *miValue = [NSValue valueWithBytes: &miNumber
                            withObjCType:@encode(ImaginaryNumber)];

ImaginaryNumber miNumber2;
[miValue getValue:&miNumber2];
```

你指定的类型必须是定长的。C 字符串、变长数组和结构体，以及其他长度不确定的数据类型都不能存入 [NSValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/cl/NSValue)——这些类型应改用 [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) 或 [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) 对象。不过，你可以把指向变长数据项的指针存入 [NSValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/cl/NSValue) 对象。下面的代码片段错误地尝试把一个 C 字符串直接放入 [NSValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/cl/NSValue) 对象：

```objc
/* 错误！ */
char *myCString = "This is a string.";
NSValue *theValue = [NSValue valueWithBytes:myCString withObjCType:@encode(char *)];
```

在这段代码中，_myCString_ 的内容被解释为指向 `char` 的指针，因此字符串中包含的前四个字节会被当作一个指针（实际使用的字节数可能因硬件架构而异）。也就是说，字符序列 “This” 被解释为一个指针值，而它几乎不可能是一个合法地址。存储此类数据项的正确做法是使用 `NSString` 对象（如果你需要把字符装进一个对象），或者传入其指针的地址，而不是指针本身：

```objc
/* 正确。 */
char *myCString = "This is a string.";
NSValue *theValue = [NSValue valueWithBytes:&myCString withObjCType:@encode(char **)];
```

这里传入的是 _myCString_ 的_地址_（_&myCString_），因此存入 _theValue_ 的是字符串首字符的地址。

[下一页](Using%20Numbers.md)[上一页](Introduction%20to%20Numbers%20and%20Other%20Values.md)
