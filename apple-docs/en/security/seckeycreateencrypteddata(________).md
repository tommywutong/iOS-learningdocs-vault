---
title: 'SecKeyCreateEncryptedData(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seckeycreateencrypteddata(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeycreateencrypteddata(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeycreateencrypteddata%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8e8c8e0a86744e07'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyCreateEncryptedData(_:_:_:_:)

<sub>Function</sub>

Encrypts a block of data using a public key and specified algorithm.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyCreateEncryptedData(_ key: SecKey, _ algorithm: SecKeyAlgorithm, _ plaintext: CFData, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

## Parameters

- `key` — The public key to use to perform the encryption.

- `algorithm` — The encryption algorithm to use. Use one of the encryption algorithms listed in [SecKeyAlgorithm](seckeyalgorithm.md). You can use the [SecKeyIsAlgorithmSupported](<seckeyisalgorithmsupported(______).md>) function to test that the key is suitable for the algorithm.

- `plaintext` — The data to be encrypted.

- `error` — The address of a [CFError](../corefoundation/cferror.md) object. If an error occurs, this is set to point at an error instance that describes the failure.

## Return Value

The encrypted data or `NULL` on failure. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free the data’s memory when you are done with it.

## Discussion

You can decrypt this data with the corresponding private key and a call to [SecKeyCreateDecryptedData](<seckeycreatedecrypteddata(________).md>).
