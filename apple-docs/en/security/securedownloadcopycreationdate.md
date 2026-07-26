---
title: SecureDownloadCopyCreationDate
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/securedownloadcopycreationdate
source_url: 'https://developer.apple.com/documentation/security/securedownloadcopycreationdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/securedownloadcopycreationdate.json'
content_hash: 'sha256:332fe714bbf09f20'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecureDownloadCopyCreationDate

<sub>Function</sub>

Returns download ticket’s creation date.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecureDownloadCopyCreationDate(SecureDownloadRef downloadRef, CFDateRef*date);
```

## Parameters

- `downloadRef` — The secure download to query.

- `date` — A pointer to a [CFDate](../corefoundation/cfdate.md) object that the function fills with the download’s creation date.

## Return Value

A result code. See [Secure Download Result Codes](secure-download-result-codes.md).
