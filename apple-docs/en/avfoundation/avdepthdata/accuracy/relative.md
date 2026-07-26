---
title: AVDepthData.Accuracy.relative
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdepthdata/accuracy/relative
source_url: 'https://developer.apple.com/documentation/avfoundation/avdepthdata/accuracy/relative'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdepthdata/accuracy/relative.json'
content_hash: 'sha256:77ebd9d2697f0bc3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVDepthData](../../avdepthdata.md) · [Accuracy](../accuracy.md)

# AVDepthData.Accuracy.relative

<sub>Case</sub>

Values within the depth data map are usable for foreground/background separation, but are not absolutely accurate in the physical world.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case relative
```

## Discussion

This level of accuracy indicates that values within a depth map are usable relative to one another (that is, a depth value of 2 is twice as far as a depth value of 1), but do not accurately convey real-world distance.

## See Also

### Accuracy values

- [AVDepthDataAccuracyAbsolute](absolute.md) — Values within the depth map are absolutely accurate within the physical world.
