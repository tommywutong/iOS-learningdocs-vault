---
title: 'class_copyMethodList(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_copymethodlist(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_copymethodlist(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_copymethodlist%28_%3A_%3A%29.json'
content_hash: 'sha256:bab54e0fe4fdbe22'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_copyMethodList(_:_:)

<sub>函数</sub>

描述某个类实现的实例方法。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_copyMethodList(_ cls: AnyClass?, _ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<Method>?
```

## 参数

- `cls` — 你要检查的类。

- `outCount` — 返回时，包含所返回数组的长度。若 `outCount` 为 `NULL`，则不返回长度。

## 返回值

一个类型为 `Method` 的指针数组，描述该类实现的实例方法——不包括任何由超类实现的实例方法。该数组包含 `*outCount` 个指针，后跟一个 `NULL` 终止符。你必须使用 `free()` 释放该数组。

若 `cls` 未实现任何实例方法，或 `cls` 为 `Nil`，则返回 `NULL`，且 `*outCount` 为 `0`。

## 讨论

要获取某个类的类方法，请使用 `class_copyMethodList(object_getClass(cls), &count)`。

要获取可能由超类实现的方法的实现，请使用 [class_getInstanceMethod](<class_getinstancemethod(____).md>) 或 [class_getClassMethod](<class_getclassmethod(____).md>)。

## 另请参阅

### 使用类

- [class_getName](<class_getname(__).md>) — 返回一个类的名称。
- [class_getSuperclass](<class_getsuperclass(__).md>) — 返回一个类的超类。
- [class_setSuperclass](<class_setsuperclass(____).md>) — 设置给定类的超类。_(已废弃)_
- [class_isMetaClass](<class_ismetaclass(__).md>) — 返回一个布尔值，指示某个类对象是否为元类。
- [class_getInstanceSize](<class_getinstancesize(__).md>) — 返回一个类的实例的大小。
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
