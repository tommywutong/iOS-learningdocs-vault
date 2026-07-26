---
title: currentPassDescription
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/currentpassdescription
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/currentpassdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/currentpassdescription.json'
content_hash: 'sha256:c1b77773649895e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# currentPassDescription

<sub>Instance Property</sub>

An object that describes the requirements for the current pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var currentPassDescription: AVAssetWriterInputPassDescription? { get }
```

## Discussion

If the value of this property is `nil`, call the asset writer input’s [- markAsFinished](<markasfinished().md>) method because there are no more requests to fulfill.

During the first pass, the request contains a single time range value, from zero to positive infinity, that indicates to append all media from the source. This condition is also true when [canPerformMultiplePasses](canperformmultiplepasses.md) is [false](../../swift/false.md), in which case the asset writer only performs a single pass.

The value of this property is `nil` before you call [- startWriting](<../avassetwriter/startwriting().md>) on the containing asset writer. It transitions to an initial non-`nil` value during the call to [- startWriting](<../avassetwriter/startwriting().md>), and changes only after a call to [- markCurrentPassAsFinished](<markcurrentpassasfinished().md>). You can use the [- respondToEachPassDescriptionOnQueue:usingBlock:](<respondtoeachpassdescription(on_using_).md>) to have the system call you at the beginning of each pass.

This property is key-value observable. The system doesn’t notify an observer on a specific thread.

## See Also

### Performing multiple-pass encoding

- [canPerformMultiplePasses](canperformmultiplepasses.md) — A Boolean value that indicates whether the input may perform multiple passes over appended media data.
- [AVAssetWriterInputPassDescription](../avassetwriterinputpassdescription.md) — An object that defines the interface to query for the requirements of the current pass.
- [- markCurrentPassAsFinished](<markcurrentpassasfinished().md>) — Tells the input to analyze the appended media to determine whether it can improve the results by reencoding certain segments.
- [performsMultiPassEncodingIfSupported](performsmultipassencodingifsupported.md) — A Boolean value that indicates whether the input attempts to encode the source media data using multiple passes.
- [- respondToEachPassDescriptionOnQueue:usingBlock:](<respondtoeachpassdescription(on_using_).md>) — Tells the input to invoke a callback whenever it begins a new pass.
- [MultiPassController](multipasscontroller.md) — Provides an interface to receive an async sequence of pass descriptions for the writer input receiver, if multi-pass is supported.
