---
title: AVAssetReader
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreader
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreader'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreader.json'
content_hash: 'sha256:45d992ae92c73cc4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetReader

<sub>Class</sub>

An object that reads media data from an asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetReader
```

## Overview

Use an asset reader to read media data from instances of [AVAsset](avasset.md). The assets you read may represent file-based media like QuickTime movies or MPEG-4 files, or media that you compose from multiple sources using [AVComposition](avcomposition.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an asset reader

- [- initWithAsset:error:](<avassetreader/init(asset_).md>) — Creates an object to read media data from an asset.

### Managing outputs

- [- canAddOutput:](<avassetreader/canadd(__).md>) — Determines whether you can add the output to the asset reader.
- [- addOutput:](<avassetreader/add(__).md>) — Adds an output to the reader. _(deprecated)_
- [outputs](avassetreader/outputs.md) — The outputs from which you read media data.

### Accessing output providers

- [outputProvider(for:)](<avassetreader/outputprovider(for_).md>) — Attaches the output to the reader and returns an output provider for reading sample buffers.
- [outputProviderWithRandomAccess(for:)](<avassetreader/outputproviderwithrandomaccess(for_).md>) — Attaches the output to the reader and returns a tuple with an output provider for reading sample buffers, and an associated random access controller.
- [outputCaptionProvider(for:validationDelegate:)](<avassetreader/outputcaptionprovider(for_validationdelegate_).md>) — Attaches the output to the reader and returns an output provider for reading caption groups.
- [outputCaptionProviderWithRandomAccess(for:validationDelegate:)](<avassetreader/outputcaptionproviderwithrandomaccess(for_validationdelegate_).md>) — Attaches the output to the reader and returns a tuple with an output provider for reading caption groups, and an associated random access controller.
- [outputMetadataProvider(for:)](<avassetreader/outputmetadataprovider(for_).md>) — Attaches the output to the reader and returns an output provider for reading timed metadata groups.
- [outputMetadataProviderWithRandomAccess(for:)](<avassetreader/outputmetadataproviderwithrandomaccess(for_).md>) — Attaches the output to the reader and returns a tuple with an output provider for timed metadata groups buffers, and an associated random access controller.

### Configuring reading

- [timeRange](avassetreader/timerange.md) — The time range within the asset to read.
- [status](avassetreader/status-swift.property.md) — The status of reading sample buffers from the asset.
- [Status](avassetreader/status-swift.enum.md) — Values that represent the possible states of an asset reader.
- [error](avassetreader/error.md) — An error that describes the reason for a failure.

### Controlling reading

- [start()](<avassetreader/start().md>) — Prepares the reader to read media data from the asset.
- [- startReading](<avassetreader/startreading().md>) — Prepares the asset reader to start reading sample buffers from the asset. _(deprecated)_
- [- cancelReading](<avassetreader/cancelreading().md>) — Cancels any background work and stops the reader’s outputs from reading more samples.

### Inspecting the asset

- [asset](avassetreader/asset.md) — The asset from which to read media data.

## See Also

### Media reading

- [Reading multiview 3D video files](reading-multiview-3d-video-files.md) — Render single images for the left eye and right eye from a multiview High Efficiency Video Coding format file by reading individual video frames.
- [AVAssetReaderOutput](avassetreaderoutput.md) — An abstract class that defines the interface to read media samples from an asset reader.
- [AVAssetReaderTrackOutput](avassetreadertrackoutput.md) — An object that reads media data from a single track of an asset.
- [AVAssetReaderAudioMixOutput](avassetreaderaudiomixoutput.md) — An object that reads audio samples that result from mixing audio from one or more tracks.
- [AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md) — An object that reads composited video frames from one or more tracks of an asset.
- [AVAssetReaderSampleReferenceOutput](avassetreadersamplereferenceoutput.md) — An object that reads sample references from an asset track.
- [AVAssetReaderOutputMetadataAdaptor](avassetreaderoutputmetadataadaptor.md) — An object that creates timed metadata group objects for an asset track. _(deprecated)_
