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
doc_path: /documentation/avfoundation/avpartialasyncproperty/preferredtransform-80d13
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/preferredtransform-80d13'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/preferredtransform-80d13.json'
content_hash: 'sha256:525fd770881d0679'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# preferredTransform

<sub>Type Property</sub>

The asset’s transform preference to apply to its visual content during presentation or processing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var preferredTransform: AVAsyncProperty<Root, CGAffineTransform> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

This value typically, but not always, equals [CGAffineTransformIdentity](../../coregraphics/cgaffinetransformidentity.md).

## See Also

### Loading asset preferences

- [preferredRate](preferredrate.md) — The asset’s rate preference for playing its media.
- [preferredVolume](preferredvolume-20mb3.md) — The asset’s volume preference for playing its audible media.
- [preferredDisplayCriteria](preferreddisplaycriteria.md) — The asset’s display mode preference for optimal playback of its content.
- [AVDisplayCriteria](../avdisplaycriteria.md) — An object the system uses to guide the selection of a display mode in tvOS.
