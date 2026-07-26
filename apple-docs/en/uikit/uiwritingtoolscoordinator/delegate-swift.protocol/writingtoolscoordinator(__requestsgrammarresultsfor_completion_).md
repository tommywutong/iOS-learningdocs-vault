---
title: 'writingToolsCoordinator(_:requestsGrammarResultsFor:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsgrammarresultsfor:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsgrammarresultsfor:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator%28_%3Arequestsgrammarresultsfor%3Acompletion%3A%29.json'
content_hash: 'sha256:3152a6c3613f6cf6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [Delegate](../delegate-swift.protocol.md)

# writingToolsCoordinator(_:requestsGrammarResultsFor:completion:)

<sub>Instance Method</sub>

Asks the delegate for information about grammar issues in the specified context.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, requestsGrammarResultsFor context: UIWritingToolsCoordinator.Context, completion: @escaping @Sendable ([NSTextCheckingResult]) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, grammarResultsFor context: UIWritingToolsCoordinator.Context) async -> [NSTextCheckingResult]
```

## Discussion

To support the grammar presentation UI, the delegate should provide information about the identified and currently indicated grammar issues in the specified context. The elements of the results array should be `NSTextCheckingResult` objects of grammar type, of the sort that are returned from grammar checking, with ranges relative to the context. If you use grammar presentation, you must implement this delegate method to provide them.
