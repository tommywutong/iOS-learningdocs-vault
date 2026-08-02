---
title: Energy Efficiency Guide for iOS Apps
apple_id: TP40015243
resource_type: Guide
platform: watchOS|iOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/AvoidExtraneousGraphicsAndAnimations.html
archived_at: '2026-07-18T01:47:26.897795Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for iOS Apps](index.md)



## Avoid Extraneous Graphics and Animations

If your app uses only standard windows and controls, you probably don’t need to worry much about extraneous content updates, as the system APIs are designed to maximize energy efficiency. However, if you have custom windows and controls, be sure your drawing code performs efficiently. Your app shouldn’t refresh content unnecessarily, such as in obscured areas on screen, or through excessive use of animations.

Every time your app updates (or “draws”) content to screen, it requires the CPU, GPU, and screen to be active. Extraneous or inefficient drawing can pull system resources out of low-power states or prevent them from powering down altogether, resulting in significant energy use.

Follow these guidelines to optimize content refreshes:

- Reduce the number of views your app uses.
- Reduce the use of opacity, such as in views that exhibit a translucent blur. If you need to use opacity, avoid using it over content that changes frequently. Otherwise, energy cost is magnified, as both the background view and the translucent view must be updated whenever content changes.
- Eliminate drawing when your app or its content is not visible, such as when your app's content is obscured by other views, clipped, or offscreen.
- Use lower frame rates for animations whenever possible. For example, a high frame rate may make sense during game play, but a lower frame rate may be sufficient for a menu screen. Use a high frame rate only when the user experience calls for it.
- Use a consistent frame rate when performing an animation. For example, if your app displays 60 frames per second, maintain that frame rate throughout the lifetime of the animation.
- Avoid using multiple frame rates at once on screen. For example, don’t have a character in your game moving at 60 frames per second, while the clouds in the sky are moving at 30 frames per second. Use the same frame rate for both, even if it means raising one of the frame rates.
- Use recommended frameworks when developing games. These frameworks are optimized to provide great performance and optimal energy efficiency:

  - Use SpriteKit for 2D games. See _[SpriteKit Programming Guide](../../Graphics%20Animation/SpriteKit%20Programming%20Guide/About%20SpriteKit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbt)_ and _[SpriteKit Framework Reference](https://developer.apple.com/documentation/spritekit)_.
  - Use SceneKit for casual 3D games. See _[Scene Kit Framework Reference](https://developer.apple.com/documentation/scenekit)_ and _Scene Kit Functions Reference_.
  - Use Metal for highly immersive games. See _[Metal Programming Guide](../../Miscellaneous/Metal%20Programming%20Guide/About%20Metal%20and%20This%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrr)_, _[Metal Framework Reference](https://developer.apple.com/documentation/metal)_, and _Metal Functions Reference_.

> [!NOTE]
> 

[Voice Over IP (VoIP) Best Practices](OptimizeVoIP.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmzqfvjvomi)

[Restrict UI When Playing Full-Screen Video](HideControlsInFullScreenVideo.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmrqfvjvomi)
