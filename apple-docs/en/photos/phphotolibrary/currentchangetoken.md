---
title: currentChangeToken
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phphotolibrary/currentchangetoken
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/currentchangetoken'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/currentchangetoken.json'
content_hash: 'sha256:de1bad8ae30f25bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# currentChangeToken

<sub>Instance Property</sub>

The opaque token that represents the current state of the Photos library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var currentChangeToken: PHPersistentChangeToken { get }
```

## See Also

### Fetching Change History

- [- fetchPersistentChangesSinceToken:error:](<fetchpersistentchanges(since_).md>) — Retrieves the Photos library changes since the token you specify.
- [PHPersistentChangeFetchResult](../phpersistentchangefetchresult.md) — An object that represents a fetch result and allows you to enumerate a very large set of change records.
- [PHPersistentChangeToken](../phpersistentchangetoken.md) — An opaque object that tracks the state of the Photos library between runs, and that you can copy and serialize for future use.
