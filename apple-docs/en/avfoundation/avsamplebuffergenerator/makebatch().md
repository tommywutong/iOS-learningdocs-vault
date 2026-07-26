---
title: makeBatch()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebuffergenerator/makebatch()
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffergenerator/makebatch()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffergenerator/makebatch%28%29.json'
content_hash: 'sha256:287c99c45fbe723e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferGenerator](../avsamplebuffergenerator.md)

# makeBatch()

<sub>Instance Method</sub>

Creates a batch object to handle generating multiple sample buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeBatch() -> AVSampleBufferGeneratorBatch
```

## Return Value

An object to batch generate sample buffers.

## Discussion

Generating sample buffers in batches optimizes performance by allowing the system to asynchronously load sample data and optimize I/O when possible.

## See Also

### Creating a sample buffer

- [- createSampleBufferForRequest:error:](<makesamplebuffer(for_).md>) — Creates a sample buffer, and attempts to load its data asynchronously if requested.
- [- createSampleBufferForRequest:addingToBatch:error:](<makesamplebuffer(for_addto_).md>) — Creates a sample buffer and attempts to defer I/O for its data.
- [- createSampleBufferForRequest:](<createsamplebuffer(for_).md>) — Creates a new sample buffer reference for the specified buffer request. _(deprecated)_
