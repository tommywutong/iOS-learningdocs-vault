---
title: trackIDs
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassettrackgroup/trackids
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrackgroup/trackids'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrackgroup/trackids.json'
content_hash: 'sha256:57c4f825585f4405'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrackGroup](../avassettrackgroup.md)

# trackIDs

<sub>Instance Property</sub>

The IDs of the tracks in the group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var trackIDs: [NSNumber] { get }
```

## Discussion

The value of this property is an array of [NSNumber](../../foundation/nsnumber.md) instances used as [CMPersistentTrackID](../../coremedia/cmpersistenttrackid.md) values, one for each track in the group.
