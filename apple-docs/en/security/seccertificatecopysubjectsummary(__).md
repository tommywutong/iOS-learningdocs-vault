---
title: 'SecCertificateCopySubjectSummary(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccertificatecopysubjectsummary(_:)'
source_url: 'https://developer.apple.com/documentation/security/seccertificatecopysubjectsummary(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatecopysubjectsummary%28_%3A%29.json'
content_hash: 'sha256:1bdd9a2f4c3dc09b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateCopySubjectSummary(_:)

<sub>Function</sub>

Returns a human-readable summary of a certificate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecCertificateCopySubjectSummary(_ certificate: SecCertificate) -> CFString?
```

## Parameters

- `certificate` — The certificate object for which you wish to return a summary string.

## Return Value

A string that contains a human-readable summary of the contents of the certificate. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it. Returns `NULL` if the data passed in the `certificate` parameter is not a valid certificate object.

## Discussion

Because all the data in the string comes from the certificate, the string is in whatever language is used in the certificate.

## See Also

### Related Documentation

- [SecCertificateCreateWithData](<seccertificatecreatewithdata(____).md>) — Creates a certificate object from a DER representation of a certificate.
