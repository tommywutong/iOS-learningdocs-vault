---
title: SecKeychainSettings
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychainsettings
source_url: 'https://developer.apple.com/documentation/security/seckeychainsettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainsettings.json'
content_hash: 'sha256:d4b7a1a5ae5c4163'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainSettings

<sub>Structure</sub>

A structure that contains information about keychain settings.

<sub>Mac Catalyst, macOS</sub>

```swift
struct SecKeychainSettings
```

## Overview

This structure contains information about a keychain’s settings such as locking on sleep and the lock time interval. Use the [SecKeychainSetSettings](<seckeychainsetsettings(____).md>) and [SecKeychainCopySettings](<seckeychaincopysettings(____).md>) functions to set and copy a keychain’s settings.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<seckeychainsettings/init().md>) — Initializes a keychain settings structure with default values.
- [init(version:lockOnSleep:useLockInterval:lockInterval:)](<seckeychainsettings/init(version_lockonsleep_uselockinterval_lockinterval_).md>) — Initializes a keychain settings structures with the given values.

### Instance Properties

- [lockInterval](seckeychainsettings/lockinterval.md) — The number of seconds to wait before the keychain locks.
- [lockOnSleep](seckeychainsettings/lockonsleep.md) — A Boolean value indicating whether the keychain locks when the system sleeps.
- [useLockInterval](seckeychainsettings/uselockinterval.md) — A Boolean value indicating whether the keychain automatically locks after a certain period of time.
- [version](seckeychainsettings/version.md) — The keychain version.
