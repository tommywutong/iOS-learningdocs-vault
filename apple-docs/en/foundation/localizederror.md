---
title: LocalizedError
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/localizederror
source_url: 'https://developer.apple.com/documentation/foundation/localizederror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/localizederror.json'
content_hash: 'sha256:8ebfdef0f01e30ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# LocalizedError

<sub>Protocol</sub>

A specialized error that provides localized messages describing the error and why it occurred.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol LocalizedError : Error
```

## Relationships

- **Inherits From**: [Error](../swift/error.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [errorDescription](localizederror/errordescription.md) — A localized message describing what error occurred.
- [failureReason](localizederror/failurereason.md) — A localized message describing the reason for the failure.
- [helpAnchor](localizederror/helpanchor.md) — A localized message providing “help” text if the user requests help.
- [recoverySuggestion](localizederror/recoverysuggestion.md) — A localized message describing how one might recover from the failure.

## See Also

### User-Relevant Errors

- [Error](../swift/error.md) — A type representing an error value that can be thrown.
- [NSError](nserror.md) — Information about an error condition including a domain, a domain-specific error code, and application-specific information.
- [RecoverableError](recoverableerror.md) — A specialized error that may be recoverable by presenting several potential recovery options to the user.
- [CustomNSError](customnserror.md) — A specialized error that provides a domain, error code, and user-info dictionary.
