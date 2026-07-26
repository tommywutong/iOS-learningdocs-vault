---
title: 'sel_isEqual(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/sel_isequal(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/sel_isequal(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/sel_isequal%28_%3A_%3A%29.json'
content_hash: 'sha256:16aaae7575d1331a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# sel_isEqual(_:_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether two selectors are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sel_isEqual(_ lhs: Selector, _ rhs: Selector) -> Bool
```

## Parameters

- `lhs` — The selector to compare with `rhs`.

- `rhs` — The selector to compare with `lhs`.

## Return Value

[YES](yes.md) if `rhs` and `rhs` are equal, otherwise [NO](no.md).

## Discussion

`sel_isEqual` is equivalent to `==`.

## See Also

### Working with Selectors

- [sel_getName](<sel_getname(__).md>) — Returns the name of the method specified by a given selector.
- [sel_registerName](<sel_registername(__).md>) — Registers a method with the Objective-C runtime system, maps the method name to a selector, and returns the selector value.
- [sel_getUid](<sel_getuid(__).md>) — Registers a method name with the Objective-C runtime system.
