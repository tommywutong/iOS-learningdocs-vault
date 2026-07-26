---
title: markCurrentPassAsFinished()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/markcurrentpassasfinished()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/markcurrentpassasfinished()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/markcurrentpassasfinished%28%29.json'
content_hash: 'sha256:fecee6346f52922f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# markCurrentPassAsFinished()

<sub>Instance Method</sub>

Tells the input to analyze the appended media to determine whether it can improve the results by reencoding certain segments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func markCurrentPassAsFinished()
```

## Discussion

When the value of the [canPerformMultiplePasses](canperformmultiplepasses.md) property is [true](../../swift/true.md), call this method after you append all of your media data. After the input determines if it warrants performing an additional pass, the value of [currentPassDescription](currentpassdescription.md) changes (typically asynchronously) to describe how to set up for the next pass. Although it’s possible to use key-value observing to determine when the value of [currentPassDescription](currentpassdescription.md) changes, it’s typically more convenient to call the [- respondToEachPassDescriptionOnQueue:usingBlock:](<respondtoeachpassdescription(on_using_).md>) method to start the work for each pass.

After reappending the media data for all of the time ranges of the new pass, call this method again to determine whether to reappend segments in another pass.

Calling this method effectively cancels any previous invocation of [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>), which means that you may call [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) again for each new pass. This method provides a convenient way to consolidate these invocations in your code.

After each pass, you have the option of keeping the most recent results by calling [- markAsFinished](<markasfinished().md>), instead of this method. If the value of [currentPassDescription](currentpassdescription.md) is `nil` at the beginning of a pass, call [- markAsFinished](<markasfinished().md>) to tell the input to not expect any further media data.

If the value of [canPerformMultiplePasses](canperformmultiplepasses.md) is [false](../../swift/false.md), the value of [currentPassDescription](currentpassdescription.md) immediately becomes `nil` after calling this method.

> [!important] Important
> Before calling this method, you must add the input to an asset writer and call the writer’s [- startWriting](<../avassetwriter/startwriting().md>) method.

## See Also

### Performing multiple-pass encoding

- [canPerformMultiplePasses](canperformmultiplepasses.md) — A Boolean value that indicates whether the input may perform multiple passes over appended media data.
- [currentPassDescription](currentpassdescription.md) — An object that describes the requirements for the current pass.
- [AVAssetWriterInputPassDescription](../avassetwriterinputpassdescription.md) — An object that defines the interface to query for the requirements of the current pass.
- [performsMultiPassEncodingIfSupported](performsmultipassencodingifsupported.md) — A Boolean value that indicates whether the input attempts to encode the source media data using multiple passes.
- [- respondToEachPassDescriptionOnQueue:usingBlock:](<respondtoeachpassdescription(on_using_).md>) — Tells the input to invoke a callback whenever it begins a new pass.
- [MultiPassController](multipasscontroller.md) — Provides an interface to receive an async sequence of pass descriptions for the writer input receiver, if multi-pass is supported.
