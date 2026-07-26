---
title: 'cancelTextAnimations(identifiers:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/canceltextanimations(identifiers:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/canceltextanimations(identifiers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/canceltextanimations%28identifiers%3A%29.json'
content_hash: 'sha256:1c25183e508094ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# cancelTextAnimations(identifiers:)

<sub>Instance Method</sub>

Used to support the presentation of grammar issues in text. If it is necessary to cancel the animation of one or more issues, call this to cancel theanimations.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func cancelTextAnimations(identifiers: [UUID])
```

## Discussion

The UUIDs passed in should be those returned when starting the animations. To cancel all ahimations, use [- stopWritingTools](<stopwritingtools().md>) instead.
