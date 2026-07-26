---
title: SecureDownloadCopyURLs
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/securedownloadcopyurls
source_url: 'https://developer.apple.com/documentation/security/securedownloadcopyurls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/securedownloadcopyurls.json'
content_hash: 'sha256:419bc30127bfdde7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecureDownloadCopyURLs

<sub>Function</sub>

Returns a list of URLs from which the data can be downloaded.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecureDownloadCopyURLs(SecureDownloadRef downloadRef, CFArrayRef*urls);
```

## Parameters

- `downloadRef` — The secure download object to query.

- `urls` — A pointer to a [CFArray](../corefoundation/cfarray.md) object that the function sets to point at a new array containing one or more [CFURL](../corefoundation/cfurl.md) objects indicating the urls to download.

## Return Value

A result code. See [Secure Download Result Codes](secure-download-result-codes.md).

## Discussion

The first URL in the list is the preferred download location. The other URLs are backup locations in case earlier locations in the list can’t be accessed.
