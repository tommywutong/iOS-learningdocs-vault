---
title: 'imp_implementationWithBlock(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/imp_implementationwithblock(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/imp_implementationwithblock(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/imp_implementationwithblock%28_%3A%29.json'
content_hash: 'sha256:443359328d6ca046'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# imp_implementationWithBlock(_:)

<sub>函数</sub>

创建一个函数指针，在该方法被调用时调用指定的 block。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func imp_implementationWithBlock(_ block: Any) -> IMP
```

## 参数

- `block` — 实现此方法的 block。`block` 的签名应为 `method_return_type ^(id self, method_args …)`。方法的选择器（selector）对 `block` 不可用。`block` 会通过 `Block_copy()` 进行拷贝。

## 返回值

调用 `block` 的 [IMP](imp.md)。你必须使用相应函数释放返回的 [IMP](imp.md)。

## 另请参阅

### 使用 Objective-C 语言特性

- [objc_enumerationMutation](<objc_enumerationmutation(__).md>) — 在 foreach 迭代过程中检测到变更时由编译器插入。
- [objc_setEnumerationMutationHandler](<objc_setenumerationmutationhandler(__).md>) — 设置当前的变更处理程序。
- [imp_getBlock](<imp_getblock(__).md>) — 返回与某个使用 [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) 创建的 `IMP` 关联的 block。
- [imp_removeBlock](<imp_removeblock(__).md>) — 将一个 block 从使用 [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) 创建的 `IMP` 中解除关联，并释放所创建的该 block 的副本。
- [objc_loadWeak](<objc_loadweak(__).md>) — 加载弱指针所引用的对象并返回它。
- [objc_storeWeak](<objc_storeweak(____).md>) — 在一个 `__weak` 变量中存储一个新值。
