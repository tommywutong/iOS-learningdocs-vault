---
title: 'CMSEncoderUpdateContent(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsencoderupdatecontent(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsencoderupdatecontent(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencoderupdatecontent%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:fdb8c93a14c662de'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderUpdateContent(_:_:_:)

<sub>Function</sub>

Feeds content bytes into the encoder.

<sub>macOS</sub>

```swift
func CMSEncoderUpdateContent(_ cmsEncoder: CMSEncoder, _ content: UnsafeRawPointer, _ contentLen: Int) -> OSStatus
```

## Parameters

- `cmsEncoder` — The CMSEncoder reference returned by the `CMSEncoderCreate` function.

- `content` — The content that you want to add to the message. The content must conform to the type set with the [CMSEncoderSetEncapsulatedContentType](cmsencodersetencapsulatedcontenttype.md) function (or type `id-data` if that function has not been called).

- `contentLen` — The length of the content being added, in bytes.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

You use this function to add the content that is to be signed or encrypted. If the message is only a container for certificates added with the [CMSEncoderAddSupportingCerts](<cmsencoderaddsupportingcerts(____).md>) function and has no other content, do not call this function. This function can be called multiple times.

After you are finished adding content, call the `CMSEncoderCopyEncodedContent` function to complete the message creation process.

None of the setter functions ([CMSEncoderSetHasDetachedContent](<cmsencodersethasdetachedcontent(____).md>), [CMSEncoderSetEncapsulatedContentType](cmsencodersetencapsulatedcontenttype.md), or [CMSEncoderSetCertificateChainMode](<cmsencodersetcertificatechainmode(____).md>)) can be called after this function has been called.
