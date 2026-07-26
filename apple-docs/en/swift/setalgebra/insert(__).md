---
title: 'insert(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/setalgebra/insert(_:)'
source_url: 'https://developer.apple.com/documentation/swift/setalgebra/insert(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra/insert%28_%3A%29.json'
content_hash: 'sha256:3901ac649b6fb0c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SetAlgebra](../setalgebra.md)

# insert(_:)

<sub>Instance Method</sub>

Inserts the given element in the set if it is not already present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func insert(_ newMember: Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)
```

## Parameters

- `newMember` — An element to insert into the set.

## Return Value

`(true, newMember)` if `newMember` was not contained in the set. If an element equal to `newMember` was already contained in the set, the method returns `(false, oldMember)`, where `oldMember` is the element that was equal to `newMember`. In some cases, `oldMember` may be distinguishable from `newMember` by identity comparison or some other means.

## Discussion

If an element equal to `newMember` is already contained in the set, this method has no effect. In this example, a new element is inserted into `classDays`, a set of days of the week. When an existing element is inserted, the `classDays` set does not change.

```swift
enum DayOfTheWeek: Int {
    case sunday, monday, tuesday, wednesday, thursday,
        friday, saturday
}

var classDays: Set<DayOfTheWeek> = [.wednesday, .friday]
print(classDays.insert(.monday))
// Prints "(true, .monday)"
print(classDays)
// Prints "[.friday, .wednesday, .monday]"

print(classDays.insert(.friday))
// Prints "(false, .friday)"
print(classDays)
// Prints "[.friday, .wednesday, .monday]"
```

## Default Implementations

### SetAlgebra Implementations

- [insert(_:)](<insert(__)-1uo97.md>)
- [insert(_:)](<insert(__)-9wohp.md>) — Adds the given element to the option set if it is not already a member.

## See Also

### Adding and Removing Elements

- [update(with:)](<update(with_).md>) — Inserts the given element into the set unconditionally.
- [remove(_:)](<remove(__).md>) — Removes the given element and any elements subsumed by the given element.
