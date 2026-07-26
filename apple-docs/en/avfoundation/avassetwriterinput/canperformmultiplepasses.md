---
title: canPerformMultiplePasses
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/canperformmultiplepasses
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/canperformmultiplepasses'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/canperformmultiplepasses.json'
content_hash: 'sha256:fae78fbbe863c835'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# canPerformMultiplePasses

<sub>Instance Property</sub>

A Boolean value that indicates whether the input may perform multiple passes over appended media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var canPerformMultiplePasses: Bool { get }
```

## Discussion

When the value for this property is [true](../../swift/true.md), configure your source media data for random access. After appending the media data for the current pass, as specified by the [currentPassDescription](currentpassdescription.md) property, call [- markCurrentPassAsFinished](<markcurrentpassasfinished().md>) so the system can determine whether it needs to perform additional passes. The system may perform only the initial pass if it determines there’s no benefit to performing multiple passes.

When the value for this property is [false](../../swift/false.md), your source for media data only needs to support sequential access. In this case, append all of the source media one time and call [- markAsFinished](<markasfinished().md>).

The default value is [false](../../swift/false.md). Currently the only way for this property to become [true](../../swift/true.md) is when the value of [performsMultiPassEncodingIfSupported](performsmultipassencodingifsupported.md) is [true](../../swift/true.md). The final value is available after you call [- startWriting](<../avassetwriter/startwriting().md>).

This property is key-value observable.

## See Also

### Performing multiple-pass encoding

- [currentPassDescription](currentpassdescription.md) — An object that describes the requirements for the current pass.
- [AVAssetWriterInputPassDescription](../avassetwriterinputpassdescription.md) — An object that defines the interface to query for the requirements of the current pass.
- [- markCurrentPassAsFinished](<markcurrentpassasfinished().md>) — Tells the input to analyze the appended media to determine whether it can improve the results by reencoding certain segments.
- [performsMultiPassEncodingIfSupported](performsmultipassencodingifsupported.md) — A Boolean value that indicates whether the input attempts to encode the source media data using multiple passes.
- [- respondToEachPassDescriptionOnQueue:usingBlock:](<respondtoeachpassdescription(on_using_).md>) — Tells the input to invoke a callback whenever it begins a new pass.
- [MultiPassController](multipasscontroller.md) — Provides an interface to receive an async sequence of pass descriptions for the writer input receiver, if multi-pass is supported.
