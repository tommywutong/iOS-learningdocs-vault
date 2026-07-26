---
title: effectContainerView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/effectcontainerview
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/effectcontainerview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/effectcontainerview.json'
content_hash: 'sha256:f629d8241af8318e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# effectContainerView

<sub>Instance Property</sub>

The view that Writing Tools uses to display visual effects during the text-rewriting process.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var effectContainerView: UIView? { get set }
```

## Discussion

Writing Tools uses the view in this property to host the visual effects it creates when making interactive changes to your view’s content. These visual effects let people know the state of the text and provide feedback about what’s happening to it. Set this property to a subview that sits visually above, and covers, all of the text in your custom text view. If you don’t assign a value to this property, the coordinator uses the object in its [view](../uiinteraction/view.md) property to host any visual effects.

If you display your view’s text using multiple text containers, implement the [- writingToolsCoordinator:requestsSingleContainerSubrangesOfRange:inContext:completion:](<delegate-swift.protocol/writingtoolscoordinator(__requestssinglecontainersubrangesof_in_completion_).md>) method to request multiple previews.

## See Also

### Getting the host views for effects

- [decorationContainerView](decorationcontainerview.md) — The view that Writing Tools uses to display background decorations such as proofreading marks.
