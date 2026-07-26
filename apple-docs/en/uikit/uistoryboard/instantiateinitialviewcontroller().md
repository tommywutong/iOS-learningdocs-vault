---
title: instantiateInitialViewController()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uistoryboard/instantiateinitialviewcontroller()
source_url: 'https://developer.apple.com/documentation/uikit/uistoryboard/instantiateinitialviewcontroller()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistoryboard/instantiateinitialviewcontroller%28%29.json'
content_hash: 'sha256:c88ab900a9707fda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStoryboard](../uistoryboard.md)

# instantiateInitialViewController()

<sub>Instance Method</sub>

Creates the initial view controller and initializes it with the data from the storyboard.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func instantiateInitialViewController() -> UIViewController?
```

## Return Value

The initial view controller in the storyboard.

## Discussion

Every storyboard file has an initial view controller that represents the default view controller to create. Typically, you use the initial view controller as the root view controller for a window. However, you can also instantiate the initial view controller when transitioning to content in a new storyboard file. This method creates a new instance of the initial view controller using its [- initWithCoder:](<../uiviewcontroller/init(coder_).md>) method.

When you specify a storyboard in the [UISceneStoryboardFile](../../bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenestoryboardfile.md) or [UIMainStoryboardFile](../../bundleresources/information-property-list/uimainstoryboardfile.md) key of your app’s `Info.plist` file, UIKit loads the initial view controller from that storyboard.

## See Also

### Loading the Initial View Controller

- [instantiateInitialViewController(creator:)](<instantiateinitialviewcontroller(creator_).md>) — Creates the initial view controller from the storyboard and initializes it using your custom initialization code.
