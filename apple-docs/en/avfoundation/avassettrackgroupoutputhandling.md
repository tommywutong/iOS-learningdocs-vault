---
title: AVAssetTrackGroupOutputHandling
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassettrackgroupoutputhandling
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrackgroupoutputhandling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrackgroupoutputhandling.json'
content_hash: 'sha256:35ea21240435dd2d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetTrackGroupOutputHandling

<sub>Structure</sub>

A type that specifies policies for how an export session processes alternate tracks in a track group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct AVAssetTrackGroupOutputHandling
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Policies

- [AVAssetTrackGroupOutputHandlingPreserveAlternateTracks](avassettrackgroupoutputhandling/preservealternatetracks.md) — A policy that passes through alternate audio tracks from the source asset during export.

### Initializers

- [init(rawValue:)](<avassettrackgroupoutputhandling/init(rawvalue_).md>) — Creates track group output handling structure with a raw value.

## See Also

### Configuring track groups

- [audioTrackGroupHandling](avassetexportsession/audiotrackgrouphandling.md) — A policy that defines how the session exports alternate audio tracks.
