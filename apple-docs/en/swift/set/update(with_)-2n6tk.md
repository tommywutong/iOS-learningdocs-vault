---
title: 'update(with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/update(with:)-2n6tk'
source_url: 'https://developer.apple.com/documentation/swift/set/update(with:)-2n6tk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/update%28with%3A%29-2n6tk.json'
content_hash: 'sha256:f1c896bc582de9c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# update(with:)

<sub>Instance Method</sub>

Inserts the given element into the set unconditionally.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func update(with newMember: Element) -> Element?
```

## Parameters

- `newMember` — An element to insert into the set.

## Return Value

An element equal to `newMember` if the set already contained such a member; otherwise, `nil`. In some cases, the returned element may be distinguishable from `newMember` by identity comparison or some other means.

## Discussion

If an element equal to `newMember` is already contained in the set, `newMember` replaces the existing element. In this example, an existing element is inserted into `classDays`, a set of days of the week.

```swift
enum DayOfTheWeek: Int {
    case sunday, monday, tuesday, wednesday, thursday,
        friday, saturday
}

var classDays: Set<DayOfTheWeek> = [.monday, .wednesday, .friday]
print(classDays.update(with: .monday))
// Prints "Optional(DayOfTheWeek.monday)"
```

## See Also

### Adding Elements

- [insert(_:)](<insert(__)-nads.md>) — Inserts the given element in the set if it is not already present.
- [insert(_:)](<insert(__)-yar4.md>)
- [update(with:)](<update(with_)-7r2g.md>)
- [reserveCapacity(_:)](<reservecapacity(__).md>) — Reserves enough space to store the specified number of elements.
