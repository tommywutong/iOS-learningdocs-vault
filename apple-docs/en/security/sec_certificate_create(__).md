---
title: 'sec_certificate_create(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_certificate_create(_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_certificate_create(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_certificate_create%28_%3A%29.json'
content_hash: 'sha256:9efed34a9d626e86'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_certificate_create(_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_certificate_create(_ certificate: SecCertificate) -> sec_certificate_t?
```

## Parameters

- `certificate` — A `SecCertificateRef` instance.

## Return Value

A `sec_certificate_t` instance.

## Discussion

Create an ARC-able `sec_certificate_t` instance from a `SecCertificateRef`.
