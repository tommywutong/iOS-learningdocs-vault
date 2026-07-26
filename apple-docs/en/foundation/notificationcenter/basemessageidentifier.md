---
title: NotificationCenter.BaseMessageIdentifier
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/notificationcenter/basemessageidentifier
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/basemessageidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/basemessageidentifier.json'
content_hash: 'sha256:1e830400d9aa0a8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationCenter](../notificationcenter.md)

# NotificationCenter.BaseMessageIdentifier

<sub>Structure</sub>

A type for use when defining optional Message identifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct BaseMessageIdentifier<MessageType>
```

## Overview

See [MessageIdentifier](messageidentifier.md) for an example of how to use this type when defining your own message identifiers.

## Relationships

- **Conforms To**: [MessageIdentifier](messageidentifier.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating an identifier for a main actor message

- [init()](<basemessageidentifier/init()-66tt2.md>)

### Creating an identifier for an asynchronous message

- [init()](<basemessageidentifier/init()-2yi72.md>)

## See Also

### Using message identifiers

- [MessageIdentifier](messageidentifier.md) — An optional identifier to associate a given message with a given type.
