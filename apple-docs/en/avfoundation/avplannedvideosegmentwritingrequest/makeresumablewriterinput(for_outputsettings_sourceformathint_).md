---
title: 'makeResumableWriterInput(for:outputSettings:sourceFormatHint:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avplannedvideosegmentwritingrequest/makeresumablewriterinput(for:outputsettings:sourceformathint:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplannedvideosegmentwritingrequest/makeresumablewriterinput(for:outputsettings:sourceformathint:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplannedvideosegmentwritingrequest/makeresumablewriterinput%28for%3Aoutputsettings%3Asourceformathint%3A%29.json'
content_hash: 'sha256:2935a788698c80cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlannedVideoSegmentWritingRequest](../avplannedvideosegmentwritingrequest.md)

# makeResumableWriterInput(for:outputSettings:sourceFormatHint:)

<sub>Instance Method</sub>

Helper function that returns a minimally configured AVAssetWriterInput object for writing the current segment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeResumableWriterInput(for mediaType: AVMediaType, outputSettings: [String : any Sendable]? = nil, sourceFormatHint: CMFormatDescription? = nil) throws -> AVAssetWriterInput
```

## Parameters

- `mediaType` — The type of media that an input accepts.

- `outputSettings` — The settings to use for configuring the AVAssetWriterInput object to be returned. Create an output settings dictionary manually, or use AVOutputSettingsAssistant to create preset-based settings.

- `sourceFormatHint` — A hint about the format of the media data to append. The input uses the source format hint to fill in missing output settings. If you specify a hint, you only need to specify AVFormatIDKey for the audio output settings, and AVVideoCodecKey is the only required key for video output settings. The system raises an error if the format description isn’t valid for the indicated media type.

## Return Value

A new writer input.

## Discussion

The final video encoder state from the previous segment will be restored before writing starts.

Clients using AVAssetWriterInput with video compression must use this method to create the writer input for writing the segment. The planner initializes the writer input in such a way that when writing starts, the video encoder’s state is restored to the final state of the last segment. The client should perform additional configurations on the returned writer input as needed, but must apply the same configurations for each segment of the track.

Client cannot call this method more than once on a writing request object. For the same segment writing request, this method and the “createResumableCompressionSessionWithAllocator” method are mutually exclusive. The client can call either one of the two, but not both. This method fails (returns nil) with error if the outputSettings or sourceFormatHint differs from the previous segment.

The writing request retains the writer input but does not mutate it after this method is returned.

> [!danger] Throws
> An error if the input cannot be created or if settings differ from previous segment.
