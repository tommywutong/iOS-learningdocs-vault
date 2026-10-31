---
title: 'objc_addLoadImageFunc(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_addloadimagefunc(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_addloadimagefunc(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_addloadimagefunc%28_%3A%29.json'
content_hash: 'sha256:799cb915a514f7ed'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_addLoadImageFunc(_:)

<sub>函数</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_addLoadImageFunc(_ func: objc_func_loadImage)
```

## 另请参阅

### 函数

- [autoreleasepool(invoking:)](<autoreleasepool(invoking_).md>)
- [class_lookupMethod](<class_lookupmethod(____).md>) _(已废弃)_
- [class_respondsToMethod](<class_respondstomethod(____).md>) _(已废弃)_
- [objc_addExceptionHandler](<objc_addexceptionhandler(____).md>)
- [objc_assertRegisteredThreadWithCollector](<objc_assertregisteredthreadwithcollector().md>) _(已废弃)_
- [objc_begin_catch](<objc_begin_catch(__).md>)
- [objc_clear_stack](<objc_clear_stack(__).md>) _(已废弃)_
- [objc_collect](<objc_collect(__).md>) _(已废弃)_
- [objc_collectableZone](<objc_collectablezone().md>) _(已废弃)_
- [objc_collecting_enabled](<objc_collecting_enabled().md>) _(已废弃)_
- [objc_collectingEnabled](<objc_collectingenabled().md>) _(已废弃)_
- [objc_end_catch](<objc_end_catch().md>)
- [objc_enumerateClasses(fromImage:matchingNamePrefix:conformingTo:subclassing:)](<objc_enumerateclasses(fromimage_matchingnameprefix_conformingto_subclassing_).md>)
- [objc_exception_rethrow](<objc_exception_rethrow().md>)
- [objc_exception_throw](<objc_exception_throw(__).md>) — 抛出一个 runtime 异常。这个函数由编译器插入到本来应该是 \\c @throw 的位置。
