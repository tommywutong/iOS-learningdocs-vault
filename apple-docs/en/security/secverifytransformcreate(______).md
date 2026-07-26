---
title: 'SecVerifyTransformCreate(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/secverifytransformcreate(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secverifytransformcreate(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secverifytransformcreate%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:e4cc1b69f3cd674b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecVerifyTransformCreate(_:_:_:)

<sub>Function</sub>

Creates a verify transform object.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecVerifyTransformCreate(_ key: SecKey, _ signature: CFData?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?
```

## Parameters

- `key` — A [SecKey](seckey.md) with the public key used for signing.

- `signature` — A [CFData](../corefoundation/cfdata.md) with the signature. This value may be `NULL`, and you may connect a transform to kSecTransformSignatureAttributeName to supply it from another signature.

- `error` — A pointer to a [CFError](../corefoundation/cferror.md). This pointer will be set if an error occurred. This value may be `NULL` if you do not want an error returned.

## Return Value

A pointer to a new transform or `NULL` on error. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free this object’s memory when you are done with it.

## Discussion

This function creates a transform which verifies a cryptographic signature. The [kSecInputIsAttributeName](ksecinputisattributename.md) attribute defaults to [kSecInputIsPlainText](ksecinputisplaintext.md), and the [kSecDigestTypeAttribute](ksecdigesttypeattribute.md) and [kSecDigestLengthAttribute](ksecdigestlengthattribute.md) attributes default to something appropriate for the type of key you have supplied.
