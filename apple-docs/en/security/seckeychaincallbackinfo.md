---
title: SecKeychainCallbackInfo
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychaincallbackinfo
source_url: 'https://developer.apple.com/documentation/security/seckeychaincallbackinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaincallbackinfo.json'
content_hash: 'sha256:909d810b62c90a5d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainCallbackInfo

<sub>Structure</sub>

Information about a keychain event that keychain services deliver to your app via a callback function.

<sub>macOS</sub>

```swift
struct SecKeychainCallbackInfo
```

## Overview

This structure contains information about the keychain event of which your application wants to be notified. Keychain services pass a pointer to this structure in the `info` parameter of your callback function. For information on how to write a keychain event callback function, see [SecKeychainCallback](seckeychaincallback.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Instance Properties

- [item](seckeychaincallbackinfo/item.md) — A reference to the keychain item in which the event occurred. If the event did not involve an item, this field is not valid.
- [keychain](seckeychaincallbackinfo/keychain.md) — A reference to the keychain in which the event occurred. If the event did not involve a keychain, this field is not valid.
- [pid](seckeychaincallbackinfo/pid.md) — The ID of the process that generated this event.
- [version](seckeychaincallbackinfo/version.md) — The version of this structure.

### Initializers

- [init(version:item:keychain:pid:)](<seckeychaincallbackinfo/init(version_item_keychain_pid_).md>) — Creates a new keychain callback information structure.
