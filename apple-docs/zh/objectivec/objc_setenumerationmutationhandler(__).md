---
title: 'objc_setEnumerationMutationHandler(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_setenumerationmutationhandler(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_setenumerationmutationhandler(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_setenumerationmutationhandler%28_%3A%29.json'
content_hash: 'sha256:56468a1ee8715cfa'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_setEnumerationMutationHandler(_:)

<sub>函数</sub>

设置当前 mutation handler。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_setEnumerationMutationHandler(_ handler: ((Any) -> Void)?)
```

## 参数

- `handler` — 指向新 mutation handler 的函数指针。

## 另请参阅

### 使用 Objective-C 语言特性

- [objc_enumerationMutation](<objc_enumerationmutation(__).md>) — 在 foreach 迭代过程中检测到变更时由编译器插入。
- [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) — 创建一个函数指针，在该方法被调用时调用指定的 block。
- [imp_getBlock](<imp_getblock(__).md>) — 返回与某个使用 [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) 创建的 `IMP` 关联的 block。
- [imp_removeBlock](<imp_removeblock(__).md>) — 将一个 block 从使用 [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) 创建的 `IMP` 中解除关联，并释放所创建的该 block 的副本。
- [objc_loadWeak](<objc_loadweak(__).md>) — 加载弱指针所引用的对象并返回它。
- [objc_storeWeak](<objc_storeweak(____).md>) — 在一个 `__weak` 变量中存储一个新值。
