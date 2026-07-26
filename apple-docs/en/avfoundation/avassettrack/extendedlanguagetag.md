---
title: extendedLanguageTag
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassettrack/extendedlanguagetag
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/extendedlanguagetag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/extendedlanguagetag.json'
content_hash: 'sha256:6756034dd8dd8981'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# extendedLanguageTag

<sub>Instance Property</sub>

The language tag of the track.

> [!warning] Deprecated
> Load the value of [extendedLanguageTag](../avpartialasyncproperty/extendedlanguagetag.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var extendedLanguageTag: String? { get }
```

## Discussion

The value is a [BCP-47](https://tools.ietf.org/html/bcp47) language tag, or `nil` if the track doesn’t specify a language tag.
