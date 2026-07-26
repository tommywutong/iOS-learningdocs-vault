---
title: 'SecCertificateCreateWithData(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccertificatecreatewithdata(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccertificatecreatewithdata(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatecreatewithdata%28_%3A_%3A%29.json'
content_hash: 'sha256:dfab5a84b7680e2f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateCreateWithData(_:_:)

<sub>Function</sub>

Creates a certificate object from a DER representation of a certificate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecCertificateCreateWithData(_ allocator: CFAllocator?, _ data: CFData) -> SecCertificate?
```

## Parameters

- `allocator` — The `CFAllocator` object you wish to use to allocate the certificate object. Pass `NULL` to use the default allocator.

- `data` — A DER (Distinguished Encoding Rules) representation of an X.509 certificate.

## Return Value

The newly created certificate object. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it. Returns `nil` if the data passed in the `data` parameter is not a valid DER-encoded X.509 certificate.

## Discussion

The certificate object returned by this function is used as input to other functions in the API.
