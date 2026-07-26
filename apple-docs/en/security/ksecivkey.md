---
title: kSecIVKey
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksecivkey
source_url: 'https://developer.apple.com/documentation/security/ksecivkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecivkey.json'
content_hash: 'sha256:a136f911224f8948'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecIVKey

<sub>Global Variable</sub>

The setting for an initialization vector.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecIVKey: CFString
```

## Discussion

The key’s associated value is an initialization vector. Provide random bytes for this value—for example, created by calling the [SecRandomCopyBytes](<secrandomcopybytes(______).md>) method—unless your specification requires something else. The number of bytes in the vector should match the block size of the underlying block cipher. For example, use 16 bytes for AES encryption.

If you don’t supply a value for this key, any operations that require an initialization vector use a value of zero by default, which can compromise the security of your encryption.
