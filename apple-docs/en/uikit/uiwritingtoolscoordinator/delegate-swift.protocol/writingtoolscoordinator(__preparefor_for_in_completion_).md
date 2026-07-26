---
title: 'writingToolsCoordinator(_:prepareFor:for:in:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:preparefor:for:in:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:preparefor:for:in:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator%28_%3Apreparefor%3Afor%3Ain%3Acompletion%3A%29.json'
content_hash: 'sha256:1c3730a49592ccaa'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [Delegate](../delegate-swift.protocol.md)

# writingToolsCoordinator(_:prepareFor:for:in:completion:)

<sub>Instance Method</sub>

Prepare for animations for the content that Writing Tools is evaluating.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, prepareFor textAnimation: UIWritingToolsCoordinator.TextAnimation, for range: NSRange, in context: UIWritingToolsCoordinator.Context, completion: @escaping @Sendable () -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, prepareFor textAnimation: UIWritingToolsCoordinator.TextAnimation, for range: NSRange, in context: UIWritingToolsCoordinator.Context) async
```

## Parameters

- `writingToolsCoordinator` — The coordinator object notifying you that animations are about to begin.

- `textAnimation` — The type of animation Writing Tools is preparing.

- `range` — The range of text affected by the animation. This range is relative to the text in your context object, and it’s your responsibility to match that location to the correct location in your text storage. If you initialized the context object with the entire contents of your view’s text storage, you can use `range` as-is to access that text storage. However, if you initialized the context object with only a portion of your view’s text, add the starting location of your context object’s text to this value to get the correct range for that text storage.

- `context` — The context object that contains the original text. Use this object to fetch the current text, and to match that text to your underlying text storage.

- `completion` — A completion handler to execute when you are done. The handler has no return value and takes no parameters. You must call this handler at some point during your implementation.

## Discussion

During an interactive evaluation of your view’s text, Writing Tools creates different animations to provide feedback on what’s happening. For example, it creates an [UIWritingToolsCoordinatorTextAnimationAnticipate](../textanimation/anticipate.md) animation to let people know the system is evaluating the text. The `textAnimation` parameter tells you what type of animation to prepare for.

Use this method to prepare for the system-provided animations of your view’s content. For interactive animations, hide the text in the specified range temporarily while the system animations run. For non-interactive animations, dim the text for the duration of the animation to indicate it’s not editable. For animations to remove or insert text, you can also use this method to set up animations to reflow your view’s content to match the changes. At the end of a given animation, use your delegate’s [- writingToolsCoordinator:finishTextAnimation:forRange:inContext:completion:](<writingtoolscoordinator(__finish_for_in_completion_).md>) method to undo any changes you make to your content.

For a single animation type, the system calls the `writingToolsCoordinator(_:requestsPreviewFor:range:context:completion:)` method, followed sequentially by this method and the [- writingToolsCoordinator:finishTextAnimation:forRange:inContext:completion:](<writingtoolscoordinator(__finish_for_in_completion_).md>) method. Each method executes asynchronously, but the system calls the next method in the sequence only after you call the completion handler of the previous method. However, multiple animations can run simultaneously, so check the `textAnimation` and `range` parameters to differentiate sequences.

## See Also

### Animating inline text changes

- [- writingToolsCoordinator:requestsPreviewForTextAnimation:ofRange:inContext:completion:](<writingtoolscoordinator(__requestspreviewfor_of_in_completion_).md>) — Asks the delegate for a preview image and layout information for the specified text.
- [- writingToolsCoordinator:finishTextAnimation:forRange:inContext:completion:](<writingtoolscoordinator(__finish_for_in_completion_).md>) — Asks the delegate to clean up any state related to the specified Writing Tools animation.
