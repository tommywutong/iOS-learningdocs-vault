---
title: 'init(sampleBuffer:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avtimedmetadatagroup/init(samplebuffer:)-bjuo'
source_url: 'https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/init(samplebuffer:)-bjuo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avtimedmetadatagroup/init%28samplebuffer%3A%29-bjuo.json'
content_hash: 'sha256:e37de303fd8e55f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVTimedMetadataGroup](../avtimedmetadatagroup.md)

# init(sampleBuffer:)

<sub>Initializer</sub>

> [!warning] Deprecated
> Use init(sampleBuffer: CMReadySampleBuffer\<CMSampleBuffer.DynamicContent\>) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(sampleBuffer: CMSampleBuffer)
```

## Parameters

- `sampleBuffer` — A CMSampleBuffer with media type kCMMediaType_Metadata.

## Return Value

An instance of AVTimedMetadataGroup.

## Discussion

Initializes an instance of AVTimedMetadataGroup with a sample buffer.

## See Also

### Creating a timed metadata group

- [init(sampleBuffer:)](<init(samplebuffer_)-6atlv.md>) — Creates a timed metadata group with a sample buffer.
- [- initWithItems:timeRange:](<init(items_timerange_).md>) — Creates a timed metadata group initialized with the given metadata items.
