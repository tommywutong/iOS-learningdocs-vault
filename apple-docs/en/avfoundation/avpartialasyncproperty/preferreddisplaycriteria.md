---
title: preferredDisplayCriteria
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/preferreddisplaycriteria
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/preferreddisplaycriteria'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/preferreddisplaycriteria.json'
content_hash: 'sha256:21ad8479bfe16284'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# preferredDisplayCriteria

<sub>Type Property</sub>

The asset’s display mode preference for optimal playback of its content.

<sub>tvOS, visionOS</sub>

```swift
static var preferredDisplayCriteria: AVAsyncProperty<Root, AVDisplayCriteria> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

## See Also

### Loading asset preferences

- [preferredRate](preferredrate.md) — The asset’s rate preference for playing its media.
- [preferredVolume](preferredvolume-20mb3.md) — The asset’s volume preference for playing its audible media.
- [preferredTransform](preferredtransform-80d13.md) — The asset’s transform preference to apply to its visual content during presentation or processing.
- [AVDisplayCriteria](../avdisplaycriteria.md) — An object the system uses to guide the selection of a display mode in tvOS.
