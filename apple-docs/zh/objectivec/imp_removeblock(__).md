---
title: 'imp_removeBlock(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/imp_removeblock(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/imp_removeblock(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/imp_removeblock%28_%3A%29.json'
content_hash: 'sha256:da981451d60f6fc6'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# imp_removeBlock(_:)

<sub>函数</sub>

将一个 block 从使用 [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) 创建的 `IMP` 中解除关联，并释放所创建的该 block 的副本。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func imp_removeBlock(_ anImp: IMP) -> Bool
```

## 参数

- `anImp` — 使用 [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) 函数创建的 [IMP](imp.md)。

## 返回值

如果成功释放了 block，则为 [YES](yes.md)；否则为 [NO](no.md)（例如，如果先前未用该 block 创建 `anImp`，则函数返回 [NO](no.md)）。

## 另请参阅

### 使用 Objective-C 语言特性

- [objc_enumerationMutation](<objc_enumerationmutation(__).md>) — 在 foreach 迭代过程中检测到变更时由编译器插入。
- [objc_setEnumerationMutationHandler](<objc_setenumerationmutationhandler(__).md>) — 设置当前的变更处理程序。
- [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) — 创建一个函数指针，在该方法被调用时调用指定的 block。
- [imp_getBlock](<imp_getblock(__).md>) — 返回与某个使用 [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) 创建的 `IMP` 关联的 block。
- [objc_loadWeak](<objc_loadweak(__).md>) — 加载弱指针所引用的对象并返回它。
- [objc_storeWeak](<objc_storeweak(____).md>) — 在一个 `__weak` 变量中存储一个新值。
