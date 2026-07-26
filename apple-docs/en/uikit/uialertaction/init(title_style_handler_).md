---
title: 'init(title:style:handler:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uialertaction/init(title:style:handler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uialertaction/init(title:style:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertaction/init%28title%3Astyle%3Ahandler%3A%29.json'
content_hash: 'sha256:60fe24c976b86842'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertAction](../uialertaction.md)

# init(title:style:handler:)

<sub>Initializer</sub>

Create and return an action with the specified title and behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(title: String?, style: UIAlertAction.Style, handler: ((UIAlertAction) -> Void)? = nil)
```

## Parameters

- `title` — The text to use for the button title. The value you specify should be localized for the user’s current language. This parameter must not be `nil`, except in a tvOS app where a `nil` title may be used with [UIAlertActionStyleCancel](style-swift.enum/cancel.md).

- `style` — Additional styling information to apply to the button. Use the style information to convey the type of action that is performed by the button. For a list of possible values, see the constants in [Style](style-swift.enum.md).

- `handler` — A block to execute when the user selects the action. This block has no return value and takes the selected action object as its only parameter.

## Return Value

A new alert action object.

## Discussion

Actions are enabled by default when you create them.
