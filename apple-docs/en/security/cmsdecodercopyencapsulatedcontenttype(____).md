---
title: 'CMSDecoderCopyEncapsulatedContentType(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsdecodercopyencapsulatedcontenttype(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsdecodercopyencapsulatedcontenttype(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsdecodercopyencapsulatedcontenttype%28_%3A_%3A%29.json'
content_hash: 'sha256:abd36b8647256e03'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSDecoderCopyEncapsulatedContentType(_:_:)

<sub>Function</sub>

Obtains the object identifier for the encapsulated data of a signed message.

<sub>macOS</sub>

```swift
func CMSDecoderCopyEncapsulatedContentType(_ cmsDecoder: CMSDecoder, _ eContentTypeOut: UnsafeMutablePointer<CFData?>) -> OSStatus
```

## Parameters

- `cmsDecoder` — The CMSDecoder reference returned by the `CMSDecoderCreate` function.

- `eContentTypeOut` — On return, the object identifier for the encapsulated data in a signed message.  Returns `NULL` if the message was not signed.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

In a signed message, the signed data consists of any type of content (referred to as the _encapsulated content_, because it is encapsulated in the signed data) plus the signature values. The content type of the encapsulated data is indicated by an object identifier. The default value for the OID is `id-data`, which indicates MIME-encoded content.

You cannot call this function until after you have called the `CMSDecoderFinalizeMessage` function.
