---
title: SecureDownloadTrustEvaluateCallback
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS 10.5+（12.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/securedownloadtrustevaluatecallback
source_url: 'https://developer.apple.com/documentation/security/securedownloadtrustevaluatecallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/securedownloadtrustevaluatecallback.json'
content_hash: 'sha256:6e90b2e3c30be4d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecureDownloadTrustEvaluateCallback

<sub>Type Alias</sub>

Optionally queries the user how to handle a failed trust evaluation.

<sub>Mac Catalyst, macOS</sub>

```objc
typedef enum SecTrustResultType (*)(struct __SecTrust *, enum SecTrustResultType, void *) SecureDownloadTrustEvaluateCallback;
```

## Parameters

- `trustRef` — The trust used for this evaluation.

- `result` — The result of the trust evaluation.

- `evaluateContext` — An arbitrary value that you passed in as the `evaluateContext` parameter to the [SecureDownloadCreateWithTicket](securedownloadcreatewithticket.md) function.

## Return Value

A trust evaluation result.
