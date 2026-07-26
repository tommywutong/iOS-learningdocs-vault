---
title: ResetFocusAction
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 12.0+, tvOS 14.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/resetfocusaction
source_url: 'https://developer.apple.com/documentation/swiftui/resetfocusaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/resetfocusaction.json'
content_hash: 'sha256:90a3ec68e937169a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ResetFocusAction

<sub>Structure</sub>

An environment value that provides the ability to reevaluate default focus.

<sub>macOS, tvOS, watchOS</sub>

```swift
struct ResetFocusAction
```

## Overview

Get the [resetFocus](environmentvalues/resetfocus.md) environment value and call it as a function to force a default focus reevaluation at runtime.

```swift
@Namespace var mainNamespace
@Environment(\.resetFocus) var resetFocus

var body: some View {
    // ...
    resetFocus(in: mainNamespace)
    // ...
}
```

## Topics

### Calling the action

- [callAsFunction(in:)](<resetfocusaction/callasfunction(in_).md>) — Asks the focus sytem to reevaluate the default focus item.

## See Also

### Resetting focus

- [resetFocus](environmentvalues/resetfocus.md) — An action that requests the focus system to reevaluate default focus.
