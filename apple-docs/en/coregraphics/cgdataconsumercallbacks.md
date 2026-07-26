---
title: CGDataConsumerCallbacks
framework: Core Graphics
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataconsumercallbacks
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataconsumercallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataconsumercallbacks.json'
content_hash: 'sha256:9898ed60f1a75b34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDataConsumerCallbacks

<sub>Structure</sub>

A structure that contains pointers to callback functions that manage the copying of data for a data consumer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CGDataConsumerCallbacks
```

## Overview

The functions specified by the `CGDataConsumerCallbacks` structure are responsible for copying data that Core Graphics sends to your consumer and for handling the consumer’s basic memory management. You supply this structure to the function [CGDataConsumerCreate](<cgdataconsumer/init(info_cbks_).md>) to create a data consumer.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cgdataconsumercallbacks/init().md>)
- [init(putBytes:releaseConsumer:)](<cgdataconsumercallbacks/init(putbytes_releaseconsumer_).md>)

### Instance Properties

- [putBytes](cgdataconsumercallbacks/putbytes.md) — A pointer to a function that copies data to the data consumer. For more information, see [CGDataConsumerPutBytesCallback](cgdataconsumerputbytescallback.md).
- [releaseConsumer](cgdataconsumercallbacks/releaseconsumer.md) — A pointer to a function that handles clean-up for the data consumer, or `NULL`.

## See Also

### Creating Data Consumers

- [CGDataConsumerCreate](<cgdataconsumer/init(info_cbks_).md>) — Creates a data consumer that uses callback functions to write data.
- [CGDataConsumerCreateWithURL](<cgdataconsumer/init(url_).md>) — Creates a data consumer that writes data to a location specified by a URL.
- [CGDataConsumerCreateWithCFData](<cgdataconsumer/init(data_).md>) — Creates a data consumer that writes to a CFData object.
- [CGDataConsumerPutBytesCallback](cgdataconsumerputbytescallback.md) — Copies data from a Core Graphics-supplied buffer into a data consumer.
- [CGDataConsumerReleaseInfoCallback](cgdataconsumerreleaseinfocallback.md) — Releases any private data or resources associated with the data consumer.
