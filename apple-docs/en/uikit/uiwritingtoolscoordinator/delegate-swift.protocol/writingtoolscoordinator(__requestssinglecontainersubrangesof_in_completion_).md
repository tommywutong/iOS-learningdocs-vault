---
title: 'writingToolsCoordinator(_:requestsSingleContainerSubrangesOf:in:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestssinglecontainersubrangesof:in:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestssinglecontainersubrangesof:in:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator%28_%3Arequestssinglecontainersubrangesof%3Ain%3Acompletion%3A%29.json'
content_hash: 'sha256:1b9be20410bfbab3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [Delegate](../delegate-swift.protocol.md)

# writingToolsCoordinator(_:requestsSingleContainerSubrangesOf:in:completion:)

<sub>Instance Method</sub>

Asks the delegate to divide the specified range of text into the separate containers that render that text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, requestsSingleContainerSubrangesOf range: NSRange, in context: UIWritingToolsCoordinator.Context, completion: @escaping @Sendable ([NSValue]) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, singleContainerSubrangesOf range: NSRange, in context: UIWritingToolsCoordinator.Context) async -> [NSValue]
```

## Parameters

- `writingToolsCoordinator` — The coordinator object requesting information from your custom view.

- `range` — The range of text to consider in the specified `context` object. The location value of this range is relative to the beginning of the text in your context object, and it’s your responsibility to match that location to the correct location in your text storage. If you initialized the context object with the entire contents of your view’s text storage, you can use `range` as-is to access that text storage. However, if you initialized the context object with only a portion of your view’s text, add the starting location of your context object’s text to this value to get the correct range for that text storage.

- `context` — The context object that contains the text to consider. Use this object to locate the appropriate text storage object for your view.

- `completion` — A completion handler to execute when you are done. The handler has no return value and takes an array of [NSValue](../../../foundation/nsvalue.md) types, each of which contains an [NSRange](../../../foundation/nsrange-c.struct.md). The union of the ranges you pass to this handler must equal all of the text in `range`. The order of the ranges in the array must be sequential, with each new range’s starting location coming after the previous one. There must also not be any gaps or overlap between ranges. You must call this handler at some point during your implementation.

## Discussion

If your view uses multiple [NSTextContainer](../../nstextcontainer.md) objects to draw text in different regions, use this method to tell Writing Tools about the containers that display the specified text. In your implementation, subdivide `range` to create one new range for each portion of text that resides in a different container object. For example, if the text in `range` is split between two containers, provide two new [NSRange](../../../foundation/nsrange-c.struct.md) types that reflect the portion of the total text in each container. If `range` resides completely within one container, call the completion handler with `range` as the only value in the array.

When configuring animations for your view, Writing Tools asks your delegate to provide separate previews for each of your view’s container object. Specifically, it calls your delegate’s `writingToolsCoordinator(_:requestsPreviewFor:range:context:completion:)` method separately for each range of text you return in the completion handler. Your implementation of that method must create a preview suitable for animating the content from the underlying text container.

## See Also

### Providing animation container views dynamically

- [- writingToolsCoordinator:requestsDecorationContainerViewForRange:inContext:completion:](<writingtoolscoordinator(__requestsdecorationcontainerviewfor_in_completion_).md>) — Asks the delegate to provide a decoration view for the specified range of text.
