---
title: NSMetadataQueryGatheringProgress
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsmetadataquerygatheringprogress
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsmetadataquerygatheringprogress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsmetadataquerygatheringprogress.json'
content_hash: 'sha256:55ff4155f6e059fe'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSMetadataQueryGatheringProgress

<sub>Type Property</sub>

Posted as the receiver is collecting results during the initial result-gathering phase of the query.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let NSMetadataQueryGatheringProgress: NSNotification.Name
```

## See Also

### Working with notifications

- [NSMetadataQueryDidFinishGatheringNotification](nsmetadataquerydidfinishgathering.md) — Posted when the receiver has finished with the initial result-gathering phase of the query.
- [NSMetadataQueryDidStartGatheringNotification](nsmetadataquerydidstartgathering.md) — Posted when the receiver begins with the initial result-gathering phase of the query.
- [NSMetadataQueryDidUpdateNotification](nsmetadataquerydidupdate.md) — Posted when the receiver’s results have changed during the live-update phase of the query.
