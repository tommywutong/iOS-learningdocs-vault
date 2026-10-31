---
title: 'class_copyProtocolList(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_copyprotocollist(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_copyprotocollist(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_copyprotocollist%28_%3A_%3A%29.json'
content_hash: 'sha256:8904dd497d727199'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_copyProtocolList(_:_:)

<sub>函数</sub>

描述一个类所采纳的协议。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_copyProtocolList(_ cls: AnyClass?, _ outCount: UnsafeMutablePointer<UInt32>?) -> AutoreleasingUnsafeMutablePointer<Protocol>?
```

## 参数

- `cls` — 你要检查的类。

- `outCount` — 返回时，包含所返回数组的长度。如果 `outCount` 为 `NULL`，则不返回长度。

## 返回值

一个由 `Protocol*` 类型的指针组成的数组，描述该类所采纳的协议。超类或其他协议所采纳的任何协议均不包含在内。该数组包含 `*outCount` 个指针，后跟一个 `NULL` 终止符。你必须用 `free()` 释放该数组。

如果 `cls` 未采纳任何协议，或 `cls` 为 `Nil`，则返回 `NULL`，并且 `*outCount` 为 `0`。

## 另请参阅

### 使用类

- [class_getName](<class_getname(__).md>) — 返回类的名称。
- [class_getSuperclass](<class_getsuperclass(__).md>) — 返回类的超类。
- [class_setSuperclass](<class_setsuperclass(____).md>) — 设置给定类的超类。_(已废弃)_
- [class_isMetaClass](<class_ismetaclass(__).md>) — 返回一个布尔值，指示某个类对象是否为元类。
- [class_getInstanceSize](<class_getinstancesize(__).md>) — 返回某个类的实例大小。
- [class_getInstanceVariable](<class_getinstancevariable(____).md>) — 返回给定类中指定实例变量的 `Ivar`。
- [class_getClassVariable](<class_getclassvariable(____).md>) — 返回给定类中指定类变量的 `Ivar`。
- [class_addIvar](<class_addivar(__________).md>) — 向类中添加一个新的实例变量。
- [class_copyIvarList](<class_copyivarlist(____).md>) — 描述某个类所声明的实例变量。
- [class_getIvarLayout](<class_getivarlayout(__).md>) — 返回给定类的 `Ivar` 布局描述。
- [class_setIvarLayout](<class_setivarlayout(____).md>) — 设置给定类的 `Ivar` 布局。
- [class_getWeakIvarLayout](<class_getweakivarlayout(__).md>) — 返回给定类的弱引用 `Ivar` 的布局描述。
- [class_setWeakIvarLayout](<class_setweakivarlayout(____).md>) — 为给定类设置弱引用 `Ivar` 的布局。
- [class_getProperty](<class_getproperty(____).md>) — 返回给定类中具有给定名称的属性。
- [class_copyPropertyList](<class_copypropertylist(____).md>) — 描述某个类所声明的属性。
