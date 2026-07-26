---
title: CGDataConsumer
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataconsumer
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataconsumer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataconsumer.json'
content_hash: 'sha256:39bae3755a16b1f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDataConsumer

<sub>Class</sub>

An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CGDataConsumer
```

## Overview

Most apps should use [CGImageDestination](../imageio/cgimagedestination.md) objects instead.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Data Consumers

- [CGDataConsumerCreate](<cgdataconsumer/init(info_cbks_).md>) — Creates a data consumer that uses callback functions to write data.
- [CGDataConsumerCreateWithURL](<cgdataconsumer/init(url_).md>) — Creates a data consumer that writes data to a location specified by a URL.
- [CGDataConsumerCreateWithCFData](<cgdataconsumer/init(data_).md>) — Creates a data consumer that writes to a CFData object.
- [CGDataConsumerCallbacks](cgdataconsumercallbacks.md) — A structure that contains pointers to callback functions that manage the copying of data for a data consumer.
- [CGDataConsumerPutBytesCallback](cgdataconsumerputbytescallback.md) — Copies data from a Core Graphics-supplied buffer into a data consumer.
- [CGDataConsumerReleaseInfoCallback](cgdataconsumerreleaseinfocallback.md) — Releases any private data or resources associated with the data consumer.

### Working with Core Foundation Types

- [CGDataConsumerGetTypeID](cgdataconsumer/typeid.md) — Returns the Core Foundation type identifier for Core Graphics data consumers.

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)

### Utility and Support Classes

- [CGDataProvider](cgdataprovider.md) — An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [CGShading](cgshading.md) — A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.
- [CGGradient](cggradient.md) — A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [CGFunction](cgfunction.md) — A general facility for defining and using callback functions.
- [CGPattern](cgpattern.md) — A 2D pattern to be used for drawing graphics paths.
