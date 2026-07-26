---
title: Entry()
framework: SwiftUI
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/entry()
source_url: 'https://developer.apple.com/documentation/swiftui/entry()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/entry%28%29.json'
content_hash: 'sha256:dedc2a052e6bbe2b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Entry()

<sub>Macro</sub>

Creates an environment values, transaction, container values, or focused values entry.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@attached(accessor) @attached(peer, names: prefixed(__Key_)) macro Entry()
```

## Environment Values

Create [EnvironmentValues](environmentvalues.md) entries by extending the [EnvironmentValues](environmentvalues.md) structure with new properties and attaching the @Entry macro to the variable declarations:

```swift
extension EnvironmentValues {
    @Entry var myCustomValue: String = "Default value"
    @Entry var anotherCustomValue = true
}
```

## Transaction Values

Create [Transaction](transaction.md) entries by extending the [Transaction](transaction.md) structure with new properties and attaching the @Entry macro to the variable declarations:

```swift
extension Transaction {
    @Entry var myCustomValue: String = "Default value"
}
```

## Container Values

Create [ContainerValues](containervalues.md) entries by extending the [ContainerValues](containervalues.md) structure with new properties and attaching the @Entry macro to the variable declarations:

```swift
extension ContainerValues {
    @Entry var myCustomValue: String = "Default value"
}
```

## Focused Values

Since the default value for [FocusedValues](focusedvalues.md) is always `nil`, [FocusedValues](focusedvalues.md) entries cannot specify a different default value and must have an Optional type.

Create [FocusedValues](focusedvalues.md) entries by extending the [FocusedValues](focusedvalues.md) structure with new properties and attaching the @Entry macro to the variable declarations:

```swift
extension FocusedValues {
    @Entry var myCustomValue: String?
}
```

## See Also

### Moving an animation to another view

- [withTransaction(_:_:)](<withtransaction(____).md>) — Executes a closure with the specified transaction and returns the result.
- [withTransaction(_:_:_:)](<withtransaction(______).md>) — Executes a closure with the specified transaction key path and value and returns the result.
- [transaction(_:)](<view/transaction(__).md>) — Applies the given transaction mutation function to all animations used within the view.
- [transaction(value:_:)](<view/transaction(value___).md>) — Applies the given transaction mutation function to all animations used within the view.
- [transaction(_:body:)](<view/transaction(__body_).md>) — Applies the given transaction mutation function to all animations used within the `body` closure.
- [Transaction](transaction.md) — The context of the current state-processing update.
- [TransactionKey](transactionkey.md) — A key for accessing values in a transaction.
