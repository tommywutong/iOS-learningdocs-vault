---
title: 'sel_isMapped(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/sel_ismapped(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/sel_ismapped(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/sel_ismapped%28_%3A%29.json'
content_hash: 'sha256:d1db180ee0f94c6f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# sel_isMapped(_:)

<sub>Function</sub>

Identifies a selector as being valid or invalid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sel_isMapped(_ sel: Selector) -> Bool
```

## Parameters

- `sel` — The selector you want to identify.

## Return Value

YES if selector is valid and has a function implementation, NO otherwise.

## Discussion

A crash.

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
- [objc_enumerateClasses(fromImage:matchingNamePrefix:conformingTo:subclassing:)](<objc_enumerateclasses(fromimage_matchingnameprefix_conformingto_subclassing_).md>)
- [objc_exception_rethrow](<objc_exception_rethrow().md>)
