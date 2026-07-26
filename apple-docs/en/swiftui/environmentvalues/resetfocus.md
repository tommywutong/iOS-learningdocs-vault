---
title: resetFocus
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 12.0+, tvOS 14.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/resetfocus
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/resetfocus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/resetfocus.json'
content_hash: 'sha256:36d895225db33bee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# resetFocus

<sub>Instance Property</sub>

An action that requests the focus system to reevaluate default focus.

<sub>macOS, tvOS, watchOS</sub>

```swift
var resetFocus: ResetFocusAction { get }
```

## Discussion

Get this environment value and call and call it as a function to force a default focus reevaluation at runtime.

```swift
@Namespace var mainNamespace
@Environment(\.resetFocus) var resetFocus

var body: some View {
    // ...
    resetFocus(in: mainNamespace)
    // ...
}
```

## See Also

### Resetting focus

- [ResetFocusAction](../resetfocusaction.md) — An environment value that provides the ability to reevaluate default focus.
