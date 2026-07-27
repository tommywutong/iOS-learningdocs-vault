---
title: NSScriptKeyValueCoding
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsscriptkeyvaluecoding
source_url: 'https://developer.apple.com/documentation/objectivec/nsscriptkeyvaluecoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsscriptkeyvaluecoding.json'
content_hash: 'sha256:50206522990001db'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# NSScriptKeyValueCoding

<sub>API 集合</sub>

一组方法，为使用键值编码提供额外的能力。

## 概述

Cocoa 脚本编写利用键值编码来获取和设置可脚本化对象中的信息。这个分类中的方法为使用键值编码提供了额外的能力，包括按索引获取和设置多值键中的键值，以及强制转换（或转换）某个键值。其他方法允许可脚本化容器类的实现者为按名称和唯一 ID 引用的元素提供快速访问。

由于 Cocoa 脚本编写会调用 [- setValue:forKey:](<nsobject-swift.class/setvalue(__forkey_).md>) 和 [- mutableArrayValueForKey:](<nsobject-swift.class/mutablearrayvalue(forkey_).md>)，AppleScript 脚本对模型对象所做的更改可以通过自动键值观察来观察到。

> [!note] Note
> 在 OS X 10.3 及更早版本中，Cocoa 脚本编写不会调用 [- setValue:forKey:](<nsobject-swift.class/setvalue(__forkey_).md>) 或 [- mutableArrayValueForKey:](<nsobject-swift.class/mutablearrayvalue(forkey_).md>)，因此脚本导致的模型对象更改并不总是会触发自动键值观察通知。从 macOS 10.4 开始，为了向后二进制兼容，如果该方法被重写，Cocoa 会调用现已废弃的方法 [- takeValue:forKey:](<nsobject-swift.class/takevalue(__forkey_).md>)，而不是 [- setValue:forKey:](<nsobject-swift.class/setvalue(__forkey_).md>)。

## 主题

### Indexed access

- [- insertValue:atIndex:inPropertyWithKey:](<nsobject-swift.class/insertvalue(__at_inpropertywithkey_).md>) — 在传入键指定的集合中，将某个对象插入到指定索引处。
- [- removeValueAtIndex:fromPropertyWithKey:](<nsobject-swift.class/removevalue(at_frompropertywithkey_).md>) — 从传入键指定的集合中，移除指定索引处的对象。
- [- replaceValueAtIndex:inPropertyWithKey:withValue:](<nsobject-swift.class/replacevalue(at_inpropertywithkey_withvalue_).md>) — 替换传入键指定的集合中指定索引处的对象。
- [- valueAtIndex:inPropertyWithKey:](<nsobject-swift.class/value(at_inpropertywithkey_).md>) — 从传入键指定的集合中检索一个按索引的对象。

### Access by name, key, or ID

- [- insertValue:inPropertyWithKey:](<nsobject-swift.class/insertvalue(__inpropertywithkey_).md>) — 在传入键指定的集合中插入一个对象。
- [- valueWithName:inPropertyWithKey:](<nsobject-swift.class/value(withname_inpropertywithkey_).md>) — 从传入键指定的集合中检索一个具名对象。
- [- valueWithUniqueID:inPropertyWithKey:](<nsobject-swift.class/value(withuniqueid_inpropertywithkey_).md>) — 从传入键指定的集合中按 ID 检索一个对象。

### Coercion

- [- coerceValue:forKey:](<nsobject-swift.class/coercevalue(__forkey_).md>) — 如有需要，使用来自类描述和 `NSScriptCoercionHandler` 的类型信息，尝试将 `key` 的 `value` 转换为正确的类型。

### 常量

- [NSScriptKeyValueCoding Exception Names](nsscriptkeyvaluecoding-exception-names.md) — 键值编码方法引发的异常。

## 另请参阅

### 相关文档

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
- [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)

### Key-Value Coding

- [NSKeyValueBindingCreation](nskeyvaluebindingcreation.md) — 一组方法，可用来在视图对象和控制器之间、或控制器和模型对象之间创建和移除绑定。
- [NSKeyValueCoding](nskeyvaluecoding.md) — 一种机制，可让你通过名称或键间接访问对象的属性。
- [NSScriptKeyValueCoding Exception Names](nsscriptkeyvaluecoding-exception-names.md) — 键值编码方法引发的异常。
