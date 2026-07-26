---
title: 'instantiateInitialViewController(creator:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uistoryboard/instantiateinitialviewcontroller(creator:)'
source_url: 'https://developer.apple.com/documentation/uikit/uistoryboard/instantiateinitialviewcontroller(creator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistoryboard/instantiateinitialviewcontroller%28creator%3A%29.json'
content_hash: 'sha256:ad56ea1955b7d84a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStoryboard](../uistoryboard.md)

# instantiateInitialViewController(creator:)

<sub>Instance Method</sub>

Creates the initial view controller from the storyboard and initializes it using your custom initialization code.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func instantiateInitialViewController<ViewController>(creator: ((NSCoder) -> ViewController?)? = nil) -> ViewController? where ViewController : UIViewController
```

## Parameters

- `creator` — A block containing your custom creation code for the view controller. Use this block to create the view controller, initialize it with the provided `coder` object and any custom information you require, and return the result. This block returns a new view controller object and takes the following parameter: - **coder** — The coder object containing the storyboard data to use when configuring the view controller. If you return `nil` from your block, this method creates the view controller using the default [- initWithCoder:](<../uiviewcontroller/init(coder_).md>) method.

## Return Value

The initial view controller in the storyboard.

## Discussion

Every storyboard file has an initial view controller that represents the default view controller to create. Typically, you use the initial view controller as the root view controller for a window. However, you can also instantiate the initial view controller when transitioning to content in a new storyboard file.

This method creates a new instance of the initial view controller using the custom block you provide. In your block, create the view controller using your custom initialization method and return it. Your custom initialization method must accept an [NSCoder](../../foundation/nscoder.md) parameter and must call the inherited [- initWithCoder:](<../uiviewcontroller/init(coder_).md>) method at some point during its execution. Not doing so is a programmer error.

## See Also

### Loading the Initial View Controller

- [- instantiateInitialViewController](<instantiateinitialviewcontroller().md>) — Creates the initial view controller and initializes it with the data from the storyboard.
