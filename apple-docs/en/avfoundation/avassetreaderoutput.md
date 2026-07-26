---
title: AVAssetReaderOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreaderoutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutput.json'
content_hash: 'sha256:eadf2175958a66ab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetReaderOutput

<sub>Class</sub>

An abstract class that defines the interface to read media samples from an asset reader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetReaderOutput
```

## Overview

You add concrete output instances, such as [AVAssetReaderTrackOutput](avassetreadertrackoutput.md) or [AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md), to an asset reader to perform specific tasks.

> [!important] Important
> If you don’t require modifying sample data in-place, set the value of the [alwaysCopiesSampleData](avassetreaderoutput/alwayscopiessampledata.md) property to [false](../swift/false.md) to prevent the output from making unnecessary copies.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVAssetReaderAudioMixOutput](avassetreaderaudiomixoutput.md), [AVAssetReaderSampleReferenceOutput](avassetreadersamplereferenceoutput.md), [AVAssetReaderTrackOutput](avassetreadertrackoutput.md), [AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring reading

- [alwaysCopiesSampleData](avassetreaderoutput/alwayscopiessampledata.md) — A Boolean value that indicates whether the output vends copied sample data. _(deprecated)_
- [supportsRandomAccess](avassetreaderoutput/supportsrandomaccess.md) — A Boolean value that indicates whether the output supports reconfiguring the time ranges it reads. _(deprecated)_
- [- resetForReadingTimeRanges:](<avassetreaderoutput/reset(forreadingtimeranges_).md>) — Restarts reading with a new set of time ranges. _(deprecated)_
- [- markConfigurationAsFinal](<avassetreaderoutput/markconfigurationasfinal().md>) — Tells the output that it’s finished reconfiguring time ranges, and allows the asset reader to advance to a completed state. _(deprecated)_

### Copying sample buffers

- [- copyNextSampleBuffer](<avassetreaderoutput/copynextsamplebuffer().md>) — Copies the next sample buffer from the output. _(deprecated)_
- [Provider](avassetreaderoutput/provider.md) — An object that reads a collection of samples of a common media type from an asset reader.
- [RandomAccessController](avassetreaderoutput/randomaccesscontroller.md) — Object used to reset an output provider to read specified time ranges.
- [SupportedPayload](avassetreaderoutput/supportedpayload.md)

### Inspecting the media type

- [mediaType](avassetreaderoutput/mediatype.md) — The media type of samples that the output reads.

## See Also

### Media reading

- [Reading multiview 3D video files](reading-multiview-3d-video-files.md) — Render single images for the left eye and right eye from a multiview High Efficiency Video Coding format file by reading individual video frames.
- [AVAssetReader](avassetreader.md) — An object that reads media data from an asset.
- [AVAssetReaderTrackOutput](avassetreadertrackoutput.md) — An object that reads media data from a single track of an asset.
- [AVAssetReaderAudioMixOutput](avassetreaderaudiomixoutput.md) — An object that reads audio samples that result from mixing audio from one or more tracks.
- [AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md) — An object that reads composited video frames from one or more tracks of an asset.
- [AVAssetReaderSampleReferenceOutput](avassetreadersamplereferenceoutput.md) — An object that reads sample references from an asset track.
- [AVAssetReaderOutputMetadataAdaptor](avassetreaderoutputmetadataadaptor.md) — An object that creates timed metadata group objects for an asset track. _(deprecated)_
