---
title: 'insert(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/insert(_:)-nads'
source_url: 'https://developer.apple.com/documentation/swift/set/insert(_:)-nads'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/insert%28_%3A%29-nads.json'
content_hash: 'sha256:c75c933590a090ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# insert(_:)

<sub>Instance Method</sub>

Inserts the given element in the set if it is not already present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func insert(_ newMember: Element) -> (inserted: Bool, memberAfterInsert: Element)
```

## Parameters

- `newMember` — An element to insert into the set.

## Return Value

`(true, newMember)` if `newMember` was not contained in the set. If an element equal to `newMember` was already contained in the set, the method returns `(false, oldMember)`, where `oldMember` is the element that was equal to `newMember`. In some cases, `oldMember` may be distinguishable from `newMember` by identity comparison or some other means.

## Discussion

If an element equal to `newMember` is already contained in the set, this method has no effect. In the following example, a new element is inserted into `classDays`, a set of days of the week. When an existing element is inserted, the `classDays` set does not change.

```swift
enum DayOfTheWeek: Int {
    case sunday, monday, tuesday, wednesday, thursday,
        friday, saturday
}

var classDays: Set<DayOfTheWeek> = [.wednesday, .friday]
print(classDays.insert(.monday))
// Prints "(inserted: true, memberAfterInsert: DayOfTheWeek.monday)"
print(classDays)
// Prints "[DayOfTheWeek.friday, DayOfTheWeek.wednesday, DayOfTheWeek.monday]"

print(classDays.insert(.friday))
// Prints "(inserted: false, memberAfterInsert: DayOfTheWeek.friday)"
print(classDays)
// Prints "[DayOfTheWeek.friday, DayOfTheWeek.wednesday, DayOfTheWeek.monday]"
```

## See Also

### Adding Elements

- [insert(_:)](<insert(__)-yar4.md>)
- [update(with:)](<update(with_)-2n6tk.md>) — Inserts the given element into the set unconditionally.
- [update(with:)](<update(with_)-7r2g.md>)
- [reserveCapacity(_:)](<reservecapacity(__).md>) — Reserves enough space to store the specified number of elements.
