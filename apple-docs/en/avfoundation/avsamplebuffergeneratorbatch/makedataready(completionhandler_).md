---
title: 'makeDataReady(completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebuffergeneratorbatch/makedataready(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffergeneratorbatch/makedataready(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffergeneratorbatch/makedataready%28completionhandler%3A%29.json'
content_hash: 'sha256:71366a300210cc5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferGeneratorBatch](../avsamplebuffergeneratorbatch.md)

# makeDataReady(completionHandler:)

<sub>Instance Method</sub>

Loads sample data asynchronously for all sample buffers within a batch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeDataReady(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeDataReady() async throws
```

## Parameters

- `completionHandler` — A callback the system invokes once when all sample buffers in the batch are data-ready, or when an error occurs.

## Discussion

Calling this method more than once on a batch generates an exception.
