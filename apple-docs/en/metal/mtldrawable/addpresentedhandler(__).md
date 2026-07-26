---
title: 'addPresentedHandler(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldrawable/addpresentedhandler(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldrawable/addpresentedhandler(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldrawable/addpresentedhandler%28_%3A%29.json'
content_hash: 'sha256:f5e4bd02f2f48d1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDrawable](../mtldrawable.md)

# addPresentedHandler(_:)

<sub>Instance Method</sub>

Registers a block of code to be called immediately after the drawable is presented.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addPresentedHandler(_ block: @escaping MTLDrawablePresentedHandler)
```

## Parameters

- `block` — A block of code to be invoked.

## Discussion

You can register multiple handlers for a single drawable object.

The following example code schedules a presentation handler that reads the [presentedTime](presentedtime.md) property and uses it to derive the interval between the last and current presentation times. From that information, it determines the app’s frame rate.

**Swift**

```swift
// Property declarations
var previousPresentedTime: CFTimeInterval = 0.0
/* ... */
// Render loop
currentDrawable.addPresentedHandler({ [weak self] drawable in
    guard let strongSelf = self else {
        return
    }
    let presentationDuration = drawable.presentedTime - strongSelf.previousPresentedTime
    let frameRate = 1.0/presentationDuration
    /* ... */
    strongSelf.previousPresentedTime = drawable.presentedTime
})
```

**Objective-C**

```objective-c
// Property declarations
@property (nonatomic) CFTimeInterval previousPresentedTime;
/* ... */
// Render loop
__block Renderer *strongSelf = self;
[view.currentDrawable addPresentedHandler:^(id<MTLDrawable> drawable) {
    CFTimeInterval presentationDuration = drawable.presentedTime - strongSelf.previousPresentedTime;
    CFTimeInterval frameRate = 1.0/presentationDuration;
    /* ... */
    strongSelf.previousPresentedTime = drawable.presentedTime;
}];
```

## See Also

### Getting presentation information

- [presentedTime](presentedtime.md) — The host time, in seconds, when the drawable was displayed onscreen.
