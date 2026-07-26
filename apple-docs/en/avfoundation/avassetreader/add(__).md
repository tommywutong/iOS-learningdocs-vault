---
title: 'add(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+（27.0 起废弃）, iPadOS 4.1+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetreader/add(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreader/add(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreader/add%28_%3A%29.json'
content_hash: 'sha256:88dceded48d367bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReader](../avassetreader.md)

# add(_:)

<sub>Instance Method</sub>

Adds an output to the reader.

> [!warning] Deprecated
> Use the appropriate AVAssetReader.outputProvider(for:...) overload for your output and optional adaptor instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func add(_ output: AVAssetReaderOutput)
```

## Parameters

- `output` — The asset reader output to add.

## Discussion

Add outputs to read from one or more tracks of an asset. You can only add outputs that retrieve media data from the asset that you associate with the asset reader.

You can’t add an output after you start reading.

## See Also

### Managing outputs

- [- canAddOutput:](<canadd(__).md>) — Determines whether you can add the output to the asset reader.
- [outputs](outputs.md) — The outputs from which you read media data.
