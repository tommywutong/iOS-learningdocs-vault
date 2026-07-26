---
title: 'findInteraction(_:sessionFor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifindinteractiondelegate/findinteraction(_:sessionfor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifindinteractiondelegate/findinteraction(_:sessionfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifindinteractiondelegate/findinteraction%28_%3Asessionfor%3A%29.json'
content_hash: 'sha256:09c576f826a15d0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFindInteractionDelegate](../uifindinteractiondelegate.md)

# findInteraction(_:sessionFor:)

<sub>Instance Method</sub>

Provides the object for managing the state, presentation, and behavior of the search.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func findInteraction(_ interaction: UIFindInteraction, sessionFor view: UIView) -> UIFindSession?
```

## Parameters

- `interaction` — The interaction object triggering the find panel.

- `view` — The view you provide a find session object for.

## Return Value

Returns an object the find interaction uses to manage the state, presentation, and behavior of the search. To prevent the find panel from appearing, return `nil`.

## Discussion

Implement the [UITextSearching](../uitextsearching-53wjq.md) protocol on the class that encapsulates the searchable content for your view to use an instance of [UITextSearchingFindSession](../uitextsearchingfindsession.md) as the session object. Alternatively, you can subclass [UIFindSession](../uifindsession.md) to manage the details of the session using a custom class.
