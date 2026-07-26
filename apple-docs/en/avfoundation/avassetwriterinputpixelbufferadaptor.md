---
title: AVAssetWriterInputPixelBufferAdaptor
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.1+（27.0 起废弃）, iPadOS 4.1+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetwriterinputpixelbufferadaptor
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputpixelbufferadaptor.json'
content_hash: 'sha256:20e91afb9c9650f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetWriterInputPixelBufferAdaptor

<sub>Class</sub>

An object that appends video samples to an asset writer input.

> [!warning] Deprecated
> Use AVAssetWriter.inputPixelBufferReceiver(for:pixelBufferAttributes:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetWriterInputPixelBufferAdaptor
```

## Overview

A pixel buffer adaptor provides a pixel buffer pool that you use to allocate pixel buffers to the output file. Using the provided pool for buffer allocation is typically more efficient than managing your own pool.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an adaptor

- [- initWithAssetWriterInput:sourcePixelBufferAttributes:](<avassetwriterinputpixelbufferadaptor/init(assetwriterinput_sourcepixelbufferattributes_).md>) — Creates a new pixel buffer adaptor to receive pixel buffers for writing to the output file. _(deprecated)_

### Appending pixel buffers

- [- appendPixelBuffer:withPresentationTime:](<avassetwriterinputpixelbufferadaptor/append(__withpresentationtime_).md>) — Appends a pixel buffer to the adaptor. _(deprecated)_

### Accessing the pool

- [pixelBufferPool](avassetwriterinputpixelbufferadaptor/pixelbufferpool.md) — A pool of pixel buffers to append to the adaptor’s input. _(deprecated)_
- [sourcePixelBufferAttributes](avassetwriterinputpixelbufferadaptor/sourcepixelbufferattributes.md) — The attributes of the pixel buffers that the pool contains. _(deprecated)_

### Inspecting a pixel buffer adaptor

- [assetWriterInput](avassetwriterinputpixelbufferadaptor/assetwriterinput.md) — The asset writer input to which the adaptor appends pixel buffers. _(deprecated)_

## See Also

### Media writing

- [Converting projected video to Apple Projected Media Profile](converting-projected-video-to-apple-projected-media-profile.md) — Convert content with equirectangular or half-equirectangular projection to APMP.
- [Converting side-by-side 3D video to multiview HEVC and spatial video](converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video.md) — Create video content for visionOS by converting an existing 3D HEVC file to a multiview HEVC format, optionally adding spatial metadata to create a spatial video.
- [Adding a display mask rectangle metadata track to a movie file](adding-a-display-mask-rectangle-metadata-track-to-a-movie-file.md) — Show a specific area of a video by using timed display mask rectangle metadata.
- [Writing fragmented MPEG-4 files for HTTP Live Streaming](writing-fragmented-mpeg-4-files-for-http-live-streaming.md) — Create an HTTP Live Streaming presentation by turning a movie file into a sequence of fragmented MPEG-4 files.
- [Creating spatial photos and videos with spatial metadata](../imageio/creating-spatial-photos-and-videos-with-spatial-metadata.md) — Add spatial metadata to stereo photos and videos to create spatial media for viewing on Apple Vision Pro.
- [Tagging media with video color information](tagging-media-with-video-color-information.md) — Inspect and set video color space information when writing and transcoding media.
- [Evaluating an app’s video color](evaluating-an-app-s-video-color.md) — Check color reproduction for a video in your app by using test patterns, video test equipment, and light-measurement instruments.
- [AVOutputSettingsAssistant](avoutputsettingsassistant.md) — An object that builds audio and video output settings dictionaries.
- [AVAssetWriter](avassetwriter.md) — An object that writes media data to a container file.
- [AVAssetWriterInput](avassetwriterinput.md) — An object that appends media samples to a track in an asset writer’s output file.
- [AVAssetWriterInputTaggedPixelBufferGroupAdaptor](avassetwriterinputtaggedpixelbuffergroupadaptor.md) — An object that appends tagged buffer groups to an asset writer input. _(deprecated)_
- [AVAssetWriterInputMetadataAdaptor](avassetwriterinputmetadataadaptor.md) — An object that appends timed metadata groups to an asset writer input. _(deprecated)_
- [AVAssetWriterInputGroup](avassetwriterinputgroup.md) — A group of inputs with tracks that are mutually exclusive to each other for playback or processing.
