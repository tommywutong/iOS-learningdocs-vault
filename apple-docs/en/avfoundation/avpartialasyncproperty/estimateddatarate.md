---
title: estimatedDataRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/estimateddatarate
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/estimateddatarate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/estimateddatarate.json'
content_hash: 'sha256:7d35a3e68ab45a6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# estimatedDataRate

<sub>Type Property</sub>

The estimated data rate, in bits per second, of the media that the track references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var estimatedDataRate: AVAsyncProperty<Root, Float> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

## See Also

### Loading temporal information

- [timeRange](timerange.md) — The time range of the track within the overall timeline of the asset.
- [naturalTimeScale](naturaltimescale.md) — The natural time scale of the media that a track references.
