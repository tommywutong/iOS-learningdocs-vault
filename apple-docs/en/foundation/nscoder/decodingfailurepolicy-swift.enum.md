---
title: NSCoder.DecodingFailurePolicy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscoder/decodingfailurepolicy-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodingfailurepolicy-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodingfailurepolicy-swift.enum.json'
content_hash: 'sha256:a28730f938d9b85f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# NSCoder.DecodingFailurePolicy

<sub>Enumeration</sub>

Policies describing the action the coder should take when encountering decode failures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum DecodingFailurePolicy
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Failure Policies

- [NSDecodingFailurePolicyRaiseException](decodingfailurepolicy-swift.enum/raiseexception.md) — A failure policy that directs the coder to raise an exception.
- [NSDecodingFailurePolicySetErrorAndReturn](decodingfailurepolicy-swift.enum/seterrorandreturn.md) — A failure policy that directs the coder to capture the failure as an error object.

### Initializers

- [init(rawValue:)](<decodingfailurepolicy-swift.enum/init(rawvalue_).md>)

## See Also

### Inspecting a Coder

- [allowsKeyedCoding](allowskeyedcoding.md) — A Boolean value that indicates whether the receiver supports keyed coding of objects.
- [- containsValueForKey:](<containsvalue(forkey_).md>) — Returns a Boolean value that indicates whether an encoded value is available for a string.
- [decodingFailurePolicy](decodingfailurepolicy-swift.property.md) — The action the coder should take when decoding fails.
