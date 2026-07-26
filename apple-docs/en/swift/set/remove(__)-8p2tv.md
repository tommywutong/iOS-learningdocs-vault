---
title: 'remove(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/remove(_:)-8p2tv'
source_url: 'https://developer.apple.com/documentation/swift/set/remove(_:)-8p2tv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/remove%28_%3A%29-8p2tv.json'
content_hash: 'sha256:10ce8162a203ddba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# remove(_:)

<sub>Instance Method</sub>

Removes the specified element from the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func remove(_ member: Element) -> Element?
```

## Parameters

- `member` — The element to remove from the set.

## Return Value

The value of the `member` parameter if it was a member of the set; otherwise, `nil`.

## Discussion

This example removes the element `"sugar"` from a set of ingredients.

```swift
var ingredients: Set = ["cocoa beans", "sugar", "cocoa butter", "salt"]
let toRemove = "sugar"
if let removed = ingredients.remove(toRemove) {
    print("The recipe is now \(removed)-free.")
}
// Prints "The recipe is now sugar-free."
```

## See Also

### Removing Elements

- [filter(_:)](<filter(__).md>) — Returns a new set containing the elements of the set that satisfy the given predicate.
- [remove(_:)](<remove(__)-4d3i1.md>)
- [removeFirst()](<removefirst().md>) — Removes the first element of the set.
- [remove(at:)](<remove(at_).md>) — Removes the element at the given index of the set.
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — Removes all members from the set.
