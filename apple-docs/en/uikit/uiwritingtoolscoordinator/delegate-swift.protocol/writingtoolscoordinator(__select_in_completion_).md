---
title: 'writingToolsCoordinator(_:select:in:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:select:in:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:select:in:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator%28_%3Aselect%3Ain%3Acompletion%3A%29.json'
content_hash: 'sha256:670eea52e80951a1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [Delegate](../delegate-swift.protocol.md)

# writingToolsCoordinator(_:select:in:completion:)

<sub>Instance Method</sub>

Asks the delegate to update your view’s current text selection.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, select ranges: [NSValue], in context: UIWritingToolsCoordinator.Context, completion: @escaping @Sendable () -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, select ranges: [NSValue], in context: UIWritingToolsCoordinator.Context) async
```

## Parameters

- `writingToolsCoordinator` — The coordinator object making the change to your view.

- `ranges` — One or more ranges of text to select. Each range is relative to the text in your context object, and it’s your responsibility to match each location to the correct location in your text storage. If you initialized the context object with the entire contents of your view’s text storage, you can use the ranges as-is to access that text storage. However, if you initialized the context object with only a portion of your view’s text, add the starting location of your context object’s text to each value to get the correct range for that text storage.

- `context` — The context object you use to identify the associated text storage.

- `completion` — The completion handler to execute when your delegate finishes updating the selection. The handler has no parameters or return value. You must call this handler at some point during the implementation of your method.

## Discussion

As Writing Tools suggests changes to your view’s text, it calls this method to update the text selection accordingly. Use this method to update the current selection in your view’s text storage. When you finish making the changes, call the provided completion block to let Writing Tools know you’re finished.

## See Also

### Incorporating Writing Tools suggestions

- [- writingToolsCoordinator:replaceRange:inContext:proposedText:reason:animationParameters:completion:](<writingtoolscoordinator(__replace_in_proposedtext_reason_animationparameters_completion_).md>) — Tells the delegate that there are text changes to incorporate into the view.
