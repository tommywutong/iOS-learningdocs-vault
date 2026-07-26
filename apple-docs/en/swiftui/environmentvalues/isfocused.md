---
title: isFocused
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/isfocused
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/isfocused'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/isfocused.json'
content_hash: 'sha256:d435f98744bdb645'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# isFocused

<sub>Instance Property</sub>

Returns whether the nearest focusable ancestor has focus.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isFocused: Bool { get }
```

## Discussion

If there is no focusable ancestor, the value is `false`.

## See Also

### Managing focus state

- [focused(_:equals:)](<../view/focused(__equals_).md>) — Modifies this view by binding its focus state to the given state value.
- [focused(_:)](<../view/focused(__).md>) — Modifies this view by binding its focus state to the given Boolean state value.
- [FocusState](../focusstate.md) — A property wrapper type that can read and write a value that SwiftUI updates as the placement of focus within the scene changes.
- [FocusedValue](../focusedvalue.md) — A property wrapper for observing values from the focused view or one of its ancestors.
- [Entry()](<../entry().md>) — Creates an environment values, transaction, container values, or focused values entry.
- [FocusedValueKey](../focusedvaluekey.md) — A protocol for identifier types used when publishing and observing focused values.
- [FocusedBinding](../focusedbinding.md) — A convenience property wrapper for observing and automatically unwrapping state bindings from the focused view or one of its ancestors.
- [searchFocused(_:)](<../view/searchfocused(__).md>) — Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [searchFocused(_:equals:)](<../view/searchfocused(__equals_).md>) — Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.
