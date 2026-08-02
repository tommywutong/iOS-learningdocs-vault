---
title: 归档与序列化编程指南
apple_id: 10000047i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2012-07-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Articles/creating.html
archived_at: '2026-07-15T05:25:42.895633Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [归档与序列化编程指南](Introduction.md)


[下一页](Encoding%20and%20Decoding%20Objects.md)[上一页](Archives.md)

# 创建和提取归档

本章描述如何创建和提取归档。要了解如何让自定义对象支持归档，请参阅 [Encoding and Decoding Objects](Encoding%20and%20Decoding%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2dqlkcineuqqskircq)。

创建对象图归档最简单的方法，是在归档器类上调用一个[类方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassMethod.html#//apple_ref/doc/uid/TP40008195-CH8)——`archiveRootObject:toFile:` 或 `archivedDataWithRootObject:` 二选一。这些便捷方法会创建一个临时的归档器对象，用于编码单个对象图；你无需再做其他事情。例如，下面的代码片段将一个名为 _aPerson_ 的自定义对象直接归档到文件中。

```objc
Person *aPerson = <#Get a Person#>;
NSString *archivePath = <Path for the archive#>;
BOOL success = [NSKeyedArchiver archiveRootObject:aPerson toFile:archivePath];
```

不过，如果你想自定义归档过程（例如用某些类替换另一些类），就必须自行创建归档器实例，按需配置，然后显式发送一个 `encode` 消息。`NSCoder` 本身并未定义任何特定的方法来创建编码器；这通常因子类而异。`NSKeyedArchiver` 定义了 [initForWritingWithMutableData:](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1409579-initforwritingwithmutabledata)。

获得配置好的编码器对象后，要编码一个对象或数据项，可以对 `NSKeyedArchiver` 编码器使用任意 `encode` 方法。编码完成后，必须在访问归档数据之前调用 `finishEncoding`。下面的示例代码片段与上面的代码类似，也归档了一个名为 _aPerson_ 的自定义对象，但允许自定义。

```objc
Person *aPerson = <#Get a Person#>;
NSString *archivePath = <Path for the archive#>;
NSMutableData *data = [NSMutableData data];
NSKeyedArchiver *archiver = [[NSKeyedArchiver alloc] initForWritingWithMutableData:data];
[archiver encodeObject:aPerson forKey:ASCPersonKey];
[archiver finishEncoding];

NSURL *archiveURL = <URL for the archive#>;
BOOL result = [data writeToURL:archiveURL atomically:YES];
```

创建不包含任何对象的归档也是可行的。要归档其他数据类型，可以直接对每个要归档的数据项调用特定类型的方法，例如 [encodeInteger:forKey:](https://developer.apple.com/documentation/foundation/nscoder/1411551-encodeinteger) 或 `encodeDouble:forKey:`，而不是使用 `encodeRootObject:`。

解码一个对象归档最简单的方法，是在解档器类上调用一个[类方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassMethod.html#//apple_ref/doc/uid/TP40008195-CH8)——[unarchiveObjectWithFile:](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1417153-unarchiveobject) 或 [unarchiveObjectWithData:](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1413894-unarchiveobjectwithdata) 二选一。这些便捷方法会创建一个临时的解档器对象，用于解码并返回单个对象图；你无需再做其他事情。`NSKeyedUnarchiver` 要求归档中的对象图是使用 `NSKeyedArchiver` 的某个便捷类方法（例如 `archiveRootObject:toFile:`）编码的。例如，下面的代码片段将一个名为 _aPerson_ 的自定义对象直接从文件中解档。

```objc
NSString *archivePath = <Path for the archive#>;
Person *aPerson = [NSKeyedUnarchiver unarchiveObjectWithFile:archivePath];
```

不过，如果你想自定义解档过程（例如用某些类替换另一些类），通常需要自行创建解档器类的实例，按需配置，然后显式发送一个 `decode` 消息。`NSCoder` 本身并未定义任何特定的方法来创建编码器；这通常因子类而异。`NSKeyedUnarchiver` 定义了 [initForReadingWithData:](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1410862-initforreadingwithdata)。

获得配置好的解码器对象后，要解码一个对象或数据项，可以使用 `decodeObjectForKey:` 方法。解码完键控归档后，应在释放解档器之前调用 `finishDecoding`。下面的示例代码片段与上面的代码样例类似，也解档了一个名为 _myMap_ 的自定义对象，但允许自定义。

```objc
NSURL *archiveURL = <URL for the archive#>;
NSData *data = [NSData dataWithContentsOfURL:archiveURL];

NSKeyedUnarchiver *unarchiver = [[NSKeyedUnarchiver alloc] initForReadingWithData:data];
// Customize the unarchiver.
Person *aPerson = [unarchiver decodeObjectForKey:ASCPersonKey];
[unarchiver finishDecoding];
```

你可以创建不包含任何对象的归档。要解档非对象数据类型，只需使用与原始 `encode...` 方法对应的 `decode...` 方法（例如 `decodeIntForKey:` 或 `decodeDoubleForKey:`）来处理每个要解档的数据项。

要自定义之前使用 `archiveRootObject:toFile:` 创建的归档的解档过程，可以使用 `decodeObjectForKey:` 和 `NSKeyedArchiveRootObjectKey` 键来识别归档中的根对象：

```objc
id object = [unarchiver decodeObjectForKey:NSKeyedArchiveRootObjectKey];
```

[下一页](Encoding%20and%20Decoding%20Objects.md)[上一页](Archives.md)
