---
title: 'class_addIvar(_:_:_:_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_addivar(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_addivar(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_addivar%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:06fb843679593143'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_addIvar(_:_:_:_:_:)

<sub>函数</sub>

向类中添加一个新的实例变量。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_addIvar(_ cls: AnyClass?, _ name: UnsafePointer<CChar>, _ size: Int, _ alignment: UInt8, _ types: UnsafePointer<CChar>?) -> Bool
```

## 返回值

如果实例变量添加成功，则为 [YES](yes.md)，否则为 [NO](no.md)（例如该类已包含同名实例变量）。

## 讨论

此函数只能在 [objc_allocateClassPair](<objc_allocateclasspair(______).md>) 之后、[objc_registerClassPair](<objc_registerclasspair(__).md>) 之前调用。不支持向已有类添加实例变量。

该类不能是元类（metaclass）。不支持向元类添加实例变量。

实例变量的最小对齐字节数为 `1<<align`。实例变量的最小对齐取决于该实例变量的类型和机器架构。对于任何指针类型的变量，传入 `log2(sizeof(pointer_type))`。

## 另请参阅

### 使用类

- [class_getName](<class_getname(__).md>) — 返回类的名称。
- [class_getSuperclass](<class_getsuperclass(__).md>) — 返回类的超类。
- [class_setSuperclass](<class_setsuperclass(____).md>) — 设置给定类的超类。_(已废弃)_
- [class_isMetaClass](<class_ismetaclass(__).md>) — 返回一个布尔值，指示某个类对象是否为元类。
- [class_getInstanceSize](<class_getinstancesize(__).md>) — 返回类的实例大小。
- [class_getInstanceVariable](<class_getinstancevariable(____).md>) — 返回给定类的指定实例变量的 `Ivar`。
- [class_getClassVariable](<class_getclassvariable(____).md>) — 返回给定类的指定类变量的 `Ivar`。
- [class_copyIvarList](<class_copyivarlist(____).md>) — 描述类所声明的实例变量。
- [class_getIvarLayout](<class_getivarlayout(__).md>) — 返回给定类的 `Ivar` 布局描述。
- [class_setIvarLayout](<class_setivarlayout(____).md>) — 设置给定类的 `Ivar` 布局。
- [class_getWeakIvarLayout](<class_getweakivarlayout(__).md>) — 返回给定类的弱 `Ivar` 布局描述。
- [class_setWeakIvarLayout](<class_setweakivarlayout(____).md>) — 设置给定类的弱 `Ivar` 布局。
- [class_getProperty](<class_getproperty(____).md>) — 返回给定类中具有给定名称的属性。
- [class_copyPropertyList](<class_copypropertylist(____).md>) — 描述类所声明的属性。
- [class_addMethod](<class_addmethod(________).md>) — 向类中添加一个具有给定名称和实现的新方法。
