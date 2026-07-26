---
title: languageCode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassettrack/languagecode
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/languagecode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/languagecode.json'
content_hash: 'sha256:a4e8c30bc3be6ea2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# languageCode

<sub>Instance Property</sub>

The language code of the track.

> [!warning] Deprecated
> Load the value of [languageCode](../avpartialasyncproperty/languagecode.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var languageCode: String? { get }
```

## Discussion

The value is an ISO 639-2/T language code, or `nil` if the track doesn’t specify a language code.
