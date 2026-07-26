---
title: Swift
framework: Swift
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift
source_url: 'https://developer.apple.com/documentation/swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift.json'
content_hash: 'sha256:e6f1017a48a98856'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Swift

<sub>Framework</sub>

Build apps using a powerful open language.

## Overview

Swift includes modern features like type inference, optionals, and closures, which make the syntax concise yet expressive. Swift ensures your code is fast and efficient, while its memory safety and native error handling make the language safe by design. Writing Swift code is interactive and fun in Swift Playgrounds, playgrounds in Xcode, and REPL.

```swift
var interestingNumbers = [
    "primes": [2, 3, 5, 7, 11, 13, 17],
    "triangular": [1, 3, 6, 10, 15, 21, 28],
    "hexagonal": [1, 6, 15, 28, 45, 66, 91]
]

for key in interestingNumbers.keys {
    interestingNumbers[key]?.sort(by: >)
}

print(interestingNumbers["primes"]!)
// Prints "[17, 13, 11, 7, 5, 3, 2]"
```

### Learn Swift

If you’re new to Swift, read [The Swift Programming Language](https://docs.swift.org/swift-book/) for a quick tour, a comprehensive language guide, and a full reference manual. If you’re new to programming, check out [Swift Playgrounds](https://www.apple.com/swift/playgrounds/) on iPad.

Swift is developed in the open. To learn more about the open source Swift project and community, visit [Swift.org](https://swift.org).

## Topics

### Essentials

- [Swift updates](updates/swift.md) — Learn about important changes to Swift.
- [Adopting strict concurrency in Swift 6 apps](swift/adoptingswift6.md) — Enable strict concurrency checking to find data races at compile time.

### Standard Library

- [Int](swift/int.md) — A signed integer value type.
- [Double](swift/double.md) — A double-precision (64-bit), floating-point value type.
- [String](swift/string.md) — A Unicode string value that is a collection of characters.
- [Array](swift/array.md) — An ordered, random-access collection.
- [Dictionary](swift/dictionary.md) — A collection whose elements are key-value pairs.
- [Swift Standard Library](swift/swift-standard-library.md) — Solve complex problems and write high-performance, readable code.

### Observation

- [Observation](observation.md) — Make responsive apps that update the presentation when underlying data changes.

### Distributed Actors

- [Distributed](distributed.md) — Build systems that run distributed code across multiple processes and devices.

### Regular Expression DSL

- [RegexBuilder](regexbuilder.md) — Use an expressive domain-specific language to build regular expressions, for operations like searching and replacing in text.

### Low-Level Atomic Operations

- [Synchronization](synchronization.md) — Build synchronization constructs using low-level, primitive operations.

### Data Modeling

- [Choosing Between Structures and Classes](swift/choosing-between-structures-and-classes.md) — Decide how to store data and model behavior.
- [Adopting Common Protocols](swift/adopting-common-protocols.md) — Make your custom types easier to use by ensuring that they conform to Swift protocols.

### Data Flow and Control Flow

- [Maintaining State in Your Apps](swift/maintaining-state-in-your-apps.md) — Use enumerations to capture and track the state of your app.
- [Preventing Timing Problems When Using Closures](swift/preventing-timing-problems-when-using-closures.md) — Understand how different API calls to your closures can affect your app.

### Language Interoperability with Objective-C and C

- [Objective-C and C Code Customization](swift/objective-c-and-c-code-customization.md) — Apply macros to your Objective-C APIs to customize how they’re imported into Swift.
- [Migrating Your Objective-C Code to Swift](swift/migrating-your-objective-c-code-to-swift.md) — Learn the recommended steps to migrate your code.
- [Cocoa Design Patterns](swift/cocoa-design-patterns.md) — Adopt and interoperate with Cocoa design patterns in your Swift apps.
- [Handling Dynamically Typed Methods and Objects in Swift](swift/handling-dynamically-typed-methods-and-objects-in-swift.md) — Cast instances of the Objective-C `id` type to a specific Swift type.
- [Using Objective-C Runtime Features in Swift](swift/using-objective-c-runtime-features-in-swift.md) — Use selectors and key paths to interact with dynamic Objective-C APIs.
- [Imported C and Objective-C APIs](swift/imported-c-and-objective-c-apis.md) — Use native Swift syntax to interoperate with types and functions in C and Objective-C.
- [Calling Objective-C APIs Asynchronously](swift/calling-objective-c-apis-asynchronously.md) — Learn how functions and methods that take a completion handler are converted to Swift asynchronous functions.

### Language Interoperability with C++

- [Mixing Languages in an Xcode project](swift/mixinglanguagesinanxcodeproject.md) — Use C++ APIs in Swift – and Swift APIs in C++ – in a single framework target, and consume the framework’s APIs in a separate app target.
- [Calling APIs Across Language Boundaries](swift/callingapisacrosslanguageboundaries.md) — Use a variety of C++ APIs in Swift – and vice-versa – across multiple targets and frameworks in an Xcode project.
