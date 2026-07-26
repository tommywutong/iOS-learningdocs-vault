---
title: UIUserInterfaceStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiuserinterfacestyle
source_url: 'https://developer.apple.com/documentation/uikit/uiuserinterfacestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiuserinterfacestyle.json'
content_hash: 'sha256:ac471c3296678410'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIUserInterfaceStyle

<sub>Enumeration</sub>

Constants that indicate the interface style for the app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIUserInterfaceStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Interface styles

- [UIUserInterfaceStyleUnspecified](uiuserinterfacestyle/unspecified.md) — An unspecified interface style.
- [UIUserInterfaceStyleLight](uiuserinterfacestyle/light.md) — The light interface style.
- [UIUserInterfaceStyleDark](uiuserinterfacestyle/dark.md) — The dark interface style.

### Initializers

- [init(_:)](<uiuserinterfacestyle/init(__).md>) — Creates a user interface style from the specified SwiftUI color scheme.
- [init(rawValue:)](<uiuserinterfacestyle/init(rawvalue_).md>)

## See Also

### Adjusting the interface style

- [overrideUserInterfaceStyle](uiviewcontroller/overrideuserinterfacestyle.md) — The user interface style adopted by the view controller and all of its children.
- [preferredUserInterfaceStyle](uiviewcontroller/preferreduserinterfacestyle.md) — The preferred interface style for this view controller.
- [childViewControllerForUserInterfaceStyle](uiviewcontroller/childviewcontrollerforuserinterfacestyle.md) — The child view controller that supports the preferred user interface style.
- [- setNeedsUserInterfaceAppearanceUpdate](<uiviewcontroller/setneedsuserinterfaceappearanceupdate().md>) — Notifies the view controller that a change occurred that might affect the preferred interface style.
