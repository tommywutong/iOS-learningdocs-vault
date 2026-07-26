---
title: passDescriptions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/multipasscontroller/passdescriptions
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/multipasscontroller/passdescriptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/multipasscontroller/passdescriptions.json'
content_hash: 'sha256:d07daba56a0cc8d7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [MultiPassController](../multipasscontroller.md)

# passDescriptions

<sub>Instance Property</sub>

An async sequence of pass descriptions to iterate over if multi-pass is supported. This property is nil when multi-pass is not supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var passDescriptions: (some AsyncSequence<AVAssetWriterInputPassDescription, Never>)? { get }
```
