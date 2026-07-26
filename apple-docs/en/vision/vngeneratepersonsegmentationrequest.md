---
title: VNGeneratePersonSegmentationRequest
framework: Vision
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/vision/vngeneratepersonsegmentationrequest
source_url: 'https://developer.apple.com/documentation/vision/vngeneratepersonsegmentationrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/vision/vngeneratepersonsegmentationrequest.json'
content_hash: 'sha256:17c2ecd70861e335'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Vision](../vision.md)

# VNGeneratePersonSegmentationRequest

<sub>Class</sub>

An object that produces a matte image for a person it finds in the input image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class VNGeneratePersonSegmentationRequest
```

## Overview

Perform this request to detect and generate an image mask for a person in an image. The request returns the resulting image mask in an instance of [VNPixelBufferObservation](vnpixelbufferobservation.md).

## Relationships

- **Inherits From**: [VNStatefulRequest](vnstatefulrequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Request

- [- init](<vngeneratepersonsegmentationrequest/init().md>) — Creates a generate person segmentation request.
- [- initWithCompletionHandler:](<vngeneratepersonsegmentationrequest/init(completionhandler_).md>) — Creates a generate person segmentation request with a completion handler.

### Configuring the Request

- [outputPixelFormat](vngeneratepersonsegmentationrequest/outputpixelformat.md) — The pixel format of the output image.
- [qualityLevel](vngeneratepersonsegmentationrequest/qualitylevel-swift.property.md) — A value that indicates how the request balances accuracy and performance.
- [QualityLevel](vngeneratepersonsegmentationrequest/qualitylevel-swift.enum.md) — Constants that define the levels of quality for a person segmentation request.

### Getting the supported output pixel formats

- [- supportedOutputPixelFormatsAndReturnError:](<vngeneratepersonsegmentationrequest/supportedoutputpixelformats().md>) — Returns a list of output pixel formats that the request supports.

### Accessing the Results

- [results](vngeneratepersonsegmentationrequest/results.md) — The results of the segmentation request.
- [VNPixelBufferObservation](vnpixelbufferobservation.md) — An object that represents an image that an image-analysis request produces.

### Identifying Request Revisions

- [VNGeneratePersonSegmentationRequestRevision1](vngeneratepersonsegmentationrequestrevision1.md) — A constant for specifying revision 1 of the person segmentation generation request.

## See Also

### Image sequence analysis

- [Applying Matte Effects to People in Images and Video](applying-matte-effects-to-people-in-images-and-video.md) — Generate image masks for people automatically by using semantic person-segmentation.
- [Detecting human actions in a live video feed](../createml/detecting-human-actions-in-a-live-video-feed.md) — Identify body movements by sending a person’s pose data from a series of video frames to an action-classification model.
- [Segmenting and colorizing individuals from a surrounding scene](segmenting-and-colorizing-individuals-from-a-surrounding-scene.md) — Use the Vision framework to isolate and apply colors to people in an image.
- [VNStatefulRequest](vnstatefulrequest.md) — An abstract request type that builds evidence of a condition over time.
- [VNGeneratePersonInstanceMaskRequest](vngeneratepersoninstancemaskrequest.md) — An object that produces a mask of individual people it finds in the input image.
- [VNDetectDocumentSegmentationRequest](vndetectdocumentsegmentationrequest.md) — An object that detects rectangular regions that contain text in the input image.
- [VNSequenceRequestHandler](vnsequencerequesthandler.md) — An object that processes image-analysis requests for each frame in a sequence.
