---
title: SecKeychainPromptSelector
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychainpromptselector
source_url: 'https://developer.apple.com/documentation/security/seckeychainpromptselector'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainpromptselector.json'
content_hash: 'sha256:0b9113ff860cb86e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainPromptSelector

<sub>Structure</sub>

Bits that define when a keychain should require a passphrase.

<sub>macOS</sub>

```swift
struct SecKeychainPromptSelector
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kSecKeychainPromptRequirePassphase](seckeychainpromptselector/requirepassphase.md) — Indicates that a passphrase should be required for every access.
- [kSecKeychainPromptUnsigned](seckeychainpromptselector/unsigned.md) — Indicates that a passphrase should be required when an unsigned application attempts to use the keychain, overriding the system default.
- [kSecKeychainPromptUnsignedAct](seckeychainpromptselector/unsignedact.md) — Indicates that a passphrase should be required when an unsigned application attempts to use the keychain.
- [kSecKeychainPromptInvalid](seckeychainpromptselector/invalid.md) — Indicates that a passphrase should be required when an application with an invalid signature attempts to use the keychain, overriding the system default.
- [kSecKeychainPromptInvalidAct](seckeychainpromptselector/invalidact.md) — Indicates that a passphrase should be required when an application with an invalid signature attempts to use the keychain.

### Initializers

- [init(rawValue:)](<seckeychainpromptselector/init(rawvalue_).md>) — Initializes a keychain prompt selector.
