---
title: busyReasons
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avprovideostorage/busyreasons
source_url: 'https://developer.apple.com/documentation/avfoundation/avprovideostorage/busyreasons'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avprovideostorage/busyreasons.json'
content_hash: 'sha256:d998cbf86ead9e6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVProVideoStorage](../avprovideostorage.md)

# busyReasons

<sub>Instance Property</sub>

Whether Pro Video Storage is busy and the associated reasons.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var busyReasons: Set<AVProVideoStorage.BusyReason> { get }
```

## Discussion

A non-empty set indicates that Pro Video Storage is currently being modified. While this is non-empty, starting a video capture will fail with an error. This property is key-value observable.

## See Also

### Determining whether storage is busy

- [BusyReason](busyreason.md) — A reason that Pro Video Storage may be busy. _(beta)_
