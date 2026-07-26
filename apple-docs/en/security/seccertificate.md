---
title: SecCertificate
framework: Security
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccertificate
source_url: 'https://developer.apple.com/documentation/security/seccertificate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificate.json'
content_hash: 'sha256:0c3360a360a19027'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificate

<sub>Class</sub>

An abstract Core Foundation-type object representing an X.509 certificate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class SecCertificate
```

## Overview

A [SecCertificate](seccertificate.md) object for a certificate that is stored in a keychain can be safely cast to a [SecKeychainItem](seckeychainitem.md) for manipulation as a keychain item. On the other hand, if the [SecCertificate](seccertificate.md) is not stored in a keychain, casting the object to a [SecKeychainItem](seckeychainitem.md) and passing it to Keychain Services functions returns errors.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)
