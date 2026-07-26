---
title: 'writingToolsCoordinator(_:requestsContextsFor:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestscontextsfor:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestscontextsfor:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator%28_%3Arequestscontextsfor%3Acompletion%3A%29.json'
content_hash: 'sha256:a0bb99601662d506'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [Delegate](../delegate-swift.protocol.md)

# writingToolsCoordinator(_:requestsContextsFor:completion:)

<sub>Instance Method</sub>

Asks your delegate to provide the text to evaluate during the Writing Tools operation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, requestsContextsFor scope: UIWritingToolsCoordinator.ContextScope, completion: @escaping @Sendable ([UIWritingToolsCoordinator.Context]) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, contextsFor scope: UIWritingToolsCoordinator.ContextScope) async -> [UIWritingToolsCoordinator.Context]
```

## Parameters

- `writingToolsCoordinator` — The coordinator object requesting information from your custom view.

- `scope` — The amount of text the coordinator requested. Use this property to determine if Writing Tools is evaluating all of your text or only a subset.

- `completion` — A completion block to execute with the required information. You must execute this block once at end of your method’s implementation. The block has no return value and takes an array of [Context](../context.md) objects that contain the requested information.

## Discussion

At the start of every operation, the [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) object calls this method to request the text to evaluate. Use this method to create one or more [Context](../context.md) objects with your view’s text. Create only one [Context](../context.md) object if your view has only one text storage object. If your view contains multiple text storage objects, create separate [Context](../context.md) objects for each text storage object. Writing Tools returns updates for each context object separately, making it easier for you to incorporate changes into the correct text storage object. Don’t create multiple context objects if your view has only one text storage object.

The `scope` parameter tells you what content Writing Tools expects you to provide in your context object. For example, Writing Tools expects you to provide the selected text when the parameter contains the [UIWritingToolsCoordinatorContextScopeUserSelection](../contextscope/userselection.md) option. When Writing Tools requests a subset of your overall text, include some of the surrounding text in your context object too. Writing Tools can use the extra text you provide to improve the results of its evaluation. For example, it might use an entire paragraph, instead of only the selected sentence, to evaluate ways to rewrite that sentence. It’s best to include the text up to the nearest paragraph boundary before and after the selection. If you include extra text in your context object, set the [range](../context/range.md) property to the range of the selected text.

> [!note] Note
> When a context object stores only a subset of your view’s text, record additional information to map the location of that text to the correct location in your view’s text storage. Keep that information up-to-date throughout the Writing Tools session.

Pass the context objects you create to the provided completion handler before your method returns. Writing Tools waits for you to call the completion handler before proceeding with the operation.
