---
title: 'objc_is_finalized(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/objc_is_finalized(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_is_finalized(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_is_finalized%28_%3A%29.json'
content_hash: 'sha256:488f80a2e1a6da18'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_is_finalized(_:)

<sub>函数</sub>

> [!warning] 已废弃
> 它始终返回 NO。定义 OBJC_SILENCE_GC_DEPRECATIONS=1 可暂时消除此诊断。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_is_finalized(_ ptr: UnsafeMutableRawPointer!) -> Bool
```

## 另请参阅

### 函数

- [autoreleasepool(invoking:)](<autoreleasepool(invoking_).md>)
- [class_lookupMethod](<class_lookupmethod(____).md>) _(已废弃)_
- [class_respondsToMethod](<class_respondstomethod(____).md>) _(已废弃)_
- [objc_addExceptionHandler](<objc_addexceptionhandler(____).md>)
- [objc_addLoadImageFunc](<objc_addloadimagefunc(__).md>)
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
