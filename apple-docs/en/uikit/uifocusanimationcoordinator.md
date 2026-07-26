---
title: UIFocusAnimationCoordinator
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusanimationcoordinator
source_url: 'https://developer.apple.com/documentation/uikit/uifocusanimationcoordinator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusanimationcoordinator.json'
content_hash: 'sha256:bd4bd2cfe3278f83'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFocusAnimationCoordinator

<sub>Class</sub>

A coordinator of focus-related animations during a focus update.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIFocusAnimationCoordinator
```

## Overview

[UIFocusAnimationCoordinator](uifocusanimationcoordinator.md) instances are always created by the system and vended to your app during a focus update, and are typically discarded after the update is complete; it is not useful to instantiate [UIFocusAnimationCoordinator](uifocusanimationcoordinator.md) objects yourself. The `UIFocus.h` header file, including its related classes and its protocol, creates a single high-level software interface for controlling focus in apps that use focus-based input. This programming interface also helps to control focus behavior on the screen.

When a focus update occurs, two main animations happen: the previously focused view animates to an unfocused state, and the next focused view animates to a focused state. The purpose of the animation coordinator is to allow other views to coordinate their animations along with the primary animations of the previously or next focused views. Every animation added to the coordinator will run together in the same animation block, with the same timing, and options.

For example, suppose a user interface consists of an focusable image with a title underneath. When the image is focused, it will animate expanding its size to a larger, focused state, so it schedules an animation using the [UIFocusAnimationCoordinator](uifocusanimationcoordinator.md) instance provided during the focus update. Since the image is expanding, the title should also animate its position to stay a fixed length from the expanding bottom edge of the image, so it also schedules this animation using the coordinator. Since both animations were scheduled using the coordinator, they will be run together at the end of the update to ensure they are correctly synchronized.

It is important to schedule animations using [UIFocusAnimationCoordinator](uifocusanimationcoordinator.md) because the properties of the animation are defined by the system to achieve certain system-level behaviors. For example, when focus is moving quickly, the timing of the animations are sped up to keep up with the user’s movement. In addition, _focusing_ animations typically run faster than _unfocusing_ animations, to create a trail effect as the user moves. As such, you should never assume a fixed duration across multiple focus updates, nor should you that timing of animations for different views in different branches of the view hierarchy is the same.

If you need more control over the timing of focus-related animations, you can add a nested animation block inside the coordinated animation. This follows all the same rules as regular nested animations, meaning that the animation duration and properties are inherited. Use [AnimationOptions](uiview/animationoptions.md)– set of options- to edit as necessary. If you want to change the timing of the animation, it is recommended that you specify a duration relative to the inherited duration in [inheritedAnimationDuration](uiview/inheritedanimationduration.md) method, so that your application still benefits from the timing behaviors.

For example, in the below code listing it shows how to add a coordinated animation that should run at half the system-defined duration:

```objc
 override func didUpdateFocusInContext(context: UIFocusUpdateContext, withAnimationCoordinator coordinator: UIFocusAnimationCoordinator) {
 coordinator.addCoordinatedAnimations({
            let duration : NSTimeInterval = UIView.inheritedAnimationDuration();
            UIView.animateWithDuration((0.5*duration), delay: 0.0, options: UIViewAnimationOptions.OverrideInheritedDuration, animations: {
                //add your animations
                }, completion: nil)
            }, completion: nil)
```

However, if you nest animations with different durations, note that the completion block of the [- addCoordinatedAnimations:completion:](<uifocusanimationcoordinator/addcoordinatedanimations(__completion_).md>) method is run only after the main (inherited) animation is complete.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Adding animations to focus updates

- [- addCoordinatedFocusingAnimations:completion:](<uifocusanimationcoordinator/addcoordinatedfocusinganimations(__completion_).md>) — Runs the specified set of animations together with the system animations for adding focus to an item.
- [- addCoordinatedUnfocusingAnimations:completion:](<uifocusanimationcoordinator/addcoordinatedunfocusinganimations(__completion_).md>) — Runs the specified set of animations together with the system animations for removing focus from an item.
- [- addCoordinatedAnimations:completion:](<uifocusanimationcoordinator/addcoordinatedanimations(__completion_).md>) — Specifies the animations to coordinate with the active focus animation.
- [UIFocusAnimationContext](uifocusanimationcontext.md) — Information about focusing animations being performed by the system.
