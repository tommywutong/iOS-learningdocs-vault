---
title: SecTrustResultType.recoverableTrustFailure
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectrustresulttype/recoverabletrustfailure
source_url: 'https://developer.apple.com/documentation/security/sectrustresulttype/recoverabletrustfailure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustresulttype/recoverabletrustfailure.json'
content_hash: 'sha256:529342a182f10707'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecTrustResultType](../sectrustresulttype.md)

# SecTrustResultType.recoverableTrustFailure

<sub>Case</sub>

Trust is denied, but recovery may be possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case recoverableTrustFailure
```

## Discussion

This value indicates that you should not trust the chain as is, but that the chain could be trusted with some minor change to the evaluation context, such as ignoring expired certificates or adding another anchor to the set of trusted anchors.

The way you handle this depends on the situation. For example, if you are performing signature validation and you know when the message was originally received, you should check again using that date to see if the message was valid when you originally received it.

You can also call the [SecTrustCopyResult](<../sectrustcopyresult(__).md>) method to get more information about the results of the trust evaluation. If applicable, you can call one or more of the methods that start with `SecTrustSet` to correct or bypass the problem. Alternatively, in macOS, you can inform the user of the problem and call the [SFCertificateTrustPanel](../../securityinterface/sfcertificatetrustpanel.md) class to let the user change the trust setting for the certificate.

After correcting the problem, reevaluate the trust. Each time you call [SecTrustEvaluateWithError](<../sectrustevaluatewitherror(____).md>) or [SecTrustEvaluateAsyncWithError](<../sectrustevaluateasyncwitherror(______).md>), the method discards the results of any previous evaluation and replaces them with the new results.

You might receive the [kSecTrustResultRecoverableTrustFailure](recoverabletrustfailure.md) value after an evaluation, but you can’t store the value as part of the user trust settings with a call to the [SecTrustSettingsSetTrustSettings](<../sectrustsettingssettrustsettings(______).md>) method.
