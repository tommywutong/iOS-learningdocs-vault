---
title: FocusedValue
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/focusedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/focusedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusedvalue.json'
content_hash: 'sha256:033f74e0c7e21a81'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FocusedValue

<sub>Structure</sub>

A property wrapper for observing values from the focused view or one of its ancestors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@propertyWrapper struct FocusedValue<Value>
```

## Overview

If multiple views publish values using the same key, the wrapped property will reflect the value from the view closest to focus.

## Relationships

- **Conforms To**: [DynamicProperty](dynamicproperty.md)

## Topics

### Creating the value

- [init(_:)](<focusedvalue/init(__).md>) — A new property wrapper for the given key path.

### Getting the value

- [wrappedValue](focusedvalue/wrappedvalue.md) — The value for the focus key given the current scope and state of the focused view hierarchy.

## See Also

### Managing focus state

- [focused(_:equals:)](<view/focused(__equals_).md>) — Modifies this view by binding its focus state to the given state value.
- [focused(_:)](<view/focused(__).md>) — Modifies this view by binding its focus state to the given Boolean state value.
- [isFocused](environmentvalues/isfocused.md) — Returns whether the nearest focusable ancestor has focus.
- [FocusState](focusstate.md) — A property wrapper type that can read and write a value that SwiftUI updates as the placement of focus within the scene changes.
- [Entry()](<entry().md>) — Creates an environment values, transaction, container values, or focused values entry.
- [FocusedValueKey](focusedvaluekey.md) — A protocol for identifier types used when publishing and observing focused values.
- [FocusedBinding](focusedbinding.md) — A convenience property wrapper for observing and automatically unwrapping state bindings from the focused view or one of its ancestors.
- [searchFocused(_:)](<view/searchfocused(__).md>) — Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [searchFocused(_:equals:)](<view/searchfocused(__equals_).md>) — Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.
