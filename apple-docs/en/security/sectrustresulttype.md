---
title: SecTrustResultType
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectrustresulttype
source_url: 'https://developer.apple.com/documentation/security/sectrustresulttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustresulttype.json'
content_hash: 'sha256:339a5ccae5fcbc23'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustResultType

<sub>Enumeration</sub>

Trust evaluation result codes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum SecTrustResultType
```

## Overview

You get one of these constants when you call the [SecTrustGetTrustResult](<sectrustgettrustresult(____).md>) method after evaluating a trust instance with either the [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) method or the [SecTrustEvaluateAsyncWithError](<sectrustevaluateasyncwitherror(______).md>) method. If evaluation fails and [SecTrustGetTrustResult](<sectrustgettrustresult(____).md>) reports [kSecTrustResultRecoverableTrustFailure](sectrustresulttype/recoverabletrustfailure.md), you might be able to change parameters like the evaluation date, and reevaluate to obtain a passing result, as described in [Configuring a Trust](configuring-a-trust.md).

See an individual constant below for more information about how to handle that result type in your app.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Result Codes

- [kSecTrustResultUnspecified](sectrustresulttype/unspecified.md) — The user did not specify a trust setting.
- [kSecTrustResultProceed](sectrustresulttype/proceed.md) — The user granted permission to trust the certificate for the purposes designated in the specified policies.
- [kSecTrustResultDeny](sectrustresulttype/deny.md) — The user specified that the certificate should not be trusted.
- [kSecTrustResultRecoverableTrustFailure](sectrustresulttype/recoverabletrustfailure.md) — Trust is denied, but recovery may be possible.
- [kSecTrustResultFatalTrustFailure](sectrustresulttype/fataltrustfailure.md) — Trust is denied and no simple fix is available.
- [kSecTrustResultOtherError](sectrustresulttype/othererror.md) — A value that indicates a failure other than trust evaluation.
- [kSecTrustResultInvalid](sectrustresulttype/invalid.md) — An indication of an invalid setting or result.
- [kSecTrustResultConfirm](sectrustresulttype/confirm.md) — User confirmation is required before proceeding.

### Initializers

- [init(rawValue:)](<sectrustresulttype/init(rawvalue_).md>)
