---
title: Cocoa Drawing Guide
apple_id: TP40003290
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: null
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Paths/Paths.html
archived_at: '2026-07-15T07:12:29.573950Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Drawing Guide](Introduction%20to%20Cocoa%20Drawing%20Guide.md)


[Next](Incorporating%20Other%20Drawing%20Technologies.md)[Previous](Text.md)

# Paths

Cocoa provides support for drawing simple or complex geometric shapes using paths. A path is a collection of points used to create primitive shapes such as lines, arcs, and curves. From these primitives, you can create more complex shapes, such as circles, rectangles, polygons, and complex curved shapes, and paint them. Because they are composed of points (as opposed to a rasterized bitmap), paths are lightweight, fast, and scale to different resolutions without losing precision or quality.

The following sections focus primarily on the use of the [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath) class, which provides the main interface for creating and manipulating paths. Cocoa also provides a handful of functions that offer similar behavior for creating and drawing paths but do not require the overhead of creating an object. Those functions are mentioned where appropriate, but for more information, see _[Foundation Framework Reference](https://developer.apple.com/documentation/foundation)_ and _[Application Kit Framework Reference](https://developer.apple.com/documentation/appkit)_.

Cocoa defines several fundamental data types for manipulating geometric information in the drawing environment. These data types include [NSPoint](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSPoint), [NSRect](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSRect), and [NSSize](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSSize). You use these data types to specify lines, rectangles, and width and height information for the shapes you want to draw. Everything from lines and rectangles to circles, arcs, and Bezier curves can be specified using one or more of these data structures.

The coordinate values for point, rectangle, and size data types are all specified using floating-point values. Floating-point values allow for much finer precision as the resolution of the underlying destination device goes up.

The `NSPoint`, `NSRect`, and `NSSize` data types have equivalents in the Quartz environment: [CGPoint](https://developer.apple.com/documentation/coregraphics/cgpoint), [CGRect](https://developer.apple.com/documentation/coregraphics/cgrect), and [CGSize](https://developer.apple.com/documentation/coregraphics/cgsize). Because the layout of the Cocoa and Quartz types are identical, you can convert between two types by casting from one type to its counterpart.

The [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath) class provides the behavior for drawing most primitive shapes, and for many complex shapes, it is the only tool available in Cocoa. An `NSBezierPath` object encapsulates the information associated with a path, including the points that define the path and the attributes that affect the appearance of the path. The following sections explain how `NSBezierPath` represents path information and also describe the attributes that affect a path’s appearance.

An [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath) object uses path elements to build a path. A path element consists of a primitive command and one or more points. The command tells the path object how to interpret the associated points. When assembled, a set of path elements creates a series of line segments that form the desired shape.

The `NSBezierPath` class handles much of the work of creating and organizing path elements initially. Knowing how to manipulate path elements becomes important, however, if you want to make changes to an existing path. If you create a complex path based on user input, you might want to give the user the option of changing that path later. Although you could create a new path object with the changes, it is far simpler to modify the existing path elements. (For information on how to modify path elements, see [Manipulating Individual Path Elements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgywueqsdjfbucrsd).)

The `NSBezierPath` class defines only four basic path element commands, which are listed in Table 8-1. These commands are enough to define all of the possible path shapes. Each command has one or more points that contain information needed to position the path element. Most path elements use the current drawing point as the starting point for drawing.

__Table 8-1__  Path element commands

| Command | Number of points | Description |
| [NSMoveToBezierPathElement](https://developer.apple.com/documentation/appkit/nsmovetobezierpathelement) | 1 | Moves the path object’s current drawing point to the specified point. This path element does not result in any drawing. Using this command in the middle of a path results in a disconnected line segment. |
| [NSLineToBezierPathElement](https://developer.apple.com/documentation/appkit/nslinetobezierpathelement) | 1 | Creates a straight line from the current drawing point to the specified point. Lines and rectangles are specified using this path element. |
| [NSCurveToBezierPathElement](https://developer.apple.com/documentation/appkit/nscurvetobezierpathelement) | 3 | Creates a curved line segment from the current point to the specified endpoint using two control points to define the curve. The points are stored in the following order: `controlPoint1`, `controlPoint2`, `endPoint`. Ovals, arcs, and Bezier curves all use curve elements to specify their geometry. |
| [NSClosePathBezierPathElement](https://developer.apple.com/documentation/appkit/nsclosepathbezierpathelement) | 1 | Marks the end of the current subpath at the specified point. (Note that the point specified for the Close Path element is essentially the same as the current point. |

When you add a new shape to a path, `NSBezierPath` breaks that shape down into one or more component path elements for storage purposes. For example, calling [moveToPoint:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520684-move) or [lineToPoint:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520742-linetopoint) creates a Move To element or Line To element respectively. In the case of more complex shapes, like rectangles and ovals, several line or curve elements may be created. Figure 8-1 shows two shapes and the resulting path elements. For the curved segment, the figure also shows the control points that define the curve.

__Figure 8-1__  Path elements for a complex path

![Path elements for a complex path](attachments/Art/path_elements_2x.png)

Listing 8-1 shows the code that creates the path shown in Figure 8-1.

__Listing 8-1__  Creating a complex path

```
NSBezierPath* aPath = [NSBezierPath bezierPath];

[aPath moveToPoint:NSMakePoint(0.0, 0.0)];
[aPath lineToPoint:NSMakePoint(10.0, 10.0)];
[aPath curveToPoint:NSMakePoint(18.0, 21.0)
        controlPoint1:NSMakePoint(6.0, 2.0)
        controlPoint2:NSMakePoint(28.0, 10.0)];

[aPath appendBezierPathWithRect:NSMakeRect(2.0, 16.0, 8.0, 5.0)];
```


A subpath is a series of connected line and curve segments within an [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath) object. A single path object may contain multiple subpaths, with each subpath delineated by a Move To or Close Path element. When you set the initial drawing point (typically using the `moveToPoint:` method), you set the starting point of the first subpath. As you draw, you build the contents of the subpath until you either close the path (using the [closePath](https://developer.apple.com/documentation/appkit/nsbezierpath/1520640-closepath) method) or add another Move To element. At that point, the subpath is considered closed and any new elements are added to a new subpath.

Some methods of `NSBezierPath` automatically create a new subpath for you. For example, creating a rectangle or oval results in the addition of a Move To element, several drawing elements, and a Close Path and Move To element (see [Figure 8-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgywueqsdjbeuessd) for an example). The Move To element at the end of the list of elements ensures that the current drawing point is left in a known location, which in this case is at the rectangle’s origin point.

Subpaths exist to help you distinguish different parts of a path object. For example, subpaths affect the way a path is filled; see [Winding Rules](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgywueqkkjffeur2e). The division of a path into subpaths also affects methods such as [bezierPathByReversingPath](https://developer.apple.com/documentation/appkit/nsbezierpath/1520656-reversed), which reverses the subpaths one at a time. In other cases, though, subpaths in an `NSBezierPath` object share the same drawing attributes.

An [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath) object maintains all of the attributes needed to determine the shape of its path. These attributes include the line width, curve flatness, line cap style, line join style, and miter limit of the path. You set these values using the methods of `NSBezierPath`.

Path attributes do not take effect until you fill or stroke the path, so if you change an attribute more than once before drawing the path, only the last value is used. The `NSBezierPath` class maintains both a custom and default version of each attribute. Path objects use custom attribute values if they are set. If no custom attribute value is set for a given path object, the default value is used. The `NSBezierPath` class does not use path attribute values set using Quartz functions.

The following sections describe the attributes you can set for a path object and how those attributes affect your rendered paths.

The line width attribute controls the width of the entire path. Line width is measured in points and specified as a floating-point value. The default width for all lines is 1. To change the default line width for all `NSBezierPath` objects, you use the `setDefaultLineWidth:` method. To set the line width for the current path object, you use the [setLineWidth:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520655-linewidth) method of that path object. To set the default line width for shapes rendered without an `NSBezierPath` object, you must use the [CGContextSetLineWidth](https://developer.apple.com/documentation/coregraphics/1455270-cgcontextsetlinewidth) function in Quartz.

Fractional line widths are rendered as close as possible to the specified width, subject to the limitations of the destination device, the position of the line, and the current anti-aliasing setting. For example, suppose you want to draw a line whose width is 0.2 points. Multiplying this width by 1/72 points per inch yields a line that is 0.0027778 inches wide. On a 90 dpi screen, the smallest possible line would be 1 pixel wide or 0.0111 inches. To ensure your line is not hidden on the screen, Cocoa nominally draws it at the screen’s larger minimum width (0.0111 inches). In reality, if the line straddles a pixel boundary or anti-aliasing is enabled, the line might affect additional pixels on either side of the path. If the output device were a 600 dpi printer instead, Quartz would be able to render the line closer to its true width of 0.0027778 inches.

Listing 8-2 draws a few paths using different techniques. The [NSFrameRect](https://developer.apple.com/documentation/appkit/1473582-nsframerect) function uses the default line width to draw a rectangle, so that value must be set prior to calling the function. Path objects use the default value only if a custom value has not been set. You can even change the line width of a path object and draw again to achieve a different path width, although you would also need to move the path to see the difference.

__Listing 8-2__  Setting the line width of a path

```
// Draw a rectangle using the default line width: 2.0.
[NSBezierPath setDefaultLineWidth:2.0];
NSFrameRect(NSMakeRect(20.0, 20.0, 10.0, 10.0));

// Set the line width for a single NSBezierPath object.
NSBezierPath* thePath = [NSBezierPath bezierPath];
[thePath setLineWidth:1.0]; // Has no effect.
[thePath moveToPoint:NSMakePoint(0.0, 0.0)];
[thePath lineToPoint:NSMakePoint(10.0, 0.0)];
[thePath setLineWidth:3.0];
[thePath lineToPoint:NSMakePoint(10.0, 10.0)];

// Because the last value set is 3.0, all lines are drawn with
// a width of 3.0, not just the second line.
[thePath stroke];

// Changing the width and stroking again draws the same path
// using the new line width.
[thePath setLineWidth:4.0];
[thePath stroke];

// Changing the default line width has no effect because a custom
// value already exists. The path is rendered with a width of 4.0.
[thePath setDefaultLineWidth:5.0];
[thePath stroke];
```


The current line cap style determines the appearance of the open end points of a path segment. Cocoa supports the line cap styles shown in Figure 8-2.

__Figure 8-2__  Line cap styles

![Line cap styles](attachments/Art/linecaps_2x.png)

To set the line cap style for a `NSBezierPath` object, use the [setLineCapStyle:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520667-linecapstyle) method. The default line cap style is set to `NSButtLineCapStyle`. To change the default line cap style, use the `setDefaultLineCapStyle:` method. Listing 8-3 demonstrates both of these methods:

__Listing 8-3__  Setting the line cap style of a path

```
[// Set the default line cap style
[NSBezierPath setDefaultLineCapStyle:NSButtLineCapStyle];

// Customize the line cap style for the new object.
NSBezierPath* aPath = [NSBezierPath bezierPath];
[aPath moveToPoint:NSMakePoint(0.0, 0.0)];
[aPath lineToPoint:NSMakePoint(10.0, 10.0)];
[aPath setLineCapStyle:NSSquareLineCapStyle];
[aPath stroke];
```


The current line join style determines how connected lines in a path are joined at the vertices. Cocoa supports the line join styles shown in Figure 8-3.

__Figure 8-3__  Line join styles

![Line join styles](attachments/Art/linejoins_2x.png)

To set the line join style for an `NSBezierPath` object, use the [setLineJoinStyle:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520726-linejoinstyle) method. The default line join style is set to `NSMiterLineJoinStyle`. To change the default line join style, use the `setDefaultLineJoinStyle:` method. Listing 8-4 demonstrates both of these methods:

__Listing 8-4__  Setting the line join style of a path

```
[// Set the default line join style
[NSBezierPath setDefaultLineJoinStyle:NSMiterLineJoinStyle];

// Customize the line join style for a new path.
NSBezierPath* aPath = [NSBezierPath bezierPath];
[aPath moveToPoint:NSMakePoint(0.0, 0.0)];
[aPath lineToPoint:NSMakePoint(10.0, 10.0)];
[aPath lineToPoint:NSMakePoint(10.0, 0.0)];
[aPath setLineJoinStyle:NSRoundLineJoinStyle];
[aPath stroke];
```


The line dash style determines the pattern used to stroke a path. By default, stroked paths appear solid. Using a line-dash pattern, you can specify an alternating group of solid and transparent swatches. When setting a line dash pattern, you specify the width (in points) of each successive solid or transparent swatch. The widths you specify are then repeated over the entire length of the path.

Figure 8-4 shows some sample line dash patterns, along with the values used to create each pattern.

__Figure 8-4__  Line dash patterns

![Line dash patterns](attachments/Art/linedash_2x.png)

The `NSBezierPath` class does not support the concept of a default line dash style. If you want a line dash style, you must apply it to a path explicitly using the [setLineDash:count:phase:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520730-setlinedash) method as shown in Listing 8-5, which renders the last pattern from the preceding figure.

__Listing 8-5__  Adding a dash style to a path

```
void AddDashStyleToPath(NSBezierPath* thePath)
{
    // Set the line dash pattern.
    float lineDash[6];

    lineDash[0] = 40.0;
    lineDash[1] = 12.0;
    lineDash[2] = 8.0;
    lineDash[3] = 12.0;
    lineDash[4] = 8.0;
    lineDash[5] = 12.0;

   [thePath setLineDash:lineDash count:6 phase:0.0];
}
```


The line flatness attribute determines the rendering accuracy for curved segments. The flatness value measures the maximum error tolerance (in pixels) to use during rendering. Smaller values result in smoother curves but require more computation time. Larger values result in more jagged curves but are rendered much faster.

Line flatness is one parameter you can tweak when you want to render a large number of curves quickly and do not care about accuracy. For example, you might increase this value during a live resize or scrolling operation when accuracy is not as crucial. Regardless, you should always measure performance to make sure such a modification actually saves time.

Figure 8-5 shows how changing the default flatness affects curved surfaces. The figure on the left shows a group of curved surfaces rendered with the flatness value set to `0.6` (its default value). The figure on the right shows the same curved surfaces rendered with the flatness value set to `20`. The curvature of each surface is lost and now appears to be a set of connected line segments.

__Figure 8-5__  Flatness effects on curves

![Flatness effects on curves](attachments/Art/flatness_comparison_2x.png)

To set the flatness for a specific `NSBezierPath` object, use the [setFlatness:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520676-flatness) method. To set the default flatness value, use `setDefaultFlatness:`, as shown in Listing 8-6:

__Listing 8-6__  Setting the flatness of a path

```
[- (void) drawRect:(NSRect)rect
{
    if ([self inLiveResize])
    {
        // Adjust the default flatness upward to reduce
        // the number of required computations.
        [NSBezierPath setDefaultFlatness:10.0];

        // Draw live resize content.
    }
    // ...

}
```


Miter limits help you avoid spikes that occur when you join two line segments at a sharp angle. If the ratio of the miter length—the diagonal length of the miter—to the line thickness exceeds the miter limit, the corner is drawn using a bevel join instead of a miter join.

Figure 8-6 shows an example of how different miter limits affect the same path. This path consists of several 10-point wide lines connected by miter joins. In the figure on the left, the miter limit is set to `5`. Because the miter lengths exceed the miter limit, the line joins are changed to bevel joins. By increasing the miter limit to `16`, as shown in the figure on the right, the miter joins are restored but extend far beyond the point where the two lines meet.

__Figure 8-6__  Miter limit effects

![Miter limit effects](attachments/Art/miter_limits_2x.png)

To set the miter limits for a specific `NSBezierPath` object, use the [setMiterLimit:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520740-miterlimit) method. To set the default miter limit for newly created `NSBezierPath` objects, use `setDefaultMiterLimit:`. Listing 8-7 demonstrates both of these methods:

__Listing 8-7__  Setting the miter limit for a path

```
// Increase the default limit
[NSBezierPath setDefaultMiterLimit:20.0];

// Customize the limit for a specific path with sharp angles.
NSBezierPath* aPath = [NSBezierPath bezierPath];
[aPath moveToPoint:NSMakePoint(0.0, 0.0)];
[aPath lineToPoint:NSMakePoint(8.0, 100.0)];
[aPath lineToPoint:NSMakePoint(16.0, 0.0)];
[aPath setLineWidth:5.0];
[aPath setMiterLimit:5.0];
[aPath stroke];
```


When you fill the area encompassed by a path, [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath) applies the current winding rule to determine which areas of the screen to fill. A _winding rule_ is simply an algorithm that tracks information about each contiguous region that makes up the path's overall fill area. A ray is drawn from a point inside a given region to any point outside the path bounds. The total number of crossed path lines (including implicit lines) and the direction of each path line are then interpreted using the rules in Table 8-2, which determine if the region should be filled.

__Table 8-2__  Winding rules

| Winding rule | Description |
| [NSNonZeroWindingRule](https://developer.apple.com/documentation/appkit/nsnonzerowindingrule) | Count each left-to-right path as +1 and each right-to-left path as -1. If the sum of all crossings is 0, the point is outside the path. If the sum is nonzero, the point is inside the path and the region containing it is filled. This is the default winding rule. |
| [NSEvenOddWindingRule](https://developer.apple.com/documentation/appkit/nsevenoddwindingrule) | Count the total number of path crossings. If the number of crossings is even, the point is outside the path. If the number of crossings is odd, the point is inside the path and the region containing it should be filled. |

Fill operations are suitable for use with both open and closed subpaths. A closed subpath is a sequence of drawing calls that ends with a Close Path path element. An open subpath ends with a Move To path element. When you fill a partial subpath, `NSBezierPath` closes it for you automatically by creating an implicit (non-rendered) line from the first to the last point of the subpath.

Figure 8-7 shows how the winding rules are applied to a particular path. Subfigure `a` shows the path rendered using the nonzero rule and subfigure `b` shows it rendered using the even-odd rule. Subfigures `c` and `d` add direction marks and the hidden path line that closes the figure to help you see how the rules are applied to two of the path’s regions.

__Figure 8-7__  Applying winding rules to a path

![Applying winding rules to a path](attachments/Art/winding_path_crossing_2x.png)

To set the winding rule for an `NSBezierPath` object, use the [setWindingRule:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520657-windingrule) method. The default winding rule is `NSNonZeroWindingRule`. To change the default winding rule for all `NSBezierPath` objects, use the `setDefaultWindingRule:` method.

The Foundation framework includes numerous functions for manipulating geometric values and for performing various calculations using those values. In addition to basic equality checks, you can perform more complex operations, such as the union and intersection of rectangles or the inclusion of a point in a rectangle’s boundaries.

Table 8-3 lists some of the more commonly used functions and their behaviors. The function syntax is provided in a shorthand notation, with parameter types omitted to demonstrate the calling convention. For a complete list of available functions, and their full syntax, see the Functions section in _[Foundation Framework Reference](https://developer.apple.com/documentation/foundation)_.

__Table 8-3__  Commonly used geometry functions

| Operation | Function | Description |
| Creation | `NSPoint `[NSMakePoint](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSMakePoint)`(x, y)` | Returns a properly formatted `NSPoint` data structure with the specified x and y values. |
| Creation | `NSSize `[NSMakeSize](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSMakeSize)`(w, h)` | Returns a properly formatted `NSSize` data structure with the specified width and height. |
| Creation | `NSRect `[NSMakeRect](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSMakeRect)`(x, y, w, h)` | Returns a properly formatted `NSRect` data structure with the specified origin (x, y) and size (width, height). |
| Equality | `BOOL `[NSEqualPoints](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSEqualPoints)`(p1, p2)` | Returns `YES` if the two points are the same. |
| Equality | `BOOL `[NSEqualSizes](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSEqualSizes)`(s1, s2)` | Returns `YES` if the two size types have identical widths and heights. |
| Equality | `BOOL `[NSEqualRects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSEqualRects)`(r1, r2)` | Returns `YES`, if the two rectangles have the same origins and the same widths and heights. |
| Rectangle manipulations | `BOOL `[NSContainsRect](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSContainsRect)`(r1, r2)` | Returns `YES` if rectangle 1 completely encloses rectangle 2. |
| Rectangle manipulations | `NSRect `[NSInsetRect](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSInsetRect)`(r, dX, dY)` | Returns a copy of the specified rectangle with its sides moved inward by the specified delta values. Negative delta values move the sides outward. Does not modify the original rectangle. |
| Rectangle manipulations | `NSRect `[NSIntersectionRect](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSIntersectionRect)`(r1, r2)` | Returns the intersection of the two rectangles. |
| Rectangle manipulations | `NSRect` [NSUnionRect](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSUnionRect)`(r1, r2)` | Returns the union of the two rectangles. |
| Rectangle manipulations | `BOOL `[NSMouseInRect](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSMouseInRect)`(p, r, flipped)` | Tests whether the point lies within the specified view rectangle. Adjusts the hit-detection algorithm to provide consistent behavior from the user’s perspective. |
| Rectangle manipulations | `BOOL `[NSPointInRect](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSPointInRect)`(p, r)` | Tests whether the point lies within the specified rectangle. This is a basic mathematical comparison. |

For many types of content, path-based drawing has several advantages over image-based drawing:

- Because paths are specified mathematically, they scale easily to different resolutions. Thus, the same path objects can be used for screen and print-based drawing.
- The geometry information associated with a path requires much less storage space than most image data formats.
- Rendering paths is often faster than compositing a comparable image. It takes less time to transfer path data to the graphics hardware than it takes to transfer the texture data associated with an image.

The following sections provide information about the primitive shapes you can draw using paths. You can combine one or more of these shapes to create a more complex path and then stroke or fill the path as described in [Drawing the Shapes in a Path](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgywueqsdijduirsj). For some shapes, there may be more than one way to add the shape to a path, or there may be alternate ways to draw the shape immediately. Wherever possible, the benefits and disadvantages of each technique are listed to help you decide which technique is most appropriate in specific situations.

An `NSPoint` structure by itself represents a location on the screen; it has no weight and cannot be drawn as such. To draw the equivalent of a point on the screen, you would need to create a small rectangle at the desired location, as shown in Listing 8-8.

__Listing 8-8__  Drawing a point

```
void DrawPoint(NSPoint aPoint)
{
    NSRect aRect = NSMakeRect(aPoint.x, aPoint.y, 1.0, 1.0);

    NSRectFill(aRect);
}
```

Of course, a more common use for points is to specify the position of other shapes. Many shapes require you to specify the current point before actually creating the shape. You set the current point using the [moveToPoint:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520684-move) or [relativeMoveToPoint:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520724-relativemovetopoint) methods. Some shapes, like rectangles and ovals, already contain location information and do not require a separate call to `moveToPoint:`.

Cocoa provides a couple of options for adding lines to a path, with each technique offering different tradeoffs between efficiency and correctness. You can draw lines in the following ways:

- Create single horizontal and vertical lines by filling a rectangle using [NSRectFill](https://developer.apple.com/documentation/appkit/1473652-nsrectfill). This technique is less precise but is often a little faster than creating an [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath) object. To create diagonal lines using this technique, you must apply a rotation transform before drawing. This technique is not appropriate for creating connected line segments.
- Use the  [lineToPoint:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520742-linetopoint), [relativeLineToPoint:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520709-relativeline), or [strokeLineFromPoint:toPoint:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520626-strokelinefrompoint) methods of `NSBezierPath` to create individual or connected line segments. This technique is fast and is the most precise option for creating lines and complex polygons.
- Use the [appendBezierPathWithPoints:count:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520749-appendbezierpathwithpoints) method to create a series of connected lines quickly. This technique is faster than adding individual lines.

Polygons are composed of multiple connected lines and should be created using an `NSBezierPath` object. The simplest way to create a four-sided nonrectangular shape, like a parallelogram, rhombus, or trapezoid, is using line segments. You could also create these shapes using transforms, but calculating the correct skew factors would require a lot more work.

Listing 8-9 shows code to draw a parallelogram using `NSBezierPath`. The method in this example inscribes the parallelogram inside the specified rectangle. The `withShift` parameter specifies the horizontal shift applied to the top left and bottom right corners of the rectangular area.

__Listing 8-9__  Using lines to draw a polygon

```
void DrawParallelogramInRect(NSRect rect, float withShift)
{
    NSBezierPath* thePath = [NSBezierPath bezierPath];

    [thePath moveToPoint:rect.origin];
    [thePath lineToPoint:NSMakePoint(rect.origin.x + withShift,  NSMaxY(rect))];
    [thePath lineToPoint:NSMakePoint(NSMaxX(rect), NSMaxY(rect))];
    [thePath lineToPoint:NSMakePoint(NSMaxX(rect) - withShift,  rect.origin.y)];
    [thePath closePath];

    [thePath stroke];
}
```


Because rectangles are used frequently, there are several options for drawing them.

- Use the methods of `NSBezierPath` to create your rectangle. The following methods are reasonably fast and offer the best precision:

  - [strokeRect:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520741-stroke)
  - [fillRect:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520747-fillrect)
  - [bezierPathWithRect:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520664-bezierpathwithrect)
  - [appendBezierPathWithRect:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520670-appendbezierpathwithrect)
- Create rectangles using the Cocoa functions described in [Drawing Rectangles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgywueqsdizaueskf). These functions draw rectangles faster than, but with less precision than, the methods of `NSBezierPath`.
- Create a rectangle using individual lines as described in [Adding Lines and Polygons](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgywueqsdjbeuir2i). You could use this technique to create diagonally oriented rectangles—that is, rectangles whose sides are not parallel to the x and y axes—without using a rotation transform.

Listing 8-10 shows a simple function that fills and strokes the same rectangle using two different techniques. The current fill and stroke colors are used when drawing the rectangle, along with the default compositing operation. In both cases, the rectangles are drawn immediately; there is no need to send a separate [fill](https://developer.apple.com/documentation/appkit/nsbezierpath/1520700-fill) or [stroke](https://developer.apple.com/documentation/appkit/nsbezierpath/1520739-stroke) message.

__Listing 8-10__  Drawing a rectangle

```
void DrawRectangle(NSRect aRect)
{
    NSRectFill(aRect);
    [NSBezierPath strokeRect:aRect];
}
```


In OS X v10.5 and later, the [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath) class includes the following methods for creating rounded-rectangles:

- [bezierPathWithRoundedRect:xRadius:yRadius:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520638-bezierpathwithroundedrect)
- [appendBezierPathWithRoundedRect:xRadius:yRadius:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520705-appendbezierpathwithroundedrect)

These methods create rectangles whose corners are curved according to the specified radius values. The radii describe the width and height of the oval to use at each corner of the rectangle. Figure 8-8 shows how this inscribed oval is used to define the path of the rectangle’s corner segments.

__Figure 8-8__  Inscribing the corner of a rounded rectangle

![Inscribing the corner of a rounded rectangle](attachments/Art/rounded-rect_2x.png)

Listing 8-11 shows a code snippet that creates and draws a path with a rounded rectangle.

__Listing 8-11__  Drawing a rounded rectangle

```
void DrawRoundedRect(NSRect rect, CGFloat x, CGFloat y)
{
    NSBezierPath* thePath = [NSBezierPath bezierPath];

    [thePath appendBezierPathWithRoundedRect:rect xRadius:x yRadius:y];
    [thePath stroke];
}
```


To draw ovals and circles, use the following methods of `NSBezierPath`:

- [bezierPathWithOvalInRect:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520647-bezierpathwithovalinrect)
- [appendBezierPathWithOvalInRect:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520718-appendbezierpathwithovalinrect)

Both methods inscribe an oval inside the rectangle you specify. You must then fill or stroke the path object to draw the oval in the current context. The following example creates an oval from the specified rectangle and strokes its path.

```
void DrawOvalInRect(NSRect ovalRect)
{
    NSBezierPath* thePath = [NSBezierPath bezierPath];

    [thePath appendBezierPathWithOvalInRect:ovalRect];
    [thePath stroke];
}
```

You could also create an oval using arcs, but doing so would duplicate what the preceding methods do internally and would be a little slower. The only reason to add individual arcs is to create a partial (non-closed) oval path. For more information, see [Adding Arcs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgywueqsdijdumqsi).

To draw arcs, use the following methods of `NSBezierPath`:

- [appendBezierPathWithArcFromPoint:toPoint:radius:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520737-appendbezierpathwitharcfrompoint)
- [appendBezierPathWithArcWithCenter:radius:startAngle:endAngle:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520680-appendarc)
- [appendBezierPathWithArcWithCenter:radius:startAngle:endAngle:clockwise:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520659-appendarc)

The `appendBezierPathWithArcFromPoint:toPoint:radius:` method creates arcs by inscribing them in an angle formed by the current point and the two points passed to the method. Inscribing a circle in this manner can result in an arc that does not intersect any of the points used to specify it. It can also result in the creation of an unwanted line from the current point to the starting point of the arc.

Figure 8-9 shows three different arcs and the control points used to create them. For the two arcs created using `appendBezierPathWithArcFromPoint:toPoint:radius:`, the current point must be set before calling the method. In both examples, the point is set to (30, 30). Because the radius of the second arc is shorter, and the starting point of the arc is not the same as the current point, a line is drawn from the current point to the starting point.

__Figure 8-9__  Creating arcs

![Creating arcs](attachments/Art/arc_examples_2x.png)

Listing 8-12 shows the code snippets you would use to create each of the arcs from Figure 8-9. (Although the figure shows the arcs individually, executing the following code would render the arcs on top of each other. )

__Listing 8-12__  Creating three arcs

```
NSBezierPath*   arcPath1 = [NSBezierPath bezierPath];
NSBezierPath*   arcPath2 = [NSBezierPath bezierPath];

[[NSColor blackColor] setStroke];

// Create the first arc
[arcPath1 moveToPoint:NSMakePoint(30,30)];
[arcPath1 appendBezierPathWithArcFromPoint:NSMakePoint(0,30)  toPoint:NSMakePoint(0,60) radius:30];
[arcPath1 stroke];

// Create the second arc.
[arcPath2 moveToPoint:NSMakePoint(30,30)];
[arcPath2 appendBezierPathWithArcFromPoint:NSMakePoint(30,40)  toPoint:NSMakePoint(70,30) radius:20];
[arcPath2 stroke];

// Clear the old arc and do not set an initial point, which prevents a
// line being drawn from the current point to the start of the arc.
[arcPath2 removeAllPoints];
[arcPath2 appendBezierPathWithArcWithCenter:NSMakePoint(30,30) radius:30  startAngle:45 endAngle:135];
[arcPath2 stroke];
```


To draw Bezier curves, you must use the [curveToPoint:controlPoint1:controlPoint2:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520628-curvetopoint) method of `NSBezierPath`. This method supports the creation of a cubic curve from the current point to the destination point you specify when calling the method. The `controlPoint1` parameter determines the curvature starting from the current point, and `controlPoint2` determines the curvature of the destination point, as shown in [Figure 8-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgywueqsdjbeuessd).

__Figure 8-10__  Cubic Bezier curve

![Cubic Bezier curve](attachments/Art/bezier_curve_2x.png)

Because [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath) only supports path-based content, you cannot add text characters directly to a path; instead, you must add glyphs. A glyph is the visual representation of a character (or partial character) in a particular font. For glyphs in an outline font, this visual representation is stored as a set of mathematical paths that can be added to an `NSBezierPath` object.

To obtain a set of glyphs, you can use the Cocoa text system or the `NSFont` class. Getting glyphs from the Cocoa text system is usually easier because you can get glyphs for an arbitrary string of characters, whereas using `NSFont` requires you to know the names of individual glyphs. To get glyphs from the Cocoa text system, you must do the following:

1. Create the text system objects needed to manage text layout.
2. Use the [glyphAtIndex:](https://developer.apple.com/documentation/appkit/nslayoutmanager/1403083-glyphatindex) or [getGlyphs:range:](https://developer.apple.com/documentation/appkit/nslayoutmanager/1402973-getglyphs) method of `NSLayoutManager` to retrieve the desired glyphs.
3. Add the glyphs to your `NSBezierPath` object using one of the following methods:

   - [appendBezierPathWithGlyph:inFont:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520661-appendglyph)
   - [appendBezierPathWithGlyphs:count:inFont:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520750-appendglyphs)

When added to your `NSBezierPath` object, glyphs are converted to a series of path elements. These path elements simply specify lines and curves and do not retain any information about the characters themselves. You can manipulate paths containing glyphs just like you would any other path by changing the points of a path element or by modifying the path attributes.

There are two options for drawing the contents of a path: you can stroke the path or fill it. Stroking a path renders an outline of the path’s shape using the current stroke color and path attributes. Filling the path renders the area encompassed by the path using the current fill color and winding rule.

Figure 8-11 shows the same path from [Figure 8-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgywueqsdjbeuessd) but with the contents filled and a different stroke width applied.

__Figure 8-11__  Stroking and filling a path.

![Stroking and filling a path.](attachments/Art/path_stroke_fill_2x.png)

Cocoa provides several functions for drawing rectangles to the current context immediately using the default attributes. These functions use Quartz primitives to draw one or more rectangles quickly, but in a way that may be less precise than if you were to use [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath). For example, these routines do not apply the current join style to the corners of a framed rectangle.

Table 8-4 lists some of the more commonly used functions for drawing rectangles along with their behaviors. You can use these functions in places where speed is more important than precision. The syntax for each function is provided in a shorthand notation, with parameter types omitted to demonstrate the calling conventions. For a complete list of available functions, and their full syntax, see _[Application Kit Functions Reference](https://developer.apple.com/documentation/appkit/functions)_.

__Table 8-4__  Rectangle frame and fill functions

| Function | Description |
| `void `[NSEraseRect](https://developer.apple.com/documentation/appkit/1473745-nseraserect)`(aRect)` | Fills the specified rectangle with white. |
| `void `[NSFrameRect](https://developer.apple.com/documentation/appkit/1473582-nsframerect)`(aRect)` | Draws the frame of the rectangle using the current fill color, the default line width, and the `NSCompositeCopy` compositing operation. |
| `void `[NSFrameRectWithWidth](https://developer.apple.com/documentation/appkit/1473822-nsframerectwithwidth)`(aRect, width)` | Draws the frame of the rectangle using the current fill color, the specified width, and the `NSCompositeCopy` compositing operation. |
| `void `[NSFrameRectWithWidthUsingOperation](https://developer.apple.com/documentation/appkit/1473662-nsframerectwithwidthusingoperati)`(aRect, width, op)` | Draws the frame of the rectangle using the current fill color, the specified width, and the specified operation. |
| `void `[NSRectFill](https://developer.apple.com/documentation/appkit/1473652-nsrectfill)`(aRect)` | Fills the rectangle using the current fill color and the `NSCompositeCopy` compositing operation. |
| `void `[NSRectFillUsingOperation](https://developer.apple.com/documentation/appkit/1473588-nsrectfillusingoperation)`(aRect, op)` | Fills the rectangle using the current fill color and specified compositing operation. |
| `void `[NSRectFillList](https://developer.apple.com/documentation/appkit/1473788-nsrectfilllist)`(rectList, count)` | Fills the C-style array of rectangles using the current fill color and the `NSCompositeCopy` compositing operation. |
| `void `[NSRectFillListWithColors](https://developer.apple.com/documentation/appkit/1473733-nsrectfilllistwithcolors)`(rects, colors, count)` | Fills the C-style array of rectangles using the corresponding list of colors. Each list must have the same number of entries. |
| `void `[NSRectFillListUsingOperation](https://developer.apple.com/documentation/appkit/1473600-nsrectfilllistusingoperation)`(rects, count, op)` | Fills the C-style array of rectangles using the current fill color and the specified compositing operation. |
| `void `[NSRectFillListWithColorsUsingOperation](https://developer.apple.com/documentation/appkit/1473686-nsrectfilllistwithcolorsusingope)`(rects, colors, count, op)` | Fills the C-style array of rectangles using the corresponding list of colors and the specified compositing operation. The list of rectangles and list of colors must contain the same number of items. |

Building a sleek and attractive user interface is hard work and most programs use a combination of images and paths to do it. Paths have the advantage of being lightweight, scalable, and fast. Even so, paths are not appropriate in all situations. The following sections provide some basic tips and guidance on how to use paths effectively in your program.

Building a path involves creating an [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath) object and adding path elements to it. All paths must start with a Move To element to mark the first point of the path. In some cases, this element is added for you but in others you must add it yourself. For example, methods that create a closed path (such as an oval or rectangle) insert a MoveTo element for you.

A single `NSBezierPath` object may have multiple subpaths. Each subpath is itself a complete path, meaning the subpath may not appear connected to any other subpaths when drawn. Filled subpaths can still interact with each other, however. Overlapping subpaths may cancel each other’s fill effect, resulting in holes in the fill area.

All subpaths in an `NSBezierPath` object share the same drawing attributes. The only way to assign different attributes to different paths is to create different `NSBezierPath` objects for each.

As you work on your drawing code, you should keep performance in mind. Drawing is a processor intensive activity but there are many ways to reduce the amount of drawing performed by your application. The following sections offer some basic tips related to improving drawing performance with Cocoa applications. For additional drawing-related performance tips, see _[Drawing Performance Guidelines](../../Performance/Drawing%20Performance%20Guidelines/Introduction%20to%20Drawing%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tc2i)_.

If you draw the same content repeatedly, consider caching the objects used to draw that content. It is usually more efficient to retain an existing `NSBezierPath` object than to recreate it during each drawing cycle. For content that might change dynamically, you might also consider maintaining a pool of reusable objects.

When writing your drawing code, you should always try to make that code as efficient as possible without sacrificing the quality of the rendered content. If your drawing code seems slow, there are some tradeoffs you can make to improve efficiency that reduce quality only temporarily:

- Use the available update rectangles to draw only what has changed. Use different [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath) objects for each part of the screen rather than one large object that covers everything. For more information, see [Reduce Path Complexity](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgywueqsdizducr2g).
- During scrolling, live resizing, or other time-critical operations, consider the following options:

  - If your screen contains animated content, pause the animation until the operation is complete.
  - Try temporarily increasing the flatness value for curved paths. The default flatness value is set to 0.6, which results in nice smooth curves. Increasing this value above 1.0 may make your curves look more jagged but should improve performance. You may want to try a few different values to determine a good tradeoff between appearance and speed.
  - Disable anti-aliasing. For more information, see [Setting the Anti-aliasing Options](Graphics%20Contexts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgmwueq2jjjfegqsc).
- When drawing rectangles, use `NSFrameRect` and `NSRectFill` for operations where the highest quality is not required. These functions offer close approximations to what you would get with `NSBezierPath` but are often a little faster.

If you are drawing a large amount of content, you should do your best to reduce the complexity of the path data you store in a single [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath) object. Path objects with hundreds of path elements require more calculations than those with 10 or 20 elements. Every line or curve segment you add increases the number of calculations required to flatten the path or determine whether a point is inside it. Numerous path crossings also increases the number of required calculations when filling the path.

If the accuracy of rendered paths is not crucial, try using multiple `NSBezierPath` objects to draw the same content. There is very little visual difference between using one path object or multiple path objects. If your path is already grouped into multiple subpaths, then it becomes easy to put some of those subpaths in other `NSBezierPath` objects. Using multiple path objects reduces the number of calculations for each subpath and also allows you to limit rendering to only those paths that are in the current update rectangle.

Given an [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath) object with some existing path data, you can retrieve the points associated with that path and modify them individually. An illustration program might do this in response to a mouse event over one of the points in a path. If the mouse event results in that point being dragged to a new location, you can quickly update the path element with the new location and redraw the path.

The [elementCount](https://developer.apple.com/documentation/appkit/nsbezierpath/1520645-elementcount) method of `NSBezierPath` returns the total number of path elements for all subpaths of the object. To find out the type of a given path element, use the [elementAtIndex:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520751-element) or [elementAtIndex:associatedPoints:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520674-elementatindex) method. These methods return one of the values listed in [Table 8-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgywueqsdjbbeoski). Use the `elementAtIndex:associatedPoints:` method if you also want to retrieve the points associated with an element. If you do not already know the type of the path element, you should pass this method an array capable of holding at least three `NSPoint` data types.

To change the points associated with a path element, use the [setAssociatedPoints:atIndex:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520671-setassociatedpoints) method. You cannot change the type of a path element, only the points associated with it. When changing the points, `NSBezierPath` takes only as many points from your point array as are needed. For example, if you specify three points for a Line To path element, only the first point is used.

Listing 8-13 shows a method that updates the control point associated with a curve path element on the end of the current path. The points that define the curve are stored in the order `controlPoint1`, `controlPoint2`, `endPoint`. This method replaces the point `controlPoint2`, which affects the end portion of the curve.

__Listing 8-13__  Changing the control point of a curve path element

```objc
- (void)replaceLastControlPointWithPoint:(NSPoint)newControl
            inPath:(NSBezierPath*)thePath
{
    int elemCount = [thePath elementCount];
    NSBezierPathElement elemType =
                [thePath elementAtIndex:(elemCount - 1)];

    if (elemType != NSCurveToBezierPathElement)
        return;

    // Get the current points for the curve.
    NSPoint points[3];
    [thePath elementAtIndex:(elemCount - 1) associatedPoints:points];

    // Replace the old control point.
    points[1] = newControl;

    // Update the points.
    [thePath setAssociatedPoints:points atIndex:(elemCount - 1)];
}
```


The coordinate system of an [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath) object always matches the coordinate system of the view in which it is drawn. Thus, given a path whose first point is at (0, 0) in your `NSBezierPath` object, drawing the path in your view places that point at (0, 0) in the view’s current coordinate system. To draw that path in a different location, you must apply a transform in one of two ways:

- Apply the transform to the view coordinate system and then draw the path. For information on how to apply transforms to a view, see [Creating and Applying a Transform](Coordinate%20Systems%20and%20Transforms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgqwueq2jjbeumrkb).
- Apply the transform to the `NSBezierPath` object itself using the [transformUsingAffineTransform:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520635-transform) method and then draw it in an unmodified view.

Both techniques cause the path to be drawn at the same location in the view; however, the second technique also has the side effect of permanently modifying the `NSBezierPath` object. Depending on your content, this may or may not be appropriate. For example, in an illustration program, you might want the user to be able to drag shapes around the view; therefore, you would want to modify the `NSBezierPath` object to retain the new position of the path.

There may be times when it is necessary to convert an [NSBezierPath](https://developer.apple.com/documentation/appkit/nsbezierpath) object to a [CGPathRef](https://developer.apple.com/documentation/coregraphics/cgpath) data type so that you can perform path-based operations using Quartz. For example, you might want to draw your path to a Quartz transparency layer or use it to do advanced hit detection. Although you cannot use a `NSBezierPath` object directly from Quartz, you can use its path elements to build a `CGPathRef` object.

Listing 8-14 shows you how to create a `CGPathRef` data type from an `NSBezierPath` object. The example extends the behavior of the `NSBezierPath` class using a category. The `quartzPath` method uses the path elements of the `NSBezierPath` object to call the appropriate Quartz path creation functions. Although the method creates a mutable `CGPathRef` object, it returns an immutable copy for drawing. To ensure that the returned path returns correct results during hit detection, this method implicitly closes the last subpath if your code does not do so explicitly. Quartz requires paths to be closed in order to do hit detection on the path’s fill area.

__Listing 8-14__  Creating a CGPathRef from an NSBezierPath

```objc
@implementation NSBezierPath (BezierPathQuartzUtilities)
// This method works only in OS X v10.2 and later.
- (CGPathRef)quartzPath
{
    int i, numElements;

    // Need to begin a path here.
    CGPathRef           immutablePath = NULL;

    // Then draw the path elements.
    numElements = [self elementCount];
    if (numElements > 0)
    {
        CGMutablePathRef    path = CGPathCreateMutable();
        NSPoint             points[3];
        BOOL                didClosePath = YES;

        for (i = 0; i < numElements; i++)
        {
            switch ([self elementAtIndex:i associatedPoints:points])
            {
                case NSMoveToBezierPathElement:
                    CGPathMoveToPoint(path, NULL, points[0].x, points[0].y);
                    break;

                case NSLineToBezierPathElement:
                    CGPathAddLineToPoint(path, NULL, points[0].x, points[0].y);
                    didClosePath = NO;
                    break;

                case NSCurveToBezierPathElement:
                    CGPathAddCurveToPoint(path, NULL, points[0].x, points[0].y,
                                        points[1].x, points[1].y,
                                        points[2].x, points[2].y);
                    didClosePath = NO;
                    break;

                case NSClosePathBezierPathElement:
                    CGPathCloseSubpath(path);
                    didClosePath = YES;
                    break;
            }
        }

        // Be sure the path is closed or Quartz may not do valid hit detection.
        if (!didClosePath)
            CGPathCloseSubpath(path);

        immutablePath = CGPathCreateCopy(path);
        CGPathRelease(path);
    }

    return immutablePath;
}
@end
```

The code from the preceding example closes only the last open path by default. Depending on your path objects, you might also want to close intermediate subpaths whenever a new Move To element is encountered. If your path objects typically contain only one path, you do not need to do so, however.

If you need to determine whether a mouse event occurred on a path or its fill area, you can use the [containsPoint:](https://developer.apple.com/documentation/appkit/nsbezierpath/1520716-contains) method of `NSBezierPath`. This method tests the point against all closed and open subpaths in the path object. If the point lies on or inside any of the subpaths, the method returns `YES`. When determining whether a point is inside a subpath, the method uses the nonzero winding rule.

If your software runs in OS X v10.4 and later, you can perform more advanced hit detection using the [CGContextPathContainsPoint](https://developer.apple.com/documentation/coregraphics/cgcontext/1454778-pathcontains) and [CGPathContainsPoint](https://developer.apple.com/documentation/coregraphics/1411175-cgpathcontainspoint) functions in Quartz. Using these functions you can determine if a point is on the path itself or if the point is inside the path using either the nonzero or even-odd winding rule. Although you cannot use these functions on an `NSBezierPath` object directly, you can convert your path object to a `CGPathRef` data type and then use them. For information on how to convert a path object to a `CGPathRef` data type, see [Creating a CGPathRef From an NSBezierPath Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgywvgvzs).

Listing 8-15 shows an example of how you might perform advanced hit detection on an `NSBezierPath` object. This example adds a method to the `NSBezierPath` class using a category. The implementation of the method adds a `CGPathRef` version of the current path to the current context and calls the [CGContextPathContainsPoint](https://developer.apple.com/documentation/coregraphics/cgcontext/1454778-pathcontains) function. This function uses the specified mode to analyze the location of the specified point relative to the current path and returns an appropriate value. Modes can include [kCGPathFill](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode/kcgpathfill), [kCGPathEOFill](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode/kcgpatheofill), [kCGPathStroke](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode/kcgpathstroke), [kCGPathFillStroke](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode/fillstroke), or [kCGPathEOFillStroke](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode/kcgpatheofillstroke).

__Listing 8-15__  Detecting hits on a path

```objc
@implementation NSBezierPath (BezierPathQuartzUtilities)
// Note, this method works only in OS X v10.4 and later.
- (BOOL)pathContainsPoint:(NSPoint)point forMode:(CGPathDrawingMode)mode
{
    CGPathRef       path = [self quartzPath]; // Custom method to create a CGPath
    CGContextRef    cgContext = (CGContextRef)[[NSGraphicsContext currentContext] graphicsPort];
    CGPoint         cgPoint;
    BOOL            containsPoint = NO;

    cgPoint.x = point.x;
    cgPoint.y = point.y;

    // Save the graphics state before doing the hit detection.
    CGContextSaveGState(cgContext);

    CGContextAddPath(cgContext, path);
    containsPoint = CGContextPathContainsPoint(cgContext, cgPoint, mode);

    CGContextRestoreGState(cgContext);

    return containsPoint;
}
@end
```

[Next](Incorporating%20Other%20Drawing%20Technologies.md)[Previous](Text.md)

