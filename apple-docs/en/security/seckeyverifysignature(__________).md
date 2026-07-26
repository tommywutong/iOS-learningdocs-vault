---
title: 'SecKeyVerifySignature(_:_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seckeyverifysignature(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeyverifysignature(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyverifysignature%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:346939dff736aa4f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyVerifySignature(_:_:_:_:_:)

<sub>Function</sub>

Verifies the cryptographic signature of a block of data using a public key and specified algorithm.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyVerifySignature(_ key: SecKey, _ algorithm: SecKeyAlgorithm, _ signedData: CFData, _ signature: CFData, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool
```

## Parameters

- `key` — The public key to use in evaluating the signature.

- `algorithm` — The algorithm that was used to create the signature. Use one of the signing algorithms listed in [SecKeyAlgorithm](seckeyalgorithm.md). You can use the [SecKeyIsAlgorithmSupported](<seckeyisalgorithmsupported(______).md>) function to test that the key is suitable for the algorithm.

- `signedData` — The data that was signed.

- `signature` — The signature that was created with a call to the [SecKeyCreateSignature](<seckeycreatesignature(________).md>) function.

- `error` — The address of a [CFError](../corefoundation/cferror.md) object. If an error occurs, this is set to point at an error instance that describes the failure.

## Return Value

A Boolean indicating whether or not the data and signature are intact.
