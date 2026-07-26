---
title: 'callAsFunction(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 12.0+, tvOS 14.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/resetfocusaction/callasfunction(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/resetfocusaction/callasfunction(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/resetfocusaction/callasfunction%28in%3A%29.json'
content_hash: 'sha256:2728f96d4ea909b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ResetFocusAction](../resetfocusaction.md)

# callAsFunction(in:)

<sub>Instance Method</sub>

Asks the focus sytem to reevaluate the default focus item.

<sub>macOS, tvOS, watchOS</sub>

```swift
func callAsFunction(in namespace: Namespace.ID)
```

## Parameters

- `namespace` — The namespace inside which SwiftUI should reevaluate default focus. The namespace should match the [focusScope(_:)](<../view/focusscope(__).md>) block where focus requires reevaluation.

## Discussion

The focus system reevaluates default focus when the currently-focused item is within the provided namespace.
