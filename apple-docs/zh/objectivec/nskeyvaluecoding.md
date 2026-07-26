---
title: NSKeyValueCoding
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nskeyvaluecoding
source_url: 'https://developer.apple.com/documentation/objectivec/nskeyvaluecoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nskeyvaluecoding.json'
content_hash: 'sha256:24921e7612f88c2c'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# NSKeyValueCoding

<sub>API 集合</sub>

一种机制，可让你通过名称或键间接访问对象的属性。

## Overview

访问对象值的基本方法是 [- setValue:forKey:](<nsobject-swift.class/setvalue(__forkey_).md>)（设置由指定键标识的属性的值）和 [- valueForKey:](<nsobject-swift.class/value(forkey_).md>)（返回由指定键标识的属性的值）。因此，可以用一致的方式访问对象的所有属性。

默认实现依赖于对象通常实现的存取方法（如有需要，也可以直接访问实例变量）。

## Topics

### Getting Values

- [- valueForKey:](<nsobject-swift.class/value(forkey_).md>) — 返回由给定键标识的属性的值。
- [- valueForKeyPath:](<nsobject-swift.class/value(forkeypath_).md>) — 返回由给定键路径标识的派生属性的值。
- [- dictionaryWithValuesForKeys:](<nsobject-swift.class/dictionarywithvalues(forkeys_).md>) — 返回一个字典，包含给定数组中每个键所标识的属性值。
- [- valueForUndefinedKey:](<nsobject-swift.class/value(forundefinedkey_).md>) — 当 [- valueForKey:](<nsobject-swift.class/value(forkey_).md>) 找不到与给定键对应的属性时被调用。
- [- mutableArrayValueForKey:](<nsobject-swift.class/mutablearrayvalue(forkey_).md>) — 返回一个可变数组代理，为给定键指定的有序一对多关系提供读写访问。
- [- mutableArrayValueForKeyPath:](<nsobject-swift.class/mutablearrayvalue(forkeypath_).md>) — 返回一个可变数组，为给定键路径指定的有序一对多关系提供读写访问。
- [- mutableSetValueForKey:](<nsobject-swift.class/mutablesetvalue(forkey_).md>) — 返回一个可变集合代理，为给定键指定的无序一对多关系提供读写访问。
- [- mutableSetValueForKeyPath:](<nsobject-swift.class/mutablesetvalue(forkeypath_).md>) — 返回一个可变集合，为给定键路径指定的无序一对多关系提供读写访问。
- [- mutableOrderedSetValueForKey:](<nsobject-swift.class/mutableorderedsetvalue(forkey_).md>) — 返回一个可变有序集合，为给定键指定的唯一化有序一对多关系提供读写访问。
- [- mutableOrderedSetValueForKeyPath:](<nsobject-swift.class/mutableorderedsetvalue(forkeypath_).md>) — 返回一个可变有序集合，为给定键路径指定的唯一化有序一对多关系提供读写访问。

### Setting Values

- [- setValue:forKeyPath:](<nsobject-swift.class/setvalue(__forkeypath_).md>) — 将给定键路径标识的属性的值设置为给定值。
- [- setValuesForKeysWithDictionary:](<nsobject-swift.class/setvaluesforkeys(__).md>) — 使用给定字典中的值设置接收者的属性，用字典的键来标识属性。
- [- setNilValueForKey:](<nsobject-swift.class/setnilvalueforkey(__).md>) — 当 [- setValue:forKey:](<nsobject-swift.class/setvalue(__forkey_).md>) 收到某个标量值（如 `int` 或 `float`）的 `nil` 值时被调用。
- [- setValue:forKey:](<nsobject-swift.class/setvalue(__forkey_).md>) — 将接收者中由给定键指定的属性设置为给定值。
- [- setValue:forUndefinedKey:](<nsobject-swift.class/setvalue(__forundefinedkey_).md>) — 当 [- setValue:forKey:](<nsobject-swift.class/setvalue(__forkey_).md>) 找不到给定键对应的属性时被调用。

### Changing Default Behavior

- [accessInstanceVariablesDirectly](nsobject-swift.class/accessinstancevariablesdirectly.md) — 返回一个布尔值，指示键值编码方法在找不到某个属性对应的存取方法时，是否应直接访问相应的实例变量。

### Validation

- [- validateValue:forKey:error:](<nsobject-swift.class/validatevalue(__forkey_).md>) — 指示给定指针指定的值对于给定键标识的属性是否有效，或是否可以变为有效。
- [- validateValue:forKeyPath:error:](<nsobject-swift.class/validatevalue(__forkeypath_).md>) — 指示给定指针指定的值相对于接收者、对于给定键路径是否无效。

### Deprecated Methods

- [+ useStoredAccessor](<nsobject-swift.class/usestoredaccessor().md>) — 如果存储值方法 [- storedValueForKey:](<nsobject-swift.class/storedvalue(forkey_).md>) 和 [- takeStoredValue:forKey:](<nsobject-swift.class/takestoredvalue(__forkey_).md>) 应优先使用私有存取方法而非公共存取方法，则返回 `true`。_(已废弃)_
- [- handleQueryWithUnboundKey:](<nsobject-swift.class/handlequery(withunboundkey_).md>) — 当 [- valueForKey:](<nsobject-swift.class/value(forkey_).md>) 找不到与 `key` 对应的属性时被调用。_(已废弃)_
- [- handleTakeValue:forUnboundKey:](<nsobject-swift.class/handletakevalue(__forunboundkey_).md>) — 当 [- takeValue:forKey:](<nsobject-swift.class/takevalue(__forkey_).md>) 找不到 `key` 对应的属性绑定时被调用。_(已废弃)_
- [- storedValueForKey:](<nsobject-swift.class/storedvalue(forkey_).md>) — 返回由给定键标识的属性。_(已废弃)_
- [- takeStoredValue:forKey:](<nsobject-swift.class/takestoredvalue(__forkey_).md>) — 设置由给定键标识的属性的值。_(已废弃)_
- [- takeValuesFromDictionary:](<nsobject-swift.class/takevalues(from_).md>) — 使用给定字典中的值设置接收者的属性，用字典的键来标识属性 _(已废弃)_
- [- takeValue:forKeyPath:](<nsobject-swift.class/takevalue(__forkeypath_).md>) — 将由 `keyPath` 标识的属性的值设置为 `value`。_(已废弃)_
- [- takeValue:forKey:](<nsobject-swift.class/takevalue(__forkey_).md>) — 将由 `key` 标识的属性的值设置为 `value`。_(已废弃)_
- [- unableToSetNilForKey:](<nsobject-swift.class/unabletosetnil(forkey_).md>) — 当 `key` 由一个标量特性表示时被调用。_(已废弃)_
- [- valuesForKeys:](<nsobject-swift.class/values(forkeys_).md>) — 返回一个字典，其键为 `keys` 中的属性名称，对应的值为相应的属性值。_(已废弃)_

### Constants

- [Key Value Coding Exception Names](key-value-coding-exception-names.md) — 这个常量定义了键值编码操作失败时引发的异常的名称。
- [NSUndefinedKeyException userInfo Keys](nsundefinedkeyexception-userinfo-keys.md) — 这些常量是 `NSUndefinedKeyException` 的 `userInfo` 字典中的键
- [NSKeyValueValidationError](../foundation/nskeyvaluevalidationerror-swift.var.md) — 一个键值编码验证错误。

## See Also

### Related Documentation

- [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)

### Key-Value Coding

- [NSKeyValueBindingCreation](nskeyvaluebindingcreation.md) — 一组方法，可用来在视图对象和控制器之间、或控制器和模型对象之间创建和移除绑定。
- [NSScriptKeyValueCoding](nsscriptkeyvaluecoding.md) — 一组方法，为使用键值编码提供额外的能力。
- [NSScriptKeyValueCoding Exception Names](nsscriptkeyvaluecoding-exception-names.md) — 键值编码方法引发的异常。
