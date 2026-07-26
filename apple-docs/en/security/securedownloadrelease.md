---
title: SecureDownloadRelease
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/securedownloadrelease
source_url: 'https://developer.apple.com/documentation/security/securedownloadrelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/securedownloadrelease.json'
content_hash: 'sha256:2ffd9eda630a52c7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecureDownloadRelease

<sub>Function</sub>

Releases the memory associated with a secure download object.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecureDownloadRelease(SecureDownloadRef downloadRef);
```

## Parameters

- `downloadRef` — The secure download object to release.

## Return Value

A result code. See [Secure Download Result Codes](secure-download-result-codes.md).
