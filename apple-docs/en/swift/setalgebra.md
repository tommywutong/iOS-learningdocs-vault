---
title: SetAlgebra
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/setalgebra
source_url: 'https://developer.apple.com/documentation/swift/setalgebra'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/setalgebra.json'
content_hash: 'sha256:d3c5c20e21ba9cbc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# SetAlgebra

<sub>Protocol</sub>

A type that provides mathematical set operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol SetAlgebra<Element> : Equatable, ExpressibleByArrayLiteral
```

## Overview

You use types that conform to the `SetAlgebra` protocol when you need efficient membership tests or mathematical set operations such as intersection, union, and subtraction. In the standard library, you can use the `Set` type with elements of any hashable type, or you can easily create bit masks with `SetAlgebra` conformance using the `OptionSet` protocol. See those types for more information.

> [!note] Note
> Unlike ordinary set types, the `Element` type of an `OptionSet` is identical to the `OptionSet` type itself. The `SetAlgebra` protocol is specifically designed to accommodate both kinds of set.

## Conforming to the SetAlgebra Protocol

When implementing a custom type that conforms to the `SetAlgebra` protocol, you must implement the required initializers and methods. For the inherited methods to work properly, conforming types must meet the following axioms. Assume that `S` is a custom type that conforms to the `SetAlgebra` protocol, `x` and `y` are instances of `S`, and `e` is of type `S.Element`—the type that the set holds.

- `S() == []`
- `x.intersection(x) == x`
- `x.intersection([]) == []`
- `x.union(x) == x`
- `x.union([]) == x`
- `x.contains(e)` implies `x.union(y).contains(e)`
- `x.union(y).contains(e)` implies `x.contains(e) || y.contains(e)`
- `x.contains(e) && y.contains(e)` if and only if `x.intersection(y).contains(e)`
- `x.isSubset(of: y)` implies `x.union(y) == y`
- `x.isSuperset(of: y)` implies `x.union(y) == x`
- `x.isSubset(of: y)` if and only if `y.isSuperset(of: x)`
- `x.isStrictSuperset(of: y)` if and only if `x.isSuperset(of: y) && x != y`
- `x.isStrictSubset(of: y)` if and only if `x.isSubset(of: y) && x != y`

## Relationships

- **Inherits From**: [Equatable](equatable.md), [ExpressibleByArrayLiteral](expressiblebyarrayliteral.md)

- **Inherited By**: [OptionSet](optionset.md)

- **Conforming Types**: [Options](../observation/observationtracking/options.md), [Set](set.md)

## Topics

### Creating a Set

- [init()](<setalgebra/init().md>) — Creates an empty set.

### Testing for Membership

- [contains(_:)](<setalgebra/contains(__).md>) — Returns a Boolean value that indicates whether the given element exists in the set.
- [Element](setalgebra/element.md) — A type for which the conforming type provides a containment test.

### Adding and Removing Elements

- [insert(_:)](<setalgebra/insert(__).md>) — Inserts the given element in the set if it is not already present.
- [update(with:)](<setalgebra/update(with_).md>) — Inserts the given element into the set unconditionally.
- [remove(_:)](<setalgebra/remove(__).md>) — Removes the given element and any elements subsumed by the given element.

### Combining Sets

- [union(_:)](<setalgebra/union(__).md>) — Returns a new set with the elements of both this and the given set.
- [formUnion(_:)](<setalgebra/formunion(__).md>) — Adds the elements of the given set to the set.
- [intersection(_:)](<setalgebra/intersection(__).md>) — Returns a new set with the elements that are common to both this set and the given set.
- [formIntersection(_:)](<setalgebra/formintersection(__).md>) — Removes the elements of this set that aren’t also in the given set.
- [symmetricDifference(_:)](<setalgebra/symmetricdifference(__).md>) — Returns a new set with the elements that are either in this set or in the given set, but not in both.
- [formSymmetricDifference(_:)](<setalgebra/formsymmetricdifference(__).md>) — Removes the elements of the set that are also in the given set and adds the members of the given set that are not already in the set.

### Comparing Sets

- [isStrictSubset(of:)](<setalgebra/isstrictsubset(of_).md>) — Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [isStrictSuperset(of:)](<setalgebra/isstrictsuperset(of_).md>) — Returns a Boolean value that indicates whether this set is a strict superset of the given set.

### Initializers

- [init(_:)](<setalgebra/init(__).md>) — Creates a new set from a finite sequence of items.

### Instance Properties

- [isEmpty](setalgebra/isempty.md) — A Boolean value that indicates whether the set has no elements.

### Instance Methods

- [isDisjoint(with:)](<setalgebra/isdisjoint(with_).md>) — Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [isSubset(of:)](<setalgebra/issubset(of_).md>) — Returns a Boolean value that indicates whether the set is a subset of another set.
- [isSuperset(of:)](<setalgebra/issuperset(of_).md>) — Returns a Boolean value that indicates whether the set is a superset of the given set.
- [subtract(_:)](<setalgebra/subtract(__).md>) — Removes the elements of the given set from this set.
- [subtracting(_:)](<setalgebra/subtracting(__).md>) — Returns a new set containing the elements of this set that do not occur in the given set.
