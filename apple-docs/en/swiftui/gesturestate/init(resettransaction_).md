---
title: 'init(resetTransaction:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/gesturestate/init(resettransaction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/gesturestate/init(resettransaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesturestate/init%28resettransaction%3A%29.json'
content_hash: 'sha256:78fa63d8f055a969'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GestureState](../gesturestate.md)

# init(resetTransaction:)

<sub>Initializer</sub>

Creates a view state that’s derived from a gesture with a transaction to reset it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(resetTransaction: Transaction = Transaction())
```

## Parameters

- `resetTransaction` — A transaction that provides metadata for view updates.

## See Also

### Creating a gesture state

- [init(initialValue:)](<init(initialvalue_).md>) — Creates a view state that’s derived from a gesture with an initial value.
- [init(initialValue:reset:)](<init(initialvalue_reset_).md>) — Creates a view state that’s derived from a gesture with an initial state value and a closure that provides a transaction to reset it.
- [init(initialValue:resetTransaction:)](<init(initialvalue_resettransaction_).md>) — Creates a view state that’s derived from a gesture with an initial state value and a transaction to reset it.
- [init(reset:)](<init(reset_).md>) — Creates a view state that’s derived from a gesture with a closure that provides a transaction to reset it.
- [init(wrappedValue:)](<init(wrappedvalue_).md>) — Creates a view state that’s derived from a gesture.
- [init(wrappedValue:reset:)](<init(wrappedvalue_reset_).md>) — Creates a view state that’s derived from a gesture with a wrapped state value and a closure that provides a transaction to reset it.
- [init(wrappedValue:resetTransaction:)](<init(wrappedvalue_resettransaction_).md>) — Creates a view state that’s derived from a gesture with a wrapped state value and a transaction to reset it.
