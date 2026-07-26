---
title: 'undoActionUserInfoValue(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/undomanager/undoactionuserinfovalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/undoactionuserinfovalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/undoactionuserinfovalue%28forkey%3A%29.json'
content_hash: 'sha256:362c217d5f80c9a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# undoActionUserInfoValue(forKey:)

<sub>Instance Method</sub>

Retrieves the undo action’s user info value for the given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func undoActionUserInfoValue(forKey key: UndoManager.UserInfoKey) -> Any?
```

## Parameters

- `key` — The key associated with the value to return.

## Return Value

The value that you previously registered to this key with [- setActionUserInfoValue:forKey:](<setactionuserinfovalue(__forkey_).md>), or `nil` if the key is absent.

## Discussion

Use this method to retrieve a user info value for the undo action you previously set with [- setActionUserInfoValue:forKey:](<setactionuserinfovalue(__forkey_).md>).

In this example, an app’s `undoButton()` method provides a SwiftUI view that incorporates a previously assigned icon for the undo action:

```swift
func undoButton() -> some SwiftUI.View {
    Button(action: {
        self.undoManager.undo()
    }) {
        Label(self.undoManager.undoActionName,
              image: self.undoManager.undoActionUserInfoValue(forKey: .icon) as? Image)
    }
}
```

## See Also

### Working with user info

- [- setActionUserInfoValue:forKey:](<setactionuserinfovalue(__forkey_).md>) — Sets a user info value for an undo or redo action.
- [- redoActionUserInfoValueForKey:](<redoactionuserinfovalue(forkey_).md>) — Retrieves the redo action’s user info value for the given key.
- [UserInfoKey](userinfokey.md) — An extensible namespace for undo and redo user info keys.
