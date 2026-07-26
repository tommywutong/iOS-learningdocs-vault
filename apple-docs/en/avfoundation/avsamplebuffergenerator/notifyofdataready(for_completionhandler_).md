---
title: 'notifyOfDataReady(for:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.10+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebuffergenerator/notifyofdataready(for:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffergenerator/notifyofdataready(for:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffergenerator/notifyofdataready%28for%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:b431b3d591ec48a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferGenerator](../avsamplebuffergenerator.md)

# notifyOfDataReady(for:completionHandler:)

<sub>Type Method</sub>

Notifies the sample buffer generator when data is ready for the sample buffer reference or an error has occurred.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func notifyOfDataReady(for sbuf: CMSampleBuffer, completionHandler: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func notifyOfDataReady(for sbuf: CMSampleBuffer) async throws
```

## Parameters

- `sbuf` — The `CMSampleBufferRef`.

- `completionHandler` — A completion block that is called when data is ready for the sample buffer or an error occurs. The `dataReady` argument is [true](../../swift/true.md) if data is read for the sample buffer. If an error occurs, the `error` argument contains the `NSError` object.
