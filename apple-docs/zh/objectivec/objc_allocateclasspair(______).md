---
title: 'objc_allocateClassPair(_:_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_allocateclasspair(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_allocateclasspair(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_allocateclasspair%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8a602261667470d0'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_allocateClassPair(_:_:_:)

<sub>函数</sub>

创建新的类和元类。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_allocateClassPair(_ superclass: AnyClass?, _ name: UnsafePointer<CChar>, _ extraBytes: Int) -> AnyClass?
```

## 参数

- `superclass` — 用作新类超类的类，或传入 `Nil` 以创建新的根类。

- `name` — 用作新类名称的字符串。该字符串会被拷贝。

- `extraBytes` — 在类和元类对象末尾为索引实例变量分配的字节数。通常应为 `0`。

## 返回值

新类，若无法创建类则返回 `Nil`（例如，所需名称已在使用中）。

## 讨论

可通过调用 `object_getClass(newClass)` 获取指向新元类的指针。

要创建新类，先调用 [objc_allocateClassPair](<objc_allocateclasspair(______).md>)。然后使用 [class_addMethod](<class_addmethod(________).md>) 和 [class_addIvar](<class_addivar(__________).md>) 等函数设置类的属性。构建完成后，调用 [objc_registerClassPair](<objc_registerclasspair(__).md>)。此时新类即可使用。

实例方法和实例变量应添加到类本身。类方法应添加到元类。

## 另请参阅

### 添加类

- [objc_disposeClassPair](<objc_disposeclasspair(__).md>) — 销毁类及其关联的元类。
- [objc_registerClassPair](<objc_registerclasspair(__).md>) — 注册使用 [objc_allocateClassPair](<objc_allocateclasspair(______).md>) 分配的类。
- [objc_duplicateClass](<objc_duplicateclass(______).md>) — 供 Foundation 的键值观察使用。
