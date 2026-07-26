---
title: 'init(delegate:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/init(delegate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/init(delegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/init%28delegate%3A%29.json'
content_hash: 'sha256:0bfdd9d171cb8874'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# init(delegate:)

<sub>Initializer</sub>

Creates a writing tools coordinator and assigns the specified delegate object to it.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(delegate: (any UIWritingToolsCoordinator.Delegate)?)
```

## Parameters

- `delegate` — An object capable of handling Writing Tools interactions for your view. The delegate must be able to modify your view’s text storage and refresh the view’s layout and appearance.

## Discussion

Create the coordinator object during your view’s initialization, and assign the object to your view. Use the [- addInteraction:](<../uiview/addinteraction(__).md>) method to add the object to your view.
