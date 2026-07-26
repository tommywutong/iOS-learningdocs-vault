---
title: 'init(identifier:source:destination:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uistoryboardsegue/init(identifier:source:destination:)'
source_url: 'https://developer.apple.com/documentation/uikit/uistoryboardsegue/init(identifier:source:destination:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistoryboardsegue/init%28identifier%3Asource%3Adestination%3A%29.json'
content_hash: 'sha256:86fe136e5db41382'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStoryboardSegue](../uistoryboardsegue.md)

# init(identifier:source:destination:)

<sub>Initializer</sub>

Initializes and returns a storyboard segue object for use in performing a segue.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(identifier: String?, source: UIViewController, destination: UIViewController)
```

## Parameters

- `identifier` — The identifier you want to associate with this particular instance of the segue. You can use this identifier to differentiate one type of segue from another at runtime.

- `source` — The view controller visible at the start of the segue.

- `destination` — The view controller to display after the completion of the segue.

## Return Value

An initialized segue object.

## Discussion

This method is the designated initializer for segue objects. If you subclass [UIStoryboardSegue](../uistoryboardsegue.md), you can override this method and perform any custom initialization in your implementation. Your implementation should call `super` first and then proceed if that method doesn’t return `nil`.
