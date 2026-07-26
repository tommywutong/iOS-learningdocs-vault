---
title: 'SecKeyCopyExternalRepresentation(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seckeycopyexternalrepresentation(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeycopyexternalrepresentation(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeycopyexternalrepresentation%28_%3A_%3A%29.json'
content_hash: 'sha256:092b73b24dc8cdab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyCopyExternalRepresentation(_:_:)

<sub>Function</sub>

Returns an external representation of the given key suitable for the key’s type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyCopyExternalRepresentation(_ key: SecKey, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

## Parameters

- `key` — The key to export.

- `error` — The address of a [CFError](../corefoundation/cferror.md) object. If an error occurs, this is set to point at an error instance that describes the failure.

## Return Value

A data object representing the key in a format suitable for the key type or `NULL` on error. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free the key’s memory when you are done with it.

## Discussion

The operation fails if the key is not exportable, for example if it is bound to a smart card or to the Secure Enclave. It also fails in macOS if the key has the attribute [kSecKeyExtractable](kseckeyextractable.md) set to [false](../swift/false.md).

The method returns data in the PKCS #1 format for an RSA key. For an elliptic curve public key, the format follows the ANSI X9.63 standard using a byte string of `04 || X || Y.` For an elliptic curve private key, the output is formatted as the public key concatenated with the big endian encoding of the secret scalar, or `04 || X || Y || K`. All of these representations use constant size integers, including leading zeros as needed.
