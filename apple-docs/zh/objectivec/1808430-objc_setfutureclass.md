---
title: objc_setFutureClass
framework: Objective-C Runtime
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/1808430-objc_setfutureclass
source_url: 'https://developer.apple.com/documentation/objectivec/1808430-objc_setfutureclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/1808430-objc_setfutureclass.json'
content_hash: 'sha256:bbb79ac05ed56f15'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [Objective-C Runtime](objective-c-runtime.md)

# objc_setFutureClass

<sub>文章</sub>

由 CoreFoundation 的免费桥接（toll-free bridging）使用。

## 概述

不要自行调用这个函数。

## 另请参阅

### Working with Classes

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
