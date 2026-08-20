---
title: Core Animation Cookbook
apple_id: TP40005406
resource_type: Guide
platform: iOS|macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreAnimation_Cookbook/Articles/Timing.html
archived_at: '2026-07-15T07:35:28.372967Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Animation Cookbook](Core%20Animation%20Cookbook.md)


[Next](Document%20Revision%20History.md)[Previous](Drawing.md)

# Timing

This chapter discusses timing issues when using Core Animation.

The `CAKeyframeAnimation` class provides a powerful means of animating layer properties. However, `CAKeyframeAnimation` does not allow you to specify a single animation timing function that is used for the entire path. Instead you are required to specify the timing using the [keyTimes](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412522-keytimes) property, or by specifying an array of timing functions in the [timingFunctions](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412465-timingfunctions) property.

You can provide a single timing function for the animation by grouping the keyframe animation in a `CAAnimationGroup`, and setting the group animation’s timing function to the desired [CAMediaTimingFunction](https://developer.apple.com/documentation/quartzcore/camediatimingfunction). The animation group’s timing function and duration take precedence over the keyframe animation’s timing properties.

A code fragment that implements this strategy is shown in Listing 1.

__Listing 1__  Using a single timing function for a keyframe animation

```
// create the path for the keyframe animation
CGMutablePathRef thePath = CGPathCreateMutable();
CGPathMoveToPoint(thePath,NULL,15.0f,15.f);
CGPathAddCurveToPoint(thePath,NULL,
                      15.f,250.0f,
                      295.0f,250.0f,
                      295.0f,15.0f);

// create an explicit keyframe animation that
// animates the target layer's position property
// and set the animation's path property
CAKeyframeAnimation *theAnimation=[CAKeyframeAnimation

                                      animationWithKeyPath:@"position"];
theAnimation.path=thePath;

// create an animation group and add the keyframe animation
CAAnimationGroup *theGroup = [CAAnimationGroup animation];
theGroup.animations=[NSArray arrayWithObject:theAnimation];

// set the timing function for the group and the animation duration
theGroup.timingFunction=[CAMediaTimingFunction

                                functionWithName:kCAMediaTimingFunctionEaseIn];
theGroup.duration=15.0;
// release the path
CFRelease(thePath);


// adding the animation to the target layer causes it
// to begin animating
[theLayer addAnimation:theGroup forKey:@"animatePosition"];
```

[Next](Document%20Revision%20History.md)[Previous](Drawing.md)

