---
title: 'SecCertificateCopyLongDescription(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccertificatecopylongdescription(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccertificatecopylongdescription(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatecopylongdescription%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ffb7f48487ee1f50'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateCopyLongDescription(_:_:_:)

<sub>Function</sub>

Returns a copy of the long description of a certificate.

<sub>macOS</sub>

```swift
func SecCertificateCopyLongDescription(_ alloc: CFAllocator?, _ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFString?
```

## Parameters

- `alloc` — The allocator that should be used. Pass `NULL` or [kCFAllocatorDefault](../corefoundation/kcfallocatordefault.md) to use the default allocator.

- `certificate` — The certificate from which the long description should be copied.

- `error` — A pointer to a [CFError](../corefoundation/cferror.md) variable where an error object is stored upon failure. If not `NULL`, the caller is responsible for checking this variable and releasing the resulting object if it exists.

## Return Value

A string object containing the long description, or `NULL` if an error occurred. In Objective-C, free this object with a call to the [CFRelease](../corefoundation/cfrelease.md) function when you are done with it.

## Discussion

The format of this string is not guaranteed to be consistent across different operating systems or versions. Do not attempt to parse it programmatically.
