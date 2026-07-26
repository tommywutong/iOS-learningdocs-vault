---
title: CAMetalLayer
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametallayer
source_url: 'https://developer.apple.com/documentation/quartzcore/cametallayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametallayer.json'
content_hash: 'sha256:8d8fea712c37f465'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAMetalLayer

<sub>Class</sub>

A Core Animation layer that Metal can render into, typically displayed onscreen.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CAMetalLayer
```

## Overview

Use a [CAMetalLayer](cametallayer.md) when you want to use Metal to render a layer’s contents; for example, to render into a view. Consider using [MTKView](../metalkit/mtkview.md) instead, because this class automatically wraps a [CAMetalLayer](cametallayer.md) object and provides a higher-level abstraction.

If you’re using UIKit, to create a view that uses a [CAMetalLayer](cametallayer.md), create a subclass of [UIView](https://developer.apple.com/library/archive/releasenotes/iPhone/RN-iPhoneSDK/index.html#//apple_ref/doc/uid/TP40007428-CH1-SW18) and override its [layerClass](../uikit/uiview/layerclass.md) class method to return a [CAMetalLayer](cametallayer.md):

```objc
+ (Class) layerClass
{
    return [CAMetalLayer class];
}
```

If you’re using AppKit, configure an [NSView](../appkit/nsview.md) object to use a backing layer and assign a [CAMetalLayer](cametallayer.md) object to the view:

```objc
myView.wantsLayer = YES;
myView.layer = [CAMetalLayer layer];
```

Adjust the layer’s properties to configure its underlying pixel format and other display behaviors.

### Rendering the Layer’s Contents

A [CAMetalLayer](cametallayer.md) creates a pool of Metal drawable objects ([CAMetalDrawable](cametaldrawable.md)). At any given time, one of these drawable objects contains the contents of the layer. To change the layer’s contents, ask the layer for a drawable object, render into it, and then update the layer’s contents to point to the new drawable.

Call the layer’s [- nextDrawable](<cametallayer/nextdrawable().md>) method to obtain a drawable object. Get the drawable object’s texture and create a render pass that renders to that texture, as shown in the code below:

```objc
CAMetalLayer *metalLayer = (CAMetalLayer*)self.layer;
id<CAMetalDrawable> *drawable = [metalLayer nextDrawable];

MTLRenderPassDescriptor *renderPassDescriptor
                               = [MTLRenderPassDescriptor renderPassDescriptor];

renderPassDescriptor.colorAttachments[0].texture = drawable.texture;
renderPassDescriptor.colorAttachments[0].loadAction = MTLLoadActionClear;
renderPassDescriptor.colorAttachments[0].clearColor = MTLClearColorMake(0.0,0.0,0.0,1.0);
...
```

To change the layer’s contents to the new drawable, call the [present(_:)](<../metal/mtlcommandbuffer/present(__).md>) method (or one of its variants) on the command buffer containing the encoded render pass, passing in the drawable object to present.

```objc
[commandBuffer presentDrawable:drawable];
```

### Keeping References to Drawables

The layer reuses a drawable only if it isn’t onscreen and there are no strong references to it. Further, if a drawable isn’t available when you call [- nextDrawable](<cametallayer/nextdrawable().md>), the system waits for one to become available. To avoid stalls in your app, request a new drawable only when you need it, and release any references to it as quickly as possible after you’re done with it.

For example, before retrieving a new drawable, you might perform other work on the CPU or submit commands to the GPU that don’t require the drawable. Then, obtain the drawable and encode a command buffer to render into it, as described above. After you commit this command buffer, release all strong references to the drawable. If you don’t release drawables correctly, the layer runs out of drawables, and future calls to [- nextDrawable](<cametallayer/nextdrawable().md>) return `nil`.

### Releasing the Drawable

Don’t release the drawable explicitly; instead, embed your render loop within an autorelease pool block:

**Swift**

```swift
func draw(in view: MTKView) {
    autoreleasepool {
        render(view: view)
    }
}
```

**Objective-C**

```objc
- (void)drawInMTKView:(MTKView *)view {
    @autoreleasepool {
        [self render:view];
    }
}
```

This block releases drawables promptly and avoids possible deadlock situations with multiple drawables. Release drawables as soon as possible after committing your onscreen render pass.

> [!note] Note
> As of iOS 10 and tvOS 10, you can safely retain a drawable to query its properties, such as [drawableID](../metal/mtldrawable/drawableid.md) and [presentedTime](../metal/mtldrawable/presentedtime.md), after the system has presented it. If you don’t need to query these properties, release the drawable when you no longer need it.

## Relationships

- **Inherits From**: [CALayer](calayer.md)

- **Conforms To**: [CAMediaTiming](camediatiming.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring the Metal Device

- [device](cametallayer/device.md) — The Metal device responsible for the layer’s drawable resources.
- [preferredDevice](cametallayer/preferreddevice.md) — The device object that the system recommends using for this layer.

### Configuring the Layer’s Drawable Objects

- [pixelFormat](cametallayer/pixelformat.md) — The pixel format of the layer’s textures.
- [colorspace](cametallayer/colorspace.md) — The color space of the rendered content.
- [framebufferOnly](cametallayer/framebufferonly.md) — A Boolean value that determines whether the layer’s textures are used only for rendering.
- [drawableSize](cametallayer/drawablesize.md) — The size, in pixels, of textures for rendering layer content.

### Configuring Presentation Behavior

- [presentsWithTransaction](cametallayer/presentswithtransaction.md) — A Boolean value that determines whether the layer presents its content using a Core Animation transaction.
- [displaySyncEnabled](cametallayer/displaysyncenabled.md) — A Boolean value that determines whether the layer synchronizes its updates to the display’s refresh rate.

### Configuring Extended Dynamic Range Behavior

- [wantsExtendedDynamicRangeContent](cametallayer/wantsextendeddynamicrangecontent.md) — Enables extended dynamic range values onscreen.
- [EDRMetadata](cametallayer/edrmetadata.md) — Metadata describing the tone mapping to apply to the extended dynamic range (EDR) values in the layer.

### Obtaining a Metal Drawable

- [- nextDrawable](<cametallayer/nextdrawable().md>) — Waits until a Metal drawable is available, and then returns it.
- [maximumDrawableCount](cametallayer/maximumdrawablecount.md) — The number of Metal drawables in the resource pool managed by Core Animation.
- [allowsNextDrawableTimeout](cametallayer/allowsnextdrawabletimeout.md) — A Boolean value that determines whether requests for a new buffer expire if the system can’t satisfy them.

### Configuring the Metal Performance HUD

- [developerHUDProperties](cametallayer/developerhudproperties.md) — The properties of the Metal performance heads-up display.

### Instance Properties

- [residencySet](cametallayer/residencyset.md)

## See Also

### Metal and OpenGL

- [CAMetalDrawable](cametaldrawable.md) — A Metal drawable associated with a Core Animation layer.
- [CAEAGLLayer](caeagllayer.md) — A layer that supports drawing OpenGL content in iOS and tvOS applications. _(deprecated)_
- [CAEDRMetadata](caedrmetadata.md) — Metadata describing how extended dynamic range (EDR) values should be tone mapped.
- [CAOpenGLLayer](caopengllayer.md) — A layer that provides a layer suitable for rendering OpenGL content. _(deprecated)_
- [CARenderer](carenderer.md) — A layer that allows an application to render a layer tree into a Core OpenGL context.
