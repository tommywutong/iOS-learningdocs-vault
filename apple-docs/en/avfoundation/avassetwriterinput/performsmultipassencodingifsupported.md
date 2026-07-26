---
title: performsMultiPassEncodingIfSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/performsmultipassencodingifsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/performsmultipassencodingifsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/performsmultipassencodingifsupported.json'
content_hash: 'sha256:248029d63025d7ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# performsMultiPassEncodingIfSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the input attempts to encode the source media data using multiple passes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var performsMultiPassEncodingIfSupported: Bool { get set }
```

## Discussion

An asset writer input may be able to achieve higher quality and lower data rate by performing multiple passes over the source media. It does this by analyzing the media data it appends and reencodes certain segments with different parameters. To perform the reencoding, you must append the media data for the segments again. See the [currentPassDescription](currentpassdescription.md) property and [- markCurrentPassAsFinished](<markcurrentpassasfinished().md>) method for the means by which the input nominates segments to reappend.

When the value of this property is [true](../../swift/true.md), the value of [readyForMoreMediaData](isreadyformoremediadata.md) for other inputs attached to the same asset writer may be [false](../../swift/false.md) more often and for longer periods of time. In particular, the value of [readyForMoreMediaData](isreadyformoremediadata.md) for inputs that don’t perform multiple passes may start as [false](../../swift/false.md) after calling the method asset writer’s [- startWriting](<../avassetwriter/startwriting().md>) method, and may not change to [true](../../swift/true.md) until after all multipass inputs complete their final pass.

When the value of this property is [true](../../swift/true.md), the input may store data in one or more temporary files before writing compressed samples to the output file. Use the asset writer’s [directoryForTemporaryFiles](../avassetwriter/directoryfortemporaryfiles.md) property if you need to specify the location of temporary file writing.

The default value is [false](../../swift/false.md), which means that no additional analysis occurs and it doesn’t reencode segments. Not all asset writer input configurations benefit from performing multiple passes over the source media. To determine whether the selected encoder can perform multiple passes, query the value of [canPerformMultiplePasses](canperformmultiplepasses.md) after calling [- startWriting](<../avassetwriter/startwriting().md>).

> [!important] Important
> It’s an error to set this property value to [true](../../swift/true.md) when the value for [expectsMediaDataInRealTime](expectsmediadatainrealtime.md) is [true](../../swift/true.md). It’s also an error for an asset writer to contain inputs with this property set to [true](../../swift/true.md) when any of its other inputs have a value of [true](../../swift/true.md) for [expectsMediaDataInRealTime](expectsmediadatainrealtime.md).

## See Also

### Performing multiple-pass encoding

- [canPerformMultiplePasses](canperformmultiplepasses.md) — A Boolean value that indicates whether the input may perform multiple passes over appended media data.
- [currentPassDescription](currentpassdescription.md) — An object that describes the requirements for the current pass.
- [AVAssetWriterInputPassDescription](../avassetwriterinputpassdescription.md) — An object that defines the interface to query for the requirements of the current pass.
- [- markCurrentPassAsFinished](<markcurrentpassasfinished().md>) — Tells the input to analyze the appended media to determine whether it can improve the results by reencoding certain segments.
- [- respondToEachPassDescriptionOnQueue:usingBlock:](<respondtoeachpassdescription(on_using_).md>) — Tells the input to invoke a callback whenever it begins a new pass.
- [MultiPassController](multipasscontroller.md) — Provides an interface to receive an async sequence of pass descriptions for the writer input receiver, if multi-pass is supported.
