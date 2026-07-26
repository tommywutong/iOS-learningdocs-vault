---
title: OSLogType
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/os/oslogtype
source_url: 'https://developer.apple.com/documentation/os/oslogtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogtype.json'
content_hash: 'sha256:9ced5f6b79f97cf4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# OSLogType

<sub>Structure</sub>

The various log levels that the unified logging system provides.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct OSLogType
```

## Overview

A log level controls how and when the system writes a message to the unified logging system. To write a message with a specific log level, create a [Logger](logger.md) and call its [log(level:_:)](<logger/log(level___).md>) method. Alternatively, call the method that corresponds to the desired log level, such as [debug(_:)](<logger/debug(__).md>) or [fault(_:)](<logger/fault(__).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md)

## Topics

### Getting Log Types

- [debug](oslogtype/debug.md) — The debug log level.
- [info](oslogtype/info.md) — The informative log level.
- [default](oslogtype/default.md) — The default log level.
- [error](oslogtype/error.md) — The error log level.
- [fault](oslogtype/fault.md) — The fault log level.

### Creating a Log Type

- [init(_:)](<oslogtype/init(__).md>) — Creates a log type from the specified value.
- [init(rawValue:)](<oslogtype/init(rawvalue_).md>) — Creates a log type from the specified raw value.

### Getting the Raw Value

- [rawValue](oslogtype/rawvalue.md) — The log type’s raw value.

## See Also

### Log Messages

- [Logger](logger.md) — An object for writing interpolated string messages to the unified logging system.
- [Message Argument Formatters](message-argument-formatters.md) — Manage the privacy and presentation of the message’s interpolated values using type-aware formatters.
