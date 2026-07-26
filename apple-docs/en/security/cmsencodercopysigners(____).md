---
title: 'CMSEncoderCopySigners(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsencodercopysigners(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsencodercopysigners(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencodercopysigners%28_%3A_%3A%29.json'
content_hash: 'sha256:239f7e66bdde8aae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderCopySigners(_:_:)

<sub>Function</sub>

Obtains the array of signers specified with the `CMSEncoderAddSigners` function.

<sub>macOS</sub>

```swift
func CMSEncoderCopySigners(_ cmsEncoder: CMSEncoder, _ signersOut: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

## Parameters

- `cmsEncoder` — The CMSEncoder reference returned by the [CMSEncoderCreate](<cmsencodercreate(__).md>) function.

- `signersOut` — On return, points to an array of identity objects of type [SecIdentity](secidentity.md) of the signers of the message. If the [CMSEncoderAddSigners](<cmsencoderaddsigners(____).md>) function has not been called for this message, this function returns a `NULL` array. You must use the [CFRelease](../corefoundation/cfrelease.md) function to free this reference when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## See Also

### Related Documentation

- [CMSEncoderCreate](<cmsencodercreate(__).md>) — Creates a CMSEncoder reference.
- [CMSEncoderAddSigners](<cmsencoderaddsigners(____).md>) — Specifies signers of the message.
