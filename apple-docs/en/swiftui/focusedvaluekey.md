---
title: FocusedValueKey
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/focusedvaluekey
source_url: 'https://developer.apple.com/documentation/swiftui/focusedvaluekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusedvaluekey.json'
content_hash: 'sha256:d7b1bbeb71ffdeec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FocusedValueKey

<sub>Protocol</sub>

A protocol for identifier types used when publishing and observing focused values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol FocusedValueKey
```

## Overview

Unlike [EnvironmentKey](environmentkey.md), `FocusedValueKey` has no default value requirement, because the default value for a key is always `nil`.

Use the `Entry` macro to create custom focused values by extending `FocusedValues` with new properties:

```swift
extension FocusedValues {
    @Entry var selectedItem: Item?
}
```

Alternatively it is possible to create a focused value key by manually creating a type that conforms to this protocol:

```swift
struct SelectedItemKey: FocusedValueKey {
    typealias Value = Item
}
```

Then extend [FocusedValues](focusedvalues.md) to add a computed property for your key:

```swift
extension FocusedValues {
    var selectedItem: Item? {
        get { self[SelectedItemKey.self] }
        set { self[SelectedItemKey.self] = newValue }
    }
}
```

## Topics

### Specifying the value type

- [Value](focusedvaluekey/value.md)

## See Also

### Managing focus state

- [focused(_:equals:)](<view/focused(__equals_).md>) — Modifies this view by binding its focus state to the given state value.
- [focused(_:)](<view/focused(__).md>) — Modifies this view by binding its focus state to the given Boolean state value.
- [isFocused](environmentvalues/isfocused.md) — Returns whether the nearest focusable ancestor has focus.
- [FocusState](focusstate.md) — A property wrapper type that can read and write a value that SwiftUI updates as the placement of focus within the scene changes.
- [FocusedValue](focusedvalue.md) — A property wrapper for observing values from the focused view or one of its ancestors.
- [Entry()](<entry().md>) — Creates an environment values, transaction, container values, or focused values entry.
- [FocusedBinding](focusedbinding.md) — A convenience property wrapper for observing and automatically unwrapping state bindings from the focused view or one of its ancestors.
- [searchFocused(_:)](<view/searchfocused(__).md>) — Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [searchFocused(_:equals:)](<view/searchfocused(__equals_).md>) — Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.
