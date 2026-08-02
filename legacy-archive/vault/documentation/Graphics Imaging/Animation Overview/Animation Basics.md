---
title: Animation Overview
apple_id: TP40004952
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/Animation_Overview/AnimationBasics/AnimationBasics.html
archived_at: '2026-07-15T07:35:23.869359Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Animation Overview](Introduction%20to%20Animation%20Overview.md)


[Next](OS%20X%20Animation%20Technologies.md)[Previous](What%20Is%20Animation.md)

# Animation Basics

There are several fundamental attributes required of all animations: They must be associated with an object to animate, and they must define what type of animation will be performed and how long the animation will last.

This chapter discusses, in abstract terms, the basic animation techniques that are common to the OS X animation technologies.

Each animation must be associated with a visual element that the animation will affect. You can think of this as the animation target object. The animation target object provides the content that is displayed to the user. An animation will act either on the animation target object as a whole, or on a specific property of the target, for example, its location in the coordinate system or the color that it is drawn with.

Animations are associated with an animation target object. You don’t explicitly start an animation; the animation target object starts and stops the animation.

OS X animation supports three distinct types of animation: basic animation, keyframe animation, and transition animations.

__Basic animation__—also known as simple animation or single keyframe animation—progresses from a starting value to a target value through a series of intermediate values. These intermediate values are calculated, or interpolated, such that the animation occurs over a specified duration. Basic animation requires that you specify a property of the animation target object to animate.

Basic animation can be used with any value types that can be interpolated, including:

- integers and doubles
- `CGRect`, `CGPoint`, `CGSize`, and `CGAffineTransform` structures
- `CATransform3D` data structures
- `CGColor` and `CGImage` references

__Keyframe animation__ is similar to basic animation; however it allows you to specify an array of target values. Each of these target values is reached, in turn, over the duration of the animation. The keyframes of a keyframe animation can be any of the types supported by basic animation, or a Core Graphics path which is decomposed into a series of `CGPoint` objects by the animation. Like a basic animation, a keyframe animation requires that the animation act on a specific property of the animation target object.

Transition animations specify a visual effect that determines how the animation target object is displayed as it is made visible, or hidden. For example, making an animation target object visible may cause it to be pushed into view from the side of the display. Transition animations are performed by using __Core Image__ filters.

Because transition animations affect the animation target object as a whole, it is not necessary to specify a property of the target object.

The overall timing of an animation is determined by several factors: duration, pacing, and the repeating behavior.

__Duration__ is the length of time that an animation takes to get from the starting or current state to the target state, measured in seconds.

__Pacing__ of an animation determines how the interpolated values are distributed over the duration of the animation. For example, a single keyframe animation from 0 to 5 with a duration of 5 seconds and linear pacing causes the intermediate values to be spread out evenly over the duration. The same animation with a pacing of "EaseIn" causes the animation to begin slowly, and then speed up as the animation progresses. The animation takes the same duration and reaches the same values, but when each of the intermediate values are reached differs.

Animation repetition can be specified by in two ways: through a simple count of how many times the animation should repeat, or by setting a duration that the animation should repeat for. For example, specifying a repeat duration of 15 seconds would cause a 5-second animation to repeat three times. You can also specify that an animation should play forward, and then again in reverse, as it repeats.

[Next](OS%20X%20Animation%20Technologies.md)[Previous](What%20Is%20Animation.md)

