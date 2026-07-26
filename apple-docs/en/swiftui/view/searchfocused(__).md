---
title: 'searchFocused(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/searchfocused(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/searchfocused(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/searchfocused%28_%3A%29.json'
content_hash: 'sha256:7d90ba9a3efc4fcf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# searchFocused(_:)

<sub>Instance Method</sub>

Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func searchFocused(_ binding: FocusState<Bool>.Binding) -> some View

```

## Parameters

- `binding` — The focus state to bind. When focus moves to the associated search field, the binding sets the bound value to `true`. If a caller sets the value to  `true` programmatically, then focus moves to the search field. When focus leaves the search field, the binding sets the value to `false`. If a caller sets the value to `false`, SwiftUI automatically dismisses focus.

## Return Value

The modified view.

## Discussion

To control focus by matching a non-boolean value, use the [searchFocused(_:equals:)](<searchfocused(__equals_).md>) modifier instead.

For more information about using searchable modifiers, refer to [Adding a search interface to your app](../adding-a-search-interface-to-your-app.md).

## See Also

### Managing focus state

- [focused(_:equals:)](<focused(__equals_).md>) — Modifies this view by binding its focus state to the given state value.
- [focused(_:)](<focused(__).md>) — Modifies this view by binding its focus state to the given Boolean state value.
- [isFocused](../environmentvalues/isfocused.md) — Returns whether the nearest focusable ancestor has focus.
- [FocusState](../focusstate.md) — A property wrapper type that can read and write a value that SwiftUI updates as the placement of focus within the scene changes.
- [FocusedValue](../focusedvalue.md) — A property wrapper for observing values from the focused view or one of its ancestors.
- [Entry()](<../entry().md>) — Creates an environment values, transaction, container values, or focused values entry.
- [FocusedValueKey](../focusedvaluekey.md) — A protocol for identifier types used when publishing and observing focused values.
- [FocusedBinding](../focusedbinding.md) — A convenience property wrapper for observing and automatically unwrapping state bindings from the focused view or one of its ancestors.
- [searchFocused(_:equals:)](<searchfocused(__equals_).md>) — Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.
