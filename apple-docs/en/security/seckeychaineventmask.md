---
title: SecKeychainEventMask
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychaineventmask
source_url: 'https://developer.apple.com/documentation/security/seckeychaineventmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaineventmask.json'
content_hash: 'sha256:5c1f666d4ee51abd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainEventMask

<sub>Structure</sub>

Bit masks corresponding to the events that can trigger a keychain callback.

<sub>Mac Catalyst, macOS</sub>

```swift
struct SecKeychainEventMask
```

## Overview

Bitwise `OR` one or more of these masks together to provide the `eventMask` input to the [SecKeychainAddCallback](<seckeychainaddcallback(______).md>) function to indicate what event or events should trigger your callback.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<seckeychaineventmask/init(rawvalue_).md>) — Initializes an event mask value.

### Constants

- [kSecLockEventMask](seckeychaineventmask/lockeventmask.md) — If the bit specified by this mask is set, your callback function is invoked when a keychain is locked.
- [kSecUnlockEventMask](seckeychaineventmask/unlockeventmask.md) — If the bit specified by this mask is set, your callback function is invoked when a keychain is unlocked.
- [kSecAddEventMask](seckeychaineventmask/addeventmask.md) — If the bit specified by this mask is set, your callback function is invoked when an item is added to a keychain.
- [kSecDeleteEventMask](seckeychaineventmask/deleteeventmask.md) — If the bit specified by this mask is set, your callback function is invoked when an item is deleted from a keychain.
- [kSecUpdateEventMask](seckeychaineventmask/updateeventmask.md) — If the bit specified by this mask is set, your callback function is invoked when a keychain item is updated.
- [kSecPasswordChangedEventMask](seckeychaineventmask/passwordchangedeventmask.md) — If the bit specified by this mask is set, your callback function is invoked when the keychain password is changed.
- [kSecDefaultChangedEventMask](seckeychaineventmask/defaultchangedeventmask.md) — If the bit specified by this mask is set, your callback function is invoked when a different keychain is specified as the default.
- [kSecDataAccessEventMask](seckeychaineventmask/dataaccesseventmask.md) — If the bit specified by this mask is set, your callback function is invoked when a process accesses a keychain item’s data. _(deprecated)_
- [kSecKeychainListChangedMask](seckeychaineventmask/keychainlistchangedmask.md) — If the bit specified by this mask is set, your callback function is invoked when a keychain list is changed.
- [kSecTrustSettingsChangedEventMask](seckeychaineventmask/trustsettingschangedeventmask.md) — If the bit specified by this mask is set, your callback function is invoked when there is a change in certificate trust settings.
- [kSecEveryEventMask](seckeychaineventmask/everyeventmask.md) — If all the bits are set, your callback function is invoked whenever any event occurs.
