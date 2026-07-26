---
title: UIAccessibilityCustomAction.Handler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitycustomaction/handler
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/handler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycustomaction/handler.json'
content_hash: 'sha256:4e9483f2a806098f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityCustomAction](../uiaccessibilitycustomaction.md)

# UIAccessibilityCustomAction.Handler

<sub>Type Alias</sub>

A closure type that defines a handler to perform for an action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor typealias Handler = (UIAccessibilityCustomAction) -> Bool
```

## See Also

### Actions

- [UIAccessibilityAction](../../objectivec/uiaccessibilityaction.md) — A set of methods that accessibility elements can use to support specific actions.
- [UIAccessibilityCustomAction](../uiaccessibilitycustomaction.md) — A custom action to perform on an accessible object.
- [Delivering an exceptional accessibility experience](../../accessibility/delivering_an_exceptional_accessibility_experience.md) — Make improvements to your app’s interaction model to support assistive technologies such as VoiceOver.
