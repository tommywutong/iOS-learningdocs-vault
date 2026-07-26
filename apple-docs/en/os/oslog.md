---
title: OSLog
framework: os
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslog
source_url: 'https://developer.apple.com/documentation/os/oslog'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslog.json'
content_hash: 'sha256:b3a1685a1ad34cdd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# OSLog

<sub>Class</sub>

A container of related log messages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class OSLog
```

## Overview

A log categorizes the messages you write and makes it easy to sort and filter them. Each log contains a subsystem and a category, which you define. A subsystem identifies a major functional area of your app, which you specify using reverse DNS notation, such as `com.your_company.your_subsystem_name`. A category segregates specific areas within a subsystem.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Log

- [init(subsystem:category:)](<oslog/init(subsystem_category_)-17gyy.md>) — Creates a log using the specified subsystem and category.
- [init(subsystem:category:)](<oslog/init(subsystem_category_)-72ghw.md>) — Creates a log using the specified subsystem and system-defined category.
- [Category](oslog/category.md) — System-defined categories that identify well-known parts of your app.

### Getting the Shared Logs

- [default](oslog/default.md) — The shared default log.
- [disabled](oslog/disabled.md) — The shared disabled log.

### Getting Log Configuration

- [os_log_type_enabled](<oslog/isenabled(type_).md>) — Returns a Boolean value that indicates whether the log can write messages with the specified log type.
- [signpostsEnabled](oslog/signpostsenabled.md) — A Boolean value that indicates whether a log is able to use signpost logging.

## See Also

### Creating a Logger

- [init()](<logger/init().md>) — Creates a logger that writes to the default subsystem.
- [init(subsystem:category:)](<logger/init(subsystem_category_).md>) — Creates a logger using the specified subsystem and category.
- [init(_:)](<logger/init(__).md>) — Creates a logger that writes to the specified log.
