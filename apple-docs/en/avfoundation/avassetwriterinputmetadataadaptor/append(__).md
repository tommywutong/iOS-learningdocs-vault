---
title: 'append(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetwriterinputmetadataadaptor/append(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor/append(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputmetadataadaptor/append%28_%3A%29.json'
content_hash: 'sha256:1f2e4df9ffe3c8c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputMetadataAdaptor](../avassetwriterinputmetadataadaptor.md)

# append(_:)

<sub>Instance Method</sub>

Appends a timed metadata group to the adaptor.

> [!warning] Deprecated
> Use AVAssetWriter.inputMetadataReceiver(for:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func append(_ timedMetadataGroup: AVTimedMetadataGroup) -> Bool
```

## Parameters

- `timedMetadataGroup` — The timed metadata group to append.

## Return Value

[true](../../swift/true.md) if the adaptor appends the group; otherwise, [false](../../swift/false.md).

## Discussion

The timing of metadata items in the output asset correspond to the time range of the timed metadata group, regardless of the values of their individual time and duration properties.

> [!important] Important
> Only call this method after you’ve attached the related input to the asset writer and called its [- startWriting](<../avassetwriter/startwriting().md>) method.
