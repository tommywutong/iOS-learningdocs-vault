---
title: 'class_getInstanceVariable(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_getinstancevariable(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_getinstancevariable(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_getinstancevariable%28_%3A_%3A%29.json'
content_hash: 'sha256:23cd79a0444adb1c'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_getInstanceVariable(_:_:)

<sub>函数</sub>

返回给定类中指定实例变量的 `Ivar`。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_getInstanceVariable(_ cls: AnyClass?, _ name: UnsafePointer<CChar>) -> Ivar?
```

## 参数

- `cls` — 你要获取其实例变量的类。

- `name` — 要获取的实例变量定义的名称。

## 返回值

指向 [Ivar](ivar.md) 数据结构的指针，该结构包含 `name` 所指定实例变量的信息。

## 另请参阅

### 使用类

- [class_getName](<class_getname(__).md>) — 返回类的名称。
- [class_getSuperclass](<class_getsuperclass(__).md>) — 返回类的超类。
- [class_setSuperclass](<class_setsuperclass(____).md>) — 设置给定类的超类。_(已废弃)_
- [class_isMetaClass](<class_ismetaclass(__).md>) — 返回一个布尔值，指示某个类对象是否为元类。
- [class_getInstanceSize](<class_getinstancesize(__).md>) — 返回类的实例大小。
- [class_getClassVariable](<class_getclassvariable(____).md>) — 返回给定类中指定类变量的 `Ivar`。
- [class_addIvar](<class_addivar(__________).md>) — 向类中添加一个新的实例变量。
- [class_copyIvarList](<class_copyivarlist(____).md>) — 描述某个类所声明的实例变量。
- [class_getIvarLayout](<class_getivarlayout(__).md>) — 返回给定类的 `Ivar` 布局描述。
- [class_setIvarLayout](<class_setivarlayout(____).md>) — 设置给定类的 `Ivar` 布局。
- [class_getWeakIvarLayout](<class_getweakivarlayout(__).md>) — 返回给定类中弱 `Ivar`s 的布局描述。
- [class_setWeakIvarLayout](<class_setweakivarlayout(____).md>) — 设置给定类中弱 `Ivar`s 的布局。
- [class_getProperty](<class_getproperty(____).md>) — 返回给定类中具有给定名称的属性。
- [class_copyPropertyList](<class_copypropertylist(____).md>) — 描述某个类所声明的属性。
- [class_addMethod](<class_addmethod(________).md>) — 向类中添加一个具有给定名称和实现的新方法。
