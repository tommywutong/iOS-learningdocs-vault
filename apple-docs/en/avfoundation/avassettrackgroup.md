---
title: AVAssetTrackGroup
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassettrackgroup
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrackgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrackgroup.json'
content_hash: 'sha256:bad0e4ecd4ab66fc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetTrackGroup

<sub>Class</sub>

A group of related tracks in an asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVAssetTrackGroup
```

## Overview

A track group describes a group of related alternative tracks, only one of which should play at a time. Groups of alternative tracks typically contain variations of the same content, like subtitles in multiple translations.

You can inspect an asset’s track groups by loading the value of its [trackGroups](avpartialasyncproperty/trackgroups.md) property.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting track ID values

- [trackIDs](avassettrackgroup/trackids.md) — The IDs of the tracks in the group.

## See Also

### Assets

- [AVAsset](avasset.md) — An object that models timed audiovisual media.
- [AVURLAsset](avurlasset.md) — An asset that represents media at a local or remote URL.
- [AVAssetTrack](avassettrack.md) — An object that models a track of media that an asset contains.
- [AVAssetTrackSegment](avassettracksegment.md) — An object that represents a time range segment of an asset track.
