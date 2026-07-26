---
title: 'init(sampleBuffer:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avtimedmetadatagroup/init(samplebuffer:)-6atlv'
source_url: 'https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/init(samplebuffer:)-6atlv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avtimedmetadatagroup/init%28samplebuffer%3A%29-6atlv.json'
content_hash: 'sha256:f6ccc111ea8a1145'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVTimedMetadataGroup](../avtimedmetadatagroup.md)

# init(sampleBuffer:)

<sub>Initializer</sub>

Creates a timed metadata group with a sample buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>)
```

## Parameters

- `sampleBuffer` — A [CMReadySampleBuffer](../../coremedia/cmreadysamplebuffer.md) with media type [kCMMediaType_Metadata](../../coremedia/kcmmediatype_metadata.md).

## Return Value

An instance of `AVTimedMetadataGroup`.

## See Also

### Creating a timed metadata group

- [- initWithItems:timeRange:](<init(items_timerange_).md>) — Creates a timed metadata group initialized with the given metadata items.
- [- initWithSampleBuffer:](<init(samplebuffer_)-bjuo.md>) _(deprecated)_
