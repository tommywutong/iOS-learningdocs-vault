---
title: 'SecKeychainAddCallback(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainaddcallback(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainaddcallback(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainaddcallback%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:15119f9721f4ad5e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainAddCallback(_:_:_:)

<sub>Function</sub>

Registers your keychain event callback function.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainAddCallback(_ callbackFunction: SecKeychainCallback, _ eventMask: SecKeychainEventMask, _ userContext: UnsafeMutableRawPointer?) -> OSStatus
```

## Parameters

- `callbackFunction` — A pointer to your keychain event callback function, described in [SecKeychainCallback](seckeychaincallback.md).

- `eventMask` — A bit mask indicating the keychain events of which your application wishes to be notified. See [SecKeychainEventMask](seckeychaineventmask.md) for valid values. Keychain Services tests this mask to determine the keychain events that you wish to receive, and passes these events in the `keychainEvent` parameter of your callback function.

- `userContext` — A pointer to application-defined storage that will be passed to your callback function. Your application can use this to associate any particular call of this function with any particular call of your keychain event callback function.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

It is important to note that the current Foundation or Core Foundation run loop must be active when making this call or the callbacks are not registered. In multithreaded programs, the notifications are registered in the run loop of the thread calling [SecKeychainAddCallback](<seckeychainaddcallback(______).md>); therefore, delivery of notifications depends on the functioning of that thread’s run loop. If that thread terminates, or is so busy that it doesn’t operate its run loop in a timely manner, notifications will be delayed, and may eventually be dropped without any notification.

For that reason, it is inadvisable for your program to depend on delivery of notifications caused by your own actions (such as depending on receiving a deletion notification before updating a UI view) unless your program is multithreaded and can take notifications on a thread different from the one generating the events.
