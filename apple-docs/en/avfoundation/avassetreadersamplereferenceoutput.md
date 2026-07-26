---
title: AVAssetReaderSampleReferenceOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreadersamplereferenceoutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreadersamplereferenceoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreadersamplereferenceoutput.json'
content_hash: 'sha256:8c4d2d70c1b4805d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetReaderSampleReferenceOutput

<sub>Class</sub>

An object that reads sample references from an asset track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetReaderSampleReferenceOutput
```

## Overview

Apps can extract information about the location of samples in a track — the file URL and offset — by adding an instance of this class to an asset reader. Read the [kCMSampleBufferAttachmentKey_SampleReferenceURL](../coremedia/kcmsamplebufferattachmentkey_samplereferenceurl.md) and [kCMSampleBufferAttachmentKey_SampleReferenceByteOffset](../coremedia/kcmsamplebufferattachmentkey_samplereferencebyteoffset.md) attachments on the extracted sample buffers to get the location of the sample data.

You can also append sample buffers that you extract using this class to an [AVAssetWriterInput](avassetwriterinput.md) instance to create movie tracks that aren’t self-contained and reference data in the original file instead. To write tracks that aren’t self-contained, use instances of [AVAssetWriter](avassetwriter.md) that you configure to write files of type [AVFileTypeQuickTimeMovie](avfiletype/mov.md).

Because this output doesn’t return sample data, it ignores the value of the [alwaysCopiesSampleData](avassetreaderoutput/alwayscopiessampledata.md) property.

## Relationships

- **Inherits From**: [AVAssetReaderOutput](avassetreaderoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a sample reference output

- [- initWithTrack:](<avassetreadersamplereferenceoutput/init(track_).md>) — Creates an object that supplies sample references.

### Inspecting the track

- [track](avassetreadersamplereferenceoutput/track.md) — The track from which the output reads sample references.

## See Also

### Media reading

- [Reading multiview 3D video files](reading-multiview-3d-video-files.md) — Render single images for the left eye and right eye from a multiview High Efficiency Video Coding format file by reading individual video frames.
- [AVAssetReader](avassetreader.md) — An object that reads media data from an asset.
- [AVAssetReaderOutput](avassetreaderoutput.md) — An abstract class that defines the interface to read media samples from an asset reader.
- [AVAssetReaderTrackOutput](avassetreadertrackoutput.md) — An object that reads media data from a single track of an asset.
- [AVAssetReaderAudioMixOutput](avassetreaderaudiomixoutput.md) — An object that reads audio samples that result from mixing audio from one or more tracks.
- [AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md) — An object that reads composited video frames from one or more tracks of an asset.
- [AVAssetReaderOutputMetadataAdaptor](avassetreaderoutputmetadataadaptor.md) — An object that creates timed metadata group objects for an asset track. _(deprecated)_
