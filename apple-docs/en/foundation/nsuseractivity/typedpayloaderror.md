---
title: NSUserActivity.TypedPayloadError
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/typedpayloaderror
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/typedpayloaderror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/typedpayloaderror.json'
content_hash: 'sha256:08701c606d40419f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# NSUserActivity.TypedPayloadError

<sub>Enumeration</sub>

An enumeration that describes the error types for getting and setting a typed payload.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum TypedPayloadError
```

## Overview

Use this enumeration to manage errors from [typedPayload(_:)](<typedpayload(__).md>) and [setTypedPayload(_:)](<settypedpayload(__).md>).

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Error](../../swift/error.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Typed payload errors

- [NSUserActivity.TypedPayloadError.encodingError](typedpayloaderror/encodingerror.md) — An encoding error that indicates that the content failed to encode into a valid dictionary.
- [NSUserActivity.TypedPayloadError.invalidContent](typedpayloaderror/invalidcontent.md) — A decoding error that indicates that the user info dictionary is empty or invalid.

## See Also

### Managing type-safe access to user info

- [setTypedPayload(_:)](<settypedpayload(__).md>) — Encodes the specified payload into the user activity’s user info dictionary.
- [typedPayload(_:)](<typedpayload(__).md>) — Decodes the user activity’s user info dictionary as an instance of the specified type.
