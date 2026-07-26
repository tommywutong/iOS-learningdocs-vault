---
title: preferredTransform
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/preferredtransform-90jdn
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/preferredtransform-90jdn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/preferredtransform-90jdn.json'
content_hash: 'sha256:c9662f6806d6d47f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# preferredTransform

<sub>Type Property</sub>

The track’s transform preference to apply to its visual content during presentation or processing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var preferredTransform: AVAsyncProperty<Root, CGAffineTransform> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

## See Also

### Loading visual characteristics

- [naturalSize](naturalsize.md) — The natural dimensions of the media data that the track references.
