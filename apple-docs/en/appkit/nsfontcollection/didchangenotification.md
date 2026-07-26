---
title: didChangeNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.7+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsfontcollection/didchangenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsfontcollection/didchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsfontcollection/didchangenotification.json'
content_hash: 'sha256:d87a9a4ab5a36240'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSFontCollection](../nsfontcollection.md)

# didChangeNotification

<sub>Type Property</sub>

Posted whenever a font collection is changed.

<sub>macOS</sub>

```swift
class let didChangeNotification: NSNotification.Name
```

## Discussion

The notification’s object is the font collection that was affected. The notification’s `userInfo` dictionary contains information about the the collection change containing the keys defined in [UserInfoKey](userinfokey.md) and the corresponding values.

To observe this notification using Swift concurrency, use [DidChangeMessage](didchangemessage.md).

## See Also

### Responding to Changes

- [UserInfoKey](userinfokey.md) — These constants are used as keys in the [NSFontCollectionDidChangeNotification](didchangenotification.md) `userInfo` dictionary to indicate the changes that have taken place.
- [ActionTypeKey](actiontypekey.md) — The following actions are possible values of the [NSFontCollectionActionKey](actionuserinfokey.md) in the [NSFontCollectionDidChangeNotification](didchangenotification.md) `userInfo` method.
