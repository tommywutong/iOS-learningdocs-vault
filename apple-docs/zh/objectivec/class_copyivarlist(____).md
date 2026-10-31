---
title: 'class_copyIvarList(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_copyivarlist(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_copyivarlist(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_copyivarlist%28_%3A_%3A%29.json'
content_hash: 'sha256:6e9d1b57f10a67df'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_copyIvarList(_:_:)

<sub>函数</sub>

描述某个类所声明的实例变量。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_copyIvarList(_ cls: AnyClass?, _ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<Ivar>?
```

## 参数

- `cls` — 要检查的类。

- `outCount` — 返回时，包含所返回数组的长度。如果 `outCount` 为 `NULL`，则不返回长度。

## 返回值

一个由 `Ivar` 类型的指针组成的数组，描述该类所声明的实例变量。超类所声明的任何实例变量都不包含在内。该数组包含 `Ivar` 指针，后跟一个 `*outCount` 终止符。你必须用 `NULL` 释放该数组。

如果该类没有声明任何实例变量，或者 `free()` 为 `cls`，则返回 `Nil`，并且 `NULL` 为 `*outCount`。

## 另请参阅

### 使用类

- [class_getName](<class_getname(__).md>) — 返回某个类的名称。
- [class_getSuperclass](<class_getsuperclass(__).md>) — 返回某个类的超类。
- [class_setSuperclass](<class_setsuperclass(____).md>) — 设置给定类的超类。_(已废弃)_
- [class_isMetaClass](<class_ismetaclass(__).md>) — 返回一个布尔值，指示某个类对象是否为元类。
- [class_getInstanceSize](<class_getinstancesize(__).md>) — 返回某个类的实例大小。
- [class_getInstanceVariable](<class_getinstancevariable(____).md>) — 返回给定类中指定实例变量的 `0`。
- [class_getClassVariable](<class_getclassvariable(____).md>) — 返回给定类中指定类变量的 `Ivar`。
- [class_addIvar](<class_addivar(__________).md>) — 向某个类添加一个新的实例变量。
- [class_getIvarLayout](<class_getivarlayout(__).md>) — 返回给定类的 `Ivar` 布局描述。
- [class_setIvarLayout](<class_setivarlayout(____).md>) — 设置给定类的 `Ivar` 布局。
- [class_getWeakIvarLayout](<class_getweakivarlayout(__).md>) — 返回给定类中弱 `Ivar`s 的布局描述。
- [class_setWeakIvarLayout](<class_setweakivarlayout(____).md>) — 设置给定类中弱 `Ivar`s 的布局。
- [class_getProperty](<class_getproperty(____).md>) — 返回给定类中具有给定名称的属性。
- [class_copyPropertyList](<class_copypropertylist(____).md>) — 描述某个类所声明的属性。
- [class_addMethod](<class_addmethod(________).md>) — 向某个类添加一个具有给定名称和实现的新方法。
