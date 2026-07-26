---
title: AVAssetWriterInputPassDescription
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinputpassdescription
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputpassdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputpassdescription.json'
content_hash: 'sha256:e15c2646d34fa85a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetWriterInputPassDescription

<sub>Class</sub>

An object that defines the interface to query for the requirements of the current pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetWriterInputPassDescription
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting source time ranges

- [sourceTimeRanges](avassetwriterinputpassdescription/sourcetimeranges.md) — An array of time ranges.

## See Also

### Performing multiple-pass encoding

- [canPerformMultiplePasses](avassetwriterinput/canperformmultiplepasses.md) — A Boolean value that indicates whether the input may perform multiple passes over appended media data.
- [currentPassDescription](avassetwriterinput/currentpassdescription.md) — An object that describes the requirements for the current pass.
- [- markCurrentPassAsFinished](<avassetwriterinput/markcurrentpassasfinished().md>) — Tells the input to analyze the appended media to determine whether it can improve the results by reencoding certain segments.
- [performsMultiPassEncodingIfSupported](avassetwriterinput/performsmultipassencodingifsupported.md) — A Boolean value that indicates whether the input attempts to encode the source media data using multiple passes.
- [- respondToEachPassDescriptionOnQueue:usingBlock:](<avassetwriterinput/respondtoeachpassdescription(on_using_).md>) — Tells the input to invoke a callback whenever it begins a new pass.
- [MultiPassController](avassetwriterinput/multipasscontroller.md) — Provides an interface to receive an async sequence of pass descriptions for the writer input receiver, if multi-pass is supported.
