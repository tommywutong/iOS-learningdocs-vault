---
title: PHPersistentChangeFetchResult
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phpersistentchangefetchresult
source_url: 'https://developer.apple.com/documentation/photos/phpersistentchangefetchresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phpersistentchangefetchresult.json'
content_hash: 'sha256:07fc35372300a751'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHPersistentChangeFetchResult

<sub>Class</sub>

An object that represents a fetch result and allows you to enumerate a very large set of change records.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHPersistentChangeFetchResult
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sequence](../swift/sequence.md)

## Topics

### Performing Operations with Objects in a Fetch Request

- [PHPersistentChange](phpersistentchange.md) — An object that represents a change in the Photos library, and allows for requesting local identifiers that identify the changes for a library object.

## See Also

### Fetching Change History

- [- fetchPersistentChangesSinceToken:error:](<phphotolibrary/fetchpersistentchanges(since_).md>) — Retrieves the Photos library changes since the token you specify.
- [currentChangeToken](phphotolibrary/currentchangetoken.md) — The opaque token that represents the current state of the Photos library.
- [PHPersistentChangeToken](phpersistentchangetoken.md) — An opaque object that tracks the state of the Photos library between runs, and that you can copy and serialize for future use.
