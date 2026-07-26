---
title: ReferenceConvertible
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/referenceconvertible
source_url: 'https://developer.apple.com/documentation/foundation/referenceconvertible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/referenceconvertible.json'
content_hash: 'sha256:9d450147ce5aef5c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ReferenceConvertible

<sub>Protocol</sub>

A decoration applied to types that are backed by a Foundation reference type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ReferenceConvertible : CustomDebugStringConvertible, CustomStringConvertible, Hashable, _ObjectiveCBridgeable
```

## Overview

All `ReferenceConvertible` types are hashable, equatable, and provide description functions.

> [!warning] Warning
> Don’t create new conformances to this protocol. `ReferenceConvertible` only supports types provided by the SDK.

## Relationships

- **Inherits From**: [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

- **Conforming Types**: [AffineTransform](affinetransform.md), [Calendar](calendar.md), [CharacterSet](characterset.md), [Data](data.md), [Date](date.md), [DateComponents](datecomponents.md), [DateInterval](dateinterval.md), [IndexPath](indexpath.md), [IndexSet](indexset.md), [Locale](locale.md), [Measurement](measurement.md), [Notification](notification.md), [PersonNameComponents](personnamecomponents.md), [TimeZone](timezone.md), [URL](url.md), [URLComponents](urlcomponents.md), [URLQueryItem](urlqueryitem.md), [URLRequest](urlrequest.md), [UUID](uuid.md)

## Topics

### Supporting types

- [ReferenceType](referenceconvertible/referencetype.md)

## See Also

### Swift Support

- [Classes Bridged to Swift Standard Library Value Types](classes-bridged-to-swift-standard-library-value-types.md) — Use bridged reference types when you need reference semantics or Foundation-specific behavior.
