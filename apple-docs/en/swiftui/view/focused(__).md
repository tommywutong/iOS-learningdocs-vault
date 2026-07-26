---
title: 'focused(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/focused(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/focused(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/focused%28_%3A%29.json'
content_hash: 'sha256:13b255961c7f6e04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# focused(_:)

<sub>Instance Method</sub>

Modifies this view by binding its focus state to the given Boolean state value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func focused(_ condition: FocusState<Bool>.Binding) -> some View

```

## Parameters

- `condition` — The focus state to bind. When focus moves to the view, the binding sets the bound value to `true`. If a caller sets the value to  `true` programmatically, then focus moves to the modified view. When focus leaves the modified view, the binding sets the value to `false`. If a caller sets the value to `false`, SwiftUI automatically dismisses focus.

## Return Value

The modified view.

## Discussion

Use this modifier to cause the view to receive focus whenever the `condition` value is `true`. You can use this modifier to observe the focus state of a single view, or programmatically set and remove focus from the view.

In the following example, a single [TextField](../textfield.md) accepts a user’s desired `username`. The text field binds its focus state to the Boolean value `usernameFieldIsFocused`. A “Submit” button’s action verifies whether the name is available. If the name is unavailable, the button sets `usernameFieldIsFocused` to `true`, which causes focus to return to the text field, so the user can enter a different name.

```swift
@State private var username: String = ""
@FocusState private var usernameFieldIsFocused: Bool
@State private var showUsernameTaken = false

var body: some View {
    VStack {
        TextField("Choose a username.", text: $username)
            .focused($usernameFieldIsFocused)
        if showUsernameTaken {
            Text("That username is taken. Please choose another.")
        }
        Button("Submit") {
            showUsernameTaken = false
            if !isUserNameAvailable(username: username) {
                usernameFieldIsFocused = true
                showUsernameTaken = true
            }
        }
    }
}
```

To control focus by matching a value, use the [focused(_:equals:)](<focused(__equals_).md>) method instead.

## See Also

### Managing focus state

- [focused(_:equals:)](<focused(__equals_).md>) — Modifies this view by binding its focus state to the given state value.
- [isFocused](../environmentvalues/isfocused.md) — Returns whether the nearest focusable ancestor has focus.
- [FocusState](../focusstate.md) — A property wrapper type that can read and write a value that SwiftUI updates as the placement of focus within the scene changes.
- [FocusedValue](../focusedvalue.md) — A property wrapper for observing values from the focused view or one of its ancestors.
- [Entry()](<../entry().md>) — Creates an environment values, transaction, container values, or focused values entry.
- [FocusedValueKey](../focusedvaluekey.md) — A protocol for identifier types used when publishing and observing focused values.
- [FocusedBinding](../focusedbinding.md) — A convenience property wrapper for observing and automatically unwrapping state bindings from the focused view or one of its ancestors.
- [searchFocused(_:)](<searchfocused(__).md>) — Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [searchFocused(_:equals:)](<searchfocused(__equals_).md>) — Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.
