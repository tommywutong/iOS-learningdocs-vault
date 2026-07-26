---
title: putBytes
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataconsumercallbacks/putbytes
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataconsumercallbacks/putbytes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataconsumercallbacks/putbytes.json'
content_hash: 'sha256:3176d4786dc33d80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDataConsumerCallbacks](../cgdataconsumercallbacks.md)

# putBytes

<sub>Instance Property</sub>

A pointer to a function that copies data to the data consumer. For more information, see [CGDataConsumerPutBytesCallback](../cgdataconsumerputbytescallback.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var putBytes: CGDataConsumerPutBytesCallback?
```

## See Also

### Instance Properties

- [releaseConsumer](releaseconsumer.md) — A pointer to a function that handles clean-up for the data consumer, or `NULL`.
