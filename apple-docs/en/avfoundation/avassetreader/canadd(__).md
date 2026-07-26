---
title: 'canAdd(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetreader/canadd(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreader/canadd(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreader/canadd%28_%3A%29.json'
content_hash: 'sha256:849d69ab330f0120'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReader](../avassetreader.md)

# canAdd(_:)

<sub>Instance Method</sub>

Determines whether you can add the output to the asset reader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func canAdd(_ output: AVAssetReaderOutput) -> Bool
```

## Parameters

- `output` — The asset reader output to test.

## Return Value

[true](../../swift/true.md) if you can add the output; otherwise, [false](../../swift/false.md).

## Discussion

You may only add outputs that retrieve media data from the asset that you associate with the asset reader.

## See Also

### Managing outputs

- [- addOutput:](<add(__).md>) — Adds an output to the reader. _(deprecated)_
- [outputs](outputs.md) — The outputs from which you read media data.
