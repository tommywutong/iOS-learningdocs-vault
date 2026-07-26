---
title: 'startTextAnimation(_:for:in:writingDirection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/starttextanimation(_:for:in:writingdirection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/starttextanimation(_:for:in:writingdirection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/starttextanimation%28_%3Afor%3Ain%3Awritingdirection%3A%29.json'
content_hash: 'sha256:3f1e9e893786c68c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# startTextAnimation(_:for:in:writingDirection:)

<sub>Instance Method</sub>

Used to support the presentation of grammar issues in text. When an issue is first identified and indicated, call this to have it animated.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func startTextAnimation(_ textAnimation: UIWritingToolsCoordinator.TextAnimation, for range: NSRange, in context: UIWritingToolsCoordinator.Context, writingDirection: NSWritingDirection) -> UUID?
```

## Discussion

The context should be large enough to contain the range being indicated, and the range should be the range of the issue within the context. Returns a UUID that can be used to cancel the animation, or nil if the animation cannot be performed. Calls delegate methods to prepare for the animation (which should hide the text), request previews (with and without underlines), and finish the animation (which should show the text).
