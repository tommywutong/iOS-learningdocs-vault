---
title: 'CFAttributedStringGetAttributes(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfattributedstringgetattributes(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringgetattributes(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringgetattributes%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ccdc915646f33e72'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringGetAttributes(_:_:_:)

<sub>Function</sub>

Returns the attributes of an attributed string at a specified location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringGetAttributes(_ aStr: CFAttributedString!, _ loc: CFIndex, _ effectiveRange: UnsafeMutablePointer<CFRange>!) -> CFDictionary!
```

## Parameters

- `aStr` — The attributed string to examine.

- `loc` — The location in `str` at which to determine the attributes. `loc` must not exceed the bounds of `str`.

- `effectiveRange` — If not `NULL`, upon return contains a range including `loc` over which exactly the same set of attributes apply as at `loc`.

## Return Value

A dictionary that contains the attributes of `str` at the specified location. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

For performance reasons, a range returned in `effectiveRange` is not necessarily the maximal range. If you need the maximum range, you should use [CFAttributedStringGetAttributesAndLongestEffectiveRange](<cfattributedstringgetattributesandlongesteffectiverange(________).md>).

Note that the returned attribute dictionary might change in unpredictable ways if the attributed string is edited after this call. If you want to preserve the state of the dictionary, you should make an actual copy of it rather than just retaining it. In addition, you should make no assumptions about the relationship of the actual dictionary returned by this call and the dictionary originally used to set the attributes, other than the fact that the values stored in the dictionaries will be identical (that is, `==`) to those originally specified.

## See Also

### Accessing Attributes

- [CFAttributedStringGetAttribute](<cfattributedstringgetattribute(________).md>) — Returns the value of a given attribute of an attributed string at a specified location.
- [CFAttributedStringGetAttributeAndLongestEffectiveRange](<cfattributedstringgetattributeandlongesteffectiverange(__________).md>) — Returns the value of a given attribute of an attributed string at a specified location.
- [CFAttributedStringGetAttributesAndLongestEffectiveRange](<cfattributedstringgetattributesandlongesteffectiverange(________).md>) — Returns the attributes of an attributed string at a specified location.
