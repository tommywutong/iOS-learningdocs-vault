---
title: 归档与序列化编程指南
apple_id: 10000047i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2012-07-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Articles/serializing.html
archived_at: '2026-07-15T05:25:44.665912Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [归档与序列化编程指南](Introduction.md)


[下一页](Document%20Revision%20History.md)[上一页](Subclassing%20NSCoder.md)

# 序列化属性列表

序列化将 Objective-C 类型转换为与体系结构无关的字节流，也可以反向转换回来。与归档不同，基本序列化不会记录值的数据类型，也不会记录值之间的关系；只会记录值本身。按正确顺序反序列化数据是你自己的责任。

属性列表序列化不会保留对象的完整类身份，只保留其大致种类——字典、数组等等。因此，如果一个属性列表先被序列化再反序列化，结果属性列表中的对象可能与原始属性列表中的对象不属于同一个类。特别是，属性列表被序列化时，容器对象（`NSDictionary` 和 `NSArray` 对象）的可变性不会被保留。不过，在反序列化时，你可以选择让所有容器对象都创建为可变的或不可变的。

序列化也不会追踪对象被多次引用的情况。属性列表中每一次对同一个对象的引用都会被单独序列化，反序列化后就会产生多个实例。

由于序列化不会保留类信息或可变性，也不处理多重引用，因此编码（由 `NSCoder` 及其子类实现）是使对象图持久化的首选方式。

`NSPropertyListSerialization` 类提供了将[属性列表](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44)对象与 XML 格式或经过优化的二进制格式相互转换的序列化方法。`NSPropertyListSerialization` 类对象为序列化过程提供了接口；你不需要创建 `NSPropertyListSerialization` 的实例。

下面的代码示例展示了如何将一个简单的属性列表序列化为 XML 格式。

```objc
NSDictionary *propertyList= @{ @"FirstNameKey" : @"Edmund",
                               @"LastNameKey" : @"Blackadder" };
NSString *errorStr;
NSData *dataRep = [NSPropertyListSerialization dataFromPropertyList:propertyList
                format:NSPropertyListXMLFormat_v1_0
                errorDescription:&errorStr];
if (!dataRep) {
    // Handle error
}
```

下面的代码示例将上面得到的 XML 数据转换回对象图。

```objc
NSDictionary *propertyList = [NSPropertyListSerialization propertyListFromData:dataRep
                mutabilityOption:NSPropertyListImmutable
                format:NULL
                errorDescription:&errorStr];
if (!propertyList) {
    // Handle error
}
```

[下一页](Document%20Revision%20History.md)[上一页](Subclassing%20NSCoder.md)
