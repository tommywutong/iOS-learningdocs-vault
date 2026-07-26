---
title: SCVideoStreamAnalyzer
framework: Sensitive Content Analysis
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/sensitivecontentanalysis/scvideostreamanalyzer
source_url: 'https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/sensitivecontentanalysis/scvideostreamanalyzer.json'
content_hash: 'sha256:622d6a721b3dcc4a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Sensitive Content Analysis](../sensitivecontentanalysis.md)

# SCVideoStreamAnalyzer

<sub>Class</sub>

An object that monitors a stream of video by analyzing frames for sensitive content.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class SCVideoStreamAnalyzer
```

## Overview

Use this class to detect sensitive content in a video stream, such as on a conference call that your app implements. The class detects sensitive content in the video stream from either the device’s camera or the remote devices signed into the call, depending on how you configure the analyzer.

Create an instance of this class for each video stream in the call.

To begin analyzing the stream, pass it to either [- beginAnalysisOfCaptureDeviceInput:error:](<scvideostreamanalyzer/beginanalysis(of_)-78qm.md>) ([AVCaptureDeviceInput](../avfoundation/avcapturedeviceinput.md)) or [- beginAnalysisOfDecompressionSession:error:](<scvideostreamanalyzer/beginanalysis(of_)-9ehkx.md>) ([VTDecompressionSession](../videotoolbox/vtdecompressionsession.md)), depending on your video playback implementation.

> [!important] Important
> This class works only when the Communication Safety parental control in Screen Time is enabled, or when the Sensitive Content Warnings setting is turned on. The initializers of this class throw an error if both settings are off.

### React to sensitive content

When the framework detects sensitive content in the stream, it calls [analysisChangedHandler](scvideostreamanalyzer/analysischangedhandler.md) immediately with an [SCSensitivityAnalysis](scsensitivityanalysis.md) object that includes information about the detection.

You implement the [analysisChangedHandler](scvideostreamanalyzer/analysischangedhandler.md) callback to inspect the detection results, which includes confirmation that content is sensitive as well as guidance on next steps your app can take. The framework offers your app suggestions in the handler, which include:

- Alerting the person to the presence of sensitive content ([shouldIndicateSensitivity](scsensitivityanalysis/shouldindicatesensitivity.md))
- Interrupting video playback ([shouldInterruptVideo](scsensitivityanalysis/shouldinterruptvideo.md))
- Muting audio ([shouldMuteAudio](scsensitivityanalysis/shouldmuteaudio.md))

To stop analyzing the stream, call [- endAnalysis](<scvideostreamanalyzer/endanalysis().md>). If your app implements a custom stream decoder, you can analyze individual frames by passing pixel buffers to [- analyzePixelBuffer:](<scvideostreamanalyzer/analyze(__).md>).

In the event of an error during analysis, the handler receives an error object that details what went wrong. For more information, see: [SCVideoStreamAnalysisChangeHandler](scvideostreamanalysischangehandler.md).

### Add the app entitlement

To use this class, the system requires the [com.apple.developer.sensitivecontentanalysis.client](../bundleresources/entitlements/com.apple.developer.sensitivecontentanalysis.client.md) entitlement in your app’s code signature. Calls to the framework fail to return positive results without it. You can add this entitlement to your app by enabling the Sensitive Content Analysis capability in Xcode; see [Adding capabilities to your app](../xcode/adding-capabilities-to-your-app.md).

For more information, see [Detecting sensitive content in media and providing intervention options](detecting-nudity-in-media-and-providing-intervention-options.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a video stream analyzer

- [- initWithParticipantUUID:streamDirection:error:](<scvideostreamanalyzer/init(participantuuid_streamdirection_).md>) — Creates a video stream analyzer for the given call participant and stream option.
- [StreamDirection](scvideostreamanalyzer/streamdirection.md) — Options for the different types of analyzed video streams.

### Analyzing a video stream

- [- analyzePixelBuffer:](<scvideostreamanalyzer/analyze(__).md>) — Analyzes individual video-stream frames for sensitive content.
- [- beginAnalysisOfCaptureDeviceInput:error:](<scvideostreamanalyzer/beginanalysis(of_)-78qm.md>) — Analyzes video frames for the given capture device input.
- [- beginAnalysisOfDecompressionSession:error:](<scvideostreamanalyzer/beginanalysis(of_)-9ehkx.md>) — Analyzes video frames for the given decompression session.
- [analysisChanges](scvideostreamanalyzer/analysischanges.md) — A stream your app uses to receive video-stream analysis results.
- [- endAnalysis](<scvideostreamanalyzer/endanalysis().md>) — Stops stream analysis.

### Responding to sensitive content

- [analysis](scvideostreamanalyzer/analysis.md) — The results of the first detected sensitive video frame.
- [- continueStream](<scvideostreamanalyzer/continuestream().md>) — Indicates that your app is ready to resume video stream analysis.
