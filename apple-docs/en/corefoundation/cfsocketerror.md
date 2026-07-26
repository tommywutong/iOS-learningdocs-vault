---
title: CFSocketError
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsocketerror
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketerror.json'
content_hash: 'sha256:03aab73b6eb943d8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketError

<sub>Enumeration</sub>

Error codes for many CFSocket functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CFSocketError
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCFSocketSuccess](cfsocketerror/success.md) — The socket operation succeeded.
- [kCFSocketError](cfsocketerror/error.md) — The socket operation failed.
- [kCFSocketTimeout](cfsocketerror/timeout.md) — The socket operation timed out.

### Initializers

- [init(rawValue:)](<cfsocketerror/init(rawvalue_).md>)

## See Also

### Constants

- [CFSocketCallBackType](cfsocketcallbacktype.md) — Types of socket activity that can cause the callback function of a CFSocket object to be called.
- [CFSocket Flags](1560944-cfsocket-flags.md) — Flags that can be set on a CFSocket object to control its behavior.
