---
title: 'createSampleBuffer(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.10+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avsamplebuffergenerator/createsamplebuffer(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffergenerator/createsamplebuffer(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffergenerator/createsamplebuffer%28for%3A%29.json'
content_hash: 'sha256:5290282ee9793d34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferGenerator](../avsamplebuffergenerator.md)

# createSampleBuffer(for:)

<sub>Instance Method</sub>

Creates a new sample buffer reference for the specified buffer request.

> [!warning] Deprecated
> Use -createSampleBufferForRequest: error:, passing NULL for the error if not required

<sub>macOS</sub>

```swift
func createSampleBuffer(for request: AVSampleBufferRequest) -> CMSampleBuffer?
```

## Parameters

- `request` — The sample buffer request.

## Return Value

Returns a new `CMSampleBufferRef`.

## Discussion

It is an error to use an `AVSampleBufferRequest` object with mode set to `AVSampleBufferRequestModeScheduled` when the `AVSampleBufferGenerator` was created with a `NULL` timebase.

## See Also

### Creating a sample buffer

- [- createSampleBufferForRequest:error:](<makesamplebuffer(for_).md>) — Creates a sample buffer, and attempts to load its data asynchronously if requested.
- [- makeBatch](<makebatch().md>) — Creates a batch object to handle generating multiple sample buffers.
- [- createSampleBufferForRequest:addingToBatch:error:](<makesamplebuffer(for_addto_).md>) — Creates a sample buffer and attempts to defer I/O for its data.
