---
title: 'class_getName(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_getname(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_getname(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_getname%28_%3A%29.json'
content_hash: 'sha256:e91fa6d0d5e0273a'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_getName(_:)

<sub>函数</sub>

返回某个类的名称。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_getName(_ cls: AnyClass?) -> UnsafePointer<CChar>
```

## 参数

- `cls` — 一个类对象。

## 返回值

该类的名称，或空字符串；如果 `cls` 为 `Nil`.

## 另请参阅

### 使用类

- [class_getSuperclass](<class_getsuperclass(__).md) — 返回某个类的超类。
- [class_setSuperclass](<class_setsuperclass(____).md) — 设置指定类的超类。 _(已废弃)_
- [class_isMetaClass](<class_ismetaclass(__).md) — 返回一个布尔值，指示某个类对象是否为元类。
- [class_getInstanceSize](<class_getinstancesize(__).md) — 返回某个类的实例大小。
- [class_getInstanceVariable](<class_getinstancevariable(____).md) — 返回给定类中指定实例变量对应的 `Ivar` 实例变量。
- [class_getClassVariable](<class_getclassvariable(____).md) — 返回给定类中指定类变量对应的 `Ivar` 类变量。
- [class_addIvar](<class_addivar(__________).md) — 向某个类添加新的实例变量。
- [class_copyIvarList](<class_copyivarlist(____).md) — 描述某个类声明的实例变量。
- [class_getIvarLayout](<class_getivarlayout(__).md) — 返回指定类的 `Ivar` 布局描述。
- [class_setIvarLayout](<class_setivarlayout(____).md) — 设置指定类的 `Ivar` 布局。
- [class_getWeakIvarLayout](<class_getweakivarlayout(__).md) — 返回指定类的弱引用 `Ivar` 布局描述。
- [class_setWeakIvarLayout](<class_setweakivarlayout(____).md) — 设置指定类的弱引用 `Ivar` 布局。
- [class_getProperty](<class_getproperty(____).md) — 返回指定类中具有指定名称的属性。
- [class_copyPropertyList](<class_copypropertylist(____).md) — 描述某个类声明的属性。
- [class_addMethod](<class_addmethod(________).md) — 向某个类添加一个具有指定名称和实现的新方法。
