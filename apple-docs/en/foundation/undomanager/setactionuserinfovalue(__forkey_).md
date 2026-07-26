---
title: 'setActionUserInfoValue(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/undomanager/setactionuserinfovalue(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/setactionuserinfovalue(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/setactionuserinfovalue%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:8bcfe43c7eafa2d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# setActionUserInfoValue(_:forKey:)

<sub>Instance Method</sub>

Sets a user info value for an undo or redo action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setActionUserInfoValue(_ info: Any?, forKey key: UndoManager.UserInfoKey)
```

## Parameters

- `info` — The value to save in the action’s user info.

- `key` — The key to associate with the user info value.

## Discussion

Set user info on an undo action to provide custom information to the action beyond its action name. You can use this for things like an icon to represent the undoable action, or a timestamp of when the undo manager registers the action.

Start by extending [UserInfoKey](userinfokey.md) with key names to identify the user info values you want to associate with undo actions.

```swift
extension UndoManager.UserInfoKey {
    static let icon: UndoManager.UserInfoKey = "icon"
}
```

Then set the user info value with this key as part of registering the undoable action. In this example, an app’s `insertLayer()` method provides a custom icon before setting up an undo action that calls the app’s `removeLayer()` method:

```swift
func insertLayer() {
    self.undoManager.setActionName("Insert layer")
    self.undoManager.setActionUserInfoValue(Image(named: "new_layer"), forKey: .icon)

    self.layers.append(Layer())

    self.undoManager.registerUndo(withTarget: self) {
        $0.removeLayer()
    }
}
```

## See Also

### Working with user info

- [- undoActionUserInfoValueForKey:](<undoactionuserinfovalue(forkey_).md>) — Retrieves the undo action’s user info value for the given key.
- [- redoActionUserInfoValueForKey:](<redoactionuserinfovalue(forkey_).md>) — Retrieves the redo action’s user info value for the given key.
- [UserInfoKey](userinfokey.md) — An extensible namespace for undo and redo user info keys.
