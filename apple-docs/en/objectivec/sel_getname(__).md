---
title: 'sel_getName(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/sel_getname(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/sel_getname(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/sel_getname%28_%3A%29.json'
content_hash: 'sha256:3a3c7aa8309be1ac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# sel_getName(_:)

<sub>Function</sub>

Returns the name of the method specified by a given selector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sel_getName(_ sel: Selector) -> UnsafePointer<CChar>
```

## Parameters

- `sel` — A pointer of type [SEL](sel.md). Pass the selector whose name you wish to determine.

## Return Value

A C string indicating the name of the selector.

## See Also

### Working with Selectors

- [sel_registerName](<sel_registername(__).md>) — Registers a method with the Objective-C runtime system, maps the method name to a selector, and returns the selector value.
- [sel_getUid](<sel_getuid(__).md>) — Registers a method name with the Objective-C runtime system.
- [sel_isEqual](<sel_isequal(____).md>) — Returns a Boolean value that indicates whether two selectors are equal.
