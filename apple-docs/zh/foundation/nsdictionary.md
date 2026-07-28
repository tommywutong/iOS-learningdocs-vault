---
title: NSDictionary
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdictionary
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary.json'
content_hash: 'sha256:8a811f5f97fde06f'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# NSDictionary

<sub>类</sub>

一个静态集合，包含与唯一键相关联的对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSDictionary
```

## 概述

在需要引用语义的情况下，你可以在 Swift 中使用此类型来代替 [Dictionary](../swift/dictionary.md)。

`NSDictionary` 类声明了管理键和值的不可变关联的对象的编程接口。例如，一个交互式表单可以表示为字典（dictionary），其中字段名作为键（key），对应到用户输入的值。

当你需要一种方便且高效的方式来检索与任意键相关联的数据时，请使用此类或其子类 [NSMutableDictionary](nsmutabledictionary.md)。`NSDictionary` 创建静态字典（static dictionary），而 `NSMutableDictionary` 创建动态字典（dynamic dictionary）。（为方便起见，术语*字典*指代此类任一实例，而不指定其具体类成员关系。）

字典中的键值对称为条目（entry）。每个条目由一个代表键的对象和另一个作为该键的值的对象组成。在一个字典中，键是唯一的。也就是说，单个字典中没有两个键是相等的（由 [isEqual(_:)](<../objectivec/nsobjectprotocol/isequal(__).md>) 判定）。通常，键可以是任何对象（前提是它符合 `NSCopying` 协议——见下文），但请注意，使用键值编码（key-value coding）时，键必须是字符串（参见 [访问对象属性](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/BasicPrinciples.html#//apple_ref/doc/uid/20002170)）。键和值都不能为 `nil`；如果你需要在字典中表示空值，应使用 [NSNull](nsnull.md)。

`NSDictionary` 与其 Core Foundation 对应类型 [CFDictionary](../corefoundation/cfdictionary.md) 是“无缝桥接（toll-free bridged）”的。有关无缝桥接的更多信息，请参见 [无缝桥接](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2)。

### 使用字典字面量创建 NSDictionary 对象

除了提供的初始化方法（如 [- initWithObjects:forKeys:](<nsdictionary/init(objects_forkeys_).md>)）之外，你还可以使用*字典字面量（dictionary literal）*来创建 `NSDictionary` 对象。

**Swift**

```swift
let dictionary: NSDictionary = [
    "anObject" : someObject,
    "helloString" : "Hello, World!",
    "magicNumber" : 42,
    "aValue" : someValue
]
```

**Objective-C**

```objc
NSDictionary *dictionary = @{
       @"anObject" : someObject,
    @"helloString" : @"Hello, World!",
    @"magicNumber" : @42,
         @"aValue" : someValue
};
```

在 Objective-C 中，编译器生成的代码会底层调用 [dictionaryWithObjects:forKeys:count:](nsdictionary/dictionarywithobjects_forkeys_count_.md) 方法。

```objc
id objects[] = { someObject, @"Hello, World!", @42, someValue };
id keys[] = { @"anObject", @"helloString", @"magicNumber", @"aValue" };
NSUInteger count = sizeof(objects) / sizeof(id);
NSDictionary *dictionary = [NSDictionary dictionaryWithObjects:objects
                                                       forKeys:keys
                                                         count:count];
```

与 [dictionaryWithObjectsAndKeys:](nsdictionary/dictionarywithobjectsandkeys_.md) 和其他初始化方法不同，字典字面量以键值对的顺序指定条目。使用此字面量语法时，你不应该用 `nil` 终止对象列表，事实上 `nil` 也是无效值。有关 Objective-C 中对象字面量的更多信息，请参见 [使用 Objective-C 编程](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011210) 中的 [使用对象](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/WorkingwithObjects/WorkingwithObjects.html#//apple_ref/doc/uid/TP40011210-CH4)。

在 Swift 中，`NSDictionary` 类符合 `DictionaryLiteralConvertible` 协议，这使其可以用字典字面量进行初始化。有关 Swift 中对象字面量的更多信息，请参见 [The Swift Programming Language (Swift 4.1)](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/index.html#//apple_ref/doc/uid/TP40014097) 中的 [字面量表达式](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/Expressions.html#//apple_ref/doc/uid/TP40014097-CH32-ID390)。

### 使用下标访问值

除了提供的实例方法（如 [- objectForKey:](<nsdictionary/object(forkey_).md>)）之外，你还可以使用*下标（subscripting）*通过键来访问 `NSDictionary` 的值。

**Swift**

```swift
let value = dictionary["helloString"]
```

**Objective-C**

```objc
id value = dictionary[@"helloString"];
```

### 使用 for-in 循环枚举条目

除了提供的实例方法（如 [- enumerateKeysAndObjectsUsingBlock:](<nsdictionary/enumeratekeysandobjects(__).md>)）之外，你还可以使用 *for-in 循环*来枚举 `NSDictionary` 条目。

**Swift**

```swift
for (key, value) in dictionary {
    print("Value: \(value) for key: \(key)")
}
```

**Objective-C**

```objc
for (NSString *key in dictionary) {
    id value = dictionary[key];
    NSLog(@"Value: %@ for key: %@", value, key);
}
```

在 Objective-C 中，`NSDictionary` 符合 [NSFastEnumeration](nsfastenumeration.md) 协议。

在 Swift 中，`NSDictionary` 符合 `SequenceType` 协议。

### 子类化说明

你通常不需要子类化 `NSDictionary`。自定义行为通常可以通过组合（composition）而非子类化来实现。

#### 需要重写的方法

如果你确实需要子类化 `NSDictionary`，要注意它是一个[类簇（class cluster）](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassCluster.html#//apple_ref/doc/uid/TP40008195-CH7)。任何子类都必须重写以下原始方法（primitive method）：

- [- initWithObjects:forKeys:count:](<nsdictionary/init(objects_forkeys_count_).md>)
- [count](nsdictionary/count.md)
- [- objectForKey:](<nsdictionary/object(forkey_).md>)
- [- keyEnumerator](<nsdictionary/keyenumerator().md>)

`NSDictionary` 的其他方法通过调用一个或多个这些原始方法来运作。非原始方法提供了一次访问多个条目的便捷方式。

#### 子类化的替代方案

在创建自定义 `NSDictionary` 类之前，请研究 [NSMapTable](nsmaptable.md) 和对应的 Core Foundation 类型 [CFDictionary](../corefoundation/cfdictionary.md)。由于 `NSDictionary` 和 `CFDictionary` 是“无缝桥接”的，你可以在代码中用 `CFDictionary` 对象替换 `NSDictionary` 对象（并进行适当的类型转换）。尽管它们是对应的类型，但 `CFDictionary` 和 `NSDictionary` 不具有完全相同的接口或实现，有时你使用 `CFDictionary` 可以完成一些用 `NSDictionary` 不易做到的事情。

如果你想要添加的行为是对现有类的补充，你可以为 `NSDictionary` 编写一个分类（category）。但请注意，此分类将对所有你使用的 `NSDictionary` 实例生效，这可能会产生意想不到的后果。或者，你可以使用组合（composition）来实现所需行为。

## 关系

- **继承自**: [NSObject](../objectivec/nsobject-swift.class.md)

- **被继承**: [NSMutableDictionary](nsmutabledictionary.md)

- **符合**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [ExpressibleByDictionaryLiteral](../swift/expressiblebydictionaryliteral.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSFastEnumeration](nsfastenumeration.md), [NSFetchRequestResult](../coredata/nsfetchrequestresult.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sequence](../swift/sequence.md)

## 主题

### 创建空字典

- [- init](<nsdictionary/init().md>) — 初始化一个新分配的空字典。

### 从对象和键创建字典

- [- initWithObjects:forKeys:](<nsdictionary/init(objects_forkeys_).md>) — 使用提供的键数组和对象数组构建键值对，来初始化一个新分配的字典。
- [- initWithObjects:forKeys:count:](<nsdictionary/init(objects_forkeys_count_).md>) — 使用提供的 C 数组中的指定数量的键值对，来初始化一个新分配的字典。
- [+ dictionaryWithObject:forKey:](<nsdictionary/init(object_forkey_).md>) — 创建一个包含给定键和值的字典。

### 从另一个字典创建字典

- [- initWithDictionary:](<nsdictionary/init(dictionary_)-9fw1u.md>) — 通过将另一个给定字典中的键和值放入其中，来初始化一个新分配的字典。
- [- initWithDictionary:copyItems:](<nsdictionary/init(dictionary_copyitems_).md>) — 使用另一个给定字典中的对象，来初始化一个新分配的字典。
- [init(dictionaryLiteral:)](<nsdictionary/init(dictionaryliteral_).md>) — 从给定的键值对初始化一个新分配的字典。

### 从外部源创建字典

- [init(contentsOfURL:error:)](<nsdictionary/init(contentsofurl_error_).md>) — 使用在给定 URL 处找到的键和值，来初始化一个新分配的字典。
- [- initWithContentsOfFile:](<nsdictionary/init(contentsoffile_).md>) — 使用在给定路径文件中找到的键和值，来初始化一个新分配的字典。_(已废弃)_

### 从 NSCoder 创建字典

- [- initWithCoder:](<nsdictionary/init(coder_).md>) — 从提供的解归档器中的数据初始化一个字典。

### 为共享键优化字典创建键集

- [+ sharedKeySetForKeys:](<nsdictionary/sharedkeyset(forkeys_).md>) — 为指定的键创建一个共享键集对象。

### 计数条目

- [count](nsdictionary/count.md) — 字典中的条目数量。

### 比较字典

- [- isEqualToDictionary:](<nsdictionary/isequal(to_).md>) — 返回一个布尔值，指示接收字典的内容是否等于另一个给定字典的内容。

### 访问键和值

- [allKeys](nsdictionary/allkeys.md) — 一个包含字典键的新数组，如果字典没有条目则为空数组。
- [- allKeysForObject:](<nsdictionary/allkeys(for_).md>) — 返回一个新数组，包含字典中给定对象所有出现对应的键。
- [allValues](nsdictionary/allvalues.md) — 一个包含字典值的新数组，如果字典没有条目则为空数组。
- [- valueForKey:](<nsdictionary/value(forkey_).md>) — 返回与给定键关联的值。
- [- objectsForKeys:notFoundMarker:](<nsdictionary/objects(forkeys_notfoundmarker_).md>) — 将字典中对应指定键的对象集合作为静态数组返回。
- [- objectForKey:](<nsdictionary/object(forkey_).md>) — 返回与给定键关联的值。
- [- objectForKeyedSubscript:](<nsdictionary/subscript(__)-52n56.md>) — 返回与给定键关联的值。
- [subscript(_:)](<nsdictionary/subscript(__)-1bt1b.md>) — 访问与给定键关联的值。

### 枚举字典

- [- keyEnumerator](<nsdictionary/keyenumerator().md>) — 提供一个枚举器来访问字典中的键。
- [- objectEnumerator](<nsdictionary/objectenumerator().md>) — 返回一个枚举器对象，让你访问字典中的每个值。
- [- enumerateKeysAndObjectsUsingBlock:](<nsdictionary/enumeratekeysandobjects(__).md>) — 对字典的每个条目应用一个给定的 block 对象。
- [- enumerateKeysAndObjectsWithOptions:usingBlock:](<nsdictionary/enumeratekeysandobjects(options_using_).md>) — 对字典的每个条目应用一个给定的 block 对象，并通过选项指定如何进行枚举。
- [makeIterator()](<nsdictionary/makeiterator().md>) — 返回此序列元素的迭代器。

### 排序字典

- [- keysSortedByValueUsingSelector:](<nsdictionary/keyssortedbyvalue(using_).md>) — 返回一个字典键的数组，按字典如果按值排序时的顺序排列。
- [- keysSortedByValueUsingComparator:](<nsdictionary/keyssortedbyvalue(comparator_).md>) — 返回一个字典键的数组，按字典如果使用给定比较器 block 按值排序时的顺序排列。
- [- keysSortedByValueWithOptions:usingComparator:](<nsdictionary/keyssortedbyvalue(options_usingcomparator_).md>) — 返回一个字典键的数组，按字典如果使用给定比较器 block 和指定选项集按值排序时的顺序排列。

### 过滤字典

- [- keysOfEntriesPassingTest:](<nsdictionary/keysofentries(passingtest_).md>) — 返回对应值满足 block 对象描述约束的键的集合。
- [- keysOfEntriesWithOptions:passingTest:](<nsdictionary/keysofentries(options_passingtest_).md>) — 返回对应值满足 block 对象描述约束的键的集合。

### 存储字典

- [- writeToURL:error:](<nsdictionary/write(to_).md>) — 将字典内容的属性列表（property list）表示写入到给定的 URL。
- [- writeToURL:atomically:](<nsdictionary/write(to_atomically_).md>) — 将字典内容的属性列表表示写入到给定的 URL。_(已废弃)_
- [- writeToFile:atomically:](<nsdictionary/write(tofile_atomically_).md>) — 将字典内容的属性列表表示写入到给定的路径。_(已废弃)_

### 访问文件属性

- [- fileSize](<nsdictionary/filesize().md>) — 返回文件大小（以字节为单位）。
- [- fileType](<nsdictionary/filetype().md>) — 返回文件类型。
- [- fileCreationDate](<nsdictionary/filecreationdate().md>) — 返回文件的创建日期。
- [- fileModificationDate](<nsdictionary/filemodificationdate().md>) — 返回文件的修改日期。
- [- filePosixPermissions](<nsdictionary/fileposixpermissions().md>) — 返回文件的 POSIX 权限。
- [- fileOwnerAccountID](<nsdictionary/fileowneraccountid().md>) — 返回文件的所有者账户 ID。
- [- fileOwnerAccountName](<nsdictionary/fileowneraccountname().md>) — 返回文件的所有者账户名称。
- [- fileGroupOwnerAccountID](<nsdictionary/filegroupowneraccountid().md>) — 返回文件的组所有者账户 ID。
- [- fileGroupOwnerAccountName](<nsdictionary/filegroupowneraccountname().md>) — 返回文件的组所有者账户名称。
- [- fileExtensionHidden](<nsdictionary/fileextensionhidden().md>) — 返回一个布尔值，指示文件是否隐藏其扩展名。
- [- fileIsImmutable](<nsdictionary/fileisimmutable().md>) — 返回一个布尔值，指示文件是否为不可变（immutable）。
- [- fileIsAppendOnly](<nsdictionary/fileisappendonly().md>) — 返回一个布尔值，指示文件是否为仅追加（append only）。
- [- fileSystemFileNumber](<nsdictionary/filesystemfilenumber().md>) — 返回文件系统文件编号。
- [- fileSystemNumber](<nsdictionary/filesystemnumber().md>) — 返回文件系统编号。
- [- fileHFSTypeCode](<nsdictionary/filehfstypecode().md>) — 返回文件的 HFS 类型代码。
- [- fileHFSCreatorCode](<nsdictionary/filehfscreatorcode().md>) — 返回文件的 HFS 创建者代码。

### 描述字典

- [description](nsdictionary/description.md) — 一个表示字典内容、格式化为属性列表的字符串。
- [descriptionInStringsFileFormat](nsdictionary/descriptioninstringsfileformat.md) — 一个表示字典内容、格式化为 `.strings` 文件格式的字符串。
- [- descriptionWithLocale:](<nsdictionary/description(withlocale_).md>) — 返回一个表示字典内容、格式化为属性列表的字符串对象。
- [- descriptionWithLocale:indent:](<nsdictionary/description(withlocale_indent_).md>) — 返回一个表示字典内容、格式化为属性列表的字符串对象。

### 支持类型

- [Iterator](nsdictionary/iterator.md) — 一个用于逐个提供字典成员的类。

### 初始化方法

- [- initWithContentsOfURL:](<nsdictionary/init(contentsof_).md>) — 使用在给定 URL 处找到的键和值，来初始化一个新分配的字典。_(已废弃)_
- [- initWithContentsOfURL:error:](<nsdictionary/init(contentsof_error_).md>) — 使用在给定 URL 处找到的键和值，来初始化一个新分配的字典。
- [init(dictionary:)](<nsdictionary/init(dictionary_)-4gc13.md>) — 初始化一个新分配的字典，并向其中添加来自另一个给定字典的对象。

### 默认实现

- [ExpressibleByDictionaryLiteral 实现](nsdictionary/expressiblebydictionaryliteral-implementations.md)
- [NSDictionary 实现](nsdictionary/nsdictionary-implementations.md)
- [Sequence 实现](nsdictionary/sequence-implementations.md)
