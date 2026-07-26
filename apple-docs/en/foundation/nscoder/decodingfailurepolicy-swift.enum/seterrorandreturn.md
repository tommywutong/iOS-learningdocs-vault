---
title: NSCoder.DecodingFailurePolicy.setErrorAndReturn
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscoder/decodingfailurepolicy-swift.enum/seterrorandreturn
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodingfailurepolicy-swift.enum/seterrorandreturn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodingfailurepolicy-swift.enum/seterrorandreturn.json'
content_hash: 'sha256:4d319ce25ead7c85'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSCoder](../../nscoder.md) · [DecodingFailurePolicy](../decodingfailurepolicy-swift.enum.md)

# NSCoder.DecodingFailurePolicy.setErrorAndReturn

<sub>Case</sub>

A failure policy that directs the coder to capture the failure as an error object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case setErrorAndReturn
```

## Discussion

On decode failure, the [NSCoder](../../nscoder.md) will capture the failure as an [NSError](../../nserror.md), and prevent further decodes (by returning `0` / `nil` equivalent as appropriate).

Use this policy if you know that all encoded objects use [- failWithError:](<../failwitherror(__).md>) to communicate decode failures and don’t raise exceptions for error propagation.

## See Also

### Failure Policies

- [NSDecodingFailurePolicyRaiseException](raiseexception.md) — A failure policy that directs the coder to raise an exception.
