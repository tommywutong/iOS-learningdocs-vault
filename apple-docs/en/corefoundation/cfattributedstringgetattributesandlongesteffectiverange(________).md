---
title: 'CFAttributedStringGetAttributesAndLongestEffectiveRange(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfattributedstringgetattributesandlongesteffectiverange(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringgetattributesandlongesteffectiverange(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringgetattributesandlongesteffectiverange%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c5b771d1d83876d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringGetAttributesAndLongestEffectiveRange(_:_:_:_:)

<sub>Function</sub>

Returns the attributes of an attributed string at a specified location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringGetAttributesAndLongestEffectiveRange(_ aStr: CFAttributedString!, _ loc: CFIndex, _ inRange: CFRange, _ longestEffectiveRange: UnsafeMutablePointer<CFRange>!) -> CFDictionary!
```

## Parameters

- `aStr` — The attributed string to examine.

- `loc` — The location in `str` at which to determine the attributes. `loc` must not exceed the bounds of `str`.

- `inRange` — The range in `str` within to find the longest effective range of the attributes at `loc`. `inRange` must not exceed the bounds of `str`.

- `longestEffectiveRange` — If  not `NULL`, upon return contains the maximal range within `inRange` over which the exact same set of attributes apply. The returned range is clipped to `inRange`.

## Return Value

A dictionary that contains the attributes of `str` at the specified location. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Accessing Attributes

- [CFAttributedStringGetAttribute](<cfattributedstringgetattribute(________).md>) — Returns the value of a given attribute of an attributed string at a specified location.
- [CFAttributedStringGetAttributes](<cfattributedstringgetattributes(______).md>) — Returns the attributes of an attributed string at a specified location.
- [CFAttributedStringGetAttributeAndLongestEffectiveRange](<cfattributedstringgetattributeandlongesteffectiverange(__________).md>) — Returns the value of a given attribute of an attributed string at a specified location.
