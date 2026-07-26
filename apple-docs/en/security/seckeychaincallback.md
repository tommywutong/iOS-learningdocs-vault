---
title: SecKeychainCallback
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/seckeychaincallback
source_url: 'https://developer.apple.com/documentation/security/seckeychaincallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaincallback.json'
content_hash: 'sha256:6d42513194102d1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainCallback

<sub>Type Alias</sub>

A customized callback function that keychain services call when a keychain event has occurred.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
typealias SecKeychainCallback = (SecKeychainEvent, UnsafeMutablePointer<SecKeychainCallbackInfo>, UnsafeMutableRawPointer?) -> OSStatus
```

## Parameters

- `keychainEvent` — The keychain event that occurred. The type of event that can trigger your callback depends on the bit mask you passed in the `eventMask` parameter of the function [SecKeychainAddCallback](<seckeychainaddcallback(______).md>). See [SecKeychainEvent](seckeychainevent.md) for a list of possible values.

- `info` — A pointer to a structure of type [SecKeychainCallbackInfo](seckeychaincallbackinfo.md). This structure provides your callback with information about the keychain event.

- `context` — A pointer to application-defined storage that your application previously passed to the function [SecKeychainAddCallback](<seckeychainaddcallback(______).md>). You can use this value to provide information that the callback function needs in order to properly handle the event, such as an object on which the callback function should call a method.

## Return Value

A result code. See `Codes`.

## Discussion

You would declare your keychain callback function like this if you were to name it `MyKeychainCallback`:

Listing 1. Declaring a keychain callback function

```objc
OSStatus MyKeychainCallback (
    SecKeychainEvent keychainEvent,
    SecKeychainCallbackInfo *info,
    void *context
);
```

To add your callback function, use the [SecKeychainAddCallback](<seckeychainaddcallback(______).md>) function. To remove your callback function, use the [SecKeychainRemoveCallback](<seckeychainremovecallback(__).md>) function.
