---
title: 'init(types:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdatadetector/init(types:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdatadetector/init(types:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdatadetector/init%28types%3A%29.json'
content_hash: 'sha256:c0ffe5c5890d2d25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDataDetector](../nsdatadetector.md)

# init(types:)

<sub>Initializer</sub>

Initializes and returns a data detector instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(types checkingTypes: NSTextCheckingTypes) throws
```

## Parameters

- `checkingTypes` — The checking types. The supported checking types are a subset of the types [CheckingType](../nstextcheckingresult/checkingtype.md). Those constants can be combined using the C-bitwise OR operator.

## Return Value

Returns the newly initialized data detector. If an error was encountered returns `nil`, and `error` contains the error.

## Discussion

Currently, the supported data detectors `checkingTypes` are:  [NSTextCheckingTypeDate](../nstextcheckingresult/checkingtype/date.md), [NSTextCheckingTypeAddress](../nstextcheckingresult/checkingtype/address.md), [NSTextCheckingTypeLink](../nstextcheckingresult/checkingtype/link.md), `NSTextCheckingTypePhoneNumber`, and `NSTextCheckingTypeTransitInformation`.

> [!note] Handling Errors in Swift
> In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Related Documentation

- [checkingTypes](checkingtypes.md) — Returns the checking types for the data detector.
