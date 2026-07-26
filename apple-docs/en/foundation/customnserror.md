---
title: CustomNSError
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/customnserror
source_url: 'https://developer.apple.com/documentation/foundation/customnserror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/customnserror.json'
content_hash: 'sha256:3ab29066c3336c04'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# CustomNSError

<sub>Protocol</sub>

A specialized error that provides a domain, error code, and user-info dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol CustomNSError : Error
```

## Relationships

- **Inherits From**: [Error](../swift/error.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [CocoaError](cocoaerror.md), [MachError](macherror.md), [POSIXError](posixerror.md), [URLError](urlerror.md)

## Topics

### Instance Properties

- [errorCode](customnserror/errorcode.md) — The error code within the given domain.
- [errorUserInfo](customnserror/erroruserinfo.md) — The user-info dictionary.

### Type Properties

- [errorDomain](customnserror/errordomain.md) — The domain of the error.

## See Also

### User-Relevant Errors

- [Error](../swift/error.md) — A type representing an error value that can be thrown.
- [NSError](nserror.md) — Information about an error condition including a domain, a domain-specific error code, and application-specific information.
- [LocalizedError](localizederror.md) — A specialized error that provides localized messages describing the error and why it occurred.
- [RecoverableError](recoverableerror.md) — A specialized error that may be recoverable by presenting several potential recovery options to the user.
