---
title: 'transaction(value:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/transaction(value:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/transaction(value:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/transaction%28value%3A_%3A%29.json'
content_hash: 'sha256:703f11ba5a69596e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# transaction(value:_:)

<sub>Instance Method</sub>

Applies the given transaction mutation function to all animations used within the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func transaction(value: some Equatable, _ transform: @escaping (inout Transaction) -> Void) -> some View

```

## Parameters

- `value` — A value to monitor for changes.

- `transform` — The transformation to apply to transactions within this view.

## Return Value

A view that wraps this view and applies a transformation to all transactions used within the view whenever `value` changes.

## Discussion

Use this modifier to change or replace the animation used in a view. Consider three identical views controlled by a button that changes all three simultaneously:

- The first view animates rotating the “Rotation” [Text](../text.md) view by 360 degrees.
- The second uses the `transaction(_:)` modifier to change the animation by adding a delay to the start of the animation by two seconds and then increases the rotational speed of the “Rotation\\nModified” [Text](../text.md) view animation by a factor of 2.
- The third uses the `transaction(_:)` modifier to disable animations affecting the “Animation\\nReplaced” [Text](../text.md) view.

The following code implements these animations:

```swift
struct TransactionExample: View {
    @State var flag = false

    var body: some View {
        VStack(spacing: 50) {
            HStack(spacing: 30) {
                Text("Rotation")
                    .rotationEffect(Angle(degrees: flag ? 360 : 0))

                Text("Rotation\nModified")
                    .rotationEffect(Angle(degrees: flag ? 360 : 0))
                    .transaction(value: flag) { t in
                        t.animation =
                            t.animation?.delay(2.0).speed(2)
                    }

                Text("Animation\nReplaced")
                    .rotationEffect(Angle(degrees: flag ? 360 : 0))
                    .transaction(value: flag) { t in
                        t.disableAnimations = true
                    }
            }

            Button("Animate") {
                withAnimation(.easeIn(duration: 2.0)) {
                    flag.toggle()
                }
            }
        }
    }
}
```

## See Also

### Moving an animation to another view

- [withTransaction(_:_:)](<../withtransaction(____).md>) — Executes a closure with the specified transaction and returns the result.
- [withTransaction(_:_:_:)](<../withtransaction(______).md>) — Executes a closure with the specified transaction key path and value and returns the result.
- [transaction(_:)](<transaction(__).md>) — Applies the given transaction mutation function to all animations used within the view.
- [transaction(_:body:)](<transaction(__body_).md>) — Applies the given transaction mutation function to all animations used within the `body` closure.
- [Transaction](../transaction.md) — The context of the current state-processing update.
- [Entry()](<../entry().md>) — Creates an environment values, transaction, container values, or focused values entry.
- [TransactionKey](../transactionkey.md) — A key for accessing values in a transaction.
