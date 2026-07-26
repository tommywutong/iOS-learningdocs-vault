---
title: Insecure
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/insecure
source_url: 'https://developer.apple.com/documentation/cryptokit/insecure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/insecure.json'
content_hash: 'sha256:87ce2a8bd8634867'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# Insecure

<sub>Enumeration</sub>

A container for older, cryptographically insecure algorithms.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Insecure
```

## Overview

> [!important] Important
> These algorithms aren’t considered cryptographically secure, but the framework provides them for backward compatibility with older services that require them. For new services, avoid these algorithms.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Hashes

- [MD5](insecure/md5.md) — An implementation of MD5 hashing.
- [SHA1](insecure/sha1.md) — An implementation of SHA1 hashing.

### Structures

- [MD5Digest](insecure/md5digest.md) — The output of a MD5 hash.
- [SHA1Digest](insecure/sha1digest.md) — The output of a SHA1 hash.
