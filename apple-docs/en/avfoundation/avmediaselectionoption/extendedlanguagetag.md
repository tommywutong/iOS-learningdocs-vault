---
title: extendedLanguageTag
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediaselectionoption/extendedlanguagetag
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/extendedlanguagetag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectionoption/extendedlanguagetag.json'
content_hash: 'sha256:9c3384976275fd3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionOption](../avmediaselectionoption.md)

# extendedLanguageTag

<sub>Instance Property</sub>

The IETF BCP 47 language tag associated with the option

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var extendedLanguageTag: String? { get }
```

## Discussion

This property may be `nil` indicating that the underlying media presented when the option is selected carries no language information. This can occur with media formats for which language information is optional, such as HTTP Live Streaming playlists, or that do not accommodate language information in machine-readable form.

Clients that are filtering media selection options by language should be prepared to handle cases in which this value is `nil`. Further, they should be prepared to handle cases in which an `extendedLanguageTag` is present but indicates that the language is “undetermined” (a language value of @“und”, as defined in ISO 639-2).

## See Also

### Getting the language and locale settings

- [displayName](displayname.md) — A string suitable for display using the current system locale.
- [- displayNameWithLocale:](<displayname(with_).md>) — Returns a string suitable for display using the specified locale.
- [locale](locale.md) — The locale for which the media option was authored.
