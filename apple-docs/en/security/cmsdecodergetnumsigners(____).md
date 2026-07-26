---
title: 'CMSDecoderGetNumSigners(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsdecodergetnumsigners(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsdecodergetnumsigners(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsdecodergetnumsigners%28_%3A_%3A%29.json'
content_hash: 'sha256:c34de0828c3363be'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSDecoderGetNumSigners(_:_:)

<sub>Function</sub>

Obtains the number of signers of a message.

<sub>macOS</sub>

```swift
func CMSDecoderGetNumSigners(_ cmsDecoder: CMSDecoder, _ numSignersOut: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `cmsDecoder` — The CMSDecoder reference returned by the `CMSDecoderCreate` function.

- `numSignersOut` — On return, the number of signers of the message. Zero indicates that the message was not signed.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Call the `CMSDecoderCopySignerStatus` function to determine the status of a signature.

You cannot call this function until after you have called the `CMSDecoderFinalizeMessage` function.

## See Also

### Related Documentation

- [CMSDecoderCreate](<cmsdecodercreate(__).md>) — Creates a CMSDecoder reference.
- [CMSDecoderFinalizeMessage](<cmsdecoderfinalizemessage(__).md>) — Indicates that there is no more data to decode.
