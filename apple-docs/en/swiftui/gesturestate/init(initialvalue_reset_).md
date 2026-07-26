---
title: 'init(initialValue:reset:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/gesturestate/init(initialvalue:reset:)'
source_url: 'https://developer.apple.com/documentation/swiftui/gesturestate/init(initialvalue:reset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesturestate/init%28initialvalue%3Areset%3A%29.json'
content_hash: 'sha256:8c516b098abf0d26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GestureState](../gesturestate.md)

# init(initialValue:reset:)

<sub>Initializer</sub>

Creates a view state that’s derived from a gesture with an initial state value and a closure that provides a transaction to reset it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) init(initialValue: Value, reset: @escaping (Value, inout Transaction) -> Void)
```

## Parameters

- `initialValue` — An initial state value.

- `reset` — A closure that provides a [Transaction](../transaction.md).

## See Also

### Creating a gesture state

- [init(initialValue:)](<init(initialvalue_).md>) — Creates a view state that’s derived from a gesture with an initial value.
- [init(initialValue:resetTransaction:)](<init(initialvalue_resettransaction_).md>) — Creates a view state that’s derived from a gesture with an initial state value and a transaction to reset it.
- [init(reset:)](<init(reset_).md>) — Creates a view state that’s derived from a gesture with a closure that provides a transaction to reset it.
- [init(resetTransaction:)](<init(resettransaction_).md>) — Creates a view state that’s derived from a gesture with a transaction to reset it.
- [init(wrappedValue:)](<init(wrappedvalue_).md>) — Creates a view state that’s derived from a gesture.
- [init(wrappedValue:reset:)](<init(wrappedvalue_reset_).md>) — Creates a view state that’s derived from a gesture with a wrapped state value and a closure that provides a transaction to reset it.
- [init(wrappedValue:resetTransaction:)](<init(wrappedvalue_resettransaction_).md>) — Creates a view state that’s derived from a gesture with a wrapped state value and a transaction to reset it.
