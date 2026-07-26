---
title: 'writingToolsCoordinator(_:requestsDecorationContainerViewFor:in:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsdecorationcontainerviewfor:in:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsdecorationcontainerviewfor:in:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator%28_%3Arequestsdecorationcontainerviewfor%3Ain%3Acompletion%3A%29.json'
content_hash: 'sha256:19fe1d55c19a31bb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [Delegate](../delegate-swift.protocol.md)

# writingToolsCoordinator(_:requestsDecorationContainerViewFor:in:completion:)

<sub>Instance Method</sub>

Asks the delegate to provide a decoration view for the specified range of text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, requestsDecorationContainerViewFor range: NSRange, in context: UIWritingToolsCoordinator.Context, completion: @escaping @Sendable (UIView) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, decorationContainerViewFor range: NSRange, in context: UIWritingToolsCoordinator.Context) async -> UIView
```

## Parameters

- `writingToolsCoordinator` — The coordinator object requesting information from your custom view.

- `range` — The range of text to consider in the specified `context` object. The location value of this range is relative to the beginning of the text in your context object, and it’s your responsibility to match that location to the correct location in your text storage. If you initialized the context object with the entire contents of your view’s text storage, you can use `range` as-is to access that text storage. However, if you initialized the context object with only a portion of your view’s text, add the starting location of your context object’s text to this value to get the correct range for that text storage.

- `context` — The context object that contains the text to consider. Use this object to locate the appropriate text storage object for your view.

- `completion` — A completion handler to execute when you are done. The handler has no return value and takes a [UIView](../../uiview.md) object as a parameter. You must call this handler at some point during your implementation.

## Discussion

If your view uses multiple [NSTextContainer](../../nstextcontainer.md) objects to draw text in different regions, use this method to provide Writing Tools with the view to use for the specified range of text. After calling your delegate’s [- writingToolsCoordinator:requestsSingleContainerSubrangesOfRange:inContext:completion:](<writingtoolscoordinator(__requestssinglecontainersubrangesof_in_completion_).md>) method, Writing Tools calls this method for each subrange of text you provided. Find or provide a view situated visibly below the specified text in your text view. It’s also satisfactory to provide a view that’s visually in front of the text. Writing Tools uses the provided view to host any proofreading marks for the specified range of text.

If your view has only one text container, use the coordinator’s [decorationContainerView](../decorationcontainerview.md) property to specify the view to use for proofreading marks.

## See Also

### Providing animation container views dynamically

- [- writingToolsCoordinator:requestsSingleContainerSubrangesOfRange:inContext:completion:](<writingtoolscoordinator(__requestssinglecontainersubrangesof_in_completion_).md>) — Asks the delegate to divide the specified range of text into the separate containers that render that text.
