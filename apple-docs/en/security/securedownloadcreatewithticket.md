---
title: SecureDownloadCreateWithTicket
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/securedownloadcreatewithticket
source_url: 'https://developer.apple.com/documentation/security/securedownloadcreatewithticket'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/securedownloadcreatewithticket.json'
content_hash: 'sha256:d3f65195f94af392'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecureDownloadCreateWithTicket

<sub>Function</sub>

Creates a secure download object for use during the download process.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecureDownloadCreateWithTicket(CFDataRef ticket, SecureDownloadTrustSetupCallback setup, void *setupContext, SecureDownloadTrustEvaluateCallback evaluate, void *evaluateContext, SecureDownloadRef*downloadRef);
```

## Parameters

- `ticket` — The download ticket.

- `setup` — A pointer to a function that Secure Download calls before trust is verified for each signer of the ticket. This allows you to modify the [SecTrust](sectrust.md) if needed.  The callback returns a [SecureDownloadTrustCallbackResult](securedownloadtrustcallbackresult.md).

- `setupContext` — An arbitrary context passed to the `setup` callback.

- `evaluate` — A pointer to a function that Secure Download calls after calling [SecTrustEvaluate](<sectrustevaluate(____).md>) for a signer if the result was not trusted. This allows you to query the user as to whether or not to trust the signer by returning a [SecTrustResultType](sectrustresulttype.md) value.

- `evaluateContext` — An arbitrary context passed to the `evaluate` callback.

- `downloadRef` — A pointer that is set to the new download reference.

## Return Value

A result code. See [Secure Download Result Codes](secure-download-result-codes.md).
