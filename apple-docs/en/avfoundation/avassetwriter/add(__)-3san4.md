---
title: 'add(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriter/add(_:)-3san4'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/add(_:)-3san4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/add%28_%3A%29-3san4.json'
content_hash: 'sha256:0289579adab07a3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# add(_:)

<sub>Instance Method</sub>

Adds an input group to an asset writer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func add(_ inputGroup: AVAssetWriterInputGroup)
```

## Parameters

- `inputGroup` — A compatible asset writer input group to add.

## Discussion

An asset writer marks tracks associated with grouped inputs as mutually exclusive to each other for playback or other processing, if the output container format supports mutually exclusive relationships among tracks.

When you add an input group to an asset writer, the system sets the value of the default input’s [marksOutputTrackAsEnabled](../avassetwriterinput/marksoutputtrackasenabled.md) property to [true](../../swift/true.md) and sets the values of the group’s other inputs to [false](../../swift/false.md).

You can’t add input groups after writing starts.

## See Also

### Configuring input groups

- [inputGroups](inputgroups.md) — The input groups an asset writer contains.
- [- canAddInputGroup:](<canadd(__)-8s1oh.md>) — Determines whether the asset writer supports adding the input group.
