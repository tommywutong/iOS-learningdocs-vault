---
title: makeNowPlayingInfoLanguageOptionGroup()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediaselectiongroup/makenowplayinginfolanguageoptiongroup()
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/makenowplayinginfolanguageoptiongroup()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectiongroup/makenowplayinginfolanguageoptiongroup%28%29.json'
content_hash: 'sha256:7f1969ef31c05bec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionGroup](../avmediaselectiongroup.md)

# makeNowPlayingInfoLanguageOptionGroup()

<sub>Instance Method</sub>

Creates a language option group from the media selection group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeNowPlayingInfoLanguageOptionGroup() -> MPNowPlayingInfoLanguageOptionGroup
```

## Return Value

The new language option group.

## Discussion

Any option from [AVMediaSelectionOption](../avmediaselectionoption.md) in the [AVMediaSelectionGroup](../avmediaselectiongroup.md) not representing an audible or legible selection option is ignored.
