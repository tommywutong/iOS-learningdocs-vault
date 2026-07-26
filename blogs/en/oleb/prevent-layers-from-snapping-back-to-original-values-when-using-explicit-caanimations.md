---
title: Prevent Layers From Snapping Back to Original Values When Using Explicit CAAnimations
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/11/prevent-caanimation-snap-back/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:bfd3f5356b1e76bf'
translated: false
---

> 原文：[Prevent Layers From Snapping Back to Original Values When Using Explicit CAAnimations](https://oleb.net/blog/2012/11/prevent-caanimation-snap-back/)　·　Ole Begemann

# Prevent Layers From Snapping Back to Original Values When Using Explicit CAAnimations

If you have used explicit `CALayer` animations in your code, you may have encountered the problem that the animated layer bounces back to its pre-animation state right after the animation finishes. For example, in the following simple example we animate a layer’s vertical position from its current state to a new value. As soon as the animation ends, the layer snaps back to its original location. In most cases, this is probably not what we want.

<sub>An explicit `CAAnimation` snaps back to the layer's original value as soon as the animation ends. [Download the video](https://oleb.net/media/CAAnimationSnapBack.mp4).</sub>

The code for this animation might look like this:

```
CABasicAnimation *animation = [CABasicAnimation animationWithKeyPath:@"position.y"];
animation.toValue = @300.0;
animation.duration = 1.0;
[layer addAnimation:animation forKey:@"positionAnimation"];
```

# Explicit Animations Only Affect the Presentation Layer

The reason for this behavior is that explicit `CAAnimation`s only affect the _presentation layer_ tree. The underlying _model layer_ tree remains unchanged. As long as the animation is running, it assigns interpolated position values to the presentation layer, which is used for displaying the scene on screen. However, when the animation has finished the presentation layer automatically reverts back to the values of its corresponding model layer, which causes the sudden bounce back to the layer’s original position on screen.

To solve the problem, we have to explicitly change the model layer’s `position` property.[1](#fn:1) Unfortunately, doing so just before or after adding the animation to the layer overrides the animation and causes the layer to snap to its new position with no animation at all. Now that we have changed the model value before running the animation, the animation’s `fromValue` and `toValue` are identical, resulting in an “animation” without movement.

To avoid this, save the original model value before changing it and explicitly set the animation’s `fromValue`:

```
// Save the original value
CGFloat originalY = layer.position.y;

// Change the model value
layer.position = CGPointMake(layer.position.x, 300.0);

CABasicAnimation *animation = [CABasicAnimation animationWithKeyPath:@"position.y"];

// Now specify the fromValue for the animation because
// the current model value is already the correct toValue
animation.fromValue = @(originalY);
animation.duration = 1.0;

// Use the name of the animated property as key
// to override the implicit animation
[layer addAnimation:animation forKey:@"position"];
```

# Override the Implicit Animation

Note a third modification I made to the code: The key passed to the `-addAnimation:forKey:` method is usually an arbitrary string (or even `nil`) you can use to later identify a specific animation. Here, I used the name of the property our animation changes (`@"position"`) for the key argument. This makes sure that any implicit animation that has been created by the modification of the model value gets overridden with our explicit animation.

Had we used a different key for the explicit animation, it’s possible that Core Animation would have to deal with two conflicting animations at the same time.

# WWDC Video

Also check out the [video for WWDC 2010](https://developer.apple.com/videos/) session 424 (Core Animation in practice, part 1) where Apple engineers explain this around the 40:00 minute mark.

1. If you search the web for this problem, you will find other “solutions”, such as setting the animation’s `fillMode` property to `kCAFillModeForwards` and at the same time setting `removedOnCompletion` to `NO`. This seems to fix the cause of the issue when in fact it only hides the symptoms. This approach basically lets the animation live forever – and show the layer in its target position as long as it lives on. However, when you query the model layer, it will still return its original value. And you may also run into problems as soon as you set up another animation for the same property. [↩︎](#fnref:1)
