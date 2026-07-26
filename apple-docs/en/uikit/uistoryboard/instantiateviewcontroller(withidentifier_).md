---
title: 'instantiateViewController(withIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uistoryboard/instantiateviewcontroller(withidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uistoryboard/instantiateviewcontroller(withidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistoryboard/instantiateviewcontroller%28withidentifier%3A%29.json'
content_hash: 'sha256:1544f7b8df0e3960'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStoryboard](../uistoryboard.md)

# instantiateViewController(withIdentifier:)

<sub>Instance Method</sub>

Creates the view controller with the specified identifier and initializes it with the data from the storyboard.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func instantiateViewController(withIdentifier identifier: String) -> UIViewController
```

## Parameters

- `identifier` — An identifier string that uniquely identifies the view controller in the storyboard file. At design time, put this same string in the Storyboard ID attribute of your view controller in Interface Builder. This identifier is not a property of the view controller object itself. The storyboard uses it to locate the appropriate data for your view controller. If the specified identifier does not exist in the storyboard file, this method raises an exception.

## Return Value

The view controller corresponding to the specified identifier string. If no view controller has the given identifier, this method throws an exception.

## Discussion

Use this method to create a view controller object to present programmatically. Each time you call this method, it creates a new instance of the view controller using the [- initWithCoder:](<../uiviewcontroller/init(coder_).md>) method.

## See Also

### Instantiating Storyboard View Controllers

- [instantiateViewController(identifier:creator:)](<instantiateviewcontroller(identifier_creator_).md>) — Creates the specified view controller from the storyboard and initializes it using your custom initialization code.
