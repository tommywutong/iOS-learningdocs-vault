---
title: 'class_getVersion(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_getversion(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_getversion(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_getversion%28_%3A%29.json'
content_hash: 'sha256:9ca7ae571fc2fb08'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_getVersion(_:)

<sub>函数</sub>

返回某个类定义的版本号。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_getVersion(_ cls: AnyClass?) -> Int32
```

## 参数

- `cls` — 指向 [Class](class.md) 数据结构的指针。传入你想获取版本号的类定义。

## 返回值

一个整数，表示该类定义的版本号。

## 讨论

你可以使用类定义的版本号，为你的类向其他类呈现的接口提供版本管理。这在对象序列化（即将对象归档为扁平形式）时尤其有用，因为此时识别实例变量的布局在不同 class-definition 版本中的变化非常重要。

派生自 Foundation 框架 `NSObject` 类的类可以获取 class-definition 版本号，使用 `getVersion` 类方法，该方法就是通过 `class_getVersion` 函数实现的。

## 另请参阅

### 使用类

- [class_getName](<class_getname(__).md>) — 返回某个类的名称。
- [class_getSuperclass](<class_getsuperclass(__).md>) — 返回某个类的超类。
- [class_setSuperclass](<class_setsuperclass(____).md>) — 设置指定类的超类。 _(已废弃)_
- [class_isMetaClass](<class_ismetaclass(__).md>) — 返回一个布尔值，指示某个类对象是否为元类。
- [class_getInstanceSize](<class_getinstancesize(__).md>) — 返回某个类的实例大小。
- [class_getInstanceVariable](<class_getinstancevariable(____).md>) — 返回指定类的某个指定实例变量所对应的 `Ivar`。
- [class_getClassVariable](<class_getclassvariable(____).md>) — 返回指定类的某个指定类变量所对应的 `Ivar`。
- [class_addIvar](<class_addivar(__________).md>) — 向某个类添加一个新的实例变量。
- [class_copyIvarList](<class_copyivarlist(____).md>) — 描述某个类声明的实例变量。
- [class_getIvarLayout](<class_getivarlayout(__).md>) — 返回指定类中 `Ivar` 布局的描述。
- [class_setIvarLayout](<class_setivarlayout(____).md>) — 设置指定类中 `Ivar` 的布局。
- [class_getWeakIvarLayout](<class_getweakivarlayout(__).md>) — 返回指定类中弱引用 `Ivar` 布局的描述。
- [class_setWeakIvarLayout](<class_setweakivarlayout(____).md>) — 设置指定类中弱引用 `Ivar` 的布局。
- [class_getProperty](<class_getproperty(____).md>) — 返回指定类中指定名称的属性。
- [class_copyPropertyList](<class_copypropertylist(____).md>) — 描述某个类声明的属性。
