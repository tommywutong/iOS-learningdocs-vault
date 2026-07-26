---
title: Mirror
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/mirror
source_url: 'https://developer.apple.com/documentation/swift/mirror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mirror.json'
content_hash: 'sha256:fc2d86611102f7ed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Mirror

<sub>Structure</sub>

A representation of the substructure and display style of an instance of any type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Mirror
```

## Overview

A mirror describes the parts that make up a particular instance, such as the instance’s stored properties, collection or tuple elements, or its active enumeration case. Mirrors also provide a “display style” property that suggests how this mirror might be rendered.

Playgrounds and the debugger use the `Mirror` type to display representations of values of any type. For example, when you pass an instance to the `dump(_:_:_:_:)` function, a mirror is used to render that instance’s runtime contents.

```swift
struct Point {
    let x: Int, y: Int
}

let p = Point(x: 21, y: 30)
print(String(reflecting: p))
// Prints "▿ Point
//           - x: 21
//           - y: 30"
```

To customize the mirror representation of a custom type, add conformance to the `CustomReflectable` protocol.

## Relationships

- **Conforms To**: [Copyable](copyable.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [Escapable](escapable.md)

## Topics

### Querying Descendants

- [descendant(_:_:)](<mirror/descendant(____).md>) — Returns a specific descendant of the reflected subject, or `nil` if no such descendant exists.
- [MirrorPath](mirrorpath.md) — A protocol for legitimate arguments to `Mirror`’s `descendant` method.

### Initializers

- [init(_:children:displayStyle:ancestorRepresentation:)](<mirror/init(__children_displaystyle_ancestorrepresentation_)-34d91.md>) — Creates a mirror representing the given subject using a dictionary literal for the structure.
- [init(_:children:displayStyle:ancestorRepresentation:)](<mirror/init(__children_displaystyle_ancestorrepresentation_)-4af97.md>) — Creates a mirror representing the given subject with a specified structure.
- [init(_:unlabeledChildren:displayStyle:ancestorRepresentation:)](<mirror/init(__unlabeledchildren_displaystyle_ancestorrepresentation_).md>) — Creates a mirror representing the given subject with unlabeled children.
- [init(reflecting:)](<mirror/init(reflecting_).md>) — Creates a mirror that reflects on the given instance.
- [init(reflectingForTest:)](<mirror/init(reflectingfortest_)-5t8yc.md>) — Initialize this instance so that it can be presented in a test’s output.
- [init(reflectingForTest:)](<mirror/init(reflectingfortest_)-6nh7d.md>) — Initialize this instance so that it can be presented in a test’s output.

### Instance Properties

- [children](mirror/children-swift.property.md) — A collection of `Child` elements describing the structure of the reflected subject.
- [displayStyle](mirror/displaystyle-swift.property.md) — A suggested display style for the reflected subject.
- [subjectType](mirror/subjecttype.md) — The static type of the subject being reflected.
- [superclassMirror](mirror/superclassmirror.md) — A mirror of the subject’s superclass, if one exists.

### Type Aliases

- [Child](mirror/child.md) — An element of the reflected instance’s structure.
- [Children](mirror/children-swift.typealias.md) — The type used to represent substructure.

### Enumerations

- [AncestorRepresentation](mirror/ancestorrepresentation.md) — The representation to use for ancestor classes.
- [DisplayStyle](mirror/displaystyle-swift.enum.md) — A suggestion of how a mirror’s subject is to be interpreted.

### Default Implementations

- [CustomReflectable Implementations](mirror/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](mirror/customstringconvertible-implementations.md)

## See Also

### Querying Runtime Values

- [ObjectIdentifier](objectidentifier.md) — A unique identifier for a class instance, actor instance, or metatype.
- [type(of:)](<type(of_).md>) — Returns the dynamic type of a value.
