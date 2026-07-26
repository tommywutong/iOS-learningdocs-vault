---
title: UIPageControlProgress
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipagecontrolprogress
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrolprogress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrolprogress.json'
content_hash: 'sha256:2ccc6b9b747f9d84'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPageControlProgress

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class UIPageControlProgress
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIPageControlTimerProgress](uipagecontroltimerprogress.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [currentProgress](uipagecontrolprogress/currentprogress.md) — The current progress value of the active page control indicator, between 0 and 1. Values outside of [0…1] will be clamped.
- [delegate](uipagecontrolprogress/delegate.md) — An object that defines the delegate of the page control progress.
- [progressVisible](uipagecontrolprogress/isprogressvisible.md) — Returns `YES` if the progress indicator is visible. The progress indicator is hidden when the user is actively interacting with the `UIPageControl`.

## See Also

### Configuring page progress

- [progress](uipagecontrol/progress.md) — An object that defines the progress of the page control. Default is nil.
- [UIPageControlTimerProgress](uipagecontroltimerprogress.md)
- [UIPageControlProgressDelegate](uipagecontrolprogressdelegate.md)
- [UIPageControlTimerProgressDelegate](uipagecontroltimerprogressdelegate.md)
