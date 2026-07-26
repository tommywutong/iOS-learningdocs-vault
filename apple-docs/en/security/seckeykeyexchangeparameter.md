---
title: SecKeyKeyExchangeParameter
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeykeyexchangeparameter
source_url: 'https://developer.apple.com/documentation/security/seckeykeyexchangeparameter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeykeyexchangeparameter.json'
content_hash: 'sha256:a6a85fb01ce81401'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyKeyExchangeParameter

<sub>Structure</sub>

The dictionary keys used to specify Diffie-Hellman key exchange parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SecKeyKeyExchangeParameter
```

## Discussion

Use these constants as keys in the dictionary that you input to the [SecKeyCopyKeyExchangeResult](<seckeycopykeyexchangeresult(__________).md>) function as a means to refine the process of Diffie-Hellman key exchange.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [kSecKeyKeyExchangeParameterRequestedSize](seckeykeyexchangeparameter/requestedsize.md)
- [kSecKeyKeyExchangeParameterSharedInfo](seckeykeyexchangeparameter/sharedinfo.md)

### Initializers

- [init(rawValue:)](<seckeykeyexchangeparameter/init(rawvalue_).md>)
