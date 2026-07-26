---
title: QualityOfService.utility
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/qualityofservice/utility
source_url: 'https://developer.apple.com/documentation/foundation/qualityofservice/utility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/qualityofservice/utility.json'
content_hash: 'sha256:f7f5286f56cc7ec6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [QualityOfService](../qualityofservice.md)

# QualityOfService.utility

<sub>Case</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case utility
```

## Discussion

Used for performing work which the user is unlikely to be immediately waiting for the results. This work may have been requested by the user or initiated automatically, and often operates at user-visible timescales using a non-modal progress indicator. For example, periodic content updates or bulk file operations, such as media import.

## See Also

### Constants

- [NSQualityOfServiceUserInteractive](userinteractive.md)
- [NSQualityOfServiceUserInitiated](userinitiated.md)
- [NSQualityOfServiceBackground](background.md)
- [NSQualityOfServiceDefault](default.md)
