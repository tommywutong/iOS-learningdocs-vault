---
title: 'writingToolsCoordinator(_:requestsPreviewFor:of:in:textDecoration:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:of:in:textdecoration:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:of:in:textdecoration:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator%28_%3Arequestspreviewfor%3Aof%3Ain%3Atextdecoration%3Acompletion%3A%29.json'
content_hash: 'sha256:923702ecc71de26b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [Delegate](../delegate-swift.protocol.md)

# writingToolsCoordinator(_:requestsPreviewFor:of:in:textDecoration:completion:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, requestsPreviewFor textAnimation: UIWritingToolsCoordinator.TextAnimation, of range: NSRange, in context: UIWritingToolsCoordinator.Context, textDecoration: UIWritingToolsCoordinator.TextDecoration, completion: @escaping @Sendable (UITargetedPreview?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, previewFor textAnimation: UIWritingToolsCoordinator.TextAnimation, range: NSRange, context: UIWritingToolsCoordinator.Context, textDecoration: UIWritingToolsCoordinator.TextDecoration) async -> UITargetedPreview?
```
