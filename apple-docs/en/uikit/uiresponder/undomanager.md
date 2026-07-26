---
title: undoManager
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/undomanager
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/undomanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/undomanager.json'
content_hash: 'sha256:634cba4bd6e5ff16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# undoManager

<sub>Instance Property</sub>

Returns the nearest shared undo manager in the responder chain.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var undoManager: UndoManager? { get }
```

## Discussion

By default, every window of an application has an undo manager: a shared object for managing undo and redo operations. However, the class of any object in the responder chain can have their own custom undo manager. (For example, instances of [UITextField](../uitextfield.md) have their own undo manager that’s cleared when the text field resigns first-responder status.) When you request an undo manager, the request goes up the responder chain and the [UIWindow](../uiwindow.md) object returns a usable instance.

You may add undo managers to your view controllers to perform undo and redo operations local to the managed view.
