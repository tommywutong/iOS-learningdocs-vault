---
title: SecKey
framework: Security
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckey
source_url: 'https://developer.apple.com/documentation/security/seckey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckey.json'
content_hash: 'sha256:d0c6b33fbe2737a1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKey

<sub>Class</sub>

An object that represents a cryptographic key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class SecKey
```

## Overview

A [SecKey](seckey.md) instance that represents a key that is stored in a keychain can be safely cast to a [SecKeychainItem](seckeychainitem.md) for manipulation as a keychain item. On the other hand, if the key is not stored in a keychain, casting the object to a [SecKeychainItem](seckeychainitem.md) and passing it to Keychain Services functions returns errors.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)
