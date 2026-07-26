---
title: 'CTFontDescriptorCopyLocalizedAttribute(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontdescriptorcopylocalizedattribute(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontdescriptorcopylocalizedattribute(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontdescriptorcopylocalizedattribute%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:fb93eec75b9eb850'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontDescriptorCopyLocalizedAttribute(_:_:_:)

<sub>Function</sub>

Returns a localized value for the requested attribute, if available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontDescriptorCopyLocalizedAttribute(_ descriptor: CTFontDescriptor, _ attribute: CFString, _ language: UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFTypeRef?
```

## Parameters

- `descriptor` — The font descriptor.

- `attribute` — The requested font attribute.

- `language` — On output, contains a reference to the matched language. The language identifier will conform to the RFC 3066bis standard.

## Return Value

A retained reference to a localized attribute based on the global language list.

## Discussion

This function passes back the matched language in `language`. If localization is not possible for the attribute, the behavior matches the value returned from [CTFontDescriptorCopyAttribute](<ctfontdescriptorcopyattribute(____).md>). Generally, localization of attributes is applicable to name attributes of only a normalized font descriptor.

## See Also

### Getting Attributes

- [CTFontDescriptorCopyAttributes](<ctfontdescriptorcopyattributes(__).md>) — Returns the attributes dictionary of the font descriptor.
- [CTFontDescriptorCopyAttribute](<ctfontdescriptorcopyattribute(____).md>) — Returns the value associated with an arbitrary attribute.
