---
title: 'makeSampleBuffer(for:addTo:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebuffergenerator/makesamplebuffer(for:addto:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffergenerator/makesamplebuffer(for:addto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffergenerator/makesamplebuffer%28for%3Aaddto%3A%29.json'
content_hash: 'sha256:52ed378326fc8973'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferGenerator](../avsamplebuffergenerator.md)

# makeSampleBuffer(for:addTo:)

<sub>Instance Method</sub>

Creates a sample buffer and attempts to defer I/O for its data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeSampleBuffer(for request: AVSampleBufferRequest, addTo batch: AVSampleBufferGeneratorBatch) throws -> CMSampleBuffer
```

## Parameters

- `request` — A sample buffer creation request.

- `batch` — A batch object to contain the output sample buffer. You must create this object by calling [- makeBatch](<makebatch().md>) on the same instance of [AVSampleBufferGenerator](../avsamplebuffergenerator.md) or an error occurs.

## Return Value

A sample buffer.

## Discussion

Call the [- makeDataReadyWithCompletionHandler:](<../avsamplebuffergeneratorbatch/makedataready(completionhandler_).md>) on [AVSampleBufferGeneratorBatch](../avsamplebuffergeneratorbatch.md) once to commence I/O and load sample data for all [CMSampleBuffer](../../coremedia/cmsamplebuffer.md) objects in a batch. After loading commences, any subsequent calls to [- createSampleBufferForRequest:addingToBatch:error:](<makesamplebuffer(for_addto_).md>) throw an exception.

The generator may defer I/O to fetch sample data depending on the source of the sample data and the generator’s timebase

The request may fail based on generator configuration or file format.

## See Also

### Creating a sample buffer

- [- createSampleBufferForRequest:error:](<makesamplebuffer(for_).md>) — Creates a sample buffer, and attempts to load its data asynchronously if requested.
- [- makeBatch](<makebatch().md>) — Creates a batch object to handle generating multiple sample buffers.
- [- createSampleBufferForRequest:](<createsamplebuffer(for_).md>) — Creates a new sample buffer reference for the specified buffer request. _(deprecated)_
