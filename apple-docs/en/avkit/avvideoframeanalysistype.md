---
title: AVVideoFrameAnalysisType
framework: AVKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avvideoframeanalysistype
source_url: 'https://developer.apple.com/documentation/avkit/avvideoframeanalysistype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avvideoframeanalysistype.json'
content_hash: 'sha256:4bc53c223c06e1d8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVVideoFrameAnalysisType

<sub>Structure</sub>

Constants that define the types of analysis a player view controller may perform on a paused video frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct AVVideoFrameAnalysisType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Analysis types

- [AVVideoFrameAnalysisTypeDefault](avvideoframeanalysistype/default.md) — The default types of analysis to perform.
- [AVVideoFrameAnalysisTypeText](avvideoframeanalysistype/text.md) — A type that finds text in a paused video frame.
- [AVVideoFrameAnalysisTypeSubject](avvideoframeanalysistype/subject.md) — A type that finds a subject that a user can copy out of frame.
- [AVVideoFrameAnalysisTypeVisualSearch](avvideoframeanalysistype/visualsearch.md) — A type that identifies objects, landmarks, art, and so on.
- [AVVideoFrameAnalysisTypeMachineReadableCode](avvideoframeanalysistype/machinereadablecode.md) — A type that recognizes machine-readable codes, such as QR codes.

### Initializers

- [init(rawValue:)](<avvideoframeanalysistype/init(rawvalue_).md>) — Creates a type from a string value.

## See Also

### Configuring frame analysis

- [allowsVideoFrameAnalysis](avplayerview/allowsvideoframeanalysis.md) — A Boolean value that indicates whether to perform video frame analysis.
- [videoFrameAnalysisTypes](avplayerview/videoframeanalysistypes.md)
