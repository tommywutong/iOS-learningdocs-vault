---
title: SecTrustGetCssmResult
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectrustgetcssmresult
source_url: 'https://developer.apple.com/documentation/security/sectrustgetcssmresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustgetcssmresult.json'
content_hash: 'sha256:b8b58a62f30189ab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustGetCssmResult

<sub>Function</sub>

Retrieves the CSSM trust result.

<sub>macOS</sub>

```objc
OSStatus SecTrustGetCssmResult(SecTrustRef trust, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR*result);
```

## Parameters

- `trust` — A trust management object that has previously been sent to the [SecTrustEvaluate](<sectrustevaluate(____).md>) function for evaluation.

- `result` — On return, points to the CSSM trust result pointer. You should not modify or free this data, as it is owned by the system.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

After calling the [SecTrustEvaluate](<sectrustevaluate(____).md>) function, you can call the [SecTrustGetTrustResult](<sectrustgettrustresult(____).md>) function or the `SecTrustGetCssmResult` function to get information about the certificates in the certificate chain and everything that might be wrong with each certificate. Whereas the [SecTrustGetTrustResult](<sectrustgettrustresult(____).md>) function returns the information in a form that you can interpret without extensive knowledge of CSSM, the `SecTrustGetCssmResult` function returns information in a form that can be passed directly to CSSM functions. See _Common Security: CDSA and CSSM, version 2 (with corrigenda)_ from The Open Group ([http://www.opengroup.org/security/cdsa.htm](http://www.opengroup.org/security/cdsa.htm) for more information about the `CSSM_TP_VERIFY_CONTEXT_RESULT` structure pointed to by the `result` parameter.

It is safe to call this function concurrently on two or more threads as long as it is not used to get values from a trust management object that is simultaneously being changed by another function. For example, you can call this function on two threads at the same time, but not if you are simultaneously calling the [SecTrustSetVerifyDate](<sectrustsetverifydate(____).md>) function for the same trust management object on another thread.

## See Also

### Related Documentation

- [SecTrustGetTrustResult](<sectrustgettrustresult(____).md>) — Returns the result code from the most recent trust evaluation.
