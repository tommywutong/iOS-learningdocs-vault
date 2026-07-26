---
title: 'CMSDecoderIsContentEncrypted(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsdecoderiscontentencrypted(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsdecoderiscontentencrypted(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsdecoderiscontentencrypted%28_%3A_%3A%29.json'
content_hash: 'sha256:a7d64d1b9937cda1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSDecoderIsContentEncrypted(_:_:)

<sub>Function</sub>

Determines whether a CMS message was encrypted.

<sub>macOS</sub>

```swift
func CMSDecoderIsContentEncrypted(_ cmsDecoder: CMSDecoder, _ isEncryptedOut: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus
```

## Parameters

- `cmsDecoder` — The CMSDecoder reference returned by the `CMSDecoderCreate` function.

- `isEncryptedOut` — Returns `TRUE` if the message was encrypted.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Note that if the message was encrypted and the decoding succeeded (`CMSDecoderFinalizeMessage` returned `noErr`), then the message was successfully decrypted. Call [CMSDecoderCopyContent](<cmsdecodercopycontent(____).md>) to retrieve the decrypted content.

You cannot call this function until after you have called the `CMSDecoderFinalizeMessage` function.

## See Also

### Related Documentation

- [CMSDecoderCreate](<cmsdecodercreate(__).md>) — Creates a CMSDecoder reference.
- [CMSEncoderAddRecipients](<cmsencoderaddrecipients(____).md>) — Specifies a message is to be encrypted and specifies the recipients of the message.
- [CMSDecoderFinalizeMessage](<cmsdecoderfinalizemessage(__).md>) — Indicates that there is no more data to decode.
