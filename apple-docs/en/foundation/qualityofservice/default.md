---
title: QualityOfService.default
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/qualityofservice/default
source_url: 'https://developer.apple.com/documentation/foundation/qualityofservice/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/qualityofservice/default.json'
content_hash: 'sha256:5673f3998ef0521e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [QualityOfService](../qualityofservice.md)

# QualityOfService.default

<sub>Case</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case `default`
```

## Discussion

Indicates no explicit quality of service information. Whenever possible, an appropriate quality of service is determined from available sources. Otherwise, some quality of service level between `NSQualityOfServiceUserInteractive` and `NSQualityOfServiceUtility` is used.

## See Also

### Constants

- [NSQualityOfServiceUserInteractive](userinteractive.md)
- [NSQualityOfServiceUserInitiated](userinitiated.md)
- [NSQualityOfServiceUtility](utility.md)
- [NSQualityOfServiceBackground](background.md)
