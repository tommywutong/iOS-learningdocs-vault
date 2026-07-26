---
title: SecureDownloadTrustSetupCallback
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS 10.5+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/securedownloadtrustsetupcallback
source_url: 'https://developer.apple.com/documentation/security/securedownloadtrustsetupcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/securedownloadtrustsetupcallback.json'
content_hash: 'sha256:e2210a374171c933'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecureDownloadTrustSetupCallback

<sub>Type Alias</sub>

Determines whether trust for a particular signer should be evaluated.

<sub>Mac Catalyst, macOS</sub>

```objc
typedef enum _SecureDownloadTrustCallbackResult (*)(struct __SecTrust *, void *) SecureDownloadTrustSetupCallback;
```

## Parameters

- `trustRef` — The trust used for this evaluation.

- `setupContext` — An arbitrary value that you passed in as the `setupContext` parameter to the [SecureDownloadCreateWithTicket](securedownloadcreatewithticket.md) function.

## Return Value

A trust callback result that indicates whether or not a signer should be evaluated.
