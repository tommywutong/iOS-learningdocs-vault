---
title: 'CMSDecoderCopySignerSigningTime(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsdecodercopysignersigningtime(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsdecodercopysignersigningtime(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsdecodercopysignersigningtime%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ae631e54b46532d1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSDecoderCopySignerSigningTime(_:_:_:)

<sub>Function</sub>

Obtains the signing time of a CMS message, if present.

<sub>macOS</sub>

```swift
func CMSDecoderCopySignerSigningTime(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ signingTime: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus
```

## Parameters

- `cmsDecoder` — A CMSDecoder reference returned by the `CMSDecoderCreate` function.

- `signerIndex` — A number indicating which signer to examine. Signer index numbers start with 0. Use the [CMSDecoderGetNumSigners](<cmsdecodergetnumsigners(____).md>) function to determine the total number of signers for a message.

- `signingTime` — The address of an absolute time value where the result should be stored.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). Typically, this function returns [errSecParam](errsecparam.md) if the CMS message was not signed or if `signerIndex` is out of bounds.

## Discussion

The timestamp is an unauthenticated time, although it is part of the signed attributes of the message.

You must call [CMSDecoderFinalizeMessage](<cmsdecoderfinalizemessage(__).md>) before you call this function.
