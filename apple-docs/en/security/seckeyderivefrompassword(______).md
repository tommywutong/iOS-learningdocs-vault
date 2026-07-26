---
title: 'SecKeyDeriveFromPassword(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeyderivefrompassword(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeyderivefrompassword(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyderivefrompassword%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ce4a2d88cade9836'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyDeriveFromPassword(_:_:_:)

<sub>Function</sub>

Returns a key object in which the key data is derived from a password.

> [!warning] Deprecated
> No longer supported

<sub>macOS</sub>

```swift
func SecKeyDeriveFromPassword(_ password: CFString, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?
```

## Parameters

- `password` — The password from which the key should be derived.

- `parameters` — A set of parameters for deriving the password.

- `error` — A pointer to a [CFError](../corefoundation/cferror.md) variable where an error object is stored upon failure. If not `NULL`, the caller is responsible for checking this variable and releasing the resulting object if it exists.

## Return Value

The derived key object, or `NULL` on error. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free the key’s memory when you are done with it.

## Discussion

The parameters dictionary must contain at least the following keys:

- [kSecKeyKeyType](kseckeykeytype.md)—the type of symmetric key to generate.
- [kSecAttrSalt](ksecattrsalt.md)—a `CFDataRef` object containing the salt value that is mixed into the pseudorandom rounds.

The parameters dictionary may contain the following optional keys:

- [kSecAttrPRF](ksecattrprf.md) - the algorithm to use for the pseudorandom-function.

If zero, this defaults to [kSecAttrPRFHmacAlgSHA1](ksecattrprfhmacalgsha1.md). For a list of possible values, see `kSecAttrPRF Value Constants`.

- [kSecAttrRounds](ksecattrrounds.md)—the number of times to call the pseudorandom function. If zero, the count is computed so that computation will take 1/10 of a second (on average).
- [kSecAttrKeySizeInBits](ksecattrkeysizeinbits.md)—a `CFNumberRef` value containing the requested key size in bits. The key size must be valid for the key type. Defaults to 128 if not provided.
