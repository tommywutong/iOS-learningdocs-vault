---
title: kSecKeyEffectiveKeySize
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/kseckeyeffectivekeysize
source_url: 'https://developer.apple.com/documentation/security/kseckeyeffectivekeysize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseckeyeffectivekeysize.json'
content_hash: 'sha256:3b28bf498de7a0e3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecKeyEffectiveKeySize

<sub>Global Variable</sub>

Type uint32; value is the effective number of bits in this key.  For example, a DES key has a key size in bits (`kSecKeyKeySizeInBits`) of 64 but a value for `kSecKeyEffectiveKeySize` of 56.

<sub>macOS</sub>

```swift
var kSecKeyEffectiveKeySize: Int32 { get }
```
