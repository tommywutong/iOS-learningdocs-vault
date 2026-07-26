---
title: SecKeychainEvent
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychainevent
source_url: 'https://developer.apple.com/documentation/security/seckeychainevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainevent.json'
content_hash: 'sha256:cc78280dceb7a6b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainEvent

<sub>Enumeration</sub>

The list of keychain events that can trigger a callback.

<sub>Mac Catalyst, macOS</sub>

```swift
enum SecKeychainEvent
```

## Overview

Keychain Services includes one of these events in the callback you register with [SecKeychainAddCallback](<seckeychainaddcallback(______).md>), using the function signature defined by [SecKeychainCallback](seckeychaincallback.md), to indicate what event triggered the callback.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kSecLockEvent](seckeychainevent/lockevent.md) — Indicates a keychain was locked.
- [kSecUnlockEvent](seckeychainevent/unlockevent.md) — Indicates a keychain was successfully unlocked.
- [kSecAddEvent](seckeychainevent/addevent.md) — Indicates an item was added to a keychain.
- [kSecDeleteEvent](seckeychainevent/deleteevent.md) — Indicates an item was deleted from a keychain.
- [kSecUpdateEvent](seckeychainevent/updateevent.md) — Indicates a keychain item was updated.
- [kSecPasswordChangedEvent](seckeychainevent/passwordchangedevent.md) — Indicates the keychain password was changed.
- [kSecDefaultChangedEvent](seckeychainevent/defaultchangedevent.md) — Indicates that a different keychain was specified as the default.
- [kSecDataAccessEvent](seckeychainevent/dataaccessevent.md) — Indicates a process has accessed a keychain item’s data. _(deprecated)_
- [kSecKeychainListChangedEvent](seckeychainevent/keychainlistchangedevent.md) — Indicates the list of keychains has changed.
- [kSecTrustSettingsChangedEvent](seckeychainevent/trustsettingschangedevent.md) — Indicates trust settings have changed.

### Initializers

- [init(rawValue:)](<seckeychainevent/init(rawvalue_).md>)
