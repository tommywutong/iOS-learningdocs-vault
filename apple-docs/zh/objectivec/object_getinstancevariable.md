---
title: object_getInstanceVariable
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/object_getinstancevariable
source_url: 'https://developer.apple.com/documentation/objectivec/object_getinstancevariable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/object_getinstancevariable.json'
content_hash: 'sha256:5b8eae941755e33d'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# object_getInstanceVariable

<sub>函数</sub>

获取类实例的某个实例变量的值。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern Ivarobject_getInstanceVariable(id obj, const char *name, void **outValue);
```

## 参数

- `obj` — 指向类实例的指针。传入包含你希望获取其值的实例变量的对象。

- `name` — C 字符串。传入你希望获取其值的实例变量的名称。

- `outValue` — 返回时，包含指向该实例变量值的指针。

## 返回值

指向 [Ivar](ivar.md) 数据结构的指针，该结构定义了由 `name` 指定的实例变量的类型和名称。

## 另请参阅

### 使用实例

- [object_copy](object_copy.md) — 返回给定对象的副本。
- [object_dispose](object_dispose.md) — 释放给定对象所占用的内存。
- [object_setInstanceVariable](object_setinstancevariable.md) — 更改某个类实例的实例变量的值。
- [object_getIndexedIvars](<object_getindexedivars(__).md>) — 返回一个指针，指向随给定实例对象分配的任何额外字节。
- [object_getIvar](<object_getivar(____).md>) — 读取对象中某个实例变量的值。
- [object_setIvar](<object_setivar(______).md>) — 设置对象中某个实例变量的值。
- [object_getClassName](<object_getclassname(__).md>) — 返回给定对象的类名。
- [object_getClass](<object_getclass(__).md>) — 返回一个对象的类。
- [object_setClass](<object_setclass(____).md>) — 设置一个对象的类。
