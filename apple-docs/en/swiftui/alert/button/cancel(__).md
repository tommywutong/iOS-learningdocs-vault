---
title: 'cancel(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/alert/button/cancel(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/alert/button/cancel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/alert/button/cancel%28_%3A%29.json'
content_hash: 'sha256:eb49e639abb136fd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Alert](../../alert.md) · [Button](../button.md)

# cancel(_:)

<sub>Type Method</sub>

Creates an alert button that indicates cancellation, with a system-provided label.

> [!warning] Deprecated
> Use View.alert(_:isPresented:presenting:actions:) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func cancel(_ action: (() -> Void)? = {}) -> Alert.Button
```

## Parameters

- `action` — A closure to execute when the user taps or presses the button.

## Return Value

An alert button that indicates cancellation.

## Discussion

The system automatically chooses locale-appropriate text for the button’s label.

## See Also

### Getting a button

- [default(_:action:)](<default(__action_).md>) — Creates an alert button with the default style. _(deprecated)_
- [cancel(_:action:)](<cancel(__action_).md>) — Creates an alert button that indicates cancellation, with a custom label. _(deprecated)_
- [destructive(_:action:)](<destructive(__action_).md>) — Creates an alert button with a style that indicates a destructive action. _(deprecated)_
