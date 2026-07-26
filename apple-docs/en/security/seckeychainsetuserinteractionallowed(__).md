---
title: 'SecKeychainSetUserInteractionAllowed(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainsetuserinteractionallowed(_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainsetuserinteractionallowed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainsetuserinteractionallowed%28_%3A%29.json'
content_hash: 'sha256:e45f54a65a2907be'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainSetUserInteractionAllowed(_:)

<sub>Function</sub>

Enables or disables the user interface for keychain services functions that automatically display a user interface.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainSetUserInteractionAllowed(_ state: Bool) -> OSStatus
```

## Parameters

- `state` — A flag that indicates whether the keychain services will display a user interface. If you pass [true](../swift/true.md), user interaction is allowed. This is the default value. If [false](../swift/false.md), keychain services functions that normally display a user interface will instead return an error.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Certain keychain services functions that require the presence of a keychain automatically display a _Keychain Not Found_ dialog if there is none. Functions that require the keychain to be unlocked automatically display the _Unlock Keychain_ dialog. The [SecKeychainSetUserInteractionAllowed](<seckeychainsetuserinteractionallowed(__).md>) function enables you to control whether these functions display a user interface. By default, user interaction is permitted.

If you are writing an application that must run unattended on a server, you may wish to disable the user interface so that any subsequent keychain calls that normally bring up the unlock UI will instead return immediately with an [errSecInteractionRequired](errsecinteractionrequired.md) result). In this case you must programmatically create a keychain or unlock the keychain when necessary.

### Special Considerations

If you disable user interaction before calling a Keychain Services function, be sure to reenable it when you are finished. Failure to reenable user interaction will affect other clients of the Keychain Services.
