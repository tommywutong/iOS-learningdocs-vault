---
title: 'CMSDecoderCopySignerTimestamp(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsdecodercopysignertimestamp(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsdecodercopysignertimestamp(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsdecodercopysignertimestamp%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:822b0c2af23f9c32'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSDecoderCopySignerTimestamp(_:_:_:)

<sub>Function</sub>

Returns the timestamp of a signer of a CMS message, if present.

<sub>macOS</sub>

```swift
func CMSDecoderCopySignerTimestamp(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus
```

## Parameters

- `cmsDecoder` — A CMSDecoder reference returned by the `CMSDecoderCreate` function.

- `signerIndex` — A number indicating which signer to examine. Signer index numbers start with 0. Use the [CMSDecoderGetNumSigners](<cmsdecodergetnumsigners(____).md>) function to determine the total number of signers for a message.

- `timestamp` — The address of an absolute time value where the result should be stored.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). Typically, this function returns [errSecParam](errsecparam.md) if the CMS message was not signed or if `signerIndex` is out of bounds.

## Discussion

This timestamp is an authenticated timestamp provided by a time stamping authority.

You must call [CMSDecoderFinalizeMessage](<cmsdecoderfinalizemessage(__).md>) before you call this function.
