---
title: 'log(level:_:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/logger/log(level:_:)'
source_url: 'https://developer.apple.com/documentation/os/logger/log(level:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/logger/log%28level%3A_%3A%29.json'
content_hash: 'sha256:ffb80a420f25b135'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [Logger](../logger.md)

# log(level:_:)

<sub>Instance Method</sub>

Writes a message to the log using the specified log type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func log(level: OSLogType, _ message: OSLogMessage)
```

## Parameters

- `level` — The message’s log level, which determines the severity of the message and whether the system persists it to disk. For possible values, see [OSLogType](../oslogtype.md).

- `message` — The interpolated string that the logger writes to the log. Each of the message’s interpolations can specify individual formatting and privacy options. For more information, see [Message Argument Formatters](../message-argument-formatters.md).

## Discussion

> [!important] Important
> Don’t create an instance of [OSLogMessage](../oslogmessage.md). Instead, provide an interpolated string as the `message` parameter and the system converts it automatically.

## See Also

### Logging a Message

- [log(_:)](<log(__).md>) — Writes a message to the log using the default log type.
- [OSLogType](../oslogtype.md) — The various log levels that the unified logging system provides.
- [OSLogMessage](../oslogmessage.md) — An object that represents a log message.
