---
title: CGPath Hit Testing
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/02/cgpath-hit-testing/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:0aa782ebc7971875'
translated: false
---

> 原文：[CGPath Hit Testing](https://oleb.net/blog/2012/02/cgpath-hit-testing/)　·　Ole Begemann

# CGPath Hit Testing

In OS X 10.7 and iOS 5.0, Apple added an inconspicuous new function named [`CGPathCreateCopyByStrokingPath()`](https://developer.apple.com/library/ios/documentation/graphicsimaging/Reference/CGPath/Reference/reference.html#//apple_ref/doc/uid/TP30000959-CH1g-SW6) to the Core Graphics framework. As the documentation says and the name implies, this function

> [c]reates a stroked copy of another path. … The new path is created so that filling the new path draws the same pixels as stroking the original path.

Sounds like a pretty obscure function that is rarely needed but in fact, this functionality can be extremely useful for a number of problems:

1. **Stroking a path with fancy graphics.** You can normally only stroke a path with a single color. If you want to do something fancier like, say, draw a gradient, `CGPathCreateCopyByStrokingPath()` lets you convert the area that would be stroked into a new path. You can then use this new path as the clipping path for the gradient you want to draw.
2. **Stroking a stroke.** If you want to draw a stroke around a path’s stroke, use `CGPathCreateCopyByStrokingPath()` to create a new path from the original path’s stroke, and stroke the new path.
3. **Hit testing.** The `CGPath` APIs can only help you if you want to hit test the for _interior_ of a path, not if your hit target is the path’s contour. Since `CGPathCreateCopyByStrokingPath()` can convert the countour into a new path’s interior, it can help with this problem, too.

In this article, I want to show you an example app that covers the second and third of these problems.

# The Demo App

Imagine you have a vector drawing app that lets the user draw both regular shapes like rectangles and ellipses and “irregular” ones like freeform paths and bezier curves. In your app, you represent the shapes that make up the current document with an array of `CGPath` objects (or an array of [`UIBezierPath`](https://developer.apple.com/library/IOs/#documentation/UIKit/Reference/UIBezierPath_class/Reference/Reference.html) (iOS)/[`NSBezierPath`](https://developer.apple.com/library/mac/#documentation/Cocoa/Reference/ApplicationKit/Classes/NSBezierPath_Class/Reference/Reference.html) (Mac) objects, which themselves wrap a `CGPath` – the difference is not important for this discussion).

The user can add new (random) shapes to the view, select shapes by tapping on their outline, drag shapes across the view and delete a selected shape. Watch this short video for an overview:

<sub>The sample iPad app. [Download the video](https://oleb.net/media/CGPathHitTestingDemoApp.mp4) (H.264, 2 MB).</sub>

The source code for the demo app is [available on GitHub](https://github.com/ole/CGPathHitTesting).

# Hit Testing with `CGPathCreateCopyByStrokingPath`

First, let’s deal with hit testing: the user should be able to select a shape by tapping on it. That means we need to figure out if a view coordinate (tap location) lies on one or more paths. To help you with this, the `CGPath` API provides the [`CGPathContainsPoint()`](https://developer.apple.com/library/ios/documentation/graphicsimaging/Reference/CGPath/Reference/reference.html#//apple_ref/doc/uid/TP30000959-CH1g-CJBGIGEF) function[1](#fn:1), which

> [c]hecks whether a point is contained in a graphics path. … A point is contained in a path if it would be inside the painted region when the path is filled.

This function is helpful if you want to hit test on the entire region the path covers. As such, `CGPathContainsPoint()` doesn’t work with unclosed paths because those don’t have an interior that would be filled. The method of selecting shapes by tapping anywhere in their interior can also be problematic from a user interface perspective? What if the user taps at a location where multiple shapes overlap? What shape should the app select?

Such ambiguities can be minimized if shape selection only works on the shape’s outline and not its entire interior.[2](#fn:2) And here is where `CGPathCreateCopyByStrokingPath()` comes into play: whenever the user creates or modifies a shape, we call `CGPathCreateCopyByStrokingPath()` on it to create a mirroring `tapTarget` object that only covers the stroked area of the path (ensuring a certain minimum width to make the tap target big enough). When the user taps on the screen, we iterate over the tap targets rather than the actual shapes, now using `CGPathContainsPoint()` on the area that would be filled by the shape’s outline, to determine which shape was selected. In the sample app, the `Shape` class contains a method named `tapTargetForPath:` that generates such a tap target for a given `path` object (which is a `UIBezierPath` in this instance). Note that I am using a minimum width of 35 points for the tap target, regardless of the path’s `lineWidth`:

```
- (UIBezierPath *)tapTargetForPath:(UIBezierPath *)path
{
    if (path == nil) {
        return nil;
    }

    CGPathRef tapTargetPath = CGPathCreateCopyByStrokingPath(path.CGPath, NULL, fmaxf(35.0f, path.lineWidth), path.lineCapStyle, path.lineJoinStyle, path.miterLimit);
    if (tapTargetPath == NULL) {
        return nil;
    }

    UIBezierPath *tapTarget = [UIBezierPath bezierPathWithCGPath:tapTargetPath];
    CGPathRelease(tapTargetPath);
    return tapTarget;
}
```

The `containsPoint:` method in the `Shape` class then uses its `tapTarget` (rather than its `path`) to test whether it contains a given point or not. The result is that it returns `YES` only for points on the path’s outline (again, with a minimum width of 35 points).

```
- (BOOL)containsPoint:(CGPoint)point
{
    return [self.tapTarget containsPoint:point];
}
```

Now the hit testing code in the view controller is trivial. We just enumerate over all existing shapes and return the index of the first shape whose tap target matches the given location:

```
- (NSUInteger)hitTest:(CGPoint)point
{
    __block NSUInteger hitShapeIndex = NSNotFound;
    [self.shapes enumerateObjectsWithOptions:NSEnumerationReverse usingBlock:^(id shape, NSUInteger idx, BOOL *stop) {
        if ([shape containsPoint:point]) {
            hitShapeIndex = idx;
            *stop = YES;
        }
    }];
    return hitShapeIndex;
}
```

# Drawing a Selection Outline with `CGPathCreateCopyByStrokingPath`

We use the `hitTest:` method to determine which shape the user has selected. In the demo app, she can drag the selected shape to another location or opt to delete it. To show the user which shape, if any, is currently selected, we should highlight the selected shape in some way. Let’s do that with a dashed outline.

I want the dashed outline to appear _around_ the shape’s regular outline, so in `CGPath` parlance, I have to stroke the path’s stroke. As mentioned above, we can do that with our new favorite Core Graphics function. In our `drawRect:` method, we check whether the shape we are currently drawing is selected, and if it is, we use `CGPathCreateCopyByStrokingPath()` to create a new path of the shape’s outline and then `stroke` this copy with a dashed line:

```
- (void)drawRect:(CGRect)rect
{
    NSUInteger numberOfShapes = [self.dataSource numberOfShapesInDrawingView:self];
    NSUInteger indexOfSelectedShape = NSNotFound;
    if ([self.dataSource respondsToSelector:@selector(indexOfSelectedShapeInDrawingView:)]) {
        indexOfSelectedShape = [self.dataSource indexOfSelectedShapeInDrawingView:self];
    }

    for (NSUInteger shapeIndex = 0; shapeIndex < numberOfShapes; shapeIndex++)
    {
        UIBezierPath *path = [self.dataSource drawingView:self pathForShapeAtIndex:shapeIndex];
        if (CGRectIntersectsRect(rect, CGRectInset(path.bounds, -(path.lineWidth + 1.0f), -(path.lineWidth + 1.0f))))
        {
            UIColor *lineColor = [self.dataSource drawingView:self lineColorForShapeAtIndex:shapeIndex];
            [lineColor setStroke];
            [path stroke];

            if (shapeIndex == indexOfSelectedShape) {
                UIBezierPath *pathCopy = [path copy];
                CGPathRef cgPathSelectionRect = CGPathCreateCopyByStrokingPath(pathCopy.CGPath, NULL, pathCopy.lineWidth, pathCopy.lineCapStyle, pathCopy.lineJoinStyle, pathCopy.miterLimit);
                UIBezierPath *selectionRect = [UIBezierPath bezierPathWithCGPath:cgPathSelectionRect];
                CGPathRelease(cgPathSelectionRect);

                CGFloat dashStyle[] = { 5.0f, 5.0f };
                [selectionRect setLineDash:dashStyle count:2 phase:0];
                [[UIColor blackColor] setStroke];
                [selectionRect stroke];
            }
        }
    }
}
```

Note that we are using the delegation pattern to have our view ask its data source for the shapes it should draw, their colors, and which one is the currently selected shape. We then take care to only draw a shape if its bounding box intersects with the rectangle we actually need to redraw to make drawing more efficient. The drawing of the selection outline takes place inside the `if (shapeIndex == indexOfSelectedShape) { … }` block. Note that the first line in the block (`UIBezierPath *pathCopy = [path copy];`) should not be necessary but I found it to be so to make sure that `pathCopy` always reflects the latest changes to the path[3](#fn:3).

# Replicating `CGPathCreateCopyByStrokingPath` in iOS 4 and Mac OS X 10.6

Since OS X 10.4 (and iOS 2.0), Core Graphics included the function [`CGContextReplacePathWithStrokedPath()`](https://developer.apple.com/library/ios/documentation/graphicsimaging/reference/CGContext/Reference/reference.html#//apple_ref/doc/uid/TP30000950-CH1g-BCIICCBI). It essentially works the same way `CGPathCreateCopyByStrokingPath()` – with the large downside that it requires a graphics context to work on, which is usually not the case when doing hit testing. But it remains the best workaround I know of if you need to support older OS versions.

For a hit testing example, look at the code listed in [this Stack Overflow question](http://stackoverflow.com/q/1143704/116862). Unlike the author claims in the question (which dates from 2009), the necessary [`CGContextCopyPath()`](https://developer.apple.com/library/ios/documentation/graphicsimaging/reference/CGContext/Reference/reference.html#//apple_ref/doc/uid/TP30000950-CH1g-SW15) function is a public API since iOS 4.0/Mac OS X 10.6.

1. Or the equivalent `containsPoint:` method of `UIBezierPath` or `NSBezierPath`. Again, the distinction is not important because we can assume that these methods either just call the function on the internal `CGPath` object they manage or work the same way. [↩︎](#fnref:1)
2. As always, this method has its own user interface issues. Users might assume that a shape’s interior is indeed the selectable region and fail to select a shape that only reacts to taps on its outline. Also, a narrow outline is much harder to hit so we have to ensure our tap targets are big enough. [↩︎](#fnref:2)
3. When the user moves the shape to another location, the `Shape` class would create an appropriate transformation matrix for the translation and then apply the translation to the `UIBezierPath` it manages by calling `[path applyTransform:…];`. Even though these transforms are supposed to be applied on the path itself, accessing the path repeatedly from `drawRect:` always returned the original, untransformed object, thereby drawing the selection outline in the wrong location. Only when I made an explicit copy of the path, it seemed to finally apply the cumulated transformations. What’s curious about this is that this issue does not affect the `[path stroke];` line above, so it only seems to be a problem if you access the `UIBezierPath`’s underlying `CGPath`. [↩︎](#fnref:3)
