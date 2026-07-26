---
title: decorationContainerView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/decorationcontainerview
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/decorationcontainerview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/decorationcontainerview.json'
content_hash: 'sha256:066fafd644afd6ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# decorationContainerView

<sub>Instance Property</sub>

The view that Writing Tools uses to display background decorations such as proofreading marks.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var decorationContainerView: UIView? { get set }
```

## Discussion

Writing Tools uses the view in this property to host proofreading marks and other visual elements that show any suggested changes. Set this property to a subview situated visibly below the text in your custom text view. It’s also satisfactory to place this view visually in front of the text. Make sure the size of the view is big enough to cover all of the affected text. If you don’t assign a value to this property, the coordinator uses the object in its [view](../uiinteraction/view.md) property to host any visual elements.

If you display your view’s text using multiple text containers, implement the [- writingToolsCoordinator:requestsSingleContainerSubrangesOfRange:inContext:completion:](<delegate-swift.protocol/writingtoolscoordinator(__requestssinglecontainersubrangesof_in_completion_).md>) and [- writingToolsCoordinator:requestsDecorationContainerViewForRange:inContext:completion:](<delegate-swift.protocol/writingtoolscoordinator(__requestsdecorationcontainerviewfor_in_completion_).md>) methods to provide separate decoration views for each container.

## See Also

### Getting the host views for effects

- [effectContainerView](effectcontainerview.md) — The view that Writing Tools uses to display visual effects during the text-rewriting process.
