---
title: SecKeySizes
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.9+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/seckeysizes
source_url: 'https://developer.apple.com/documentation/security/seckeysizes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeysizes.json'
content_hash: 'sha256:980f8e1447738b1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeySizes

<sub>Enumeration</sub>

The supported sizes for keys of various common types.

> [!warning] Deprecated
> No longer supported

<sub>macOS</sub>

```swift
enum SecKeySizes
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kSecDefaultKeySize](seckeysizes/secdefaultkeysize.md) — The default key size for the specified type. _(deprecated)_
- [kSec3DES192](seckeysizes/sec3des192.md) — 192-bit DES. _(deprecated)_
- [kSecAES128](seckeysizes/secaes128.md) — 128-bit AES. _(deprecated)_
- [kSecAES192](seckeysizes/secaes192.md) — 192-bit AES. _(deprecated)_
- [kSecAES256](seckeysizes/secaes256.md) — 256-bit AES. _(deprecated)_
- [kSecp192r1](seckeysizes/secp192r1.md) — 192-bit ECC Keys for Suite-B from RFC 4492 section 5.1.1. _(deprecated)_
- [kSecp256r1](seckeysizes/secp256r1.md) — 256-bit ECC Keys for Suite-B from RFC 4492 section 5.1.1. _(deprecated)_
- [kSecp384r1](seckeysizes/secp384r1.md) — 384-bit ECC Keys for Suite-B from RFC 4492 section 5.1.1. _(deprecated)_
- [kSecp521r1](seckeysizes/secp521r1.md) — 521-bit ECC Keys for Suite-B from RFC 4492 section 5.1.1. _(deprecated)_
- [kSecRSAMin](seckeysizes/secrsamin.md) — 1024 bits is the minimum size for an RSA key. _(deprecated)_
- [kSecRSAMax](seckeysizes/secrsamax.md) — 4096 bits is the maximum size for an RSA key. _(deprecated)_

### Initializers

- [init(rawValue:)](<seckeysizes/init(rawvalue_).md>) _(deprecated)_
