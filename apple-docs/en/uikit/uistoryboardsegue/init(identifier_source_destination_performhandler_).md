---
title: 'init(identifier:source:destination:performHandler:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uistoryboardsegue/init(identifier:source:destination:performhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uistoryboardsegue/init(identifier:source:destination:performhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistoryboardsegue/init%28identifier%3Asource%3Adestination%3Aperformhandler%3A%29.json'
content_hash: 'sha256:735b3f7f94eb56a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStoryboardSegue](../uistoryboardsegue.md)

# init(identifier:source:destination:performHandler:)

<sub>Initializer</sub>

Creates a segue that calls a block to perform the segue transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(identifier: String?, source: UIViewController, destination: UIViewController, performHandler: @escaping () -> Void)
```

## Parameters

- `identifier` — The identifier you want to associate with this particular instance of the segue. You can use this identifier to differentiate one type of segue from another at runtime.

- `source` — The view controller visible at the start of the segue.

- `destination` — The view controller to display after the completion of the segue.

- `performHandler` — A block to be called when the segue’s [- perform](<perform().md>) method is called.

## Return Value

An initialized segue object.

## Discussion

You use this method as an alternative to creating a subclass. Your perform handler should do all of the work necessary to transition between the source and destination view controllers, exactly as if you were implementing the [- perform](<perform().md>) method.

## See Also

### Related Documentation

- [- perform](<perform().md>) — Performs the visual transition for the segue.
