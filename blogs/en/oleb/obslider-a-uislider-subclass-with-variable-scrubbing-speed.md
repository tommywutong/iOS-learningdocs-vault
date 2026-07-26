---
title: OBSlider, a UISlider Subclass With Variable Scrubbing Speed
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/01/obslider-a-uislider-subclass-with-variable-scrubbing-speed/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:90df175410a81cdd'
translated: false
---

> 原文：[OBSlider, a UISlider Subclass With Variable Scrubbing Speed](https://oleb.net/blog/2011/01/obslider-a-uislider-subclass-with-variable-scrubbing-speed/)　·　Ole Begemann

# OBSlider, a UISlider Subclass With Variable Scrubbing Speed

The iPod app on the iPhone has a nice feature: the user can slow down the scrubbing speed of the time slider by moving their finger vertically while dragging the slider. Yesterday, [the question how to do this in our own code turned up on StackOverflow](http://stackoverflow.com/q/4579592/116862), which inspired me to find a solution. (By the way: I find this is an awesome way to improve my own coding skills. Find a question on SO that I cannot answer and try to work out a solution.)

The result is [`OBSlider`](https://github.com/ole/OBSlider), a drop-in replacement for `UISlider` with the addition of variable scrubbing speeds.

<sub>[Download the video](https://oleb.net/media/OBSliderDemo.mp4).</sub>

# How does it work?

`OBSlider` is a sublcass of `UISlider`. Subclassing UIKit classes is often a little tricky because the internals of the classes (especially what subviews they contain and how they track touches) are unknown and/or might change in future SDK releases. As a subclass of `UIControl`, `UISlider` handles its touch tracking quite transparently, though. `UISlider` inherits three methods from `UIControl` that subclasses are meant to override:

```
beginTrackingWithTouch:withEvent:
continueTrackingWithTouch:withEvent:
endTrackingWithTouch:withEvent:
```

The control receives these messages as touch event is being tracked. It is supposed to return `YES` when it is interested in tracking that particular touch, or `NO` otherwise. For the slider, that means a touch should only be tracked as long as it originated on the thumb button. By overriding these methods and inspecting the `tracking` property (inherited from `UIControl` as well), we can determine whether the current touch is dragging the slider. Then it is a simple matter of manually calculating the change in the slider’s value depending on the vertical offset of the touch:

```
- (BOOL) continueTrackingWithTouch:(UITouch *)touch withEvent:(UIEvent *)event
{
    if (self.tracking)
    {
        CGPoint previousLocation = [touch previousLocationInView:self];
        CGPoint currentLocation  = [touch locationInView:self];
        CGFloat trackingOffset = currentLocation.x - previousLocation.x;

        // Find the scrubbing speed that curresponds to the touch's vertical offset
        CGFloat verticalOffset = fabsf(currentLocation.y - self.beganTrackingLocation.y);
        NSUInteger scrubbingSpeedChangePosIndex = [self.scrubbingSpeedChangePositions indexOfObjectPassingTest:^(id obj, NSUInteger idx, BOOL *stop) {
            return (BOOL)(verticalOffset < [obj floatValue]);
        }];
        if (scrubbingSpeedChangePosIndex == NSNotFound) {
            scrubbingSpeedChangePosIndex = [self.scrubbingSpeeds count];
        }
        self.scrubbingSpeed = [[self.scrubbingSpeeds objectAtIndex:scrubbingSpeedChangePosIndex - 1] floatValue];

        CGRect trackRect = [self trackRectForBounds:self.bounds];
        self.value = self.value + self.scrubbingSpeed * (self.maximumValue - self.minimumValue) * (trackingOffset / trackRect.size.width);

        if (self.continuous) {
            [self sendActionsForControlEvents:UIControlEventValueChanged];
        }
    }
    return self.tracking;
}
```

# Customizing scrubbing speeds

To modify which scrubbing speed should be set at which vertical offset position of the user’s touch, you can modify the `scrubbingSpeeds` and `scrubbingSpeedChangePositions` arrays. Both arrays should contain the same number of objects. `scrubbingSpeedChangePositions` should indicate the vertical offsets at which scrubbing speed changes should take place in ascending order. The first entry in this array should always be `[NSNumber numberWithFloat:0.0f]`. `scrubbingSpeeds` should contain the actual values for the scrubbing speed that correspond to the offset positions.

The default values for the two arrays are:

```
scrubbingSpeeds = [NSArray arrayWithObjects:
    [NSNumber numberWithFloat:1.0f],
    [NSNumber numberWithFloat:0.5f],
    [NSNumber numberWithFloat:0.25f],
    [NSNumber numberWithFloat:0.1f],
    nil];

scrubbingSpeedChangePositions = [NSArray arrayWithObjects:
    [NSNumber numberWithFloat:0.0f],
    [NSNumber numberWithFloat:50.0f],
    [NSNumber numberWithFloat:100.0f],
    [NSNumber numberWithFloat:150.0f],
    nil];
```

(That is, scrubbing speed changes from 100% to 50% to 25% to 10% when the user moves the finger upward/downward by 50.0/100.0/150.0 points, respectively.)

# Get the code

I am releasing the code under the MIT license, so you can use it in your commercial and non-commercial projects. [Get in on GitHub](https://github.com/ole/OBSlider). Note that the code is basically untested ~~and currently only works on iOS 4.0 and higher (though adapting it to 3.0 would be trivial)~~. Please report bugs via GitHub’s issue tracker.

**Update January 5, 2010:** I modified the code above slightly to make it behave more like the slider in the iPod app. There, when you drag your finger towards the slider again, it accelerates to meet your finger at the slider. Also, [David Linsin](https://github.com/dlinsin) contributed a patch to make the class compatible with iOS 3.x. Thanks! Please get the updated code from GitHub.
