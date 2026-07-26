---
title: UndoManager.UserInfoKey
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/userinfokey
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/userinfokey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/userinfokey.json'
content_hash: 'sha256:9cbd854ccfa86c53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# UndoManager.UserInfoKey

<sub>Structure</sub>

An extensible namespace for undo and redo user info keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct UserInfoKey
```

## Discussion

Extend this type with the names of user info keys you want to associate with undo actions, like this:

```swift
extension UndoManager.UserInfoKey {
    static let icon: UndoManager.UserInfoKey = "icon"
}
```

You then use this key when you set and get undo user info values.

```swift
self.undoManager.setActionUserInfoValue(Image(named: "new_layer"), forKey: .icon)

```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a user info key from a raw value

- [init(_:)](<userinfokey/init(__).md>) — Creates a user info key from the given string.
- [init(rawValue:)](<userinfokey/init(rawvalue_).md>)

## See Also

### Working with user info

- [- setActionUserInfoValue:forKey:](<setactionuserinfovalue(__forkey_).md>) — Sets a user info value for an undo or redo action.
- [- undoActionUserInfoValueForKey:](<undoactionuserinfovalue(forkey_).md>) — Retrieves the undo action’s user info value for the given key.
- [- redoActionUserInfoValueForKey:](<redoactionuserinfovalue(forkey_).md>) — Retrieves the redo action’s user info value for the given key.
