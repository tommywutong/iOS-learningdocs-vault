---
title: NSCoder.DecodingFailurePolicy.raiseException
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscoder/decodingfailurepolicy-swift.enum/raiseexception
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodingfailurepolicy-swift.enum/raiseexception'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodingfailurepolicy-swift.enum/raiseexception.json'
content_hash: 'sha256:946f89f2550f1247'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSCoder](../../nscoder.md) · [DecodingFailurePolicy](../decodingfailurepolicy-swift.enum.md)

# NSCoder.DecodingFailurePolicy.raiseException

<sub>Case</sub>

A failure policy that directs the coder to raise an exception.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case raiseException
```

## Discussion

With this policy, the [NSCoder](../../nscoder.md) raises an exception internally to propagate failure messages (and unwind the stack). In Objective-C, this exception can be transformed into an [NSError](../../nserror.md) via methods like [decodeTopLevelObjectAndReturnError:](../decodetoplevelobjectandreturnerror_.md)

## See Also

### Failure Policies

- [NSDecodingFailurePolicySetErrorAndReturn](seterrorandreturn.md) — A failure policy that directs the coder to capture the failure as an error object.
