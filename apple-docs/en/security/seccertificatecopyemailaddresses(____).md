---
title: 'SecCertificateCopyEmailAddresses(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 10.2+, visionOS 1.0+, watchOS 3.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccertificatecopyemailaddresses(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccertificatecopyemailaddresses(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatecopyemailaddresses%28_%3A_%3A%29.json'
content_hash: 'sha256:d4d6ea0e2bc26798'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateCopyEmailAddresses(_:_:)

<sub>Function</sub>

Retrieves the email addresses for the subject of a certificate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecCertificateCopyEmailAddresses(_ certificate: SecCertificate, _ emailAddresses: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

## Parameters

- `certificate` — The certificate object from which to retrieve the email addresses.

- `emailAddresses` — On return, an array of zero or more `CFStringRef` elements, each containing one email address found in the certificate subject. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Not every certificate subject includes an email address. If the function does not find any email addresses, it returns a `CFArrayRef` object with zero elements in the array.
