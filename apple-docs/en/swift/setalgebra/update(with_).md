---
title: 'update(with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/update(with:)'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/update(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/update%28with%3A%29.json'
content_hash: 'sha256:735fa7f91d76e2a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# update(with:)

<sub>Instance Method</sub>

Inserts the given element into the set unconditionally.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func update(with newMember: Self.Element) -> Self.Element?
```

## Parameters

- `newMember` — An element to insert into the set.

## Return Value

For ordinary sets, an element equal to `newMember` if the set already contained such a member; otherwise, `nil`. In some cases, the returned element may be distinguishable from `newMember` by identity comparison or some other means.

For sets where the set type and element type are the same, like `OptionSet` types, this method returns any intersection between the set and `[newMember]`, or `nil` if the intersection is empty.

## Discussion

If an element equal to `newMember` is already contained in the set, `newMember` replaces the existing element. In this example, an existing element is inserted into `classDays`, a set of days of the week.

```swift
enum DayOfTheWeek: Int {
    case sunday, monday, tuesday, wednesday, thursday,
        friday, saturday
}

var classDays: Set<DayOfTheWeek> = [.monday, .wednesday, .friday]
print(classDays.update(with: .monday))
// Prints "Optional(.monday)"
```

## Default Implementations

### SetAlgebra Implementations

- [update(with:)](<update(with_)-2oa9l.md>) — Inserts the given element into the set.

## See Also

### Adding and Removing Elements

- [insert(_:)](<insert(__).md>) — Inserts the given element in the set if it is not already present.
- [remove(_:)](<remove(__).md>) — Removes the given element and any elements subsumed by the given element.
