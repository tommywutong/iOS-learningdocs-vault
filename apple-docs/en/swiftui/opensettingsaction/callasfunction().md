---
title: callAsFunction()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/opensettingsaction/callasfunction()
source_url: 'https://developer.apple.com/documentation/swiftui/opensettingsaction/callasfunction()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/opensettingsaction/callasfunction%28%29.json'
content_hash: 'sha256:0b3736c66810ba1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [OpenSettingsAction](../opensettingsaction.md)

# callAsFunction()

<sub>Instance Method</sub>

Opens the window associated to the [Settings](../settings.md) scene defined by this app, if one exists.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func callAsFunction()
```

## Discussion

Calling this action when the window is already open will order it to the front.

Don’t call this method directly. SwiftUI calls it when you call the [openSettings](../environmentvalues/opensettings.md) action:

```swift
openSettings()
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in _The Swift Programming Language_.
