---
title: 'displayName(with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmediaselectionoption/displayname(with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/displayname(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectionoption/displayname%28with%3A%29.json'
content_hash: 'sha256:254162345e3cc960'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionOption](../avmediaselectionoption.md)

# displayName(with:)

<sub>Instance Method</sub>

Returns a string suitable for display using the specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func displayName(with locale: Locale) -> String
```

## Parameters

- `locale` — The locale to use in generating the display name.

## Return Value

A string containing the localized display name.

## Discussion

The string takes into account this option’s common metadata, media characteristics and locale properties in addition to the provided locale to formulate a string intended for display

## See Also

### Getting the language and locale settings

- [displayName](displayname.md) — A string suitable for display using the current system locale.
- [locale](locale.md) — The locale for which the media option was authored.
- [extendedLanguageTag](extendedlanguagetag.md) — The IETF BCP 47 language tag associated with the option
