---
title: errSSLDecryptionFail
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.0+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/errssldecryptionfail
source_url: 'https://developer.apple.com/documentation/security/errssldecryptionfail'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/errssldecryptionfail.json'
content_hash: 'sha256:f5b1d5aea2c82b37'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# errSSLDecryptionFail

<sub>Global Variable</sub>

Decryption failed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var errSSLDecryptionFail: OSStatus { get }
```

## Discussion

Among other causes, this may be caused by invalid data coming from the remote host, a damaged crypto key, or insufficient permission to use a key that is stored in the keychain.
