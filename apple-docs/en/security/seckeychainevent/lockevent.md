---
title: SecKeychainEvent.lockEvent
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychainevent/lockevent
source_url: 'https://developer.apple.com/documentation/security/seckeychainevent/lockevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainevent/lockevent.json'
content_hash: 'sha256:f3cd4185a039958a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainEvent](../seckeychainevent.md)

# SecKeychainEvent.lockEvent

<sub>Case</sub>

Indicates a keychain was locked.

<sub>Mac Catalyst, macOS</sub>

```swift
case lockEvent
```

## Discussion

It is impossible to distinguish between a lock event caused by an explicit request and one caused by a keychain that locked itself because of a timeout. Therefore, the `pid` parameter in the [SecKeychainCallbackInfo](../seckeychaincallbackinfo.md) structure does not contain useful information for this event. Note that when the login session terminates, all keychains become effectively locked; however, no `kSecLockEvent` events are generated in this case.
