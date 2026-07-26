---
title: cancelReading()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreader/cancelreading()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreader/cancelreading()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreader/cancelreading%28%29.json'
content_hash: 'sha256:af5c1286fdf98c22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReader](../avassetreader.md)

# cancelReading()

<sub>Instance Method</sub>

Cancels any background work and stops the reader’s outputs from reading more samples.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func cancelReading()
```

## Discussion

To stop reading samples before reaching the end of the time range, call this method to stop any in-progress background read operations.

## See Also

### Controlling reading

- [start()](<start().md>) — Prepares the reader to read media data from the asset.
- [- startReading](<startreading().md>) — Prepares the asset reader to start reading sample buffers from the asset. _(deprecated)_
