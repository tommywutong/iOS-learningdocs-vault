---
title: UIPageControlTimerProgressDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipagecontroltimerprogressdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontroltimerprogressdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontroltimerprogressdelegate.json'
content_hash: 'sha256:07f0fd7abe3b07b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPageControlTimerProgressDelegate

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol UIPageControlTimerProgressDelegate : UIPageControlProgressDelegate
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIPageControlProgressDelegate](uipagecontrolprogressdelegate.md)

## Topics

### Instance Methods

- [- pageControlTimerProgress:shouldAdvanceToPage:](<uipagecontroltimerprogressdelegate/pagecontroltimerprogress(__shouldadvancetopage_).md>) — Determines if the time interval progress should advance to the next page upon progress completion of the current page’s duration. Default is YES.
- [- pageControlTimerProgressDidChange:](<uipagecontroltimerprogressdelegate/pagecontroltimerprogressdidchange(__).md>) — Called when the progress has changed from the time interval progress.

## See Also

### Configuring page progress

- [progress](uipagecontrol/progress.md) — An object that defines the progress of the page control. Default is nil.
- [UIPageControlProgress](uipagecontrolprogress.md)
- [UIPageControlTimerProgress](uipagecontroltimerprogress.md)
- [UIPageControlProgressDelegate](uipagecontrolprogressdelegate.md)
