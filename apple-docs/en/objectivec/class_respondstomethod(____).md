---
title: 'class_respondsToMethod(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/class_respondstomethod(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_respondstomethod(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_respondstomethod%28_%3A_%3A%29.json'
content_hash: 'sha256:86cd45017adee0f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_respondsToMethod(_:_:)

<sub>Function</sub>

> [!warning] Deprecated
> use class_respondsToSelector instead

<sub>tvOS, visionOS, watchOS</sub>

```swift
func class_respondsToMethod(_ cls: AnyClass?, _ sel: Selector) -> Bool
```

## See Also

### Functions

- [autoreleasepool(invoking:)](<autoreleasepool(invoking_).md>)
- [class_lookupMethod](<class_lookupmethod(____).md>) _(deprecated)_
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
