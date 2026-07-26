---
title: requestAgeRange
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/requestagerange
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/requestagerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/requestagerange.json'
content_hash: 'sha256:8b1acb31b9e7c2af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# requestAgeRange

<sub>Instance Property</sub>

An action that presents a system interface to request a person’s age range.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var requestAgeRange: DeclaredAgeRangeAction { get }
```

## Discussion

Call this action from a [Button](../button.md) or [onAppear(perform:)](<../view/onappear(perform_).md>) to ask people to share their age range with your app.
