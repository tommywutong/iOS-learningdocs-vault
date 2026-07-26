---
title: displayName
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediaselectionoption/displayname
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/displayname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectionoption/displayname.json'
content_hash: 'sha256:fe2276a18d21a1e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionOption](../avmediaselectionoption.md)

# displayName

<sub>Instance Property</sub>

A string suitable for display using the current system locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var displayName: String { get }
```

## Discussion

The string takes into account this option’s common metadata, media characteristics, and locale properties in addition to the provided locale to formulate a string intended for display

## See Also

### Getting the language and locale settings

- [- displayNameWithLocale:](<displayname(with_).md>) — Returns a string suitable for display using the specified locale.
- [locale](locale.md) — The locale for which the media option was authored.
- [extendedLanguageTag](extendedlanguagetag.md) — The IETF BCP 47 language tag associated with the option
