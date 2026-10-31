---
title: 'class_getInstanceMethod(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_getinstancemethod(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_getinstancemethod(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_getinstancemethod%28_%3A_%3A%29.json'
content_hash: 'sha256:a93762017270a761'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_getInstanceMethod(_:_:)

<sub>函数</sub>

返回指定类中某个指定的实例方法。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_getInstanceMethod(_ cls: AnyClass?, _ name: Selector) -> Method?
```

## 参数

- `cls` — 你要检查的类。

- `name` — 你要获取的方法的选择器（selector）。

## 返回值

与 `aSelector` 所指定选择器在 `aClass` 所指定类中的实现相对应的方法；如果指定的类及其超类（superclass）都不包含具有该指定选择器的实例方法，则返回 `NULL`。

## 讨论

请注意，此函数会在超类中搜索实现，而 [class_copyMethodList](<class_copymethodlist(____).md>) 不会。

## 另请参阅

### 使用类

- [class_getName](<class_getname(__).md>) — 返回一个类的名称。
- [class_getSuperclass](<class_getsuperclass(__).md>) — 返回一个类的超类。
- [class_setSuperclass](<class_setsuperclass(____).md>) — 设置指定类的超类。_(已废弃)_
- [class_isMetaClass](<class_ismetaclass(__).md>) — 返回一个布尔值，指示某个类对象是否为元类（metaclass）。
- [class_getInstanceSize](<class_getinstancesize(__).md>) — 返回某个类的实例的大小。
- [class_getInstanceVariable](<class_getinstancevariable(____).md>) — 返回指定类中某个指定实例变量的 `Ivar`。
- [class_getClassVariable](<class_getclassvariable(____).md>) — 返回指定类中某个指定类变量的 `Ivar`。
- [class_addIvar](<class_addivar(__________).md>) — 向一个类中添加新的实例变量。
- [class_copyIvarList](<class_copyivarlist(____).md>) — 描述一个类声明的实例变量。
- [class_getIvarLayout](<class_getivarlayout(__).md>) — 返回指定类的 `Ivar` 布局的描述。
- [class_setIvarLayout](<class_setivarlayout(____).md>) — 设置指定类的 `Ivar` 布局。
- [class_getWeakIvarLayout](<class_getweakivarlayout(__).md>) — 返回指定类的弱 `Ivar`s 布局的描述。
- [class_setWeakIvarLayout](<class_setweakivarlayout(____).md>) — 设置指定类的弱 `Ivar`s 布局。
- [class_getProperty](<class_getproperty(____).md>) — 返回指定类中某个指定名称的属性。
- [class_copyPropertyList](<class_copypropertylist(____).md>) — 描述一个类声明的属性。
