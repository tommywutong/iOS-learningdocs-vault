---
title: SecKeychainItem
framework: Security
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychainitem
source_url: 'https://developer.apple.com/documentation/security/seckeychainitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainitem.json'
content_hash: 'sha256:ab64b9f0efb708f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainItem

<sub>Class</sub>

An opaque type that represents a keychain item.

<sub>macOS</sub>

```swift
class SecKeychainItem
```

## Overview

A [SecKeychainItem](seckeychainitem.md) object for a certificate that is stored in a keychain can be safely cast to a [SecCertificate](seccertificate.md) for use with [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)
