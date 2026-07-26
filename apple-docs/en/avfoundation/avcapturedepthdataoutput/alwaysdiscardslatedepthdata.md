---
title: alwaysDiscardsLateDepthData
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedepthdataoutput/alwaysdiscardslatedepthdata
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedepthdataoutput/alwaysdiscardslatedepthdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedepthdataoutput/alwaysdiscardslatedepthdata.json'
content_hash: 'sha256:586c48ff8b24c43e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDepthDataOutput](../avcapturedepthdataoutput.md)

# alwaysDiscardsLateDepthData

<sub>Instance Property</sub>

A Boolean value that determines whether the capture output should discard any depth data that is not processed before the next depth data is captured.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var alwaysDiscardsLateDepthData: Bool { get set }
```

## Discussion

If the [delegateCallbackQueue](delegatecallbackqueue.md) dispatch queue is blocked when new depth data is captured, this property determines whether the capture output allows your delegate object more time to process old depth data. If this property’s value is [false](../../swift/false.md), the capture output delivers old data to your delegate as soon as possible, but application memory usage may increase as a result. The default value is [true](../../swift/true.md).

## See Also

### Configuring depth data capture

- [filteringEnabled](isfilteringenabled.md) — A Boolean value that determines whether the depth data output should filter depth data to smooth out noise and fill invalid values.
