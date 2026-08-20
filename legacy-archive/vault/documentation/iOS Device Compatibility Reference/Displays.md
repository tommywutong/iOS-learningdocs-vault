---
title: iOS Device Compatibility Reference
apple_id: TP40013599
resource_type: Guide
platform: iOS
topic: Data Management
technology: null
published: '2017-10-30'
source_url: https://developer.apple.com/library/archive/documentation/DeviceInformation/Reference/iOSDeviceCompatibility/Displays/Displays.html
archived_at: '2026-07-15T07:31:54.537615Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [iOS Device Compatibility Reference](Introduction.md)


[Next](Graphics%20Processors.md)[Previous](Device%20Compatibility.md)

# Displays

The display is a key part of the great user experience on iOS devices. Users interact with the display surface, and see the results after an app reacts to these touches and updates the displayed image. Apple continues to improve the display hardware and software pipeline that drives the display, so understanding the display characteristics is often a critical part of creating a great user experience.

[Table 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqhawvgvzs) summarizes the physical dimensions of iOS displays and how those pixels are mapped to the logical coordinate system in UIKit.

__Table 2-1__  Screen Geometry

| Device | Native Resolution (Pixels) | UIKit Size (Points) | Native Scale factor | UIKit Scale factor |
| iPhone X | 1125 x 2436 | 375 x 812 | 3.0 | 3.0 |
| iPhone 8 Plus | 1080 x 1920 | 414 x 736 | 2.608 | 3.0 |
| iPhone 8 | 750 x 1334 | 375 x 667 | 2.0 | 2.0 |
| iPhone 7 Plus | 1080 x 1920 | 414 x 736 | 2.608 | 3.0 |
| iPhone 6s Plus | 1080 x 1920 | 375 x 667 | 2.608 | 3.0 |
| iPhone 6 Plus | 1080 x 1920 | 375 x 667 | 2.608 | 3.0 |
| iPhone 7 | 750 x 1334 | 375 x 667 | 2.0 | 2.0 |
| iPhone 6s | 750 x 1334 | 375 x 667 | 2.0 | 2.0 |
| iPhone 6 | 750 x 1334 | 375 x 667 | 2.0 | 2.0 |
| iPhone SE | 640 x 1136 | 320 x 568 | 2.0 | 2.0 |
| iPad Pro 12.9-inch (2nd generation) | 2048 x 2732 | 1024 x 1366 | 2.0 | 2.0 |
| iPad Pro 10.5-inch | 2224 x 1668 | 1112 x 834 | 2.0 | 2.0 |
| iPad Pro (12.9-inch) | 2048 x 2732 | 1024 x 1366 | 2.0 | 2.0 |
| iPad Pro (9.7-inch) | 1536 x 2048 | 768 x 1024 | 2.0 | 2.0 |
| iPad Air 2 | 1536 x 2048 | 768 x 1024 | 2.0 | 2.0 |
| iPad Mini 4 | 1536 x 2048 | 768 x 1024 | 2.0 | 2.0 |

At runtime, use the [bounds](https://developer.apple.com/documentation/uikit/uiscreen/1617838-bounds) and [scale](https://developer.apple.com/documentation/uikit/uiscreen/1617836-scale) properties of a [UIScreen](https://developer.apple.com/documentation/uikit/uiscreen) object to understand how UIKit present the display to your app, and the [nativeBounds](https://developer.apple.com/documentation/uikit/uiscreen/1617810-nativebounds) and[nativeScale](https://developer.apple.com/documentation/uikit/uiscreen/1617825-nativescale) when you need to work with the exact number of pixels on the display.

If the native scale differs from the UIKit scale factor, then iOS first renders the content at the UIKit scale factor and then scales it to fit into the native number of pixels on the screen. For games and other apps that perform many calculations per pixel, rendering these additional pixels can be expensive. Instead, configure a view to render at the native scale instead. For more information on how to do this in Metal, see [Native Screen Scale (iOS and tvOS)](../3D%20Drawing/Metal%20Best%20Practices%20Guide/NativeScreenScale.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqoa).

[Table 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqhawvgvzt) describes the ability to reproduce color and adapt the color display to the environment around the device.

__Table 2-2__  Color Reproduction

| Device | Native Color Space | TrueTone Display | Active Color Management |
| iPhone X | Display P3 | Yes | Yes |
| iPhone 8 Plus | Display P3 | Yes | Yes |
| iPhone 8 | Display P3 | Yes | Yes |
| iPhone 7 Plus | Display P3 | No | Yes |
| iPhone 7 | Display P3 | No | Yes |
| iPhone 6s Plus | sRGB | No | Yes |
| iPhone 6s | sRGB | No | Yes |
| iPhone SE | sRGB | No | Yes |
| iPhone 6 Plus | sRGB | No | Yes |
| iPhone 6 | sRGB | No | Yes |
| iPad Mini 4 | sRGB | No | Yes |
| iPad Air 2 | sRGB | No | Yes |
| iPad Pro 12.9-inch (2nd generation) | Display P3 | Yes | Yes |
| iPad Pro 10.5-inch | Display P3 | Yes | Yes |
| iPad Pro (12.9-inch) | sRGB | No | Yes |
| iPad Pro (9.7-inch) | Display P3 | Yes | Yes |

The P3 Display color space has a larger color gamut than an sRGB color space, with more saturated reds and greens. For information on supporting wide color in your app, see [WWDC 2016 - Session 712: Working with Wide Color](https://developer.apple.com/videos/play/wwdc2016/712/).

A True Tone display uses advanced ambient light sensors to automatically adapt the color and intensity of the display to match the light in the surrounding environment. Different kinds of apps many need to react to these changes differently. To specify how the display should adapt when your app is frontmost, see `UIWhitePointAdaptivityStyle`.

[Table 2-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqhawvgvzu) describes the rate at which the hardware can adjust the contents of the screen.

__Table 2-3__  Display Refresh

| Device | Refresh Rate | Recommended Frame Rates |
| iPhone X | 60 hz | 60, 30, 20 |
| iPhone 8 Plus | 60 hz | 60, 30, 20 |
| iPhone 8 | 60 hz | 60, 30, 20 |
| iPhone 7 Plus | 60 hz | 60, 30, 20 |
| iPhone 7 | 60 hz | 60, 30, 20 |
| iPhone 6s Plus | 60 hz | 60, 30, 20 |
| iPhone 6s | 60 hz | 60, 30, 20 |
| iPhone SE | 60 hz | 60, 30, 20 |
| iPhone 6 Plus | 60 hz | 60, 30, 20 |
| iPhone 6 | 60 hz | 60, 30, 20 |
| iPad Pro 12.9-inch (2nd generation) | 120 hz maximum | 120, 60, 40, 30, 24, 20 |
| iPad Pro 10.5-inch | 120 hz maximum | 120, 60, 40, 30, 24, 20 |
| iPad Pro (12.9-inch) | 60 hz | 60, 30, 20 |
| iPad Pro (9.7-inch) | 60 hz | 60, 30, 20 |
| iPad Mini 4 | 60 hz | 60, 30, 20 |

Under most circumstances, UIKit handles redrawing and animation for you, adjusting the frame rate as necessary to provide a good viewing experience with reasonable energy usage. However, when you configure a view animation, you can optionally specify a hint when you know that the animation should run at a higher or lower rate. For more information, see [UIViewAnimationOptions](https://developer.apple.com/documentation/uikit/uiviewanimationoptions).

In full screen apps and games, animation is often driven explicitly using a [CADisplayLink](https://developer.apple.com/documentation/quartzcore/cadisplaylink) object. Set the display link’s [preferredFramesPerSecond](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1648421-preferredframespersecond) property to the frame rate you want, ideally using one of the preferred values specified in [Table 2-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqhawvgvzu). SpriteKit, SceneKit, or MetalKit also provide this property on the the [SKView](https://developer.apple.com/documentation/spritekit/skview), [SCNView](https://developer.apple.com/documentation/scenekit/scnview), and [MTKView](https://developer.apple.com/documentation/metalkit/mtkview) classes. For more information on animating content in Metal, see [Frame Rate (iOS and tvOS)](../3D%20Drawing/Metal%20Best%20Practices%20Guide/FrameRate.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmrt).

[Table 2-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqhawvgvzv) summarize the how often the display register touches from fingers or Apple Pencil and delivers them to UIKit.

__Table 2-4__  Touch Input

| Device | Touch Sample Rate | Apple Pencil Sample Rate | Touch Delivery Rate | 3D Touch |
| iPhone X | 120 hz | Not supported | 60 hz | Yes |
| iPhone 8 Plus | 60 hz | Not supported | 60 hz | Yes |
| iPhone 8 | 60 hz | Not supported | 60 hz | Yes |
| iPhone 7 Plus | 60 hz | Not supported | 60 hz | Yes |
| iPhone 7 | 60 hz | Not supported | 60 hz | Yes |
| iPhone 6s Plus | 60 hz | Not supported | 60 hz | Yes |
| iPhone 6s | 60 hz | Not supported | 60 hz | Yes |
| iPhone SE | 60 hz | Not supported | 60 hz | No |
| iPhone 6 Plus | 60 hz | Not supported | 60 hz | No |
| iPhone 6 | 60 hz | Not supported | 60 hz | No |
| iPad Air 2 | 60 hz | Not supported | 60 hz | No |
| iPad Mini 4 | 60 hz | Not supported | 60 hz | No |
| iPad Pro 12.9-inch (2nd generation) | 120 hz | 240 hz | 120 hz | No |
| iPad Pro 10.5-inch | 120 hz | 240 hz | 120 hz | No |
| iPad Pro (12.9-inch) | 120 hz | 240 hz | 60 hz | No |
| iPad Pro (9.7-inch) | 120 hz | 240 hz | 60 hz | No |

The display hardware periodically captures data from sensors embedded in the screen. When a user touches the screen, the sensor information is recorded, processed, and delivered to UIKit. On displays that support 3D Touch, additional information about how much pressure the user applied to the display is also recorded. Only some displays support Apple Pencil. On these displays, the capture rate is different when reading Apple Pencil events than the capture rate for finger touches, and additional stylus information, such as the azimuth, is also recorded in each event.

When the capture rate is higher than the delivery rate, multiple events are coalesced into one touch event whose location reflects the most recent touch. However, the additional touch information is available for apps that need more precision.

For more information on event handling, coalesced touches, 3D Touch, and Apple Pencil, see _Event Handling Guide for iOS_.

These subsections provide further details on the features listed in [iOS Device Display Summary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqhawvgvzw) above.

Use the [nativeBounds](https://developer.apple.com/documentation/uikit/uiscreen/1617810-nativebounds), [bounds](https://developer.apple.com/documentation/uikit/uiscreen/1617838-bounds), [nativeScale](https://developer.apple.com/documentation/uikit/uiscreen/1617825-nativescale), and [scale](https://developer.apple.com/documentation/uikit/uiscreen/1617836-scale) properties of a [UIScreen](https://developer.apple.com/documentation/uikit/uiscreen) object to retrieve the characteristics of a display.

If the native scale differs from the UIKit scale factor, then iOS first renders any content at the UIKit scale factor and then downsamples it to fit on the screen. For games and other apps that perform many calculations per pixel, rendering these additional pixels can be expensive. Instead, use a view that is configured to render at the native scale instead. For more information on how to do this in Metal, see [Native Screen Scale (iOS and tvOS)](../3D%20Drawing/Metal%20Best%20Practices%20Guide/NativeScreenScale.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqoa).

The P3 Display color space has a larger color gamut than an sRGB color space, with more saturated reds and greens. For information on how to support wide color in your app, see [WWDC 2016 - Session 712: Working with Wide Color](https://developer.apple.com/videos/play/wwdc2016/712/).

A True Tone display uses advanced ambient light sensors to automatically adapt the color and intensity of the display to match the light in the surrounding environment. You can configure your app to define how the display’s white point is adjusted when your app is front most. For more information, see `UIWhitePointAdaptivityStyle`.

Under most circumstances, UIKit handles redrawing and animation for you, adjusting the frame rate as necessary to provide a good viewing experience with reasonable energy usage. However, when you configure a view animation, you can optionally specify a hint that specifies whether that animation should run at a higher or lower rate. For more information, see [UIViewAnimationOptions](https://developer.apple.com/documentation/uikit/uiviewanimationoptions).

In full screen apps and games, animation is often driven explicitly using a [CADisplayLink](https://developer.apple.com/documentation/quartzcore/cadisplaylink) object. Set the display link’s [preferredFramesPerSecond](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1648421-preferredframespersecond) property to the frame rate you want, ideally using one of the preferred values specified in [Table 2-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqhawvgvzu). SpriteKit, SceneKit, or MetalKit also provide this property on the the [SKView](https://developer.apple.com/documentation/spritekit/skview), [SCNView](https://developer.apple.com/documentation/scenekit/scnview), and [MTKView](https://developer.apple.com/documentation/metalkit/mtkview) classes. For more information on animating content in Metal, see [Frame Rate (iOS and tvOS)](../3D%20Drawing/Metal%20Best%20Practices%20Guide/FrameRate.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmrt).

The display hardware periodically captures data from sensors embedded in the screen. When a user touches the screen, the sensor information is recorded, processed, and delivered to UIKit. On displays that support 3D Touch, additional information about how much pressure the user applied to the display is also recorded. On displays that support Apple Pencil, the capture rate is different when an Apple Pencil is in use, and additional stylus information, such as the azimuth, is also recorded.

When the capture rate is higher than the delivery rate, multiple events are coalesced into one touch event whose location reflects the most recent touch. However, the additional touch information is available for apps that need more precision.

For more information on event handling, coalesced touches, 3D Touch, and Apple Pencil, see [UIKit](https://developer.apple.com/documentation/uikit).

[Next](Graphics%20Processors.md)[Previous](Device%20Compatibility.md)

