---
title: 'class_replaceMethod(_:_:_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_replacemethod(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_replacemethod(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_replacemethod%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:29c05e29bab75000'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_replaceMethod(_:_:_:_:)

<sub>函数</sub>

替换给定类中某个方法的实现。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_replaceMethod(_ cls: AnyClass?, _ name: Selector, _ imp: IMP, _ types: UnsafePointer<CChar>?) -> IMP?
```

## 参数

- `cls` — 要修改的类。

- `name` — 标识你要替换其实现的方法的选择器（selector）。

- `imp` — 由 `cls` 标识的类中、由 `name` 标识的方法的新实现。

- `types` — 描述方法参数类型的字符数组。可能的取值请参阅 [Objective-C Runtime Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008048) \> [Type Encodings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html#//apple_ref/doc/uid/TP40008048-CH100)。由于该函数必须至少接受两个参数——`self` 和 `_cmd`，因此第二和第三个字符必须是 “`@:`”（第一个字符是返回类型）。

## 返回值

由 `cls` 标识的类中、由 `name` 标识的方法的先前实现。

## 讨论

此函数有两种不同的行为：

- 如果由 `name` 标识的方法尚不存在，则会像调用了 [class_addMethod](<class_addmethod(________).md>) 一样添加它。此时会按给定方式使用 `types` 指定的类型编码。
- 如果由 `name` 标识的方法确实存在，则会像调用了 [method_setImplementation](<method_setimplementation(____).md>) 一样替换其 IMP。此时会忽略 `types` 指定的类型编码。

## 另请参阅

### 使用类

- [class_getName](<class_getname(__).md>) — 返回一个类的名称。
- [class_getSuperclass](<class_getsuperclass(__).md>) — 返回一个类的超类。
- [class_setSuperclass](<class_setsuperclass(____).md>) — 设置给定类的超类。 _(已废弃)_
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
