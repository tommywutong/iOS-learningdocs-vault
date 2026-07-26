---
title: AVAssetWriterInput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput.json'
content_hash: 'sha256:aa440e5938e0c02d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetWriterInput

<sub>Class</sub>

An object that appends media samples to a track in an asset writer’s output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetWriterInput
```

## Overview

Create an asset writer input to write a single track of media, and optional track-level metadata, to the output file. To write multiple concurrent tracks with ideal interleaving of media data, observe the value of the [readyForMoreMediaData](avassetwriterinput/isreadyformoremediadata.md) property of each input.

You can use an asset writer input to create tracks in a QuickTime movie file that aren’t self-contained, and instead reference sample data that exists in another file.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an input

- [- initWithMediaType:outputSettings:](<avassetwriterinput/init(mediatype_outputsettings_).md>) — Creates an input to append sample buffers of the specified type to the output file.
- [- initWithMediaType:outputSettings:sourceFormatHint:](<avassetwriterinput/init(mediatype_outputsettings_sourceformathint_).md>) — Creates an input that appends sample buffers of the specified type and format hint to the output file.

### Configuring presentation

- [naturalSize](avassetwriterinput/naturalsize.md) — The natural display dimensions of the output’s visual media.
- [transform](avassetwriterinput/transform.md) — The transform to use for display of the output’s visual media.
- [preferredVolume](avassetwriterinput/preferredvolume.md) — The volume to prefer for playback of the output’s audio data.
- [mediaTimeScale](avassetwriterinput/mediatimescale.md) — The time scale of the track in the output file.
- [marksOutputTrackAsEnabled](avassetwriterinput/marksoutputtrackasenabled.md) — A Boolean value that indicates whether to enable a track in the output for playback and processing.

### Configuring language support

- [languageCode](avassetwriterinput/languagecode.md) — The language code of the input’s track.
- [extendedLanguageTag](avassetwriterinput/extendedlanguagetag.md) — The extended language for the input’s track.

### Configuring metadata

- [metadata](avassetwriterinput/metadata.md) — The track-level metadata to write to the output.

### Configuring media data layout

- [preferredMediaChunkAlignment](avassetwriterinput/preferredmediachunkalignment.md) — The boundary, in bytes, for aligning media chunks.
- [preferredMediaChunkDuration](avassetwriterinput/preferredmediachunkduration.md) — The duration to use for each chunk of sample data in the output file.
- [sampleReferenceBaseURL](avassetwriterinput/samplereferencebaseurl.md) — The base URL sample references are relative to.
- [mediaDataLocation](avassetwriterinput/mediadatalocation-swift.property.md) — Specifies how the input lays out and interleaves media data.
- [MediaDataLocation](avassetwriterinput/mediadatalocation-swift.struct.md) — A structure that indicates how to lay out and interleave media data.

### Configuring track associations

- [- canAddTrackAssociationWithTrackOfInput:type:](<avassetwriterinput/canaddtrackassociation(withtrackof_type_).md>) — Determines whether it’s valid to associate another input’s track with this input’s track.
- [- addTrackAssociationWithTrackOfInput:type:](<avassetwriterinput/addtrackassociation(withtrackof_type_).md>) — Adds an association between input tracks.

### Appending media samples

- [expectsMediaDataInRealTime](avassetwriterinput/expectsmediadatainrealtime.md) — A Boolean value that indicates whether the input tailors its processing for real-time sources. _(deprecated)_
- [readyForMoreMediaData](avassetwriterinput/isreadyformoremediadata.md) — A Boolean value that indicates whether the input is ready to accept media data. _(deprecated)_
- [- requestMediaDataWhenReadyOnQueue:usingBlock:](<avassetwriterinput/requestmediadatawhenready(on_using_).md>) — Tells the input to request media data, at its convenience, to write to the output file. _(deprecated)_
- [- appendSampleBuffer:](<avassetwriterinput/append(__).md>) — Appends a sample buffer to an input to write to the output file. _(deprecated)_
- [- markAsFinished](<avassetwriterinput/markasfinished().md>) — Marks the input as finished to indicate that you’re done appending samples to it.
- [SampleBufferReceiver](avassetwriterinput/samplebufferreceiver.md) — Provides an interface for writing sample buffers to an input.
- [PixelBufferReceiver](avassetwriterinput/pixelbufferreceiver.md) — Provides an interface for writing pixel buffers to an input.
- [TaggedPixelBufferGroupReceiver](avassetwriterinput/taggedpixelbuffergroupreceiver.md) — Provides an interface for writing tagged pixel buffers to an input.
- [MetadataReceiver](avassetwriterinput/metadatareceiver.md) — Provides an interface for writing timed metadata groups to an input.
- [CaptionReceiver](avassetwriterinput/captionreceiver.md) — Provides an interface for writing caption data to an input.

### Performing multiple-pass encoding

- [canPerformMultiplePasses](avassetwriterinput/canperformmultiplepasses.md) — A Boolean value that indicates whether the input may perform multiple passes over appended media data.
- [currentPassDescription](avassetwriterinput/currentpassdescription.md) — An object that describes the requirements for the current pass.
- [AVAssetWriterInputPassDescription](avassetwriterinputpassdescription.md) — An object that defines the interface to query for the requirements of the current pass.
- [- markCurrentPassAsFinished](<avassetwriterinput/markcurrentpassasfinished().md>) — Tells the input to analyze the appended media to determine whether it can improve the results by reencoding certain segments.
- [performsMultiPassEncodingIfSupported](avassetwriterinput/performsmultipassencodingifsupported.md) — A Boolean value that indicates whether the input attempts to encode the source media data using multiple passes.
- [- respondToEachPassDescriptionOnQueue:usingBlock:](<avassetwriterinput/respondtoeachpassdescription(on_using_).md>) — Tells the input to invoke a callback whenever it begins a new pass.
- [MultiPassController](avassetwriterinput/multipasscontroller.md) — Provides an interface to receive an async sequence of pass descriptions for the writer input receiver, if multi-pass is supported.

### Inspecting an input

- [mediaType](avassetwriterinput/mediatype.md) — The media type of the samples that the input accepts.
- [outputSettings](avassetwriterinput/outputsettings.md) — The settings to use for encoding media data you append to the output.
- [sourceFormatHint](avassetwriterinput/sourceformathint.md) — A hint about the format of the sample buffers to append to the input.

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
- [AVAssetWriterInputPixelBufferAdaptor](avassetwriterinputpixelbufferadaptor.md) — An object that appends video samples to an asset writer input. _(deprecated)_
- [AVAssetWriterInputTaggedPixelBufferGroupAdaptor](avassetwriterinputtaggedpixelbuffergroupadaptor.md) — An object that appends tagged buffer groups to an asset writer input. _(deprecated)_
- [AVAssetWriterInputMetadataAdaptor](avassetwriterinputmetadataadaptor.md) — An object that appends timed metadata groups to an asset writer input. _(deprecated)_
- [AVAssetWriterInputGroup](avassetwriterinputgroup.md) — A group of inputs with tracks that are mutually exclusive to each other for playback or processing.
