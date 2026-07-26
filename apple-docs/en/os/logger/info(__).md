---
title: 'info(_:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/logger/info(_:)'
source_url: 'https://developer.apple.com/documentation/os/logger/info(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/logger/info%28_%3A%29.json'
content_hash: 'sha256:87c3f4098ad465b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [Logger](../logger.md)

# info(_:)

<sub>Instance Method</sub>

Writes an informative message to the log.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func info(_ message: OSLogMessage)
```

## Parameters

- `message` — The interpolated string that the logger writes to the log. Each of the message’s interpolations can specify individual formatting and privacy options. For more information, see [Message Argument Formatters](../message-argument-formatters.md).

## Discussion

> [!important] Important
> Don’t create an instance of [OSLogMessage](../oslogmessage.md). Instead, provide an interpolated string as the `message` parameter and the system converts it automatically.

Use this method to write messages with the [info](../oslogtype/info.md) log level to the in-memory log store only. If you use the `log` command line tool to collect your logs, the method also writes messages to the on-disk log store.

## See Also

### Logging a Scoped Message

- [notice(_:)](<notice(__).md>) — Writes a message to the log using the default log type.
- [debug(_:)](<debug(__).md>) — Writes a debug message to the log.
- [trace(_:)](<trace(__).md>) — Writes a trace message to the log.
- [error(_:)](<error(__).md>) — Writes information about an error to the log.
- [warning(_:)](<warning(__).md>) — Writes information about a warning to the log.
- [fault(_:)](<fault(__).md>) — Writes a message to the log about a bug that occurs when your app executes.
- [critical(_:)](<critical(__).md>) — Writes a message to the log about a critical event in your app’s execution.
