---
title: SecKeychainEvent.unlockEvent
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychainevent/unlockevent
source_url: 'https://developer.apple.com/documentation/security/seckeychainevent/unlockevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainevent/unlockevent.json'
content_hash: 'sha256:c4542436287947ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainEvent](../seckeychainevent.md)

# SecKeychainEvent.unlockEvent

<sub>Case</sub>

Indicates a keychain was successfully unlocked.

<sub>Mac Catalyst, macOS</sub>

```swift
case unlockEvent
```

## Discussion

It is impossible to distinguish between an unlock event caused by an explicit request and one that occurred automatically because the keychain was needed to perform an operation. In either case, however, the `pid` parameter in the `SecKeychainCallbackInfo` structure does return the ID of the process whose actions caused the unlock event.
