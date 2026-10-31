---
title: 'objc_addExceptionHandler(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_addexceptionhandler(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_addexceptionhandler(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_addexceptionhandler%28_%3A_%3A%29.json'
content_hash: 'sha256:5850b332b78904f2'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_addExceptionHandler(_:_:)

<sub>函数</sub>

<sub>macOS</sub>

```swift
func objc_addExceptionHandler(_ fn: objc_exception_handler, _ context: UnsafeMutableRawPointer?) -> UInt
```

## 另请参阅

### 函数

- [autoreleasepool(invoking:)](<autoreleasepool(invoking_).md>)
- [class_lookupMethod](<class_lookupmethod(____).md>) _(已废弃)_
- [class_respondsToMethod](<class_respondstomethod(____).md>) _(已废弃)_
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
- [objc_exception_throw](<objc_exception_throw(__).md>) — 抛出一个 runtime 异常。这个函数由编译器插入到本来应该是 \\c @throw 的位置。
