---
title: 'subscript(dynamicMember:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Type Subscript
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shaderlibrary/subscript(dynamicmember:)-swift.type.subscript'
source_url: 'https://developer.apple.com/documentation/swiftui/shaderlibrary/subscript(dynamicmember:)-swift.type.subscript'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shaderlibrary/subscript%28dynamicmember%3A%29-swift.type.subscript.json'
content_hash: 'sha256:6d700d98124d6442'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShaderLibrary](../shaderlibrary.md)

# subscript(dynamicMember:)

<sub>Type Subscript</sub>

Returns a new shader function representing the stitchable MSL function called `name` in the default shader library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static subscript(dynamicMember name: String) -> ShaderFunction { get }
```

## Overview

Typically this subscript is used implicitly via the dynamic member syntax, for example:

let fn = ShaderLibrary.myFunction

which creates a reference to the MSL function called `myFunction()`.
