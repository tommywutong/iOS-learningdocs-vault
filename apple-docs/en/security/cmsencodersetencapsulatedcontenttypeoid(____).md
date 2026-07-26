---
title: 'CMSEncoderSetEncapsulatedContentTypeOID(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsencodersetencapsulatedcontenttypeoid(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsencodersetencapsulatedcontenttypeoid(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencodersetencapsulatedcontenttypeoid%28_%3A_%3A%29.json'
content_hash: 'sha256:1201f4bb0d85f27d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderSetEncapsulatedContentTypeOID(_:_:)

<sub>Function</sub>

Specifies an object identifier for the encapsulated data of a signed message.

<sub>macOS</sub>

```swift
func CMSEncoderSetEncapsulatedContentTypeOID(_ cmsEncoder: CMSEncoder, _ eContentTypeOID: CFTypeRef) -> OSStatus
```

## Parameters

- `cmsEncoder` — The CMSEncoder reference returned by the `CMSEncoderCreate` function.

- `eContentTypeOID` — The object identifier for the encapsulated data in a signed message.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

In a signed message, the signed data consists of any type of content (referred to as the _encapsulated content_, because it is encapsulated in the signed data) plus the signature values. You can indicate the content type of the encapsulated data by specifying an object identifier (OID) in the `eContentTypeOID` parameter of this function, in the form of a Core Foundation string—`CFSTR("1.2.840.113549.1.7.1")`, for example.

The default value for the OID (used if this function is not called) is `id-data`. This is the normal encapsulated content type for applications such as S/MIME, which uses it to indicate MIME-encoded content. You can pass any value that is meaningful to your application. Examples of CMS OIDs are listed in [http://www.imc.org/ietf-smime/other-smime-oids.asn](http://www.imc.org/ietf-smime/other-smime-oids.asn).

If you do call this function, you must call it before the first call to the `CMSEncoderUpdateContent` function.

## See Also

### Related Documentation

- [CMSDecoderCopyEncapsulatedContentType](<cmsdecodercopyencapsulatedcontenttype(____).md>) — Obtains the object identifier for the encapsulated data of a signed message.
- [CMSEncoderUpdateContent](<cmsencoderupdatecontent(______).md>) — Feeds content bytes into the encoder.
- [CMSEncoderCreate](<cmsencodercreate(__).md>) — Creates a CMSEncoder reference.
- [CMSEncoderCopyEncapsulatedContentType](<cmsencodercopyencapsulatedcontenttype(____).md>) — Obtains the object identifier for the encapsulated data of a signed message.
