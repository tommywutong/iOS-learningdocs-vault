---
title: 'class_getMethodImplementation_stret(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_getmethodimplementation_stret(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_getmethodimplementation_stret(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_getmethodimplementation_stret%28_%3A_%3A%29.json'
content_hash: 'sha256:7bb6275f71be92de'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C 运行时](../objectivec.md)

# class_getMethodImplementation_stret(_:_:)

<sub>函数</sub>

返回向某个类的实例发送特定消息时会被调用的函数指针。

<sub>macOS</sub>

```swift
func class_getMethodImplementation_stret(_ cls: AnyClass?, _ name: Selector) -> IMP?
```

## 参数

- `cls` — 你想检查的类。

- `name` — 一个选择器（selector）。

## 返回值

如果 `[object name]` 以该类的实例调用，则会调用的函数指针；或者为 `NULL`，如果 `cls` 为 `Nil`.

## 另请参阅

### 使用类

- [class_getName](<class_getname(__).md>) — 返回类的名称。
- [class_getSuperclass](<class_getsuperclass(__).md>) — 返回类的超类。
- [class_setSuperclass](<class_setsuperclass(____).md>) — 设置给定类的超类。 _已废弃_
- [class_isMetaClass](<class_ismetaclass(__).md>) — 返回一个布尔值，指示某个类对象是否为元类。
- [class_getInstanceSize](<class_getinstancesize(__).md>) — 返回某个类的实例的大小。
- [class_getInstanceVariable](<class_getinstancevariable(____).md>) — 返回给定类指定实例变量的 `Ivar`。
- [class_getClassVariable](<class_getclassvariable(____).md>) — 返回给定类指定类变量的 `Ivar`。
- [class_addIvar](<class_addivar(__________).md>) — 向类中添加一个新的实例变量。
- [class_copyIvarList](<class_copyivarlist(____).md>) — 描述由某个类声明的实例变量。
- [class_getIvarLayout](<class_getivarlayout(__).md>) — 返回给定类的 `Ivar` 布局描述。
- [class_setIvarLayout](<class_setivarlayout(____).md>) — 设置给定类的 `Ivar` 布局。
- [class_getWeakIvarLayout](<class_getweakivarlayout(__).md>) — 返回给定类的弱 `Ivar` 布局描述。
- [class_setWeakIvarLayout](<class_setweakivarlayout(____).md>) — 设置给定类的弱 `Ivar` 布局。
- [class_getProperty](<class_getproperty(____).md>) — 返回给定类中具有给定名称的属性（property）。
- [class_copyPropertyList](<class_copypropertylist(____).md>) — 描述由某个类声明的属性。
