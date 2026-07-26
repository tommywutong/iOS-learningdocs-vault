---
title: hasMotion
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transitionproperties/hasmotion
source_url: 'https://developer.apple.com/documentation/swiftui/transitionproperties/hasmotion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transitionproperties/hasmotion.json'
content_hash: 'sha256:107c2caf43e30958'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TransitionProperties](../transitionproperties.md)

# hasMotion

<sub>Instance Property</sub>

Whether the transition includes motion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hasMotion: Bool
```

## Discussion

When this behavior is included in a transition, that transition will be replaced by opacity when Reduce Motion is enabled.

Defaults to `true`.

## See Also

### Creating the transition properties

- [init(hasMotion:)](<init(hasmotion_).md>)
