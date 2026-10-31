---
title: 'class_getMethodImplementation(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_getmethodimplementation(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_getmethodimplementation(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_getmethodimplementation%28_%3A_%3A%29.json'
content_hash: 'sha256:1e75eb0a76b1a120'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C 运行时](../objectivec.md)

# class_getMethodImplementation(_:_:)

<sub>函数</sub>

返回当向某个类的实例发送特定消息时会调用的函数指针。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_getMethodImplementation(_ cls: AnyClass?, _ name: Selector) -> IMP?
```

## 参数

- `cls` — 你要检查的类。

- `name` — 一个选择器（selector）。

## 返回值

如果 `[object name]` 以类的实例调用，则会调用的函数指针；或者 `NULL` 如果 `cls` 是 `Nil`.

## 讨论

[class_getMethodImplementation](<class_getmethodimplementation(____).md>) 可能比 `method_getImplementation(class_getInstanceMethod(cls, name))`.

返回的函数指针可能是运行时内部的函数，而不是实际的方法实现。例如，如果类的实例不响应该选择器，返回的函数指针将属于运行时的消息转发机制。

## 另请参阅

### 处理类

- [class_getName](<class_getname(__).md>) — 返回类的名称。
- [class_getSuperclass](<class_getsuperclass(__).md>) — 返回类的超类。
- [class_setSuperclass](<class_setsuperclass(____).md>) — 设置给定类的超类。_（已废弃）_
- [class_isMetaClass](<class_ismetaclass(__).md>) — 返回一个布尔值，指示类对象是否为元类。
- [class_getInstanceSize](<class_getinstancesize(__).md>) — 返回类的实例的大小。
- [class_getInstanceVariable](<class_getinstancevariable(____).md>) — 返回给定类指定实例变量的 `Ivar`。
- [class_getClassVariable](<class_getclassvariable(____).md>) — 返回给定类指定类变量的 `Ivar`。
- [class_addIvar](<class_addivar(__________).md>) — 向类添加新的实例变量。
- [class_copyIvarList](<class_copyivarlist(____).md>) — 描述类所声明的实例变量。
- [class_getIvarLayout](<class_getivarlayout(__).md>) — 返回给定类的 `Ivar` 布局描述。
- [class_setIvarLayout](<class_setivarlayout(____).md>) — 设置给定类的 `Ivar` 布局。
- [class_getWeakIvarLayout](<class_getweakivarlayout(__).md>) — 返回给定类弱 `Ivar`s 的布局描述。
- [class_setWeakIvarLayout](<class_setweakivarlayout(____).md>) — 为给定类设置弱 `Ivar`s 的布局。
- [class_getProperty](<class_getproperty(____).md>) — 返回给定类中具有给定名称的属性。
- [class_copyPropertyList](<class_copypropertylist(____).md>) — 描述类所声明的属性。
