---
title: audioTrackGroupHandling
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession/audiotrackgrouphandling
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/audiotrackgrouphandling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/audiotrackgrouphandling.json'
content_hash: 'sha256:1b6d419f611fb76a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# audioTrackGroupHandling

<sub>Instance Property</sub>

A policy that defines how the session exports alternate audio tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var audioTrackGroupHandling: AVAssetTrackGroupOutputHandling { get set }
```

## Discussion

By default, a session exports only the enabled audio tracks within an alternate track group from the source asset. You can specify that the session preserve all audio tracks within an alternate track group by setting this value to [AVAssetTrackGroupOutputHandlingPreserveAlternateTracks](../avassettrackgroupoutputhandling/preservealternatetracks.md).

If no audio alternate track group is present, the value of this property has no effect. You can query the [trackGroups](../avpartialasyncproperty/trackgroups.md) property of [AVAsset](../avasset.md) to determine whether it contains audio track groups.

> [!important] Important
> You can’t specify alternate track output handling while also setting a value for the export session’s [audioMix](audiomix.md) property. The system throws an exception if you specify both.

## See Also

### Configuring track groups

- [AVAssetTrackGroupOutputHandling](../avassettrackgroupoutputhandling.md) — A type that specifies policies for how an export session processes alternate tracks in a track group.
