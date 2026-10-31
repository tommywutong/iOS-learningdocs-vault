---
title: 'class_getInstanceSize(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_getinstancesize(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_getinstancesize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_getinstancesize%28_%3A%29.json'
content_hash: 'sha256:16fb00c705b518cf'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_getInstanceSize(_:)

<sub>函数</sub>

返回一个类的实例的大小。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_getInstanceSize(_ cls: AnyClass?) -> Int
```

## 参数

- `cls` — 一个类对象。

## 返回值

类 `cls` 的实例以字节计的大小；若 `cls` 为 `Nil`，则为 `0`。

## 另请参阅

### 使用类

- [class_getName](<class_getname(__).md>) — 返回一个类的名称。
- [class_getSuperclass](<class_getsuperclass(__).md>) — 返回一个类的超类。
- [class_setSuperclass](<class_setsuperclass(____).md>) — 设置给定类的超类。_(已废弃)_
- [class_isMetaClass](<class_ismetaclass(__).md>) — 返回一个布尔值，指示某个类对象是否为元类。
- [class_getInstanceVariable](<class_getinstancevariable(____).md>) — 返回给定类中指定实例变量的 `Ivar`。
- [class_getClassVariable](<class_getclassvariable(____).md>) — 返回给定类中指定类变量的 `Ivar`。
- [class_addIvar](<class_addivar(__________).md>) — 向一个类添加一个新的实例变量。
- [class_copyIvarList](<class_copyivarlist(____).md>) — 描述某个类声明的实例变量。
- [class_getIvarLayout](<class_getivarlayout(__).md>) — 返回给定类的 `Ivar` 布局的描述。
- [class_setIvarLayout](<class_setivarlayout(____).md>) — 设置给定类的 `Ivar` 布局。
- [class_getWeakIvarLayout](<class_getweakivarlayout(__).md>) — 返回给定类中弱 `Ivar` 布局的描述。
- [class_setWeakIvarLayout](<class_setweakivarlayout(____).md>) — 设置给定类中弱 `Ivar` 的布局。
- [class_getProperty](<class_getproperty(____).md>) — 返回给定类中具有给定名称的属性。
- [class_copyPropertyList](<class_copypropertylist(____).md>) — 描述某个类声明的属性。
- [class_addMethod](<class_addmethod(________).md>) — 以给定的名称和实现向一个类添加一个新方法。
