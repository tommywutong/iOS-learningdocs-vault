---
title: 'class_addMethod(_:_:_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_addmethod(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_addmethod(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_addmethod%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:33255a4da75d70d1'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_addMethod(_:_:_:_:)

<sub>函数</sub>

向类中添加一个具有给定名称和实现的新方法。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_addMethod(_ cls: AnyClass?, _ name: Selector, _ imp: IMP, _ types: UnsafePointer<CChar>?) -> Bool
```

## 参数

- `cls` — 要添加方法的类。

- `name` — 一个选择器（selector），用于指定正在添加的方法的名称。

- `imp` — 实现新方法的函数。该函数必须至少接受两个参数——`self` 和 `_cmd`。

- `types` — 一个字符数组，描述该方法的参数类型。有关可能的值，请参阅 [Objective-C Runtime 编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008048) \> [类型编码](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html#//apple_ref/doc/uid/TP40008048-CH100)。由于该函数必须至少接受两个参数——`self` 和 `_cmd`，因此第二个和第三个字符必须是“`@:`”（第一个字符是返回类型）。

## 返回值

如果方法添加成功，返回 [YES](yes.md)；否则返回 [NO](no.md)（例如，该类已经包含具有该名称的方法实现）。

## 讨论

[class_addMethod](<class_addmethod(________).md>) 会添加一个覆盖超类（superclass）实现的方法，但不会替换该类中已有的实现。要更改已有的实现，请使用 [method_setImplementation](<method_setimplementation(____).md>)。

Objective-C 方法只不过是一个至少接受两个参数的 C 函数——`self` 和 `_cmd`。例如，给定以下函数：

```objc
void myMethodIMP(id self, SEL _cmd)
{
    // implementation ....
}
```

你可以像这样将它作为方法（名为 `resolveThisMethodDynamically`）动态添加到类中：

```objc
class_addMethod([self class], @selector(resolveThisMethodDynamically), (IMP) myMethodIMP, "v@:");
```

## 另请参阅

### 使用类

- [class_getName](<class_getname(__).md>) — 返回类的名称。
- [class_getSuperclass](<class_getsuperclass(__).md>) — 返回类的超类。
- [class_setSuperclass](<class_setsuperclass(____).md>) — 设置给定类的超类。_（已废弃）_
- [class_isMetaClass](<class_ismetaclass(__).md>) — 返回一个布尔值，指示类对象是否为元类。
- [class_getInstanceSize](<class_getinstancesize(__).md>) — 返回类的实例大小。
- [class_getInstanceVariable](<class_getinstancevariable(____).md>) — 返回给定类的指定实例变量的 `Ivar`。
- [class_getClassVariable](<class_getclassvariable(____).md>) — 返回给定类的指定类变量的 `Ivar`。
- [class_addIvar](<class_addivar(__________).md>) — 向类添加一个新的实例变量。
- [class_copyIvarList](<class_copyivarlist(____).md>) — 描述类所声明的实例变量。
- [class_getIvarLayout](<class_getivarlayout(__).md>) — 返回给定类的 `Ivar` 布局（layout）的描述。
- [class_setIvarLayout](<class_setivarlayout(____).md>) — 设置给定类的 `Ivar` 布局。
- [class_getWeakIvarLayout](<class_getweakivarlayout(__).md>) — 返回给定类的弱 `Ivar` 布局的描述。
- [class_setWeakIvarLayout](<class_setweakivarlayout(____).md>) — 设置给定类的弱 `Ivar` 布局。
- [class_getProperty](<class_getproperty(____).md>) — 返回给定类中具有给定名称的属性（property）。
- [class_copyPropertyList](<class_copypropertylist(____).md>) — 描述类所声明的属性。
