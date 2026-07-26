---
title: state
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/state-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/state-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/state-swift.property.json'
content_hash: 'sha256:4ddf4b48669e7958'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# state

<sub>Instance Property</sub>

The current level of Writing Tools activity in your view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var state: UIWritingToolsCoordinator.State { get }
```

## Discussion

Use this property to determine when Writing Tools is actively making changes to your view. During the course of Writing Tools interactions, the system reports state changes to the delegate’s [- writingToolsCoordinator:willChangeToState:completion:](<delegate-swift.protocol/writingtoolscoordinator(__willchangeto_completion_).md>) method and updates this property accordingly.

## See Also

### Managing the current state

- [- stopWritingTools](<stopwritingtools().md>) — Stops the current Writing Tools operation and dismisses the system UI.
- [State](state-swift.enum.md) — The states that indicate the current activity, if any, Writing Tools is performing in your view.
