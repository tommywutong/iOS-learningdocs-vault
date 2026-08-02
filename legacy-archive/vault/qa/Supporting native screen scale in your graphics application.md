---
title: Supporting native screen scale in your graphics application
apple_id: DTS40016633
resource_type: QA
platform: iOS
topic: Graphics & Animation
technology: Metal
published: '2015-11-09'
source_url: https://developer.apple.com/library/archive/qa/qa1909/_index.html
archived_at: '2026-07-18T02:35:43.072328Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1909

# Supporting native screen scale in your graphics application

## Q:  How can I render at the precise dimensions of the display in my graphics application?

A: The iPhone 6 Plus and 6S Plus use a Retina HD display with a very high DPI screen. To support this resolution, in a UIKit app, the system creates a UIScreen object with a screen size of 414 x 736 points and a screen scale of 3.0 (1242 x 2208 pixels). After the contents of the screen are rendered, UIKit samples this content down to fit the actual screen dimensions of 1080 x 1920. In a graphics app that uses Metal or OpenGL ES, however, contents should be rendered at the precise dimensions of the display without requiring an additional sampling stage. This is critical in high-performance 3D apps that perform many calculations for each rendered pixel. To achieve that, the buffers that you render into must have the exact pixel resolutions of the display.

If you are writing a Metal app and you use a MTKView, there is nothing you need to worry about. MTKView automatically supports native screen scale.

If you use a GLKView, the render target attachments are created and managed on your application's behalf based on the view’s point size and the value of its `contentScaleFactor` property. A UIScreen object has a property `nativeScale` which provides the native screen scale factor for the screen. To support the native scale, after the GLKView has been added to a window, you need to set its `contentScaleFactor` property to the value stored in the screen’s `nativeScale` property, as shown in __Listing 1__ (MTKView does so for you by default):

__Listing 1__  Supporting native screen scale in a GLKView object

```objc
- (void)didMoveToWindow
{
    self.contentScaleFactor = self.window.screen.nativeScale;
}
```

If you create your own UIView subclass that is backed by a CAMetalLayer or CAEAGLLayer, you would create those render targets yourself. You should have code similar to the code found in __Listing 1__. In addition, you need to adjust the size of the buffers accordingly whenever your view’s size changes, and in the case of a Metal app also prior to asking the Metal layer for a new drawable. __Listing 2__ shows how to calculate and set a Metal layer’s `drawableSize` property to match the native screen scale. See our [MetalBasic3D](https://developer.apple.com/library/ios/samplecode/MetalBasic3D/Introduction/Intro.html) sample for an example.

__Listing 2__  Adjusting the drawable size of a Metal layer to match the native screen scale

```
// the screen property of the UIWindow can be nil during some backgrounding/foregrounding situations
UIScreen* screen = self.window.screen ?: [UIScreen mainScreen];
CGSize drawableSize = self.bounds.size;

drawableSize.width *= screen.nativeScale;
drawableSize.height *= screen.nativeScale;

metalLayer.drawableSize = drawableSize;
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-11-09 | New document that discusses how to support native screen scale in a graphics application. |

