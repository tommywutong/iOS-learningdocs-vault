---
title: 'objc_storeWeak(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_storeweak(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_storeweak(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_storeweak%28_%3A_%3A%29.json'
content_hash: 'sha256:2135c0973018fe4e'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_storeWeak(_:_:)

<sub>函数</sub>

Stores a new value in a `__weak` variable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_storeWeak(_ location: AutoreleasingUnsafeMutablePointer<AnyObject?>, _ obj: Any?) -> Any?
```

## 参数

- `location` — 弱指针的地址。

- `obj` — 希望弱指针现在指向的新对象。

## 返回值

The value stored in `location` (that is, `obj`).

## 讨论

此函数通常用于 `__weak` 变量作为赋值目标的任何位置。

## 另请参阅

### 使用 Objective-C 语言特性

- [objc_enumerationMutation](<objc_enumerationmutation(__).md>) — 在 foreach 迭代期间检测到突变时由编译器插入。
- [objc_setEnumerationMutationHandler](<objc_setenumerationmutationhandler(__).md>) — 设置当前的变更处理程序。
- [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) — 创建一个函数指针，在该方法被调用时调用指定的 block。
- [imp_getBlock](<imp_getblock(__).md>) — 返回与某个使用 [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) 创建的 `IMP` 关联的 block。
- [imp_removeBlock](<imp_removeblock(__).md>) — 将一个 block 从使用 [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) 创建的 `IMP` 中解除关联，并释放所创建的该 block 的副本。
- [objc_loadWeak](<objc_loadweak(__).md>) — 加载弱指针所引用的对象并返回它。
