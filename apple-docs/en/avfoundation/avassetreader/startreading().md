---
title: startReading()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+（27.0 起废弃）, iPadOS 4.1+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetreader/startreading()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreader/startreading()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreader/startreading%28%29.json'
content_hash: 'sha256:615d44b014af2df7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReader](../avassetreader.md)

# startReading()

<sub>Instance Method</sub>

Prepares the asset reader to start reading sample buffers from the asset.

> [!warning] Deprecated
> Use start() instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func startReading() -> Bool
```

## Return Value

`true` if the reader is able to start reading; otherwise, `false`.

## Discussion

If this method returns `false`, you can determine the reason by checking the values of the [status](status-swift.property.md) and [error](error.md) properties.

## See Also

### Controlling reading

- [start()](<start().md>) — Prepares the reader to read media data from the asset.
- [- cancelReading](<cancelreading().md>) — Cancels any background work and stops the reader’s outputs from reading more samples.
