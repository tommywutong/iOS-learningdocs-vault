---
title: 'failWithError(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/failwitherror(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/failwitherror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/failwitherror%28_%3A%29.json'
content_hash: 'sha256:4847ff2c0983a7ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# failWithError(_:)

<sub>Instance Method</sub>

Signals to this coder that the decode operation has failed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func failWithError(_ error: any Error)
```

## Parameters

- `error` — An error that indicates why decoding failed.

## Discussion

Typically, you call this method in your [- initWithCoder:](<../nscoding/init(coder_).md>) implementation. You should set the error when you detect problems such as lack of secure coding, data corruption, or a domain validation failure.

This method is only meaningful to call for decodes.

The effect of calling this method depends on the value of [decodingFailurePolicy](decodingfailurepolicy-swift.property.md), as follows:

- If the policy is [NSDecodingFailurePolicyRaiseException](decodingfailurepolicy-swift.enum/raiseexception.md), calling this method throws an exception immediately. Swift code cannot catch this kind of exception.
- If the policy is [NSDecodingFailurePolicySetErrorAndReturn](decodingfailurepolicy-swift.enum/seterrorandreturn.md), calling this method sets the error property once per call to one of the `decode` methods. Calling it repeatedly has no effect until the call stack unwinds to one of these methods’ entry points.

## See Also

### Managing Decode Errors

- [error](error.md) — An error in the top-level encode.
