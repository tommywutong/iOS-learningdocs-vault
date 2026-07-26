---
title: 'writingToolsCoordinator(_:requestsRangeInContextWithIdentifierFor:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.2+（18.4 起废弃）, iPadOS 18.2+（18.4 起废弃）, Mac Catalyst 18.2+（18.4 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsrangeincontextwithidentifierfor:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsrangeincontextwithidentifierfor:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator%28_%3Arequestsrangeincontextwithidentifierfor%3Acompletion%3A%29.json'
content_hash: 'sha256:ad167be37b639276'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [Delegate](../delegate-swift.protocol.md)

# writingToolsCoordinator(_:requestsRangeInContextWithIdentifierFor:completion:)

<sub>Instance Method</sub>

Asks the delegate to provide the location of the character at the specified point in your view’s coordinate system.

> [!warning] Deprecated
> In iOS 18.4 and later and visionOS 2.4 and later, UIWritingToolsCoordinator automatically determines the location of the character at the specified point in your view's coordinate system and no longer calls this method.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, requestsRangeInContextWithIdentifierFor point: CGPoint, completion: @escaping @Sendable (NSRange, UUID) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, rangeInContextWithIdentifierFor point: CGPoint) async -> (NSRange, UUID)
```

## Parameters

- `writingToolsCoordinator` — The coordinator object requesting information from your custom view.

- `point` — A point in your view’s coordinate space. Find the location of the text under this point, if any.

- `completion` — A handler to execute with the required information. This handler has no return value and takes an [NSRange](../../../foundation/nsrange-c.struct.md) and [UUID](../../../foundation/uuid.md) as parameters. Set the range to the character’s location in one of your [Context](../context.md) objects, which you specify using the [UUID](../../../foundation/uuid.md) parameter. You must call this handler at some point during your method’s implementation.

## Discussion

When someone interacts with your view during a proofreading operation, Writing Tools calls this method to get the location of the interaction. If the interaction occurs in the text of one of your [Context](../context.md) objects, configure an [NSRange](../../../foundation/nsrange-c.struct.md) with the character’s location in that context object and a length of `1`. If the interaction occurs outside of the text of your context objects, configure the range with a location of `NSNotFound`.

When specifying the location of a character in your context object, provide a location relative to the start of your context object’s text. The first character in a context object’s text is always at location `0`, and it’s your responsibility to track the location of the context object’s text in your text storage object. When the context object’s text begins in the middle of your text storage, subtract the starting location of the context object’s text from the location you specify in your range value. For example, if the context object’s text starts at character `100` in your text storage, and an interaction occurs with the character at location `102`, specify a range with a location of `2` and a length of `1`.

## See Also

### Displaying proofreading marks

- [- writingToolsCoordinator:requestsBoundingBezierPathsForRange:inContext:completion:](<writingtoolscoordinator(__requestsboundingbezierpathsfor_in_completion_).md>) — Asks the delegate to provide the bounding paths for the specified text in your view.
- [- writingToolsCoordinator:requestsUnderlinePathsForRange:inContext:completion:](<writingtoolscoordinator(__requestsunderlinepathsfor_in_completion_).md>) — Asks the delegate to provide an underline shape for the specified text during a proofreading session.
