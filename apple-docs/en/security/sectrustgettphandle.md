---
title: SecTrustGetTPHandle
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectrustgettphandle
source_url: 'https://developer.apple.com/documentation/security/sectrustgettphandle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustgettphandle.json'
content_hash: 'sha256:04d317557bd0d153'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustGetTPHandle

<sub>Function</sub>

Retrieves the trust policy handle.

<sub>macOS</sub>

```objc
OSStatus SecTrustGetTPHandle(SecTrustRef trust, CSSM_TP_HANDLE *handle);
```

## Parameters

- `trust` — The trust management object from which to obtain the trust policy handle. A trust management object includes one or more certificates plus the policy or policies to be used in evaluating trust. Use the [SecTrustCreateWithCertificates](<sectrustcreatewithcertificates(______).md>) function to create a trust management object.

- `handle` — On return, points to a CSSM trust policy handle. This handle remains valid until the trust management object is released or until the next call to the function [SecTrustEvaluate](<sectrustevaluate(____).md>) that uses this trust management object.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The trust policy handle is the CSSM identifier of the trust policy module that is managing the certificate. The trust policy handle is used as an input to a number of CSSM functions.

It is safe to call this function concurrently on two or more threads as long as it is not used to get values from a trust management object that is simultaneously being changed by another function. For example, you can call this function on two threads at the same time, but not if you are simultaneously calling the [SecTrustSetVerifyDate](<sectrustsetverifydate(____).md>) function for the same trust management object on another thread.
