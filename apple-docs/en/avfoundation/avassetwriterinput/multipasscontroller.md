---
title: AVAssetWriterInput.MultiPassController
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/multipasscontroller
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/multipasscontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/multipasscontroller.json'
content_hash: 'sha256:743b3553c72ef09d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# AVAssetWriterInput.MultiPassController

<sub>Class</sub>

Provides an interface to receive an async sequence of pass descriptions for the writer input receiver, if multi-pass is supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MultiPassController
```

## Topics

### Accessing pass descriptions

- [passDescriptions](multipasscontroller/passdescriptions.md) — An async sequence of pass descriptions to iterate over if multi-pass is supported. This property is nil when multi-pass is not supported.

## See Also

### Performing multiple-pass encoding

- [canPerformMultiplePasses](canperformmultiplepasses.md) — A Boolean value that indicates whether the input may perform multiple passes over appended media data.
- [currentPassDescription](currentpassdescription.md) — An object that describes the requirements for the current pass.
- [AVAssetWriterInputPassDescription](../avassetwriterinputpassdescription.md) — An object that defines the interface to query for the requirements of the current pass.
- [- markCurrentPassAsFinished](<markcurrentpassasfinished().md>) — Tells the input to analyze the appended media to determine whether it can improve the results by reencoding certain segments.
- [performsMultiPassEncodingIfSupported](performsmultipassencodingifsupported.md) — A Boolean value that indicates whether the input attempts to encode the source media data using multiple passes.
- [- respondToEachPassDescriptionOnQueue:usingBlock:](<respondtoeachpassdescription(on_using_).md>) — Tells the input to invoke a callback whenever it begins a new pass.
