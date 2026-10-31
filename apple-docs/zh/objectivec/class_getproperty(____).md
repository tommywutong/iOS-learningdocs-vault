---
title: 'class_getProperty(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_getproperty(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_getproperty(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_getproperty%28_%3A_%3A%29.json'
content_hash: 'sha256:2bd9f7d3b9ba3a79'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_getProperty(_:_:)

<sub>函数</sub>

返回指定类中具有指定名称的属性。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_getProperty(_ cls: AnyClass?, _ name: UnsafePointer<CChar>) -> objc_property_t?
```

## 返回值

一个类型为 `objc_property_t` 的指针，用于描述该属性；或者 `NULL` 如果该类没有声明具有该名称的属性，或者 `NULL` 如果 `cls` 为 `Nil`.

## 另请参阅

### 使用类

- [class_getName](<class_getname(__) — 返回类的名称。
- [class_getSuperclass](<class_getsuperclass(__) — 返回类的超类。
- [class_setSuperclass](<class_setsuperclass(____) — 设置指定类的超类。_已废弃_
- [class_isMetaClass](<class_ismetaclass(__) — 返回一个布尔值，指示一个类对象是否为元类。
- [class_getInstanceSize](<class_getinstancesize(__) — 返回一个类的实例的大小。
- [class_getInstanceVariable](<class_getinstancevariable(____) — 返回指定类中指定实例变量的 `Ivar`。
- [class_getClassVariable](<class_getclassvariable(____) — 返回指定类中指定类变量的 `Ivar`。
- [class_addIvar](<class_addivar(__________) — 向类中添加一个新的实例变量。
- [class_copyIvarList](<class_copyivarlist(____) — 描述一个类所声明的实例变量。
- [class_getIvarLayout](<class_getivarlayout(__) — 返回指定类的 `Ivar` 布局描述。
- [class_setIvarLayout](<class_setivarlayout(____) — 设置指定类的 `Ivar` 布局。
- [class_getWeakIvarLayout](<class_getweakivarlayout(__) — 返回指定类中弱 `Ivar` 的布局描述。
- [class_setWeakIvarLayout](<class_setweakivarlayout(____) — 设置指定类中弱 `Ivar` 的布局。
- [class_copyPropertyList](<class_copypropertylist(____) — 描述一个类所声明的属性。
- [class_addMethod](<class_addmethod(________) — 向类中添加一个具有指定名称和实现的新方法。
