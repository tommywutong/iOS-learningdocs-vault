---
title: delegate
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avexperiencecontroller/delegate-swift.property
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/delegate-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/delegate-swift.property.json'
content_hash: 'sha256:77906d46752010d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVExperienceController](../avexperiencecontroller.md)

# delegate

<sub>Instance Property</sub>

A delegate object for the experience controller.

<sub>visionOS</sub>

```swift
@MainActor weak final var delegate: (any AVExperienceController.Delegate)? { get set }
```

## Discussion

Provide a delegate to have the system notify your app about transitions and other state changes. Use the delegate callbacks to update your app’s state and user interface in response.

## See Also

### Configuring a delegate

- [Delegate](delegate-swift.protocol.md) — A protocol that defines the methods to implement to respond to experience changes.
