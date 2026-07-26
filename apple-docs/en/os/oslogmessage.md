---
title: OSLogMessage
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogmessage
source_url: 'https://developer.apple.com/documentation/os/oslogmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogmessage.json'
content_hash: 'sha256:a1464749fb3c2fe3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# OSLogMessage

<sub>Structure</sub>

An object that represents a log message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct OSLogMessage
```

## Overview

> [!important] Important
> You don’t create instances of [OSLogMessage](oslogmessage.md) directly. Instead, the system creates them for you when writing messages to the unified logging system using a [Logger](logger.md).

## Relationships

- **Conforms To**: [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringInterpolation](../swift/expressiblebystringinterpolation.md), [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md)

## Topics

### Getting the Message Details

- [bufferSize](oslogmessage/buffersize.md) — The byte size of the buffer that the logging system receives.
- [interpolation](oslogmessage/interpolation.md) — The log message’s string interpolation.
- [maxOSLogArgumentCount](maxoslogargumentcount.md) — The maximum number of interpolated expressions that a log message may contain.

## See Also

### Logging a Message

- [log(_:)](<logger/log(__).md>) — Writes a message to the log using the default log type.
- [log(level:_:)](<logger/log(level___).md>) — Writes a message to the log using the specified log type.
- [OSLogType](oslogtype.md) — The various log levels that the unified logging system provides.
