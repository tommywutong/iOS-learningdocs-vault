---
title: makeNowPlayingInfoLanguageOption()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediaselectionoption/makenowplayinginfolanguageoption()
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/makenowplayinginfolanguageoption()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectionoption/makenowplayinginfolanguageoption%28%29.json'
content_hash: 'sha256:5c2879d37cc8c9a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionOption](../avmediaselectionoption.md)

# makeNowPlayingInfoLanguageOption()

<sub>Instance Method</sub>

Creates a language option for a media selection option.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeNowPlayingInfoLanguageOption() -> MPNowPlayingInfoLanguageOption?
```

## Return Value

A new language option, or `nil` if the media selection option isn’t an audible or legible option.
