---
title: 'init(inputs:defaultInput:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinputgroup/init(inputs:defaultinput:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup/init(inputs:defaultinput:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputgroup/init%28inputs%3Adefaultinput%3A%29.json'
content_hash: 'sha256:f1af677583442c9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputGroup](../avassetwriterinputgroup.md)

# init(inputs:defaultInput:)

<sub>Initializer</sub>

Creates a group for the asset writer inputs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(inputs: [AVAssetWriterInput], defaultInput: AVAssetWriterInput?)
```

## Parameters

- `inputs` — The inputs with tracks to arrange into a mutually exclusive group.

- `defaultInput` — The group’s default input.

## Discussion

When you add an input group to an asset writer, the system sets the default input’s [marksOutputTrackAsEnabled](../avassetwriterinput/marksoutputtrackasenabled.md) property value to [true](../../swift/true.md), and the value of the other inputs in the group to [false](../../swift/false.md).
