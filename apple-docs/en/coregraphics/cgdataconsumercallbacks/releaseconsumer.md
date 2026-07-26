---
title: releaseConsumer
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataconsumercallbacks/releaseconsumer
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataconsumercallbacks/releaseconsumer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataconsumercallbacks/releaseconsumer.json'
content_hash: 'sha256:e3fad6f89b1ae938'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDataConsumerCallbacks](../cgdataconsumercallbacks.md)

# releaseConsumer

<sub>Instance Property</sub>

A pointer to a function that handles clean-up for the data consumer, or `NULL`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var releaseConsumer: CGDataConsumerReleaseInfoCallback?
```

## Discussion

For more information, see [CGDataConsumerReleaseInfoCallback](../cgdataconsumerreleaseinfocallback.md).

## See Also

### Instance Properties

- [putBytes](putbytes.md) — A pointer to a function that copies data to the data consumer. For more information, see [CGDataConsumerPutBytesCallback](../cgdataconsumerputbytescallback.md).
