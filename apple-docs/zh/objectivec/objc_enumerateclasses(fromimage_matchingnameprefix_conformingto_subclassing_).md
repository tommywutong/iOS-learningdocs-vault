---
title: 'objc_enumerateClasses(fromImage:matchingNamePrefix:conformingTo:subclassing:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_enumerateclasses(fromimage:matchingnameprefix:conformingto:subclassing:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_enumerateclasses(fromimage:matchingnameprefix:conformingto:subclassing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_enumerateclasses%28fromimage%3Amatchingnameprefix%3Aconformingto%3Asubclassing%3A%29.json'
content_hash: 'sha256:ad207508e838bd73'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_enumerateClasses(fromImage:matchingNamePrefix:conformingTo:subclassing:)

<sub>函数</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_enumerateClasses(fromImage: ObjCEnumerationImage = .machHeader(#dsohandle), matchingNamePrefix: String? = nil, conformingTo: Protocol? = nil, subclassing: AnyClass? = nil) -> ObjCClassList
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
- [objc_exception_rethrow](<objc_exception_rethrow().md>)
- [objc_exception_throw](<objc_exception_throw(__).md>) — 抛出一个 runtime 异常。这个函数由编译器插入到本来应该是 \\c @throw 的位置。
