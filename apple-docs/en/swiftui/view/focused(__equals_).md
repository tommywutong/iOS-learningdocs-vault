---
title: 'focused(_:equals:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/focused(_:equals:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/focused(_:equals:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/focused%28_%3Aequals%3A%29.json'
content_hash: 'sha256:0433475d3a4c33e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# focused(_:equals:)

<sub>Instance Method</sub>

Modifies this view by binding its focus state to the given state value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func focused<Value>(_ binding: FocusState<Value>.Binding, equals value: Value) -> some View where Value : Hashable

```

## Parameters

- `binding` — The state binding to register. When focus moves to the modified view, the binding sets the bound value to the corresponding match value. If a caller sets the state value programmatically to the matching value, then focus moves to the modified view. When focus leaves the modified view, the binding sets the bound value to `nil`. If a caller sets the value to `nil`, SwiftUI automatically dismisses focus.

- `value` — The value to match against when determining whether the binding should change.

## Return Value

The modified view.

## Discussion

Use this modifier to cause the view to receive focus whenever the `binding` equals the `value`. Typically, you create an enumeration of fields that may receive focus, bind an instance of this enumeration, and assign its cases to focusable views.

The following example uses the cases of a `LoginForm` enumeration to bind the focus state of two [TextField](../textfield.md) views. A sign-in button validates the fields and sets the bound `focusedField` value to any field that requires the user to correct a problem.

```swift
struct LoginForm {
    enum Field: Hashable {
        case usernameField
        case passwordField
    }

    @State private var username = ""
    @State private var password = ""
    @FocusState private var focusedField: Field?

    var body: some View {
        Form {
            TextField("Username", text: $username)
                .focused($focusedField, equals: .usernameField)

            SecureField("Password", text: $password)
                .focused($focusedField, equals: .passwordField)

            Button("Sign In") {
                if username.isEmpty {
                    focusedField = .usernameField
                } else if password.isEmpty {
                    focusedField = .passwordField
                } else {
                    handleLogin(username, password)
                }
            }
        }
    }
}
```

To control focus using a Boolean, use the [focused(_:)](<focused(__).md>) method instead.

## See Also

### Managing focus state

- [focused(_:)](<focused(__).md>) — Modifies this view by binding its focus state to the given Boolean state value.
- [isFocused](../environmentvalues/isfocused.md) — Returns whether the nearest focusable ancestor has focus.
- [FocusState](../focusstate.md) — A property wrapper type that can read and write a value that SwiftUI updates as the placement of focus within the scene changes.
- [FocusedValue](../focusedvalue.md) — A property wrapper for observing values from the focused view or one of its ancestors.
- [Entry()](<../entry().md>) — Creates an environment values, transaction, container values, or focused values entry.
- [FocusedValueKey](../focusedvaluekey.md) — A protocol for identifier types used when publishing and observing focused values.
- [FocusedBinding](../focusedbinding.md) — A convenience property wrapper for observing and automatically unwrapping state bindings from the focused view or one of its ancestors.
- [searchFocused(_:)](<searchfocused(__).md>) — Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [searchFocused(_:equals:)](<searchfocused(__equals_).md>) — Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.
