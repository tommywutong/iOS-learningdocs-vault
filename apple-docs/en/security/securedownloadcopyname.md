---
title: SecureDownloadCopyName
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/securedownloadcopyname
source_url: 'https://developer.apple.com/documentation/security/securedownloadcopyname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/securedownloadcopyname.json'
content_hash: 'sha256:c884b23fffbd444f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecureDownloadCopyName

<sub>Function</sub>

Returns the printable name of the download ticket.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecureDownloadCopyName(SecureDownloadRef downloadRef, CFStringRef*name);
```

## Parameters

- `downloadRef` — The secure download to query.

- `name` — A pointer to a CFStringRef object that the function fills with the secure download’s name.

## Return Value

A result code. See [Secure Download Result Codes](secure-download-result-codes.md).
