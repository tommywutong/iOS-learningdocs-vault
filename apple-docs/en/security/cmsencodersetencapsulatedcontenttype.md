---
title: CMSEncoderSetEncapsulatedContentType
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cmsencodersetencapsulatedcontenttype
source_url: 'https://developer.apple.com/documentation/security/cmsencodersetencapsulatedcontenttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencodersetencapsulatedcontenttype.json'
content_hash: 'sha256:bbd14495c81214d7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderSetEncapsulatedContentType

<sub>Function</sub>

Specifies an object identifier for the encapsulated data of a signed message.

<sub>macOS</sub>

```objc
OSStatus CMSEncoderSetEncapsulatedContentType(CMSEncoderRef cmsEncoder, const SecAsn1Oid *eContentType);
```

## Parameters

- `cmsEncoder` — The CMSEncoder reference returned by the `CMSEncoderCreate` function.

- `eContentType` — The object identifier for the encapsulated data in a signed message.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

In a signed message, the signed data consists of any type of content (referred to as the _encapsulated content_, because it is encapsulated in the signed data) plus the signature values. You can indicate the content type of the encapsulated data by specifying an object identifier (OID) in the `eContentType` parameter of this function. The default value for the OID (used if this function is not called) is `id-data`. This is the normal encapsulated content type for applications such as S/MIME, which uses it to indicate MIME-encoded content. You can pass any value that is meaningful to your application. Examples of CMS OIDs are listed in [http://www.imc.org/ietf-smime/other-smime-oids.asn](http://www.imc.org/ietf-smime/other-smime-oids.asn).

If you do call this function, you must call it before the first call to the `CMSEncoderUpdateContent` function.

### Special Considerations

Use [CMSEncoderSetEncapsulatedContentTypeOID](<cmsencodersetencapsulatedcontenttypeoid(____).md>) for new development.

## See Also

### Related Documentation

- [CMSDecoderCopyEncapsulatedContentType](<cmsdecodercopyencapsulatedcontenttype(____).md>) — Obtains the object identifier for the encapsulated data of a signed message.
- [CMSEncoderUpdateContent](<cmsencoderupdatecontent(______).md>) — Feeds content bytes into the encoder.
- [CMSEncoderCreate](<cmsencodercreate(__).md>) — Creates a CMSEncoder reference.
- [CMSEncoderCopyEncapsulatedContentType](<cmsencodercopyencapsulatedcontenttype(____).md>) — Obtains the object identifier for the encapsulated data of a signed message.
