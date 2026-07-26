---
title: SecureDownloadCopyTicketLocation
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/securedownloadcopyticketlocation
source_url: 'https://developer.apple.com/documentation/security/securedownloadcopyticketlocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/securedownloadcopyticketlocation.json'
content_hash: 'sha256:4923c2204b0fc788'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecureDownloadCopyTicketLocation

<sub>Function</sub>

Copies the ticket location from a secure download URL.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecureDownloadCopyTicketLocation(CFURLRef url, CFURLRef*ticketLocation);
```

## Parameters

- `url` — A secure download URL.

- `ticketLocation` — A pointer to a [CFURL](../corefoundation/cfurl.md) object that the function fills with the URL of the ticket.

## Return Value

A result code. See [Secure Download Result Codes](secure-download-result-codes.md).
