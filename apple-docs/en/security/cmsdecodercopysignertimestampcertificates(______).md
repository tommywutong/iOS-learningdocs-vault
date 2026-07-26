---
title: 'CMSDecoderCopySignerTimestampCertificates(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsdecodercopysignertimestampcertificates(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsdecodercopysignertimestampcertificates(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsdecodercopysignertimestampcertificates%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:4914a6540560d20f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSDecoderCopySignerTimestampCertificates(_:_:_:)

<sub>Function</sub>

Returns an array containing the certificates from a timestamp response.

<sub>macOS</sub>

```swift
func CMSDecoderCopySignerTimestampCertificates(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ certificateRefs: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

## Parameters

- `cmsDecoder` — A CMSDecoder reference returned by the `CMSDecoderCreate` function.

- `signerIndex` — A number indicating which signer to examine. Signer index numbers start with 0. Use the [CMSDecoderGetNumSigners](<cmsdecodergetnumsigners(____).md>) function to determine the total number of signers for a message.

- `certificateRefs` — The address of a Core Foundation array reference where the resulting array should be stored.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). Typically, this function returns [errSecParam](errsecparam.md) if the CMS message was not signed or `signerIndex` is out of bounds, and returns [errSecItemNotFound](errsecitemnotfound.md) if no certificates were found.

## Discussion

The signature must contain an authenticated timestamp provided by a time stamping authority. Elements of the returned array are of type `SecCertificateRef`. The caller is responsible for releasing the returned array by calling `CFRelease`.

You must call [CMSDecoderFinalizeMessage](<cmsdecoderfinalizemessage(__).md>) before you call this function.
