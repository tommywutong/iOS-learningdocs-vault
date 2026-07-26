---
title: 'writingToolsCoordinator(_:requestsBoundingBezierPathsFor:in:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsboundingbezierpathsfor:in:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsboundingbezierpathsfor:in:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator%28_%3Arequestsboundingbezierpathsfor%3Ain%3Acompletion%3A%29.json'
content_hash: 'sha256:8b480c7a8dea97e0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [Delegate](../delegate-swift.protocol.md)

# writingToolsCoordinator(_:requestsBoundingBezierPathsFor:in:completion:)

<sub>Instance Method</sub>

Asks the delegate to provide the bounding paths for the specified text in your view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, requestsBoundingBezierPathsFor range: NSRange, in context: UIWritingToolsCoordinator.Context, completion: @escaping @Sendable ([UIBezierPath]) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, boundingBezierPathsFor range: NSRange, context: UIWritingToolsCoordinator.Context) async -> [UIBezierPath]
```

## Parameters

- `writingToolsCoordinator` — The coordinator object requesting information from your custom view.

- `range` — The range of text to evaluate. This range is relative to the text in your context object, and it’s your responsibility to match that location to the correct location in your text storage. If you initialized the context object with the entire contents of your view’s text storage, you can use `range` as-is to access that text storage. However, if you initialized the context object with only a portion of your view’s text, add the starting location of your context object’s text to this value to get the correct range for that text storage.

- `context` — The context object with the target text. Use this object to find the text in your view’s text storage.

- `completion` — A handler to execute with the required information. The handler has no return value and takes an array of Bezier paths as a parameter. You must call this handler at some point during your method’s implementation.

## Discussion

After applying proofreading marks to your view’s text, Writing Tools lets the person accept or reject individual suggestions. To facilitate interactions, the coordinator asks your delegate to provide one or more Bezier paths that surround those proofreading suggestions. For each distinct range of text with a suggestion, it calls this method to get the Bezier paths that surround the corresponding text.

After you determine the location of the specified range of text in your view’s text storage, call the [enumerateTextSegments(in:type:options:using:)](<../../../appkit/nstextlayoutmanager/enumeratetextsegments(in_type_options_using_).md>) method of your view’s [NSTextLayoutManager](../../nstextlayoutmanager.md) to compute the selection rectangles for that text. That method finds the text segments that contain the text and returns the frame rectangle for each one. Create a Bezier path for each rectangle, and convert the coordinates of each path to the coordinate space of the view in your coordinator’s [decorationContainerView](../decorationcontainerview.md) property. Pass the resulting paths to the completion handler.

## See Also

### Displaying proofreading marks

- [- writingToolsCoordinator:requestsRangeInContextWithIdentifierForPoint:completion:](<writingtoolscoordinator(__requestsrangeincontextwithidentifierfor_completion_).md>) — Asks the delegate to provide the location of the character at the specified point in your view’s coordinate system. _(deprecated)_
- [- writingToolsCoordinator:requestsUnderlinePathsForRange:inContext:completion:](<writingtoolscoordinator(__requestsunderlinepathsfor_in_completion_).md>) — Asks the delegate to provide an underline shape for the specified text during a proofreading session.
