---
title: 'writingToolsCoordinator(_:finish:for:in:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:finish:for:in:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:finish:for:in:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator%28_%3Afinish%3Afor%3Ain%3Acompletion%3A%29.json'
content_hash: 'sha256:52d333bedaf389ec'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [Delegate](../delegate-swift.protocol.md)

# writingToolsCoordinator(_:finish:for:in:completion:)

<sub>Instance Method</sub>

Asks the delegate to clean up any state related to the specified Writing Tools animation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, finish textAnimation: UIWritingToolsCoordinator.TextAnimation, for range: NSRange, in context: UIWritingToolsCoordinator.Context, completion: @escaping @Sendable () -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, finish textAnimation: UIWritingToolsCoordinator.TextAnimation, for range: NSRange, in context: UIWritingToolsCoordinator.Context) async
```

## Parameters

- `writingToolsCoordinator` — The coordinator object notifying you that animations are about to begin.

- `textAnimation` — The type of animation Writing Tools finished.

- `range` — The range of text that finished animating. This range is relative to the text in your context object, and it’s your responsibility to match that location to the correct location in your text storage. If you initialized the context object with the entire contents of your view’s text storage, you can use `range` as-is to access that text storage. However, if you initialized the context object with only a portion of your view’s text, add the starting location of your context object’s text to this value to get the correct range for that text storage.

- `context` — The context object that contains the original text.

- `completion` — A completion handler to execute when you are done. The handler has no return value and takes no parameters. You must call this handler at some point during your implementation.

## Discussion

Use this method to clean up any data structures you created to support the specified type of Writing Tools animation. You can also use this method to restore the visibility of any text you hid previously. When you finish your cleanup work, call the completion handler to notify Writing Tools.

Writing Tools calls this method only after previous calls to the `writingToolsCoordinator(_:requestsPreviewFor:range:context:completion:)` and `writingToolsCoordinator(_:prepareFor:range:context:completion:)` methods for the same animation type. However, Writing Tools can interleave calls to this method with calls to prepare an animation of a different type. In your implementation of this method, make sure the actions you take don’t interfere with other in-flight animations.

## See Also

### Animating inline text changes

- [- writingToolsCoordinator:requestsPreviewForTextAnimation:ofRange:inContext:completion:](<writingtoolscoordinator(__requestspreviewfor_of_in_completion_).md>) — Asks the delegate for a preview image and layout information for the specified text.
- [- writingToolsCoordinator:prepareForTextAnimation:forRange:inContext:completion:](<writingtoolscoordinator(__preparefor_for_in_completion_).md>) — Prepare for animations for the content that Writing Tools is evaluating.
