---
title: 'showGrammarPresentation(for:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/showgrammarpresentation(for:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/showgrammarpresentation(for:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/showgrammarpresentation%28for%3Ain%3A%29.json'
content_hash: 'sha256:00e6af800fa0485b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# showGrammarPresentation(for:in:)

<sub>Instance Method</sub>

Used to support the presentation of grammar issues in text. When the user interacts with an issue, call this to bring up the relevant UI.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func showGrammarPresentation(for range: NSRange, in context: UIWritingToolsCoordinator.Context) -> Bool
```

## Discussion

Pass in context and range to identify the issue the user selected. Returns NO if the UI cannot be brought up.
