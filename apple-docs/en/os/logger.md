---
title: Logger
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/logger
source_url: 'https://developer.apple.com/documentation/os/logger'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/logger.json'
content_hash: 'sha256:c3627fff833037ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# Logger

<sub>Structure</sub>

An object for writing interpolated string messages to the unified logging system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Logger
```

## Overview

Create a [Logger](logger.md) structure and use it to log messages about your app’s behavior. When logging a message, you specify the message and any program variables or custom data to help you assess the state of your app. You also choose a log level to indicate the severity of that message. The system records log messages in memory and, in some cases, also writes those messages to an on-disk data store. The log level determines which messages stay in memory and which go to disk.

When you create a [Logger](logger.md) structure, assign an optional subsystem and category string to add context to all messages you log. A subsystem corresponds to a large functional area of your app, and a category corresponds to a specific area within a particular subsystem. When diagnosing problems, use those strings to filter out unrelated messages.

To log a message, call the method that represents the appropriate log level for that message. To create the message, use a Swift string. Strings may contain interpolated values, such as signed and unsigned integers, floating-point and double values, Booleans, other strings, Objective-C objects, and types that conform to the [CustomStringConvertible](../swift/customstringconvertible.md) protocol. You can also include metatypes such as `Int.self`.

```swift
let logger = Logger()
let x = 42
logger.info("The answer is \(x)")
```

When you include an interpolated string or custom object in your message, the system redacts the value of that string or object by default. This behavior prevents the system from leaking potentially user-sensitive information in the log files, such as the user’s account information. If the data doesn’t contain sensitive information, change the privacy option of that value when logging the information. In the following code example, the system redacts the account information in the first log message, but displays the user’s selection in the second log message:

```swift
logger.log("Paid with bank account \(accountNumber)")   // Redacted!
logger.log("Ordered smoothie \(smoothieName, privacy: .public)")  // Visible
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Logger

- [init()](<logger/init().md>) — Creates a logger that writes to the default subsystem.
- [init(subsystem:category:)](<logger/init(subsystem_category_).md>) — Creates a logger using the specified subsystem and category.
- [init(_:)](<logger/init(__).md>) — Creates a logger that writes to the specified log.
- [OSLog](oslog.md) — A container of related log messages.

### Logging a Message

- [log(_:)](<logger/log(__).md>) — Writes a message to the log using the default log type.
- [log(level:_:)](<logger/log(level___).md>) — Writes a message to the log using the specified log type.
- [OSLogType](oslogtype.md) — The various log levels that the unified logging system provides.
- [OSLogMessage](oslogmessage.md) — An object that represents a log message.

### Logging a Scoped Message

- [notice(_:)](<logger/notice(__).md>) — Writes a message to the log using the default log type.
- [debug(_:)](<logger/debug(__).md>) — Writes a debug message to the log.
- [trace(_:)](<logger/trace(__).md>) — Writes a trace message to the log.
- [info(_:)](<logger/info(__).md>) — Writes an informative message to the log.
- [error(_:)](<logger/error(__).md>) — Writes information about an error to the log.
- [warning(_:)](<logger/warning(__).md>) — Writes information about a warning to the log.
- [fault(_:)](<logger/fault(__).md>) — Writes a message to the log about a bug that occurs when your app executes.
- [critical(_:)](<logger/critical(__).md>) — Writes a message to the log about a critical event in your app’s execution.

### Instance Methods

- [isEnabled(type:)](<logger/isenabled(type_).md>) — Checks if the Logger can emit log messages for a given log type. This allows for more granular control over logging based on the log level.

### Type Properties

- [disabled](logger/disabled.md) — A disabled Logger that won’t emit log messages at runtime. Use to turn off all logging emitted using a specific logger variable.

## See Also

### Log Messages

- [Message Argument Formatters](message-argument-formatters.md) — Manage the privacy and presentation of the message’s interpolated values using type-aware formatters.
- [OSLogType](oslogtype.md) — The various log levels that the unified logging system provides.
