---
title: 键值编码编程指南
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/Compliant.html
archived_at: '2026-07-15T07:16:12.556056Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [键值编码编程指南](index.md)



## 规范符合性检查清单

按照本节汇总的步骤操作，确保对象符合键值编码规范。详细信息请参阅前面的章节。

### 属性和对一关系的规范符合性

对于每个属于属性或对一关系的属性：

- 实现名为 `<key>` 或 `is<Key>` 的方法，或创建实例变量 `<key>` 或 `_<key>`。编译器自动合成属性时通常会替你完成这项工作。

- 如果属性可变，请实现 `set<Key>:` 方法。允许编译器自动合成属性时，编译器通常会替你完成这项工作。

- 如果属性是标量，请重写 [setNilValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415174-setnilvalueforkey) 方法，以妥善处理将 `nil` 值赋给标量属性的情况。

### 索引式对多关系的规范符合性

对于每个有序的对多关系属性（例如 `NSArray` 对象）：

- 实现名为 `<key>` 且返回数组的方法，或提供名为 `<key>` 或 `_<key>` 的数组实例变量。编译器自动合成属性时通常会替你完成这项工作。
- 也可以实现 `countOf<Key>` 方法，并实现 `objectIn<Key>AtIndex:` 和 `<key>AtIndexes:` 中的一个或两个。
- 可以选择实现 `get<Key>:range:` 以提升性能。

此外，如果属性可变：

- 实现 `insertObject:in<Key>AtIndex:` 和 `insert<Key>:atIndexes:` 方法中的一个或两个。
- 实现 `removeObjectFrom<Key>AtIndex:` 和 `remove<Key>AtIndexes:` 方法中的一个或两个。
- 可以选择实现 `replaceObjectIn<Key>AtIndex:withObject:` 或 `replace<Key>AtIndexes:with<Key>:` 以提升性能。

### 无序对多关系的规范符合性

对于每个无序的对多关系属性（例如 `NSSet` 对象）：

- 实现返回集合的 `<key>` 方法，或提供名为 `<key>` 或 `_<key>` 的 `NSSet` 实例变量。编译器自动合成属性时通常会替你完成这项工作。
- 也可以实现 `countOf<Key>`、`enumeratorOf<Key>` 和 `memberOf<Key>:` 方法。

此外，如果属性可变：

- 实现 `add<Key>Object:` 和 `add<Key>:` 方法中的一个或两个。
- 实现 `remove<Key>Object:` 和 `remove<Key>:` 方法中的一个或两个。
- 可以选择实现 `intersect<Key>:` 以提升性能。

### 验证

为需要验证的属性选择启用验证：

- 实现 `validate<Key>:error:` 方法，返回指示该值是否有效的布尔值，并在适当时返回错误对象的引用。

[针对性能进行设计](Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tklkdjjbeiqsiinba)
