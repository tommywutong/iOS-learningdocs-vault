---
title: 'sel_registerName(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/sel_registername(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/sel_registername(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/sel_registername%28_%3A%29.json'
content_hash: 'sha256:c4e1853e80c3bf09'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# sel_registerName(_:)

<sub>Function</sub>

Registers a method with the Objective-C runtime system, maps the method name to a selector, and returns the selector value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sel_registerName(_ str: UnsafePointer<CChar>) -> Selector
```

## Parameters

- `str` — A pointer to a C string. Pass the name of the method you wish to register.

## Return Value

A pointer of type [SEL](sel.md) specifying the selector for the named method.

## Discussion

You must register a method name with the Objective-C runtime system to obtain the method’s selector before you can add the method to a class definition. If the method name has already been registered, this function simply returns the selector.

## See Also

### Working with Selectors

- [sel_getName](<sel_getname(__).md>) — Returns the name of the method specified by a given selector.
- [sel_getUid](<sel_getuid(__).md>) — Registers a method name with the Objective-C runtime system.
- [sel_isEqual](<sel_isequal(____).md>) — Returns a Boolean value that indicates whether two selectors are equal.
