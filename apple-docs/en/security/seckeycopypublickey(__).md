---
title: 'SecKeyCopyPublicKey(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seckeycopypublickey(_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeycopypublickey(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeycopypublickey%28_%3A%29.json'
content_hash: 'sha256:fa82e0bed2b7881d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyCopyPublicKey(_:)

<sub>Function</sub>

Gets the public key associated with the given private key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyCopyPublicKey(_ key: SecKey) -> SecKey?
```

## Parameters

- `key` — The private key for which you want the corresponding public key.

## Return Value

The public key corresponding to the given private key. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free this key’s memory when you are done with it.

## Discussion

The returned public key may be `nil` if the app that created the private key didn’t also store the corresponding public key in the keychain, or if the system can’t reconstruct the corresponding public key.
