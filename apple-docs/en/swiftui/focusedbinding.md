---
title: FocusedBinding
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/focusedbinding
source_url: 'https://developer.apple.com/documentation/swiftui/focusedbinding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusedbinding.json'
content_hash: 'sha256:9af027f8e9e0283b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FocusedBinding

<sub>Structure</sub>

A convenience property wrapper for observing and automatically unwrapping state bindings from the focused view or one of its ancestors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@propertyWrapper struct FocusedBinding<Value>
```

## Overview

If multiple views publish bindings using the same key, the wrapped property will reflect the value of the binding from the view closest to focus.

## Relationships

- **Conforms To**: [DynamicProperty](dynamicproperty.md)

## Topics

### Creating the binding

- [init(_:)](<focusedbinding/init(__).md>) — A new property wrapper for the given key path.

### Getting the value

- [projectedValue](focusedbinding/projectedvalue.md) — A binding to the optional value.
- [wrappedValue](focusedbinding/wrappedvalue.md) — The unwrapped value for the focus key given the current scope and state of the focused view hierarchy.

## See Also

### Managing focus state

- [focused(_:equals:)](<view/focused(__equals_).md>) — Modifies this view by binding its focus state to the given state value.
- [focused(_:)](<view/focused(__).md>) — Modifies this view by binding its focus state to the given Boolean state value.
- [isFocused](environmentvalues/isfocused.md) — Returns whether the nearest focusable ancestor has focus.
- [FocusState](focusstate.md) — A property wrapper type that can read and write a value that SwiftUI updates as the placement of focus within the scene changes.
- [FocusedValue](focusedvalue.md) — A property wrapper for observing values from the focused view or one of its ancestors.
- [Entry()](<entry().md>) — Creates an environment values, transaction, container values, or focused values entry.
- [FocusedValueKey](focusedvaluekey.md) — A protocol for identifier types used when publishing and observing focused values.
- [searchFocused(_:)](<view/searchfocused(__).md>) — Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [searchFocused(_:equals:)](<view/searchfocused(__equals_).md>) — Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.
