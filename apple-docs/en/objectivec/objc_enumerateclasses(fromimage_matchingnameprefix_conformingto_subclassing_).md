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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_enumerateClasses(fromImage:matchingNamePrefix:conformingTo:subclassing:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_enumerateClasses(fromImage: ObjCEnumerationImage = .machHeader(#dsohandle), matchingNamePrefix: String? = nil, conformingTo: Protocol? = nil, subclassing: AnyClass? = nil) -> ObjCClassList
```

## See Also

### Functions

- [autoreleasepool(invoking:)](<autoreleasepool(invoking_).md>)
- [class_lookupMethod](<class_lookupmethod(____).md>) _(deprecated)_
- [class_respondsToMethod](<class_respondstomethod(____).md>) _(deprecated)_
- [objc_addExceptionHandler](<objc_addexceptionhandler(____).md>)
- [objc_addLoadImageFunc](<objc_addloadimagefunc(__).md>)
- [objc_assertRegisteredThreadWithCollector](<objc_assertregisteredthreadwithcollector().md>) _(deprecated)_
- [objc_begin_catch](<objc_begin_catch(__).md>)
- [objc_clear_stack](<objc_clear_stack(__).md>) _(deprecated)_
- [objc_collect](<objc_collect(__).md>) _(deprecated)_
- [objc_collectableZone](<objc_collectablezone().md>) _(deprecated)_
- [objc_collecting_enabled](<objc_collecting_enabled().md>) _(deprecated)_
- [objc_collectingEnabled](<objc_collectingenabled().md>) _(deprecated)_
- [objc_end_catch](<objc_end_catch().md>)
- [objc_exception_rethrow](<objc_exception_rethrow().md>)
- [objc_exception_throw](<objc_exception_throw(__).md>) — Throw a runtime exception. This function is inserted by the compiler where \\c @throw would otherwise be.
