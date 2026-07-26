---
title: 'init(wrappedValue:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, tvOS 16.4+, visionOS, Swift 5.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/viewloading/init(wrappedvalue:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/viewloading/init(wrappedvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/viewloading/init%28wrappedvalue%3A%29.json'
content_hash: 'sha256:33a5f5dd22bb5590'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIViewController](../../uiviewcontroller.md) · [ViewLoading](../viewloading.md)

# init(wrappedValue:)

<sub>Initializer</sub>

Creates a property wrapper that loads the view controller’s view before accessing the property.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(wrappedValue: Value)
```

## Parameters

- `wrappedValue` — The underlying value tied to the loading of the view.

## See Also

### Creating a ViewLoading property wrapper

- [init()](<init().md>) — Creates an empty property wrapper that loads the view controller’s view before accessing the property.
