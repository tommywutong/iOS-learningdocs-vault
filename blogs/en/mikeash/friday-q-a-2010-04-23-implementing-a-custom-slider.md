---
title: 'Friday Q&A 2010-04-23: Implementing a Custom Slider'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-04-23-implementing-a-custom-slider.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d206d800d5e6db4e'
translated: false
---

> 原文：[Friday Q&A 2010-04-23: Implementing a Custom Slider](https://www.mikeash.com/pyblog/friday-qa-2010-04-23-implementing-a-custom-slider.html)　·　mikeash.com Friday Q&A

Posted at 2010-04-23 16:01 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-04-30: Dealing with Retain Cycles](https://www.mikeash.com/pyblog/friday-qa-2010-04-30-dealing-with-retain-cycles.html)  
Previous article: [Mistakes and Chains of Events](https://www.mikeash.com/pyblog/mistakes-and-chains-of-events.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [controls](https://www.mikeash.com/pyblog/?tag=controls) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2010-04-23: Implementing a Custom Slider

by [Mike Ash](https://www.mikeash.com/)

Specifically, he requested a diagonal slider. This slider works much like a regular Cocoa slider, except that it's oriented diagonally. To make the example more useful, I implemented it completely from scratch rather than trying to base it off of NSSlider (which would probably not be very easy for this anyway).

**Getting the Code**  
 As usual, the code that I wrote for this post is available in my Subversion repository:

```
    svn co http://mikeash.com/svn/DiagonalSlider/
```

Or just click the URL above to browse the source.

**Planning**  
 When building a custom control, it's helpful to break your tasks down as much as possible. The concept of building a custom control can be daunting, but when broken into small pieces, each small piece can become easy.

There are three main pieces to any custom control:

1. **Drawing:** The code with which the control draws itself. As controls are just views, this usually means implementing `drawRect:` to draw whatever you want your control to look like. In the case of the diagonal slider, it needs to draw the slider track and the knob.
2. **Event Tracking:** This involves getting and responding to events. In this case, looking at mouse down/dragged/up events and moving the slider knob around appropriately.
3. **Geometry:** This is code which figures out where the various components of the control are located. The geometry information is then used by the drawing and event tracking code to figure out where to draw things and where events are in the control. In this case, the geometry code consists of figuring out where the slider track is, where the knob is, and converting from a point to a slider value.

**Interface**  
 Before getting into the implementation, let's define the interface of the class. It will subclass `NSControl`. It will implement `setDoubleValue:` and `doubleValue` to return its position. For instance variables, it needs to store its value. Also, because `NSControl` tends to assume that you have an `NSCell`, and I don't want to build a cell, I also need instance variables to hold the control's target and action:

```
    @interface DiagonalSlider : NSControl
    {
        double _value;
        id _target;
        SEL _action;
    }
    
    - (void)setDoubleValue: (double)value;
    - (double)doubleValue;
    
    @end
```

**Geometry**  
 Since magic numbers are evil, the first thing I do for the geometry code is define some constants that determine the geometry of the control. The slider will extend from the bottom left corner to the top right corner of the control, but the ends need to be inset a bit to allow room to draw the slider and knob. These insets are defined here. The slider width and knob size are also defined as constants:

```
    const CGFloat kInsetX = 12;
    const CGFloat kInsetY = 12;
    const CGFloat kSliderWidth = 6;
    const CGFloat kKnobRadius = 10;
```

Now for some actual code. A major theme you'll see here is building up small methods, where each method computes a single value, relying on other methods for intermediate results. This helps enormously with simplifying the task of programming the control.

First, two methods for getting the slider endpoints:

```
    - (NSPoint)_point1
    {
        return NSMakePoint(kInsetX, kInsetY);
    }
    
    - (NSPoint)_point2
    {
        NSRect bounds = [self bounds];
        return NSMakePoint(NSMaxX(bounds) - kInsetX, NSMaxY(bounds) - kInsetY);
    }
```

Next, finding the center of the knob. To do that, I just take a weighted average of the two endpoints, using `_value` as the weight:

```
    - (NSPoint)_knobCenter
    {
        NSPoint p1 = [self _point1];
        NSPoint p2 = [self _point2];
        
        return NSMakePoint(p1.x * (1.0 - _value) + p2.x * _value, p1.y * (1.0 - _value) + p2.y * _value);
    }
```

Next I create a method that returns an `NSBezierPath` that describes the knob. You might think that this belongs in drawing, not geometry. However, I plan to use this path not only for drawing the knob, but also for determining whether the mouse is within the knob or not. Conceptually, this bezier path is part of the common geometry code:

```
    - (NSBezierPath *)_knobPath
    {
        NSRect knobR = { [self _knobCenter], NSZeroSize };
        return [NSBezierPath bezierPathWithOvalInRect: NSInsetRect(knobR, kKnobRadius, kKnobRadius)];
    }
```

Next, I'll write code to determine the slider value that corresponds to a point, and whether the slider track contains a point. In order to write those, I need some utility functions. Specifically, I need vector subtraction, vector dot product, and vector length. To keep things simple, I use `NSPoint` as my "vector" type. These three utility functions are then easy to write:

```
    static NSPoint sub(NSPoint p1, NSPoint p2)
    {
        return NSMakePoint(p1.x - p2.x, p1.y - p2.y);
    }
    
    static CGFloat dot(NSPoint p1, NSPoint p2)
    {
        return p1.x * p2.x + p1.y * p2.y;
    }
    
    static CGFloat len(NSPoint p)
    {
        return sqrt(p.x * p.x + p.y * p.y);
    }
```

Now, code for determining the value for a point. The math here is not complex, but may not be obvious. I start by doing a [vector projection](http://en.wikipedia.org/wiki/Vector_projection) of the vector from the slider start to the point in question onto the vector of the slider itself. This projection gives me the distance of the point in question from the slider start in the direction of the slider, ignoring any side component. I then divide this length by the length of the slider, and that gives me a proportion. I want the value to be between 0 and 1, so that number is exactly what I want. Here's the code:

```
    - (double)_valueForPoint: (NSPoint)p
    {
        // vector from slider start to point
        NSPoint delta = sub(p, [self _point1]);
        
        // vector of slider
        NSPoint slider = sub([self _point2], [self _point1]);
        
        // project delta onto slider
        CGFloat projection = dot(delta, slider) / len(slider);
        
        // value is projection length divided by slider length
        return projection / len(slider);
    }
```

Finally, I need code for determining whether a point is within the slider track. (This is used to determine whether a mouse click was on the slider track, and should be responded to, or whether it was outside.)

The concept for this code is similar. First, I use `_valueForPoint:` to see if the point is off the ends of the slider. If it is, instant rejection. Otherwise, I see how far to the side the point is from the slider. If this distance is within the slider width, then the point is contained by the slider.

Finding that distance is similar to the above code. Instead of projecting onto the slider's vector, I project onto a vector perpendicular to the slider. The length of that projection is the distance from the middle of the slider track:

```
    - (BOOL)_sliderContainsPoint: (NSPoint)p
    {
        // if beyond the ends, then it's not contained
        double value = [self _valueForPoint: p];
        if(value < 0 || value > 1)
            return NO;
        
        // vector from slider start to point
        NSPoint delta = sub(p, [self _point1]);
        
        // vector of slider
        NSPoint slider = sub([self _point2], [self _point1]);
        
        // vector of perpendicular to slider
        NSPoint sliderPerp = { -slider.y, slider.x };
        
        // project delta onto perpendicular
        CGFloat projection = dot(delta, sliderPerp) / len(sliderPerp);
        
        // distance to slider is absolute value of projection
        // see if that's within the slider width
        return fabs(projection) <= kSliderWidth;
    }
```

**Drawing**  
 With all of these geometry methods, drawing is a snap. First, I draw a line between `_point1` and `_point2`. Then I get the `_knobPath` and fill it. And that's it!

Note that I'm going for technical information, not graphical prettiness, so my slider is ugly. The track is just a blue line, and the knob is just a red circle. Making it beautiful is up to you!

Here's what the drawing code looks like:

```
    - (void)drawRect: (NSRect)r
    {
        NSBezierPath *slider = [NSBezierPath bezierPath];
        [slider moveToPoint: [self _point1]];
        [slider lineToPoint: [self _point2]];
        [slider setLineWidth: kSliderWidth];
        
        [[NSColor blueColor] setStroke];
        [slider stroke];
        
        [[NSColor redColor] setFill];
        [[self _knobPath] fill];
    }
```

**Event Tracking**  
 For tracking a mouse down/dragged/up sequence, there are two ways to do things.

One way is to implement `mouseDown:`, `mouseDragged:`, and `mouseUp:`, to do what you need in each situation. The other way is to only implement `mouseDown:`, then run your own event loop inside that to look for dragged/up events.

This second way is how most (possibly all) Apple controls work, and in my opinion generally works better. You often have state which is generated by the mouse down event, and then needs to be referenced by the dragged/up handlers, and this is easier to manage when everything is in the same place instead of scattered through several different methods. The dragged and up code is also often similar, and a single event loop allows consolidating the two cases. Because I think this way is superior, that's how `DiagonalSlider` will handle event tracking.

To do this, implement `mouseDown:`. First, figure out whether to handle the event or not. In the case of the slider, we want to handle the event if the click was in the knob or slider track, but not if it fell outside them. Handle any necessary setup, then start the inner event loop.

The slider has two cases which act slightly differently. One case is clicking in the knob itself, which does nothing to begin with, then moves the knob relative to the mouse's movements. The other case is clicking directly in the slider track, which jumps the knob to that position, then tracks further movement.

These two cases handle the same tracking at the end, but have slightly different setup. To facilitate this, I split most of the tracking into a separate method, `_trackMouseWithStartPoint`, which can then be called by these two cases.

The `mouseDown:` method first gets the location of the event, then sees if it's within the knob. If it is, then it just goes straight to tracking:

```
    - (void)mouseDown: (NSEvent *)event
    {
        NSPoint p = [self convertPoint: [event locationInWindow] fromView: nil];
        
        if([[self _knobPath] containsPoint: p])
        {
            [self _trackMouseWithStartPoint: p];
        }
```

Otherwise, it checks to see if the event is within the slider track. If it is, then it jumps the value to the current mouse position. It also sends the slider's action, to notify the target that the slider moved immediately. It then starts tracking:

```
        else if([self _sliderContainsPoint: p])
        {
            [self setDoubleValue: [self _valueForPoint: p]];
            [self sendAction: [self action] to: [self target]];
            [self _trackMouseWithStartPoint: p];
        }
    }
```

If the event is not within the knob or slider, then it's just ignored.

Now for the actual event tracking. The first thing to do is compute a value offset. This is the difference between the slider's current value, and the value which corresponds to the location of the initial mouse down event. The purpose of this is to preserve the distance between the slider knob's center and the mouse cursor. If you click on the edge of the knob and drag, your cursor should stay on the edge, not have the knob suddenly jump to be centered. Note that this is only necessary when clicking the knob, not the track. However, when clicking the track, this value will be `0` and thus do nothing, so it's not necessary to conditionalize the code:

```
    - (void)_trackMouseWithStartPoint: (NSPoint)p
    {
        // compute the value offset: this makes the pointer stay on the
        // same piece of the knob when dragging
        double valueOffset = [self _valueForPoint: p] - _value;
```

Next, start the event loop. This consists of calling `-[NSWindow nextEventMatchingMask:]` in a loop, until a `NSLeftMouseUp` event is received. I also toss in an `NSAutoreleasePool` to ensure that memory doesn't build up if the loop continues for a long time:

```
        // create a pool to flush each time through the cycle
        NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
        // track!
        NSEvent *event = nil;
        while([event type] != NSLeftMouseUp)
        {
            [pool release];
            pool = [[NSAutoreleasePool alloc] init];
            
            event = [[self window] nextEventMatchingMask: NSLeftMouseDraggedMask | NSLeftMouseUpMask];
```

Once the event comes in, figure out where it is, set the slider's value appropriately, and send the action:

```
            NSPoint p = [self convertPoint: [event locationInWindow] fromView: nil];
            double value = [self _valueForPoint: p];
            [self setDoubleValue: value - valueOffset];
            [self sendAction: [self action] to: [self target]];
        }
```

And that's it for this method, just dump the last autorelease pool and exit:

```
        [pool release];
    }
```

**Miscellaneous**  
 The slider needs a bit more support code. The only one that does anything of consequence is `setDoubleValue:`. It performs several tasks. First, it clamps the incoming value to be between 0 and 1. Then it assigns the value, and finally marks the control as needing a redisplay, so that the GUI updates accordingly. Note that simply redisplaying the entire view is somewhat inefficient, and it would be better to compute a minimal changed rect. However, in the spirit of avoiding premature optimization, I didn't do this.

```
    - (void)setDoubleValue: (double)value
    {
        // clamp to [0, 1]
        value = MAX(value, 0);
        value = MIN(value, 1);
        
        _value = value;
        [self setNeedsDisplay: YES];
    }
```

I also have a few one-liners to return the value, and handle target/action:

```
    - (double)doubleValue
    {
        return _value;
    }
    
    - (void)setTarget: (id)anObject
    {
        _target = anObject;
    }
    
    - (id)target
    {
        return _target;
    }
    
    - (void)setAction: (SEL)aSelector
    {
        _action = aSelector;
    }
    
    - (SEL)action
    {
        return _action;
    }
```

And that's it!

**Using the Slider**  
 Using this custom slider is much like using any other control, just with somewhat worse Interface Builder support. To create the slider in IB, you have to drag out a plain `NSView`, then set the class of that view to `DiagonalSlider`. IB doesn't know what a `DiagonalSlider` looks like, so it'll still show up as a plain box, but it will work correctly at runtime. IB is smart enough to notice that `DiagonalSlider` is an `NSControl` subclass, and thus allows you to set the target/action of the slider right in the nib. Convenient!

Implement the action as you would for any other control. Then you can fetch the slider's current value using `doubleValue`. Update its value using `setDoubleValue:`. And that's it!

**Conclusion**  
 Building a custom control in Cocoa can be a daunting task, but if you break it down into components and build the control up from small pieces, it's really not that hard. By separating the code into geometry, drawing, and tracking sections, and buildingu p each section from parts, building a custom control can become relatively straightforward.

That's it for this edition of Friday Q&A. Come back next week for another one. Until then, keep sending your ideas for topics. Friday Q&A is driven by user ideas, so if you'd like to see a particular topic covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-04-23-implementing-a-custom-slider.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
