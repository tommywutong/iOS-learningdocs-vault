---
title: SecKeyGenerate
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/seckeygenerate
source_url: 'https://developer.apple.com/documentation/security/seckeygenerate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeygenerate.json'
content_hash: 'sha256:9c1b96443f60e8fa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyGenerate

<sub>Function</sub>

Creates a symmetric key and optionally stores it in a keychain.

<sub>macOS</sub>

```objc
OSStatus SecKeyGenerate(SecKeychainRef keychainRef, CSSM_ALGORITHMS algorithm, uint32 keySizeInBits, CSSM_CC_HANDLE contextHandle, CSSM_KEYUSE keyUsage, uint32 keyAttr, SecAccessRef initialAccess, SecKeyRef*keyRef);
```

## Parameters

- `keychainRef` — The keychain in which to store the generated key. Specify `NULL` to generate a transient key.

- `algorithm` — The algorithm to use in generating the symmetric key. Possible values are defined in `cssmtype.h`. Algorithms supported by the AppleCSP module are listed in [Apple Cryptographic Service Provider Functional Specification](https://developer.apple.com/library/archive/documentation/Security/Reference/SecAppleCryptoSpec/Apple_Cryptographic_Service_Provider_Functional_Specification.pdf). This parameter is ignored if the `contextHandle` parameter is not `0`.

- `keySizeInBits` — A key size for the key pair. This parameter is ignored if the `contextHandle` parameter is not `0`.

- `contextHandle` — A CSSM CSP handle, or `0`. If this argument is not `0`, the `algorithm` and `keySizeInBits` parameters are ignored.

- `keyUsage` — A bit mask indicating all permitted uses for the new key. The possible values for the `CSSM_KEYUSE` data type are defined in `cssmtype.h`.

- `keyAttr` — A bit mask defining attribute values for the new key. The bit mask values are defined in `CSSM_KEYATTR_FLAGS` in `cssmtype.h`.

- `initialAccess` — An access object that sets the initial access control list for the key returned. See Creating an Access Object in [Keychain services](keychain-services.md) for functions that create an access object. This parameter is ignored if you specify `NULL` for the `keychainRef` parameter.

- `keyRef` — On return, points to the keychain item object of the new public key. Use this object as input to the [SecKeyGetCSSMKey](seckeygetcssmkey.md) function to obtain the `CSSM_KEY` structure containing the key. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Key-generation algorithms supported by the AppleCSP module are listed in [Apple Cryptographic Service Provider Functional Specification](https://developer.apple.com/library/archive/documentation/Security/Reference/SecAppleCryptoSpec/Apple_Cryptographic_Service_Provider_Functional_Specification.pdf). For details about algorithms and default values for key-generation parameters, download the CDSA security framework from Apple’s Open Source website at [https://opensource.apple.com/](https://opensource.apple.com/) and read the file `Supported_CSP_Algorithms.doc` in the Documentation folder.

If you need extra parameters to generate a key—as required by some algorithms—call [SecKeychainGetCSPHandle](seckeychaingetcsphandle.md) to obtain a CSSM CSP handle and then call `CSSM_CSP_CreateKeyGenContext` to create a context. With this context, use `CSSM_UpdateContextAttributes` to add additional parameters. Finally, call `CSSM_DeleteContext` to dispose of the context after calling this function.

### Special Considerations

Use [SecKeyGenerateSymmetric](<seckeygeneratesymmetric(____).md>) instead.
