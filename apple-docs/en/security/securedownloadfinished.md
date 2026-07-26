---
title: SecureDownloadFinished
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/securedownloadfinished
source_url: 'https://developer.apple.com/documentation/security/securedownloadfinished'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/securedownloadfinished.json'
content_hash: 'sha256:1722e547fe899831'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecureDownloadFinished

<sub>Function</sub>

Concludes the secure download process.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecureDownloadFinished(SecureDownloadRef downloadRef);
```

## Parameters

- `downloadRef` — The secure download object to finish.

## Return Value

A result code. See [Secure Download Result Codes](secure-download-result-codes.md).

## Discussion

Call this after all data has been received.
