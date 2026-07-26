---
title: MTLCaptureDestination
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcapturedestination
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturedestination'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturedestination.json'
content_hash: 'sha256:2f4f3ed7c9c7bdd4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCaptureDestination

<sub>Enumeration</sub>

The kinds of destinations for captured command data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLCaptureDestination
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Choosing a destination

- [MTLCaptureDestinationDeveloperTools](mtlcapturedestination/developertools.md) — An option specifying that data should be captured to Xcode and that execution should stop in Xcode after the data is captured.
- [MTLCaptureDestinationGPUTraceDocument](mtlcapturedestination/gputracedocument.md) — An option specifying that the captured command data should be saved to a GPU trace document.

### Initializers

- [init(rawValue:)](<mtlcapturedestination/init(rawvalue_).md>)

## See Also

### Frame capture

- [MTLCaptureDescriptor](mtlcapturedescriptor.md) — A configuration for a Metal capture session.
- [MTLCaptureManager](mtlcapturemanager.md) — An instance you use to capture Metal command data in your app.
- [MTLCaptureScope](mtlcapturescope.md) — A type that can programmatically customize a GPU frame capture.
