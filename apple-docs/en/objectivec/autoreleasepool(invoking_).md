---
title: 'autoreleasepool(invoking:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 1.0+, iPadOS 1.0+, Mac Catalyst 1.0+, macOS 10.0+, tvOS 1.0+, visionOS, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/autoreleasepool(invoking:)'
source_url: 'https://developer.apple.com/documentation/objectivec/autoreleasepool(invoking:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/autoreleasepool%28invoking%3A%29.json'
content_hash: 'sha256:506f3184d4229622'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# autoreleasepool(invoking:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func autoreleasepool<E, Result>(invoking body: () throws(E) -> Result) throws(E) -> Result where E : Error, Result : ~Copyable
```

## See Also

### Functions

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
- [objc_enumerateClasses(fromImage:matchingNamePrefix:conformingTo:subclassing:)](<objc_enumerateclasses(fromimage_matchingnameprefix_conformingto_subclassing_).md>)
- [objc_exception_rethrow](<objc_exception_rethrow().md>)
- [objc_exception_throw](<objc_exception_throw(__).md>) — Throw a runtime exception. This function is inserted by the compiler where \\c @throw would otherwise be.
