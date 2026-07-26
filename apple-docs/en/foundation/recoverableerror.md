---
title: RecoverableError
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/recoverableerror
source_url: 'https://developer.apple.com/documentation/foundation/recoverableerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/recoverableerror.json'
content_hash: 'sha256:87b6a0e998399c78'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# RecoverableError

<sub>Protocol</sub>

A specialized error that may be recoverable by presenting several potential recovery options to the user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol RecoverableError : Error
```

## Relationships

- **Inherits From**: [Error](../swift/error.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [recoveryOptions](recoverableerror/recoveryoptions.md) — Provides a set of possible recovery options to present to the user.

### Instance Methods

- [attemptRecovery(optionIndex:)](<recoverableerror/attemptrecovery(optionindex_).md>) — Attempt to recover from this error when the user selected the option at the given index. Returns true to indicate successful recovery, and false otherwise.
- [attemptRecovery(optionIndex:resultHandler:)](<recoverableerror/attemptrecovery(optionindex_resulthandler_).md>) — Attempt to recover from this error when the user selected the option at the given index. This routine must call handler and indicate whether recovery was successful (or not).

## See Also

### User-Relevant Errors

- [Error](../swift/error.md) — A type representing an error value that can be thrown.
- [NSError](nserror.md) — Information about an error condition including a domain, a domain-specific error code, and application-specific information.
- [LocalizedError](localizederror.md) — A specialized error that provides localized messages describing the error and why it occurred.
- [CustomNSError](customnserror.md) — A specialized error that provides a domain, error code, and user-info dictionary.
