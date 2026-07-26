---
title: 'CMSEncoderCopyRecipients(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsencodercopyrecipients(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsencodercopyrecipients(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencodercopyrecipients%28_%3A_%3A%29.json'
content_hash: 'sha256:f8458c5cb62b52ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderCopyRecipients(_:_:)

<sub>Function</sub>

Obtains the array of recipients specified with the `CMSEncoderAddRecipients` function.

<sub>macOS</sub>

```swift
func CMSEncoderCopyRecipients(_ cmsEncoder: CMSEncoder, _ recipientsOut: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

## Parameters

- `cmsEncoder` — The CMSEncoder reference returned by the [CMSEncoderCreate](<cmsencodercreate(__).md>) function.

- `recipientsOut` — On return, points to an array of certificate objects of type [SecCertificate](seccertificate.md) of the recipients of the message. If the [CMSEncoderAddRecipients](<cmsencoderaddrecipients(____).md>) function has not been called for this message, this function returns a `NULL` array. You must use the [CFRelease](../corefoundation/cfrelease.md) function to free this reference when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## See Also

### Related Documentation

- [CMSEncoderCreate](<cmsencodercreate(__).md>) — Creates a CMSEncoder reference.
- [CMSEncoderAddRecipients](<cmsencoderaddrecipients(____).md>) — Specifies a message is to be encrypted and specifies the recipients of the message.
