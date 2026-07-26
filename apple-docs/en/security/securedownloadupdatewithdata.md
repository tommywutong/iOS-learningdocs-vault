---
title: SecureDownloadUpdateWithData
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/securedownloadupdatewithdata
source_url: 'https://developer.apple.com/documentation/security/securedownloadupdatewithdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/securedownloadupdatewithdata.json'
content_hash: 'sha256:91623d8a4481b089'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecureDownloadUpdateWithData

<sub>Function</sub>

Checks data received during download for validity.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecureDownloadUpdateWithData(SecureDownloadRef downloadRef, CFDataRef data);
```

## Parameters

- `downloadRef` — The secure download object to query.

- `data` — The data to check.

## Return Value

A result code. See [Secure Download Result Codes](secure-download-result-codes.md). If the data is invalid, the result code is `enum (unnamed)-3yczz/errSecureDownloadInvalidDownload`.

## Discussion

Call this function each time data is received.
