---
title: App Programming Guide for tvOS
apple_id: TP40015241
resource_type: Guide
platform: tvOS
topic: General
technology: null
published: '2017-01-12'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/AppleTV_PG/WorkingwithGameControllers.html
archived_at: '2026-07-15T07:33:07.804191Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Programming Guide for tvOS](index.md)



## Working with Game Controllers

Users can connect game controllers to Apple TV just as they do with iOS devices. When a game controller is connected to an Apple TV, the controller can also be used to control the focus-based user interface. Low-level controller inputs are automatically turned into higher-level events that are delivered through the responder chain. If your app relies solely on UIKit and focus interactions, you don’t need to do any work to support Game Controllers. Whether or not a user is using an Apple TV remote or a game controller is transparently handled for you by tvOS.

If you want to get low-level controller input, you use the Game Controller framework. See _[Game Controller Programming Guide](../../Game%20Controller%20Programming%20Guide/About%20Game%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenzw)_ for more information.

[Designing the Keyboard Input Experience](CreatingaGreatTextInputExperience.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbrfvbuqmjxfvjvomi)

[Creating Layered Images](CreatingParallaxArtwork.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbrfvbuqmjzfvjvomi)
