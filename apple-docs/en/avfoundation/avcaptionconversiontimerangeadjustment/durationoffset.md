---
title: durationOffset
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionconversiontimerangeadjustment/durationoffset
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionconversiontimerangeadjustment/durationoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionconversiontimerangeadjustment/durationoffset.json'
content_hash: 'sha256:f52f2729c719cca4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionConversionTimeRangeAdjustment](../avcaptionconversiontimerangeadjustment.md)

# durationOffset

<sub>Instance Property</sub>

The time value by which the system offsets the durations of captions to correct a problem.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var durationOffset: CMTime { get }
```

## Discussion

The value may any numeric value, positive, negative, or zero.

## See Also

### Accessing time offsets

- [startTimeOffset](starttimeoffset.md) — The time value by which the system offsets the start times of captions to correct a problem.
