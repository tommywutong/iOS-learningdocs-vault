---
title: 'class_conformsToProtocol(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_conformstoprotocol(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_conformstoprotocol(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_conformstoprotocol%28_%3A_%3A%29.json'
content_hash: 'sha256:b958ffbe3f4e8dfd'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_conformsToProtocol(_:_:)

<sub>函数</sub>

返回一个布尔值，指示某个类是否遵循给定协议。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_conformsToProtocol(_ cls: AnyClass?, _ protocol: Protocol?) -> Bool
```

## 参数

- `cls` — 你要检查的类。

- `protocol` — 一个协议。

## 返回值

如果 `cls` 遵循 `protocol`，则返回 [YES](yes.md)，否则返回 [NO](no.md)。

## 讨论

你通常应当使用 `NSObject` 的 [- conformsToProtocol:](<nsobjectprotocol/conforms(to_).md>) 方法，而不是使用这个函数。

## 另请参阅

### 使用类

- [class_getName](<class_getname(__).md>) — 返回类的名称。
- [class_getSuperclass](<class_getsuperclass(__).md>) — 返回类的超类。
- [class_setSuperclass](<class_setsuperclass(____).md>) — 设置给定类的超类。_(已废弃)_
- [class_isMetaClass](<class_ismetaclass(__).md>) — 返回一个布尔值，指示某个类对象是否为元类。
- [class_getInstanceSize](<class_getinstancesize(__).md>) — 返回某个类的实例大小。
- [class_getInstanceVariable](<class_getinstancevariable(____).md>) — 返回给定类的指定实例变量的 `Ivar`。
- [class_getClassVariable](<class_getclassvariable(____).md>) — 返回给定类的指定类变量的 `Ivar`。
- [class_addIvar](<class_addivar(__________).md>) — 向类中添加一个新的实例变量。
- [class_copyIvarList](<class_copyivarlist(____).md>) — 描述某个类声明的实例变量。
- [class_getIvarLayout](<class_getivarlayout(__).md>) — 返回给定类的 `Ivar` 布局描述。
- [class_setIvarLayout](<class_setivarlayout(____).md>) — 设置给定类的 `Ivar` 布局。
- [class_getWeakIvarLayout](<class_getweakivarlayout(__).md>) — 返回给定类的弱 `Ivar`s 布局描述。
- [class_setWeakIvarLayout](<class_setweakivarlayout(____).md>) — 设置给定类的弱 `Ivar`s 布局。
- [class_getProperty](<class_getproperty(____).md>) — 返回给定类中具有给定名称的属性。
- [class_copyPropertyList](<class_copypropertylist(____).md>) — 描述某个类声明的属性。
