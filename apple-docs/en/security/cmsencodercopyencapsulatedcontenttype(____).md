---
title: 'CMSEncoderCopyEncapsulatedContentType(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsencodercopyencapsulatedcontenttype(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsencodercopyencapsulatedcontenttype(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencodercopyencapsulatedcontenttype%28_%3A_%3A%29.json'
content_hash: 'sha256:b8bdeffe49475248'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderCopyEncapsulatedContentType(_:_:)

<sub>Function</sub>

Obtains the object identifier for the encapsulated data of a signed message.

<sub>macOS</sub>

```swift
func CMSEncoderCopyEncapsulatedContentType(_ cmsEncoder: CMSEncoder, _ eContentTypeOut: UnsafeMutablePointer<CFData?>) -> OSStatus
```

## Parameters

- `cmsEncoder` — The CMSEncoder reference returned by the `CMSEncoderCreate` function.

- `eContentTypeOut` — On return, points to the object identifier for the encapsulated data in the signed message.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

In a signed message, the signed data consists of any type of data (the _encapsulated content_) plus the signature values. This function returns the object identifier (OID) of the encapsulated content as it was specified with the `CMSEncoderSetEncapsulatedContentType` function.

If the `CMSEncoderSetEncapsulatedContentType` function has not been called for this message, this function returns a  `NULL` pointer.
