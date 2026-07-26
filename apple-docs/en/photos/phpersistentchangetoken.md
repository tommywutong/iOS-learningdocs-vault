---
title: PHPersistentChangeToken
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phpersistentchangetoken
source_url: 'https://developer.apple.com/documentation/photos/phpersistentchangetoken'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phpersistentchangetoken.json'
content_hash: 'sha256:57cf5289d184b51d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHPersistentChangeToken

<sub>Class</sub>

An opaque object that tracks the state of the Photos library between runs, and that you can copy and serialize for future use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHPersistentChangeToken
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(coder:)](<phpersistentchangetoken/init(coder_).md>)

## See Also

### Fetching Change History

- [- fetchPersistentChangesSinceToken:error:](<phphotolibrary/fetchpersistentchanges(since_).md>) — Retrieves the Photos library changes since the token you specify.
- [PHPersistentChangeFetchResult](phpersistentchangefetchresult.md) — An object that represents a fetch result and allows you to enumerate a very large set of change records.
- [currentChangeToken](phphotolibrary/currentchangetoken.md) — The opaque token that represents the current state of the Photos library.
