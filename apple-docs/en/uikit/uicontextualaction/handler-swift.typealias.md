---
title: UIContextualAction.Handler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontextualaction/handler-swift.typealias
source_url: 'https://developer.apple.com/documentation/uikit/uicontextualaction/handler-swift.typealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextualaction/handler-swift.typealias.json'
content_hash: 'sha256:b1e19551e42b85bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextualAction](../uicontextualaction.md)

# UIContextualAction.Handler

<sub>Type Alias</sub>

The handler block to call in response to the selection of an action.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor typealias Handler = (UIContextualAction, UIView, @escaping (Bool) -> Void) -> Void
```

## Parameters

- `action` — The object containing information about the selected action.

- `sourceView` — The view in which the action was displayed.

- `completionHandler` — The handler block for you to execute after you have performed the action. This block has no return value and takes the following parameter: - **actionPerformed** — A Boolean value indicating whether you performed the action. Specify [true](../../swift/true.md) if you performed the action or [false](../../swift/false.md) if you were unable to perform the action for some reason.

## See Also

### Getting the configuration details

- [handler](handler-swift.property.md) — The handler block to execute when the user selects the action.
- [style](style-swift.property.md) — The style that applies to the action button.
- [Style](style-swift.enum.md) — Constants indicating the style information that applies to the action button.
