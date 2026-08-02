---
title: 属性列表编程指南
apple_id: 10000048i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/ReadWritePlistData/ReadWritePlistData.html
archived_at: '2026-07-15T07:18:03.489344Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [属性列表编程指南](Introduction%20to%20Property%20Lists.md)


[下一页](Old-Style%20ASCII%20Property%20Lists.md)[上一页](Serializing%20a%20Property%20List.md)

# 读写属性列表数据

把属性列表数据写入文件系统主要有两种方式：

- 如果属性列表的根对象是 [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) 或 [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray) 对象——几乎总是如此——你可以调用这两个类的 `writeToFile:atomically:` 或 `writeToURL:atomically:` 方法，把根对象传进去。这些方法会先把属性列表对象图保存为 XML 属性列表，然后再写成文件或 URL 资源。

  要把属性列表数据读回程序，可以调用 `initWithContentsOfFile:` 和 `initWithContentsOfURL:` 方法来[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)一个已分配的集合对象，或者调用相应的类[工厂方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)（例如 [dictionaryWithContentsOfURL:](https://developer.apple.com/documentation/foundation/nsdictionary/1574185-dictionarywithcontentsofurl)）。
- 你可以用[类方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassMethod.html#//apple_ref/doc/uid/TP40008195-CH8) [dataFromPropertyList:format:errorDescription:](https://developer.apple.com/documentation/foundation/nspropertylistserialization/1416061-datafrompropertylist) 把属性列表对象序列化成 [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) 对象，然后调用 `NSData` 类的 [writeToFile:atomically:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/writeToFile:atomically:) 或 [writeToURL:atomically:](https://developer.apple.com/documentation/foundation/nsdata/1415134-writetourl) 方法保存该对象。

  要把属性列表数据读回程序，先调用 [initWithContentsOfFile:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/initWithContentsOfFile:) 或 [initWithContentsOfURL:](https://developer.apple.com/documentation/foundation/nsdata/1413892-init) 初始化一个已分配的 `NSData` 对象，或者调用相应的类工厂方法，例如 [dataWithContentsOfFile:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/clm/NSData/dataWithContentsOfFile:)。然后调用 `NSPropertyListSerialization` 的类方法 [propertyListFromData:mutabilityOption:format:errorDescription:](https://developer.apple.com/documentation/foundation/propertylistserialization/1411993-propertylistfromdata)，把这个数据对象传进去。

第一种方式更简单——只需要调用一个方法而不是两个——但第二种方式有它的优势。它允许你把运行时的属性列表转换成二进制格式，而不只是 XML 属性列表。而且当你把属性列表的静态表示还原成对象图时，它还让你能更灵活地指定这些对象是[可变还是不可变](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectMutability.html#//apple_ref/doc/uid/TP40008195-CH42)的。

为了把最后这一点说清楚，来看这个例子。假设你有一个 XML 属性列表，它的根对象是一个 [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray) 对象，其中包含若干 [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) 对象。如果你这样加载该属性列表：

```objc
NSArray * a = [NSArray arrayWithContentsOfFile:xmlFile];
```

那么 `a` 是一个不可变数组，其中每个元素都是不可变字典。每个字典中的每个键和每个值也都是不可变的。

如果你这样加载该属性列表：

```objc
NSMutableArray * ma = [NSMutableArray arrayWithContentsOfFile:xmlFile];
```

那么 `ma` 是一个可变数组，其中每个元素仍是不可变字典。每个字典中的每个键和每个值都是不可变的。

如果你需要对属性列表中各对象的可变性做更细粒度的控制，请使用类方法 [propertyListFromData:mutabilityOption:format:errorDescription:](https://developer.apple.com/documentation/foundation/propertylistserialization/1411993-propertylistfromdata)，它的第二个参数允许你指定聚合属性列表中各个层级对象的可变性。你可以指定所有对象都不可变（[NSPropertyListImmutable](https://developer.apple.com/documentation/foundation/nspropertylistmutabilityoptions/nspropertylistimmutable)）、只有容器（数组和字典）对象可变（[NSPropertyListMutableContainers](https://developer.apple.com/documentation/foundation/nspropertylistmutabilityoptions/nspropertylistmutablecontainers)），或者所有对象都可变（[NSPropertyListMutableContainersAndLeaves](https://developer.apple.com/documentation/foundation/propertylistserialization/mutabilityoptions/1411313-mutablecontainersandleaves)）。

例如，你可以这样写代码：

```objc
NSMutableArray *dma = (NSMutableArray *)[NSPropertyListSerialization
                        propertyListFromData:plistData
                        mutabilityOption:NSPropertyListMutableContainersAndLeaves
                        format:&format
                        errorDescription:&error];
```

这个调用会产生一个可变数组，其中每个元素都是可变字典。每个字典中的每个键和每个值本身也都是可变的。

要用 Property List Services（Core Foundation）写出 XML 属性列表，请调用 [CFURLWriteDataAndPropertiesToResource](https://developer.apple.com/documentation/corefoundation/1420723-cfurlwritedataandpropertiestores) 函数，把调用 [CFPropertyListCreateXMLData](https://developer.apple.com/documentation/corefoundation/1429991-cfpropertylistcreatexmldata) 创建出的 CFData 对象传进去。要从文件系统或 URL 资源读取 XML 属性列表，请调用 [CFURLCreateDataAndPropertiesFromResource](https://developer.apple.com/documentation/corefoundation/1420742-cfurlcreatedataandpropertiesfrom) 函数。然后调用 [CFPropertyListCreateFromXMLData](https://developer.apple.com/documentation/corefoundation/1429995-cfpropertylistcreatefromxmldata) 函数，把创建出的 CFData 对象转换成属性列表对象图。

清单 6-1 摘录了[在 Core Foundation 中保存和恢复属性列表](Serializing%20a%20Property%20List.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2jninedolktk42q)中那个更完整的代码示例的一部分，用以说明这些函数的用法。

__清单 6-1__  使用 Core Foundation 函数读写属性列表

```c
void WriteMyPropertyListToFile( CFPropertyListRef propertyList,
            CFURLRef fileURL ) {
   CFDataRef xmlData;
   Boolean status;
   SInt32 errorCode;

   // 把属性列表转换成 XML 数据。
   xmlData = CFPropertyListCreateXMLData( kCFAllocatorDefault, propertyList );

   // 把 XML 数据写入文件。
   status = CFURLWriteDataAndPropertiesToResource (
               fileURL,                  // 要使用的 URL
               xmlData,                  // 要写入的数据
               NULL,
               &errorCode);

   CFRelease(xmlData);
}

CFPropertyListRef CreateMyPropertyListFromFile( CFURLRef fileURL ) {
   CFPropertyListRef propertyList;
   CFStringRef       errorString;
   CFDataRef         resourceData;
   Boolean           status;
   SInt32            errorCode;

   // 读取 XML 文件。
   status = CFURLCreateDataAndPropertiesFromResource(
               kCFAllocatorDefault,
               fileURL,
               &resourceData,            // 用于存放文件数据的位置
               NULL,
               NULL,
               &errorCode);

   // 用这些 XML 数据重建字典。
   propertyList = CFPropertyListCreateFromXMLData( kCFAllocatorDefault,
               resourceData,
               kCFPropertyListImmutable,
               &errorString);

   if (resourceData) {
        CFRelease( resourceData );
    else {
        CFRelease( errorString );
    }
   return propertyList;
}
```

你也可以使用 [CFPropertyListWriteToStream](https://developer.apple.com/documentation/corefoundation/1430031-cfpropertylistwritetostream) 和 [CFPropertyListCreateFromStream](https://developer.apple.com/documentation/corefoundation/1429993-cfpropertylistcreatefromstream) 函数在文件系统中读写属性列表。这两个函数要求你自己打开并配置读写流。

[下一页](Old-Style%20ASCII%20Property%20Lists.md)[上一页](Serializing%20a%20Property%20List.md)

