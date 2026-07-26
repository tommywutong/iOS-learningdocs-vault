---
title: preflight()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/preflight()
source_url: 'https://developer.apple.com/documentation/foundation/bundle/preflight()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/preflight%28%29.json'
content_hash: 'sha256:3829eb12bf6955b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# preflight()

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the bundle’s executable code could be loaded successfully.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func preflight() throws
```

## Discussion

This method does not actually load the bundle’s executable code. Instead, it performs several checks to see if the code could be loaded and with one exception returns the same errors that would occur during an actual load operation. The one exception is the `NSExecutableLinkError` error, which requires the actual loading of the code to verify link errors.

For a list of possible load errors, see the discussion for the [- loadAndReturnError:](<loadandreturnerror().md>) method.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Loading code from a bundle

- [executableArchitectures](executablearchitectures.md) — An array of numbers indicating the architecture types supported by the bundle’s executable.
- [- load](<load().md>) — Dynamically loads the bundle’s executable code into a running program, if the code has not already been loaded.
- [- loadAndReturnError:](<loadandreturnerror().md>) — Loads the bundle’s executable code and returns any errors.
- [- unload](<unload().md>) — Unloads the code associated with the receiver.
- [loaded](isloaded.md) — The load status of a bundle.
- [Mach-O Architecture](../1495005-mach-o-architecture.md) — Constants that describe the CPU types that a bundle’s executable code supports.
