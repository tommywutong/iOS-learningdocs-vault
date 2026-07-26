---
title: AVFragmentedAssetTrack
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avfragmentedassettrack
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentedassettrack'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentedassettrack.json'
content_hash: 'sha256:3e9cc0bb31a57bbf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVFragmentedAssetTrack

<sub>Class</sub>

An object that provides the track-level interface to inspect a fragmented asset’s media tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVFragmentedAssetTrack
```

## Overview

This class subclasses [AVAssetTrack](avassettrack.md). It has no methods or properties of its own.

## Relationships

- **Inherits From**: [AVAssetTrack](avassettrack.md)

- **Conforms To**: [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## See Also

### Fragmented assets

- [AVFragmentedAsset](avfragmentedasset.md) — An asset with a duration that the system can extend without modifying its existing media data.
- [AVFragmentedAssetMinder](avfragmentedassetminder.md) — An object that periodically checks whether the system adds new fragments to a fragmented asset.
- [AVFragmentMinding](avfragmentminding.md) — A protocol that defines whether an asset supports fragment minding.
