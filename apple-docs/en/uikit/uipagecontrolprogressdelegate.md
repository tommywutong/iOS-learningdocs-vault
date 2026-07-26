---
title: UIPageControlProgressDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipagecontrolprogressdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrolprogressdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrolprogressdelegate.json'
content_hash: 'sha256:7d28410550bbf39a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPageControlProgressDelegate

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol UIPageControlProgressDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [UIPageControlTimerProgressDelegate](uipagecontroltimerprogressdelegate.md)

## Topics

### Instance Methods

- [- pageControlProgress:initialProgressForPage:](<uipagecontrolprogressdelegate/pagecontrolprogress(__initialprogressforpage_).md>) — Returns the initial progress (between 0…1) for the specified page. By default, `currentProgress` is set to 0 when the page changes.
- [- pageControlProgressVisibilityDidChange:](<uipagecontrolprogressdelegate/pagecontrolprogressvisibilitydidchange(__).md>) — Called when the page control progress visibility has changed, which could occur when the page control is being interacted with. The page control progress becomes hidden when the user begins to interact with the page control (when it begins continuous interaction), and is visible again when the user stops interacting with the control. Observe the page control progress visibility to pause or resume the paging content.

## See Also

### Configuring page progress

- [progress](uipagecontrol/progress.md) — An object that defines the progress of the page control. Default is nil.
- [UIPageControlProgress](uipagecontrolprogress.md)
- [UIPageControlTimerProgress](uipagecontroltimerprogress.md)
- [UIPageControlTimerProgressDelegate](uipagecontroltimerprogressdelegate.md)
