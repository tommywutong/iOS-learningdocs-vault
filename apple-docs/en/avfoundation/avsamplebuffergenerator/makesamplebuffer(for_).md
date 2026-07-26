---
title: 'makeSampleBuffer(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebuffergenerator/makesamplebuffer(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffergenerator/makesamplebuffer(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffergenerator/makesamplebuffer%28for%3A%29.json'
content_hash: 'sha256:2c2700bb153fed9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferGenerator](../avsamplebuffergenerator.md)

# makeSampleBuffer(for:)

<sub>Instance Method</sub>

Creates a sample buffer, and attempts to load its data asynchronously if requested.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeSampleBuffer(for request: AVSampleBufferRequest) throws -> sending CMSampleBuffer
```

## Parameters

- `request` — A sample buffer creation request.

## Return Value

A sample buffer object.

## Discussion

If you created the generator with a `nil` timebase, any associated [AVSampleBufferRequest](../avsamplebufferrequest.md) objects default to using a request mode of [AVSampleBufferRequestModeImmediate](../avsamplebufferrequest/mode-swift.enum/immediate.md).

Call the [+ notifyOfDataReadyForSampleBuffer:completionHandler:](<notifyofdataready(for_completionhandler_).md>) class method to have the system notify you when sample buffer data is available.

The request may fail based on generator configuration or file format.

## See Also

### Creating a sample buffer

- [- makeBatch](<makebatch().md>) — Creates a batch object to handle generating multiple sample buffers.
- [- createSampleBufferForRequest:addingToBatch:error:](<makesamplebuffer(for_addto_).md>) — Creates a sample buffer and attempts to defer I/O for its data.
- [- createSampleBufferForRequest:](<createsamplebuffer(for_).md>) — Creates a new sample buffer reference for the specified buffer request. _(deprecated)_
