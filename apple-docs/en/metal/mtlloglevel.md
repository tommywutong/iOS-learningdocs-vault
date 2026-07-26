---
title: MTLLogLevel
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlloglevel
source_url: 'https://developer.apple.com/documentation/metal/mtlloglevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlloglevel.json'
content_hash: 'sha256:65c509fb4638c965'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLLogLevel

<sub>Enumeration</sub>

The supported log levels for shader logging.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLLogLevel
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration cases

- [MTLLogLevelDebug](mtlloglevel/debug.md) — The log level that captures diagnostic information.
- [MTLLogLevelInfo](mtlloglevel/info.md) — The log level that captures additional information.
- [MTLLogLevelNotice](mtlloglevel/notice.md) — The log level that captures notifications.
- [MTLLogLevelError](mtlloglevel/error.md) — The log level that captures error information.
- [MTLLogLevelFault](mtlloglevel/fault.md) — The log level that captures fault information.
- [MTLLogLevelUndefined](mtlloglevel/undefined.md) — The log level when the log level hasn’t been configured.

### Initializers

- [init(rawValue:)](<mtlloglevel/init(rawvalue_).md>)
