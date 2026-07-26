---
title: 'searchFocused(_:equals:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/searchfocused(_:equals:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/searchfocused(_:equals:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/searchfocused%28_%3Aequals%3A%29.json'
content_hash: 'sha256:16c393fe398773b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# searchFocused(_:equals:)

<sub>Instance Method</sub>

Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func searchFocused<V>(_ binding: FocusState<V>.Binding, equals value: V) -> some View where V : Hashable

```

## Parameters

- `binding` — The state binding to register. When focus moves to the associated search field, the binding sets the bound value to the corresponding match value. If a caller sets the state value programmatically to the matching value, then focus moves to the search field. When focus leaves the search field, the binding sets the bound value to `nil`. If a caller sets the value to `nil`, SwiftUI automatically dismisses focus.

- `value` — The value to match against when determining whether the binding should change.

## Return Value

The modified view.

## Discussion

To control focus by matching a simple boolean condition, use the [searchFocused(_:)](<searchfocused(__).md>) modifier instead.

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
- [searchFocused(_:)](<searchfocused(__).md>) — Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
