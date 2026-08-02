---
title: Dashboard Programming Topics
apple_id: TP40002837
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: null
published: '2010-02-01'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/Articles/AppleAnimator.html
archived_at: '2026-07-15T05:17:17.441289Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashboard Programming Topics](Introduction%20to%20Dashboard%20Programming%20Topics.md)


[Next](Using%20an%20Apple%20Button.md)[Previous](Using%20an%20Apple%20Slider.md)

# Using Animation

Apple provides a JavaScript class that functions as an animation timer, useful for animating fading elements or a series of images. The classes that provide this, `AppleAnimator` and `AppleAnimation`, are part of the Apple Classes included in OS X v10.4.3 and later.

For more on using all of the Apple Classes, including `AppleAnimator` and `AppleAnimation`, read [Introduction to the Apple Classes](Introduction%20to%20the%20Apple%20Classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcobwfvjvomi).

Providing an animation in your widget can be achieved using the `AppleAnimator` and `AppleAnimation` classes. `AppleAnimator` is a timer that fires at designated intervals for a defined duration. The `AppleAnimation` contains a set of values and a handler. As `AppleAnimations` are added to `AppleAnimators`, values in the animation's range are provided to the handler each time the animator fires. To use animators and animations, you need to:

- Include the `AppleAnimator` class in your HTML file
- Construct an animator timer
- Construct an animation
- Provide a handler used to act when the timer fires

In order to declare `AppleAnimator` and `AppleAnimation` objects and use them in JavaScript, you need to include the class in your widget's HTML file. If you're planning backward compatibility with pre-OS X v.10.4.3 versions, follow the directions in [Backwards Compatible Usage](Introduction%20to%20the%20Apple%20Classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcobwfvjvomq) and include this path:

```
<script type='text/javascript' src='AppleClasses/AppleAnimator.js' charset='utf-8'/>
```

If you plan on requiring OS X v.10.4.3 or newer for your widget, include the `AppleAnimation` class in its location in `/System/Library/WidgetResources/`:

```
<script type='text/javascript' src='/System/Library/WidgetResources/AppleClasses/AppleAnimator.js' charset='utf-8'/>
```


There are two ways to set up the animation timers and associated animation ranges within your widget's JavaScript:

- Full setup, allowing you to associate multiple ranges of values with one timer
- Quick setup, allowing you to easily create a timer and an associated range of values

The `AppleAnimator` and `AppleAnimation` classes have no default appearance and provide no actual animations; instead, they provide numerical values that can be useful when animating elements in your widget's user interface. For instance, if you have elements that fade, resize, or change over time, these classes can provide you with relevant values over time.

The `AppleAnimator` class provides an object that functions as a timer. Its constructor takes in two parameters, the length of time that the timer should fire over, and the interval at which the timer should fire, both in milliseconds:

```
currentAnimator = new AppleAnimator(500, 13);
```

In this instance, the timer, when activated, lasts for 500 milliseconds and fires every 13 milliseconds.

Now that the timer has been created, the animation range needs to be as well. The constructor for the `AppleAnimation` class takes three values: a starting value, a finishing value, and a handler:

```
currentAnimation = new AppleAnimation(0.0, 1.0, animationHandler);
```

This animation provides values between `0.0` and `1.0` and, whenever its timer fires, calls a handler function called `animationHandler`. The handler for the animation needs to accept four arguments: the animator that is processing the animation, the current value of the animation, the animation's starting value, and its finishing value.

```
function animationHandler(currentAnimator, current, start, finish)
{
... // do something with a current value
}
```

Now that the animation is set up, it needs to be associated with a timer:

```
currentAnimator.addAnimation(currentAnimation);
```

By adding, or associating, the animation with the timer, the timer calls the animation's handler whenever it fires. When the timer fires and provides the appropriate value for the interval, based on the animation's range mapped to the duration of the timer. Each animator can be associated with multiple animations, allowing you to track multiple sets of values with one timer.

At this point, the timer and the animation are ready to be run. To begin the timer, send it the start message:

```
currentAnimator.start();
```

Additionally, you can stop a time at any point by calling `stop()` on the animator:

```
currentAnimator.stop();
```


The previous section described how to perform a full setup of an `AppleAnimator` timer and an `AppleAnimation`. This allows you to include multiple animations with one animator and is appropriate for circumstances where one animation is associated with one animator.

The `AppleAnimator` constructor, however, allows you to specify animation specifications in addition to its usual parameters. This allows you to bypass having a separate `AppleAnimation` object, useful for when you only need one animation:

```
AppleAnimator(duration, interval, start, finish, handler)
```

The first two values, `duration` and `interval`, are the duration of the timer and how often it fires. The next two values, `start` and `finish`, are the starting and finishing values of the range of numbers that are calculated as the timer runs. Finally, `handler` is the name of the function that you provide; it is called whenever the timer fires:

```
function handler(currentAnimator, current, start, finish)
{
... // do something with a current value
}
```

As with the animation handler above, this handler needs to accept four arguments: the animator that is processing the animation, the current value of the animation, the animation's starting value, and its finishing value.

To start the animation and the animator's timer, call `start()` on the animator:

```
currentAnimator.start();
```

After starting the animator's timer, the `handler` function is called every interval until the end of the animator's duration is finished. The `current` value passed to `handler` reflects an increasing value between `start` and `finish`. To stop the animator's timer before it has run out, call `stop()`:

```
currentAnimator.stop();
```


These properties are available to an `AppleAnimator` object:

| Property | Description |
| --- | --- |
| `animator.duration` | The duration of the animator's timer |
| `animator.interval` | The interval at which the animation's handler is called |
| `animator.animations` | An array of the Apple Animation objects associated with an animator |
| `animator.timer` | The current value of the timer |
| `animator.oncomplete` | A handler called when the timer is complete |

These properties are available to an `AppleAnimation` object:

| Property | Description |
| --- | --- |
| `animation.from` | The animation's starting value |
| `animation.to` | The animation's finishing value |
| `animation.now` | The animation's current value |
| `animation.callback` | The handler for the animation |

The `AppleRectangleAnimation` subclass provides values useful when transitioning between two rectangles (the subclass has no default appearance). An `AppleRectangleAnimation` uses the `AppleAnimator` timer to trigger its handlers, but require that starting and finishing rectangles be specified as Apple Rectangles, using the `AppleRect` subclass.

An `AppleRect` is defined as:

```
AppleRect(left, top, right, bottom)
```

The rectangle is specified by its top left and bottom right coordinates. To create a new `AppleRect` object, call its constructor and assign the resulting object into a variable:

```
startingRect = new AppleRect( 0, 0, 100, 100 );
```

Once you have created a starting and finishing rectangle, create an `AppleRectAnimation` object, passing in the two `AppleRect` objects and the name of a handler that's to be called when the rectangle animation's animator timer fires:

```
currentRectAnimation = new AppleRectAnimation( startingRect, finishingRect, rectHandler );
```

The rectangle animation handler you provide needs to accept four arguments: the rectangle animation that triggered the handler, an `AppleRect` object with the current rectangle values, the starting `AppleRect` object, and the finishing `AppleRect` object:

```
function rectHandler( rectAnimation, currentRect, startingRect, finishingRect );
```

Once the `AppleRectangleAnimation` object is created, construct a new `AppleAnimator` object, associate it with your rectangle animation, and start the animator's timer:

```
currentAnimator = new AppleAnimator (500, 13);
currentAnimator.addAnimation(currentRectAnimation);
currentAnimator.start();
```


These properties are available to an `AppleRectangleAnimator` object:

| Property | Description |
| --- | --- |
| `rectAnimation.from` | The animation's starting rectangle |
| `rectAnimation.to` | The animation's finishing rectangle |
| `rectAnimation.now` | The animation's current rectangle |
| `rectAnimation.callback` | The handler for the animation |

These properties are available to an `AppleRect` object:

| Property | Description |
| --- | --- |
| `rectangle.left` | The rectangle's left value, of the top left corner of the rectangle |
| `rectangle.top` | The rectangle's top value, of the top left corner of the rectangle |
| `rectangle.right` | The rectangle's right value, of the bottom right corner of the rectangle |
| `rectangle.bottom` | The rectangle's bottom value, of the bottom right corner of the rectangle |

[Next](Using%20an%20Apple%20Button.md)[Previous](Using%20an%20Apple%20Slider.md)

