---
title: 'writingToolsCoordinator(_:setGrammarCheckingEnabled:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:setgrammarcheckingenabled:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:setgrammarcheckingenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator%28_%3Asetgrammarcheckingenabled%3A%29.json'
content_hash: 'sha256:1e1daa8ca96413f5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [Delegate](../delegate-swift.protocol.md)

# writingToolsCoordinator(_:setGrammarCheckingEnabled:)

<sub>Instance Method</sub>

Notifies the delegate when the user chooses to disable grammar checking.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, setGrammarCheckingEnabled enabled: Bool)
```

## Discussion

To support the grammar presentation UI, the delegate is notified if the user chooses the option provided in the grammar presentation UI to disable grammar checking for the view. If you use grammar presentation, you should implement this method to respond to that action.
