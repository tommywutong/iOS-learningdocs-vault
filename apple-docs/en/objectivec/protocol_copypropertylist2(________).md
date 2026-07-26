---
title: 'protocol_copyPropertyList2(_:_:_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/protocol_copypropertylist2(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/protocol_copypropertylist2(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/protocol_copypropertylist2%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:754c75bcf012e613'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# protocol_copyPropertyList2(_:_:_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func protocol_copyPropertyList2(_ proto: Protocol, _ outCount: UnsafeMutablePointer<UInt32>?, _ isRequiredProperty: Bool, _ isInstanceProperty: Bool) -> UnsafeMutablePointer<objc_property_t>?
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
- [objc_enumerateClasses(fromImage:matchingNamePrefix:conformingTo:subclassing:)](<objc_enumerateclasses(fromimage_matchingnameprefix_conformingto_subclassing_).md>)
- [objc_exception_rethrow](<objc_exception_rethrow().md>)
