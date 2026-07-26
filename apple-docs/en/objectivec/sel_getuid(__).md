---
title: 'sel_getUid(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/sel_getuid(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/sel_getuid(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/sel_getuid%28_%3A%29.json'
content_hash: 'sha256:efa5752d8338b768'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# sel_getUid(_:)

<sub>Function</sub>

Registers a method name with the Objective-C runtime system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sel_getUid(_ str: UnsafePointer<CChar>) -> Selector
```

## Parameters

- `str` — A pointer to a C string. Pass the name of the method you wish to register.

## Return Value

A pointer of type [SEL](sel.md) specifying the selector for the named method.

## Discussion

The implementation of this method is identical to the implementation of [sel_registerName](<sel_registername(__).md>).

### Version-Notes

Prior to OS X version 10.0, this method tried to find the selector mapped to the given name and returned `NULL` if the selector was not found. This was changed for safety, because it was observed that many of the callers of this function did not check the return value for `NULL`.

## See Also

### Working with Selectors

- [sel_getName](<sel_getname(__).md>) — Returns the name of the method specified by a given selector.
- [sel_registerName](<sel_registername(__).md>) — Registers a method with the Objective-C runtime system, maps the method name to a selector, and returns the selector value.
- [sel_isEqual](<sel_isequal(____).md>) — Returns a Boolean value that indicates whether two selectors are equal.
