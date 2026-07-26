---
title: 'externalMacro(module:type:)'
framework: Swift
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/externalmacro(module:type:)'
source_url: 'https://developer.apple.com/documentation/swift/externalmacro(module:type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/externalmacro%28module%3Atype%3A%29.json'
content_hash: 'sha256:ff5190368ff64fdd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# externalMacro(module:type:)

<sub>Macro</sub>

Specifies the module and type name for a macro’s implementation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@freestanding(expression) macro externalMacro<T>(module: String, type: String) -> T
```

## Parameters

- `module` — The module name.

- `type` — The type that implements the macro.

## Return Value

The macro’s implementation.

## Overview

This macro can only be used to define a macro; using it in any other context is an error. The specified type must conform to the protocols that correspond to the roles of the macro being declared. For example:

```swift
macro stringify(_ value: T) -> (T, String) =
    #externalMacro(module: "ExampleMacros", type: "StringifyMacro")
```
