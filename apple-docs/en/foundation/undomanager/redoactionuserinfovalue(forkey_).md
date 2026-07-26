---
title: 'redoActionUserInfoValue(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/undomanager/redoactionuserinfovalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/redoactionuserinfovalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/redoactionuserinfovalue%28forkey%3A%29.json'
content_hash: 'sha256:d5c29554d29b4301'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# redoActionUserInfoValue(forKey:)

<sub>Instance Method</sub>

Retrieves the redo action’s user info value for the given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func redoActionUserInfoValue(forKey key: UndoManager.UserInfoKey) -> Any?
```

## Parameters

- `key` — The key associated with the value to return.

## Return Value

The value that you previously registered to this key with [- setActionUserInfoValue:forKey:](<setactionuserinfovalue(__forkey_).md>), or `nil` if the key is absent.

## Discussion

Use this method to retrieve a user info value for the redo action you previously set with [- setActionUserInfoValue:forKey:](<setactionuserinfovalue(__forkey_).md>).

In this example, an app’s `redoButton()` method provides a SwiftUI view that incorporates a previously assigned icon for the action:

```swift
func redoButton() -> some SwiftUI.View {
    Button(action: {
        self.undoManager.redo()
    }) {
        Label(self.undoManager.redoActionName,
              image: self.undoManager.redoActionUserInfoValue(forKey: .icon) as? Image)
    }
}
```

## See Also

### Working with user info

- [- setActionUserInfoValue:forKey:](<setactionuserinfovalue(__forkey_).md>) — Sets a user info value for an undo or redo action.
- [- undoActionUserInfoValueForKey:](<undoactionuserinfovalue(forkey_).md>) — Retrieves the undo action’s user info value for the given key.
- [UserInfoKey](userinfokey.md) — An extensible namespace for undo and redo user info keys.
