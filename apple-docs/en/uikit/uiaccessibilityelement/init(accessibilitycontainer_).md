---
title: 'init(accessibilityContainer:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibilityelement/init(accessibilitycontainer:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityelement/init(accessibilitycontainer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityelement/init%28accessibilitycontainer%3A%29.json'
content_hash: 'sha256:f9b7e42e3b73c7ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityElement](../uiaccessibilityelement.md)

# init(accessibilityContainer:)

<sub>Initializer</sub>

Creates and initializes an accessibility element to represent an item in the specified container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(accessibilityContainer container: Any)
```

## Parameters

- `container` — The view that contains the accessibility element.

## Return Value

An accessibility element to represent a non-view item in the container.

## Discussion

In general, you do not create accessibility elements for items in your application because standard UIKit controls and views are accessible by default. However, if you have a view that contains nonview items, such as icons or text images, that need to be accessible to users with disabilities, you create accessibility elements to represent them. In this case, the containing view should implement the UIAccessibilityContainer informal protocol and use this method to create an accessibility element to represent each item that should be exposed to an assistive application.
