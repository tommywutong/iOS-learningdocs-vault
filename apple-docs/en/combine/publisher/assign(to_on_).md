---
title: 'assign(to:on:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/assign(to:on:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/assign(to:on:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/assign%28to%3Aon%3A%29.json'
content_hash: 'sha256:12e2572124492cd6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# assign(to:on:)

<sub>Instance Method</sub>

Assigns each element from a publisher to a property on an object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func assign<Root>(to keyPath: ReferenceWritableKeyPath<Root, Self.Output>, on object: Root) -> AnyCancellable
```

## Parameters

- `keyPath` — A key path that indicates the property to assign. See [Key-Path Expression](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/Expressions.html#//apple_ref/doc/uid/TP40014097-CH32-ID563) in _The Swift Programming Language_ to learn how to use key paths to specify a property of an object.

- `object` — The object that contains the property. The subscriber assigns the object’s property every time it receives a new value.

## Return Value

An [AnyCancellable](../anycancellable.md) instance. Call [cancel()](<../cancellable/cancel().md>) on this instance when you no longer want the publisher to automatically assign the property. Deinitializing this instance will also cancel automatic assignment.

## Discussion

Use the [assign(to:on:)](<assign(to_on_).md>) subscriber when you want to set a given property each time a publisher produces a value.

In this example, the [assign(to:on:)](<assign(to_on_).md>) sets the value of the `anInt` property on an instance of `MyClass`:

```swift
class MyClass {
    var anInt: Int = 0 {
        didSet {
            print("anInt was set to: \(anInt)", terminator: "; ")
        }
    }
}

var myObject = MyClass()
let myRange = (0...2)
cancellable = myRange.publisher
    .assign(to: \.anInt, on: myObject)

// Prints: "anInt was set to: 0; anInt was set to: 1; anInt was set to: 2"
```

> [!important] Important
> The [Assign](../subscribers/assign.md) instance created by this operator maintains a strong reference to `object`, and sets it to `nil` when the upstream publisher completes (either normally or with an error).

## See Also

### Connecting simple subscribers

- [assign(to:)](<assign(to_).md>) — Republishes elements received from a publisher, by assigning them to a property marked as a publisher.
- [sink(receiveCompletion:receiveValue:)](<sink(receivecompletion_receivevalue_).md>) — Attaches a subscriber with closure-based behavior.
- [sink(receiveValue:)](<sink(receivevalue_).md>) — Attaches a subscriber with closure-based behavior to a publisher that never fails.
