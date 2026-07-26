---
title: Accessing and Pretty-Printing the Elements of a CGPath
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/12/accessing-pretty-printing-cgpath-elements/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:2fcaab33eee27cf8'
translated: false
---

> 原文：[Accessing and Pretty-Printing the Elements of a CGPath](https://oleb.net/blog/2012/12/accessing-pretty-printing-cgpath-elements/)　·　Ole Begemann

# Accessing and Pretty-Printing the Elements of a CGPath

[Peter Steinberger](http://petersteinberger.com) asked this question on Twitter yesterday:

> Is there an easy way to pretty-print CGPath’s?

The short answer is: there may not be an easy way to log the contents of a [`CGPath`](https://developer.apple.com/library/ios/#documentation/graphicsimaging/Reference/CGPath/Reference/reference.html), but it is certainly possible.

# CGPath and UIBezierPath are Opaque

`CGPath` is an opaque data type that does not expose a straightforward way to list or access the individual elements of the path. Similarly, the UIKit wrapper for `CGPath`, [`UIBezierPath`](http://developer.apple.com/library/ios/#documentation/uikit/reference/UIBezierPath_class/Reference/Reference.html), does not provide a nice log output or a method to access the path elements.

Things are different with the AppKit counterpart, [`NSBezierPath`](https://developer.apple.com/library/mac/#documentation/Cocoa/Reference/ApplicationKit/Classes/NSBezierPath_Class/Reference/Reference.html). This class does have an APIs for individual element access (the [`elementAtIndex:`](https://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSBezierPath_Class/Reference/Reference.html#//apple_ref/doc/uid/20000339-CHDCDJIG) and related methods) and produces a very nice log output in its `description` method. Here’s an example:

```
NSLog(@"%@", bezierPath);
> Path <0x101411090>
  Bounds: {{10, 10}, {100, 122.5}}
  Control point bounds: {{10, 10}, {100, 130}}
    10.000000 10.000000 moveto
    10.000000 110.000000 lineto
    30.000000 140.000000 80.000000 140.000000 110.000000 110.000000 curveto
    110.000000 10.000000 lineto
    10.000000 10.000000 lineto
    closepath
```

# Replicating NSBezierPath Behavior

Let’s try to replicate this log output for a `UIBezierPath`. Rather than working with `CGPath` directly, I decided to implement a category on `UIBezierPath` because I find it is a convenient place to put this code. If you have a plain `CGPath`, simply instantiate a `UIBezierPath` with it. Alternatively, the code should be easy to adapt for use with regular `CGPath` objects.

## Accessing Individual Path Elements

While we cannot access the individual path elements directly, the [`CGPathApply()`](https://developer.apple.com/library/ios/documentation/graphicsimaging/Reference/CGPath/Reference/reference.html#//apple_ref/doc/uid/TP30000959-CH1g-BBCDGDIJ) function lets us specify a callback function that will be called for each element. The prototype of this callback function looks like this:

```
void MyCGPathApplierFunc (void *info, const CGPathElement *element);
```

The `info` parameter is a pointer to an arbitrary piece of data we can pass to the callback from `CGPathApply()`. The second parameter, `element`, points to a `struct` that describes an individual path element.

## CGPathElement

A [`CGPathElement`](https://developer.apple.com/library/ios/documentation/graphicsimaging/Reference/CGPath/Reference/reference.html#//apple_ref/doc/uid/TP30000959-CH3g-CGPathElement) can have one of five `type`s, describing the drawing command this particular element represents. Depending on the element type, the `points` member of `CGPathElement` points to an array of zero (`kCGPathElementCloseSubpath`), one (`kCGPathElementMoveToPoint`, `kCGPathElementAddLineToPoint`), two (`kCGPathElementAddQuadCurveToPoint`) or three (`kCGPathElementAddCurveToPoint`) points that define the exact form and endpoint of the drawing command.

## enumerateElementsUsingBlock:

Rather than just writing a better `description` method for `UIBezierPath`, I opted for a slightly more general solution. The new method `ob_enumerateElementsUsingBlock:` allows you to iterate over the path elements much like `CGPathApply()`. Instead of a callback function pointer, however, it takes a handler block in which you can specify what you want to do with the path elements. The implementation is simple: we use the `info` parameter of `CGPathApply()` to pass the block to the callback function.

```
//UIBezierPath+OBAdditions.h
#import <UIKit/UIKit.h>

typedef void(^OBUIBezierPathEnumerationHandler)(const CGPathElement *element);

@interface UIBezierPath (OBAdditions)

- (void)ob_enumerateElementsUsingBlock:(OBUIBezierPathEnumerationHandler)handler;
- (NSString *)ob_description;

@end
```

## Implementing the New description method

With this in place, writing the new `ob_description` method is a matter of enumerating over the path elements and creating an appropriate log string for each element in the block. Since the creation of the log string involves a rather large `switch` statement, I extracted this part into a separate method. The entire implementation looks like this:

```
//UIBezierPath+OBAdditions.m
#import "UIBezierPath+OBAdditions.h"

@implementation UIBezierPath (OBAdditions)

- (void)ob_enumerateElementsUsingBlock:(OBUIBezierPathEnumerationHandler)handler
{
    CGPathRef cgPath = self.CGPath;
    void CGPathEnumerationCallback(void *info, const CGPathElement *element);
    CGPathApply(cgPath, handler, CGPathEnumerationCallback);
}

- (NSString *)ob_description
{
    CGPathRef cgPath = self.CGPath;
    CGRect bounds = CGPathGetPathBoundingBox(cgPath);
    CGRect controlPointBounds = CGPathGetBoundingBox(cgPath);

    NSMutableString *mutableDescription = [NSMutableString string];
    [mutableDescription appendFormat:@"%@ <%p>\n", [self class], self];
    [mutableDescription appendFormat:@"  Bounds: %@\n", NSStringFromCGRect(bounds)];
    [mutableDescription appendFormat:@"  Control Point Bounds: %@\n", NSStringFromCGRect(controlPointBounds)];

    [self ob_enumerateElementsUsingBlock:^(const CGPathElement *element) {
        [mutableDescription appendFormat:@"    %@\n", [self ob_descriptionForPathElement:element]];
    }];

    return [mutableDescription copy];
}

- (NSString *)ob_descriptionForPathElement:(const CGPathElement *)element
{
    NSString *description = nil;
    switch (element->type) {
        case kCGPathElementMoveToPoint: {
            CGPoint point = element ->points[0];
            description = [NSString stringWithFormat:@"%f %f %@", point.x, point.y, @"moveto"];
            break;
        }
        case kCGPathElementAddLineToPoint: {
            CGPoint point = element ->points[0];
            description = [NSString stringWithFormat:@"%f %f %@", point.x, point.y, @"lineto"];
            break;
        }
        case kCGPathElementAddQuadCurveToPoint: {
            CGPoint point1 = element->points[0];
            CGPoint point2 = element->points[1];
            description = [NSString stringWithFormat:@"%f %f %f %f %@", point1.x, point1.y, point2.x, point2.y, @"quadcurveto"];
            break;
        }
        case kCGPathElementAddCurveToPoint: {
            CGPoint point1 = element->points[0];
            CGPoint point2 = element->points[1];
            CGPoint point3 = element->points[2];
            description = [NSString stringWithFormat:@"%f %f %f %f %f %f %@", point1.x, point1.y, point2.x, point2.y, point3.x, point3.y, @"curveto"];
            break;
        }
        case kCGPathElementCloseSubpath: {
            description = @"closepath";
            break;
        }
    }
    return description;
}

@end

void CGPathEnumerationCallback(void *info, const CGPathElement *element)
{
    OBUIBezierPathEnumerationHandler handler = info;
    if (handler) {
        handler(element);
    }
}
```
