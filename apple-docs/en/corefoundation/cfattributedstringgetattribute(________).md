---
title: 'CFAttributedStringGetAttribute(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfattributedstringgetattribute(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringgetattribute(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringgetattribute%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:37a10d7964d12a2a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringGetAttribute(_:_:_:_:)

<sub>Function</sub>

Returns the value of a given attribute of an attributed string at a specified location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringGetAttribute(_ aStr: CFAttributedString!, _ loc: CFIndex, _ attrName: CFString!, _ effectiveRange: UnsafeMutablePointer<CFRange>!) -> CFTypeRef!
```

## Parameters

- `aStr` — The attributed string to examine.

- `loc` — The location in `str` at which to determine the attributes. `loc` must not exceed the bounds of `str`.

- `attrName` — The name of the attribute whose value you want to determine.

- `effectiveRange` — If not `NULL`, upon return contains a range including `loc` over which exactly the same set of attributes apply as at `loc`.

## Return Value

The value of the specified attribute at the specified location in `str`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

For performance reasons, a range returned in `effectiveRange` is not necessarily the maximal range. If you need the maximum range, you should use [CFAttributedStringGetAttributeAndLongestEffectiveRange](<cfattributedstringgetattributeandlongesteffectiverange(__________).md>).

## See Also

### Accessing Attributes

- [CFAttributedStringGetAttributes](<cfattributedstringgetattributes(______).md>) — Returns the attributes of an attributed string at a specified location.
- [CFAttributedStringGetAttributeAndLongestEffectiveRange](<cfattributedstringgetattributeandlongesteffectiverange(__________).md>) — Returns the value of a given attribute of an attributed string at a specified location.
- [CFAttributedStringGetAttributesAndLongestEffectiveRange](<cfattributedstringgetattributesandlongesteffectiverange(________).md>) — Returns the attributes of an attributed string at a specified location.
