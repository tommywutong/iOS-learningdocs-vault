---
title: Using Imported Protocol-Qualified Classes in Swift
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/using-imported-protocol-qualified-classes-in-swift
source_url: 'https://developer.apple.com/documentation/swift/using-imported-protocol-qualified-classes-in-swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/using-imported-protocol-qualified-classes-in-swift.json'
content_hash: 'sha256:f5f4308e250d48a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Imported C and Objective-C APIs](imported-c-and-objective-c-apis.md)

# Using Imported Protocol-Qualified Classes in Swift

<sub>Article</sub>

Learn how imported Objective-C protocol-qualified classes and metaclasses are represented.

## Overview

Objective-C classes qualified by one or more protocols, like the one in the example below, are imported by Swift as protocol composition types. The following Objective-C property refers to a view controller that also acts a data source and delegate:

```occ
@property UIViewController<UITableViewDataSource, UITableViewDelegate> * myController;
```

When you import it, here’s the Swift interface:

```swift
var myController: UIViewController & UITableViewDataSource & UITableViewDelegate
```

An Objective-C protocol-qualified metaclass is imported by Swift as a protocol metatype, which is a type that represents the type of a protocol itself. For example, given the following Objective-C method that performs an operation on the specified class:

```occ
- (void)doSomethingForClass:(Class<NSCoding>)codingClass;
```

When you import it, here’s the Swift interface:

```swift
func doSomething(for codingClass: NSCoding.Type)
```

## See Also

### Objective-C APIs

- [Using Imported Lightweight Generics in Swift](using-imported-lightweight-generics-in-swift.md) — Understand the constraints of imported Obj-C lightweight generic type declarations.
