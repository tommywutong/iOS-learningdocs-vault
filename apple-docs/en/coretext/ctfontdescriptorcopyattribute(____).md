---
title: 'CTFontDescriptorCopyAttribute(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontdescriptorcopyattribute(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontdescriptorcopyattribute(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontdescriptorcopyattribute%28_%3A_%3A%29.json'
content_hash: 'sha256:a546a23b994bd95c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontDescriptorCopyAttribute(_:_:)

<sub>Function</sub>

Returns the value associated with an arbitrary attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontDescriptorCopyAttribute(_ descriptor: CTFontDescriptor, _ attribute: CFString) -> CFTypeRef?
```

## Parameters

- `descriptor` — The font descriptor.

- `attribute` — The requested attribute.

## Return Value

A retained reference to an arbitrary attribute, or `NULL` if the requested attribute is not present.

## Discussion

Refer to Accessing Font Attributes for documentation explaining how each attribute is packaged as a CFType object.

## See Also

### Getting Attributes

- [CTFontDescriptorCopyAttributes](<ctfontdescriptorcopyattributes(__).md>) — Returns the attributes dictionary of the font descriptor.
- [CTFontDescriptorCopyLocalizedAttribute](<ctfontdescriptorcopylocalizedattribute(______).md>) — Returns a localized value for the requested attribute, if available.
