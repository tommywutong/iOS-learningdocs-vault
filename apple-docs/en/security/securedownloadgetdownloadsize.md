---
title: SecureDownloadGetDownloadSize
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/securedownloadgetdownloadsize
source_url: 'https://developer.apple.com/documentation/security/securedownloadgetdownloadsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/securedownloadgetdownloadsize.json'
content_hash: 'sha256:bec63403e15fa1cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecureDownloadGetDownloadSize

<sub>Function</sub>

Returns the size of the expected download.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecureDownloadGetDownloadSize(SecureDownloadRef downloadRef, SInt64 *downloadSize);
```

## Parameters

- `downloadRef` — The secure download object to query.

- `downloadSize` — A pointer that the function fills with the the download size.

## Return Value

A result code. See [Secure Download Result Codes](secure-download-result-codes.md).
