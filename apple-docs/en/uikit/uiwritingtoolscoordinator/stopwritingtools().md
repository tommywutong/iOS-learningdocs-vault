---
title: stopWritingTools()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/stopwritingtools()
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/stopwritingtools()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/stopwritingtools%28%29.json'
content_hash: 'sha256:a50ea3d79f2251be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# stopWritingTools()

<sub>Instance Method</sub>

Stops the current Writing Tools operation and dismisses the system UI.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func stopWritingTools()
```

## Discussion

Call this method to abort the current Writing Tools operation. This method dismisses the system’s Writing Tools UI and stops any in-flight interactions with your view. This method does not undo any changes that Writing Tools already made to your view’s content.

## See Also

### Managing the current state

- [state](state-swift.property.md) — The current level of Writing Tools activity in your view.
- [State](state-swift.enum.md) — The states that indicate the current activity, if any, Writing Tools is performing in your view.
