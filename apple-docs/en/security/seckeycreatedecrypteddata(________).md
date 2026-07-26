---
title: 'SecKeyCreateDecryptedData(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seckeycreatedecrypteddata(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeycreatedecrypteddata(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeycreatedecrypteddata%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:f37aabddd8119c50'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyCreateDecryptedData(_:_:_:_:)

<sub>Function</sub>

Decrypts a block of data using a private key and specified algorithm.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyCreateDecryptedData(_ key: SecKey, _ algorithm: SecKeyAlgorithm, _ ciphertext: CFData, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

## Parameters

- `key` — The private key to use to perform the decryption.

- `algorithm` — The algorithm that was used to encrypt the data in the first place. Use one of the encryption algorithms listed in [SecKeyAlgorithm](seckeyalgorithm.md). You can use the [SecKeyIsAlgorithmSupported](<seckeyisalgorithmsupported(______).md>) function to test that the key is suitable for the algorithm.

- `ciphertext` — The data, produced with the corresponding public key and a call to the [SecKeyCreateEncryptedData](<seckeycreateencrypteddata(________).md>) function, that you want to decrypt.

- `error` — The address of a [CFError](../corefoundation/cferror.md) object. If an error occurs, this is set to point at an error instance that describes the failure.

## Return Value

The decrypted data or `NULL` on failure. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free the data’s memory when you are done with it.
