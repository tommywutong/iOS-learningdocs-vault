---
title: AVAssetWriter
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter.json'
content_hash: 'sha256:75a1ad4179371601'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetWriter

<sub>Class</sub>

An object that writes media data to a container file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetWriter
```

## Overview

You use an asset writer to write media to file formats such as the QuickTime movie file format and MPEG-4 file format. An asset writer automatically supports interleaving media data from concurrent tracks for efficient playback and storage. It can reencode media samples it writes to the output file, and may also write collections of metadata to the output file.

> [!important] Important
> An asset writer is a single-use object that writes one output file. Create multiple asset writer instances if your app requires writing multiple output files.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an asset writer

- [+ assetWriterWithURL:fileType:error:](<avassetwriter/init(url_filetype_)-xt34.md>) — Returns a new object that writes media data to a container file at the output URL.
- [- initWithURL:fileType:error:](<avassetwriter/init(outputurl_filetype_).md>) — Creates an object that writes media data to a container file at the output URL.
- [- initWithContentType:](<avassetwriter/init(contenttype_).md>) — Creates an object that outputs segment data in a specified container format.

### Configuring inputs

- [inputs](avassetwriter/inputs.md) — The inputs an asset writer contains.
- [availableMediaTypes](avassetwriter/availablemediatypes.md) — The media types the asset writer supports adding as inputs.
- [- canApplyOutputSettings:forMediaType:](<avassetwriter/canapply(outputsettings_formediatype_).md>) — Determines whether the output file format supports the output settings for a specific media type.
- [- canAddInput:](<avassetwriter/canadd(__)-6al7j.md>) — Determines whether the asset writer supports adding the input.
- [- addInput:](<avassetwriter/add(__)-4c4d0.md>) — Adds an input to an asset writer. _(deprecated)_

### Configuring input receivers

- [inputReceiver(for:)](<avassetwriter/inputreceiver(for_).md>) — Attaches the input to the writer and returns an input receiver for writing sample buffers.
- [inputCaptionReceiver(for:)](<avassetwriter/inputcaptionreceiver(for_).md>) — Attaches the input to the writer and returns an input receiver for writing caption data.
- [inputCaptionReceiverRequestingMultiPass(for:)](<avassetwriter/inputcaptionreceiverrequestingmultipass(for_).md>) — Attaches the input to the writer and returns a tuple with an input receiver for writing caption data, and an associated multi pass controller.
- [inputMetadataReceiver(for:)](<avassetwriter/inputmetadatareceiver(for_).md>) — Attaches the input to the writer and returns an input receiver for writing timed metadata group.
- [inputMetadataReceiverRequestingMultiPass(for:)](<avassetwriter/inputmetadatareceiverrequestingmultipass(for_).md>) — Attaches the input to the writer and returns a tuple with an input receiver for writing timed metadata group, and an associated multi pass controller.
- [inputPixelBufferReceiver(for:pixelBufferAttributes:)](<avassetwriter/inputpixelbufferreceiver(for_pixelbufferattributes_).md>) — Attaches the input to the writer and returns an input receiver for writing pixel buffers.
- [inputPixelBufferReceiverRequestingMultiPass(for:pixelBufferAttributes:)](<avassetwriter/inputpixelbufferreceiverrequestingmultipass(for_pixelbufferattributes_).md>) — Attaches the input to the writer and returns a tuple with an input receiver for writing pixel buffers, and an associated multi pass controller.
- [inputReceiverRequestingMultiPass(for:)](<avassetwriter/inputreceiverrequestingmultipass(for_).md>) — Attaches the input to the writer and returns a tuple with an input receiver for writing sample buffers, and an associated multi pass controller.
- [inputTaggedPixelBufferGroupReceiver(for:pixelBufferAttributes:)](<avassetwriter/inputtaggedpixelbuffergroupreceiver(for_pixelbufferattributes_).md>) — Attaches the input to the writer and returns an input receiver for writing tagged pixel buffers.
- [inputTaggedPixelBufferGroupReceiverRequestingMultiPass(for:pixelBufferAttributes:)](<avassetwriter/inputtaggedpixelbuffergroupreceiverrequestingmultipass(for_pixelbufferattributes_).md>) — Attaches the input to the writer and returns a tuple with an input receiver for writing tagged pixel buffers, and an associated multi pass controller.

### Configuring input groups

- [inputGroups](avassetwriter/inputgroups.md) — The input groups an asset writer contains.
- [- canAddInputGroup:](<avassetwriter/canadd(__)-8s1oh.md>) — Determines whether the asset writer supports adding the input group.
- [- addInputGroup:](<avassetwriter/add(__)-3san4.md>) — Adds an input group to an asset writer.

### Configuring output

- [metadata](avassetwriter/metadata.md) — An array of metadata items to write to the output file.
- [shouldOptimizeForNetworkUse](avassetwriter/shouldoptimizefornetworkuse.md) — A Boolean value that indicates whether to write the output file to make it more suitable for playback over a network.
- [directoryForTemporaryFiles](avassetwriter/directoryfortemporaryfiles.md) — A directory to contain temporary files that the export process generates.

### Configuring fragment output

- [movieFragmentInterval](avassetwriter/moviefragmentinterval.md) — The interval at which to write movie fragments.
- [initialMovieFragmentInterval](avassetwriter/initialmoviefragmentinterval.md) — The interval at which to write the initial movie fragment.
- [initialMovieFragmentSequenceNumber](avassetwriter/initialmoviefragmentsequencenumber.md) — The sequence number of the initial movie fragment.
- [producesCombinableFragments](avassetwriter/producescombinablefragments.md) — A Boolean value that indicates whether the asset writer outputs movie fragments suitable for combining with others.
- [overallDurationHint](avassetwriter/overalldurationhint.md) — A hint of the final duration of the output file.
- [movieTimeScale](avassetwriter/movietimescale.md) — The time scale of the movie.

### Managing writing sessions

- [start()](<avassetwriter/start().md>) — Prepares the writer to write media data to its output file.
- [- startWriting](<avassetwriter/startwriting().md>) — Tells the writer to start writing its output. _(deprecated)_
- [- startSessionAtSourceTime:](<avassetwriter/startsession(atsourcetime_).md>) — Starts an asset-writing session.
- [- endSessionAtSourceTime:](<avassetwriter/endsession(atsourcetime_).md>) — Finishes an asset-writing session.
- [- finishWritingWithCompletionHandler:](<avassetwriter/finishwriting(completionhandler_).md>) — Marks all unfinished inputs as finished and completes the writing of the output file.
- [- cancelWriting](<avassetwriter/cancelwriting().md>) — Cancels the creation of the output file.
- [- finishWriting](<avassetwriter/finishwriting().md>) — Completes the writing of the output file. _(deprecated)_

### Inspecting writing status

- [status](avassetwriter/status-swift.property.md) — The status of writing samples to the output file.
- [Status](avassetwriter/status-swift.enum.md) — Values that indicate the state of an asset writer.
- [error](avassetwriter/error.md) — An error object that describes an asset-writing failure.

### Configuring segment writing

- [delegate](avassetwriter/delegate.md) — A delegate object that responds to asset-writing events.
- [AVAssetWriterDelegate](avassetwriterdelegate.md) — A delegate protocol that defines the methods to implement to respond to asset-writing events.
- [preferredOutputSegmentInterval](avassetwriter/preferredoutputsegmentinterval.md) — The interval of output segments that you prefer.
- [initialSegmentStartTime](avassetwriter/initialsegmentstarttime.md) — The start time of the initial segment.
- [outputFileTypeProfile](avassetwriter/outputfiletypeprofile.md) — A profile for the output file type.
- [- flushSegment](<avassetwriter/flushsegment().md>) — Closes the current segment and outputs it to a delegate method.

### Accessing output settings

- [outputURL](avassetwriter/outputurl.md) — The location of the container file that the writer outputs.
- [outputFileType](avassetwriter/outputfiletype.md) — The type of container file that the writer outputs.

### Initializers

- [init(URL:fileType:)](<avassetwriter/init(url_filetype_)-24qcl.md>)
- [init(URL:fileType:)](<avassetwriter/init(url_filetype_)-9j3k4.md>)

### Instance Properties

- [proVideoStorageSupported](avassetwriter/isprovideostoragesupported.md) — Indicates whether the receiver supports writing to pre-allocated storage on this device for high data rate video capture formats such as ProRes. _(beta)_
- [usesProVideoStorage](avassetwriter/usesprovideostorage.md) — Indicates whether to use pre-allocated storage. _(beta)_

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
- [AVAssetWriterInput](avassetwriterinput.md) — An object that appends media samples to a track in an asset writer’s output file.
- [AVAssetWriterInputPixelBufferAdaptor](avassetwriterinputpixelbufferadaptor.md) — An object that appends video samples to an asset writer input. _(deprecated)_
- [AVAssetWriterInputTaggedPixelBufferGroupAdaptor](avassetwriterinputtaggedpixelbuffergroupadaptor.md) — An object that appends tagged buffer groups to an asset writer input. _(deprecated)_
- [AVAssetWriterInputMetadataAdaptor](avassetwriterinputmetadataadaptor.md) — An object that appends timed metadata groups to an asset writer input. _(deprecated)_
- [AVAssetWriterInputGroup](avassetwriterinputgroup.md) — A group of inputs with tracks that are mutually exclusive to each other for playback or processing.
