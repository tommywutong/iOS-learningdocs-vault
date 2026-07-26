---
title: start()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreader/start()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreader/start()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreader/start%28%29.json'
content_hash: 'sha256:fdfc3ebd121fe298'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReader](../avassetreader.md)

# start()

<sub>Instance Method</sub>

Prepares the reader to read media data from the asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func start() throws
```

## Discussion

> [!danger] Throws
> An error if reading fails to start.

## See Also

### Controlling reading

- [- startReading](<startreading().md>) — Prepares the asset reader to start reading sample buffers from the asset. _(deprecated)_
- [- cancelReading](<cancelreading().md>) — Cancels any background work and stops the reader’s outputs from reading more samples.
