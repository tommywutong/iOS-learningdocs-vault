---
title: AVAssetReaderOutputMetadataAdaptor
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetreaderoutputmetadataadaptor
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutputmetadataadaptor.json'
content_hash: 'sha256:cfe724ed4f13ac64'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetReaderOutputMetadataAdaptor

<sub>Class</sub>

An object that creates timed metadata group objects for an asset track.

> [!warning] Deprecated
> Use AVAssetReader.outputMetadataProvider(for:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetReaderOutputMetadataAdaptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a metadata adaptor

- [- initWithAssetReaderTrackOutput:](<avassetreaderoutputmetadataadaptor/init(assetreadertrackoutput_).md>) — Creates an object that reads timed metadata groups from an asset reader output. _(deprecated)_

### Retrieving timed metadata groups

- [- nextTimedMetadataGroup](<avassetreaderoutputmetadataadaptor/nexttimedmetadatagroup().md>) — Returns the next timed metadata group for the asset reader output. _(deprecated)_

### Inspecting the track output

- [assetReaderTrackOutput](avassetreaderoutputmetadataadaptor/assetreadertrackoutput.md) — The asset reader track output that provides the timed metadata groups. _(deprecated)_

## See Also

### Media reading

- [Reading multiview 3D video files](reading-multiview-3d-video-files.md) — Render single images for the left eye and right eye from a multiview High Efficiency Video Coding format file by reading individual video frames.
- [AVAssetReader](avassetreader.md) — An object that reads media data from an asset.
- [AVAssetReaderOutput](avassetreaderoutput.md) — An abstract class that defines the interface to read media samples from an asset reader.
- [AVAssetReaderTrackOutput](avassetreadertrackoutput.md) — An object that reads media data from a single track of an asset.
- [AVAssetReaderAudioMixOutput](avassetreaderaudiomixoutput.md) — An object that reads audio samples that result from mixing audio from one or more tracks.
- [AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md) — An object that reads composited video frames from one or more tracks of an asset.
- [AVAssetReaderSampleReferenceOutput](avassetreadersamplereferenceoutput.md) — An object that reads sample references from an asset track.
