---
title: UIUserInterfaceIdiom
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiuserinterfaceidiom
source_url: 'https://developer.apple.com/documentation/uikit/uiuserinterfaceidiom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiuserinterfaceidiom.json'
content_hash: 'sha256:0ad03620f5bd1325'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIUserInterfaceIdiom

<sub>Enumeration</sub>

Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIUserInterfaceIdiom
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Idioms

- [UIUserInterfaceIdiomUnspecified](uiuserinterfaceidiom/unspecified.md) — An unspecified idiom.
- [UIUserInterfaceIdiomPhone](uiuserinterfaceidiom/phone.md) — An interface designed for iPhone and iPod touch.
- [UIUserInterfaceIdiomPad](uiuserinterfaceidiom/pad.md) — An interface designed for iPad.
- [UIUserInterfaceIdiomTV](uiuserinterfaceidiom/tv.md) — An interface designed for tvOS and Apple TV.
- [UIUserInterfaceIdiomCarPlay](uiuserinterfaceidiom/carplay.md) — An interface designed for an in-car experience.
- [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) — An interface designed for the Mac.
- [UIUserInterfaceIdiomVision](uiuserinterfaceidiom/vision.md) — An interface designed for visionOS and Apple Vision Pro.

### Initializers

- [init(rawValue:)](<uiuserinterfaceidiom/init(rawvalue_).md>)

## See Also

### Getting the current idiom

- [UI_USER_INTERFACE_IDIOM](<ui_user_interface_idiom().md>) — Returns the interface idiom supported by the current device (recommended for apps that run in versions of iOS earlier than 3.2). _(deprecated)_
