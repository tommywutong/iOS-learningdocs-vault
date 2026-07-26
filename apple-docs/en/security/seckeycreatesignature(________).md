---
title: 'SecKeyCreateSignature(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seckeycreatesignature(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeycreatesignature(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeycreatesignature%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:7f010085af2dd50d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyCreateSignature(_:_:_:_:)

<sub>Function</sub>

Creates the cryptographic signature for a block of data using a private key and specified algorithm.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyCreateSignature(_ key: SecKey, _ algorithm: SecKeyAlgorithm, _ dataToSign: CFData, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

## Parameters

- `key` — The private key to use in creating the signature.

- `algorithm` — The signing algorithm to use. Use one of the signing algorithms listed in [SecKeyAlgorithm](seckeyalgorithm.md). You can use the [SecKeyIsAlgorithmSupported](<seckeyisalgorithmsupported(______).md>) function to test that the key is suitable for the algorithm.

- `dataToSign` — The data whose signature you want.

- `error` — The address of a [CFError](../corefoundation/cferror.md) object. If an error occurs, this is set to point at an error instance that describes the failure.

## Return Value

The digital signature or `NULL` on failure. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free the data’s memory when you are done with it.

## Discussion

You later evaluate the combined data and signature with the corresponding public key and a call to the [SecKeyVerifySignature](<seckeyverifysignature(__________).md>) function.
