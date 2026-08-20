---
title: Safari CSS Reference
apple_id: TP40002050
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: User Experience
technology: WebKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariCSSRef/Articles/Functions.html
archived_at: '2026-07-15T05:19:01.763084Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari CSS Reference](Introduction%20to%20Safari%20CSS%20Reference.md)


[Next](Document%20Revision%20History.md)[Previous](Supported%20CSS%20Rules.md)

# CSS Property Functions

This chapter describes the functions you can use with supported CSS properties.

Gradient functions can be passed to the `background` and `background-image` properties.

Specifies an intermediary color value for a gradient.

```
color-stop(stop, color)
```

____Parameters____: __`stop`__: The point in the gradient that should have the specified color value. Represented as a percentage or a decimal value between `0` and `1`.

__`color`__: The color of the gradient at the stop.

____Discussion____: For more information, see `[-webkit-gradient](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tsnjvfvjvomrv)`.

____Availability____: Available in Safari 4.0 and later.

A convenience function for the `[color-stop](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tsnjvfvjvomrw)` function that specifies the first color stop in a gradient.

```
from(color)
```

____Parameters____: __`color`__: The color of the gradient at the stop.

____Discussion____: Equivalent to calling `color-stop()` with a `stop` value of `0%`.

____Availability____: Available in Safari 4.0 and later.

A convenience function for the `[color-stop](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tsnjvfvjvomrw)` function that specifies the last color stop in a gradient.

```
to(color)
```

____Parameters____: __`color`__: The color of the gradient at the stop.

____Discussion____: Equivalent to calling `color-stop()` with a `stop` value of `100%`.

____Availability____: Available in Safari 4.0 and later.

Generates a gradient image.

```
-webkit-gradient(type, start_point, end_point, / stop...)
-webkit-gradient(type, inner_center, inner_radius, outer_center, outer_radius, / stop...)
```

____Parameters____: __`type`__: The type of gradient. Can be `linear` or `radial`.

__`start_point`__: The point in the image at which the linear gradient begins.

__`end_point`__: The point in the image at which the linear gradient ends.

__`stop`__: A `color-stop()` function indicating the desired color for the gradient at a particular point in its progression.

__`inner_center`__: The center point of the inner, starting circle in a radial gradient.

__`inner_radius`__: The radius of the inner, starting circle in a radial gradient.

__`outer_center`__: The center point of the outer, ending circle in a radial gradient.

__`outer_radius`__: The radius of the outer, ending circle in a radial gradient.

____Constants____: __`left top`__: The point corresponding to the top left corner of the image.

__`left bottom`__: The point corresponding to the bottom left corner of the image.

__`right top`__: The point corresponding to the top right corner of the image.

__`right bottom`__: The point corresponding to the bottom right corner of the image.

____Discussion____: `-webkit-gradient()` can be used in any place an image URL is used.

A linear gradient determines its color by interpolating between values specified by the `color-stop()` functions provided. Each `color-stop()` function specifies a percentage or a decimal between `0` and `1` and a color, indicating that the gradient should have the specified color value at the specified fraction of the gradient’s length. The shorthand functions `from()` and `to()` are supported as special-case `color-stop()` functions. The following example creates a linear gradient that shifts from yellow to orange in its first half and from orange to red in its second half, moving from the top left of the image to the bottom right of the image:

```
-webkit-gradient(linear, left top, right bottom, from(#ff0), color-stop(0.5, orange), to(rgb(255, 0, 0));
```

A radial gradient specifies its start and end with two (typically concentric) circles, each identified by a center point and radius. The color value at a point between the circumference of the inner circle and the circumference of the outer circle is determined by interpolating between `color-stop()` functions. The color value inside the inner circle is the color value of the first `color-stop()` function.

____Availability____: Available in Safari 4.0 and later.

Generates a linear gradient image.

```
-webkit-linear-gradient(direction | angle, color_stop,... )
```

____Parameters____: __`direction`__: Specifies the gradient line which gives the gradient a direction and determines how color stops are positioned. Possible values are described in “Constants.” The default value is `top`.

__`angle`__: Optionally, specifies the gradient line as an angle value where `0` degrees is east, `90` degrees is north, and positive angles are counter-clockwise.

__`color_stop`__: A color for the gradient at a particular point in its progression. You can specify multiple color stops including a start and end color.

Color stops are expressed as two values with the following syntax: _color_ | _stop_.

__`color`__: The color of the gradient at the stop. This parameter is mandatory.

__`stop`__: The point in the gradient that should have the specified color value. The position can be specified in pixels or as a percentage of the gradient line. When a position is not specified, the browser distributes the color stop evenly between the adjacent color stops. Color stops at the same position result in sharp color changes.

____Constants____: __`bottom`__: The bottom side of the image.

__`bottom left`__: The bottom left corner of the image.

__`bottom right`__: The bottom right corner of the image.

__`left`__: The left side of the image.

__`top`__: The top side of the image.

__`top left`__: The top left corner of the image.

__`top right`__: The top right corner of the image.

__`right`__: The right side of the image.

____Discussion____: Parameters that have default values are optional. However, two or more color stops are required to render a gradient.

For example, you can create a paper roll effect on one side:

```
.ribbon {
background-image:
   -webkit-linear-gradient(
      left, #900, #F33 10px, red 50px);
}
```

This can be combined with another gradient to create a ribbon with a diagonal edge:

```
.ribbon {
background-image:
   -webkit-linear-gradient(
      left, #900, #F33 10px, rgba(255, 0, 0, 0) 50px),
   -webkit-linear-gradient(135deg, transparent 25%, red 25%);
}
```

____Availability____: Available in Safari 5.1 and later.

Available in iOS 5.0 and later.

Generates a radial gradient image.

```
-webkit-radial-gradient(center, [shape ||  size] | [length | percentage], color_stop,...)
```

____Parameters____: __`center`__: The center point of the cirlce or ellipse. This parameter allows you to move the origin of the shape. The position can be specified in terms of pixels or percentages of the image or using the keywords `top`, `left`, `center`, `right`, or `bottom`. The default is `center`.

__`shape`__: The shape of the radient. Possible values are `circle` and `ellipse`. The default is `ellipse`.

__`size`__: The size of the radient. Possible values are `closest-side`, `closest-corner`, `farthest-side`, `farthest-corner`, `contain`, and `cover`. The default is `cover`.

__`length`__: Optionally, specifies the shape of an eclipse by providing two lengths: the length of the horizontal and vertical axes of the ellipse. The axis length is the length from the center of the ellipse to the edge, not the diameter. The lengths must be non-negative.

__`percentage`__: Optionally, specifies the shape of an eclipse by providing two percentage values: the percentage of the horizontal and vertical axes of the eclipse relative to the width and height of the box. The percentages must be non-negative.

__`color_stop`__: A color for the gradient at a particular point in its progression. You can specify multiple color stops including a start and end color.

Color stops are expressed as two values with the following syntax: _color_ | _stop_.

__`color`__: The color of the gradient at the stop. This parameter is mandatory.

__`stop`__: The point in the gradient that should have the specified color value. The position can be specified in pixels or as a percentage of the gradient line. When a position is not specified, the browser distributes the color stop evenly between the adjacent color stops. Color stops at the same position result in sharp color changes.

For example, specify a gradient that progresses equally from red to green and then green to blue as follows:

```
-webkit-linear-gradient(left, red, green, blue)
```

Specify a gradient where red starts at `20px` and blue starts at `90%` with other colors distributed between as follows:

```
-webkit-linear-gradient(bottom left, red 20px, yellow, green, blue 90%)
```

Create a sharp color change between green and purple as follows:

```
-webkit-linear-gradient(top left, red, yellow, green 60%, purple 60%, blue)
```

____Discussion____: Parameters that have default values are optional. However, one or more color stops are required to render a gradient. If only one parameter is provided before the color stops and it could be interpreted as either a position or an explicit size, it is assumed to be a position.

For example, the following gradient is centered in the box and is large enough to fill it to the corners:

```
-webkit-radial-gradient(white, black)
```

This is equivalent to:

```
-webkit-radial-gradient(center, ellipse cover, white, black)
```

You can also specify an alternate origin than `center` as follows:

```
-webkit-radial-gradient(10% 30%, white, black)
```

Examples of specifying the shape and size of the gradient are:

```
-webkit-radial-gradient(30% 30%, closest-corner, white, black)
-webkit-radial-gradient(30% 30%, circle closest-corner, white, black)
```

where `circle` specifies the shape and `closest-corner` specifies the size.

You can also specify the ending radius of the gradient explicitly and separately for the horizontal and vertical axes:

```
-webkit-radial-gradient(center, 5em 40px, white, black)
```

where `5em` is the x-value and `40px` is the y-value.

If only percentages appear before color stops, the parameters are interpreted as a starting point, not the size of the ellipse:

```
-webkit-radial-gradient(10% 10%, red, blue)
```

____Availability____: Available in Safari 5.1 and later.

Available in iOS 5.0 and later.

Generates a linear gradient where the specified color stops repeat in both directions to fill the image.

```
-webkit-linear-gradient(direction | angle, color_stop,... )
```

____Parameters____: __`direction`__: Specifies the gradient line which gives the gradient a direction and determines how color stops are positioned. Possible values are described in “Constants.” The default value is `top`.

__`angle`__: Specifies the gradient line as an angle value where `0` degrees is east, `90` degrees is north, and positive angles are counter-clockwise.

__`color_stop`__: A color for the gradient at a particular point in its progression. You can specify multiple color stops including a start and end color.

Color stops are expressed as two values with the following syntax: _color_ | _stop_.

__`color`__: The color of the gradient at the stop. This parameter is mandatory.

__`stop`__: The point in the gradient that should have the specified color value. The position can be specified in pixels or as a percentage of the gradient line. When a position is not specified, the browser distributes the color stop evenly between the adjacent color stops. Color stops at the same position result in sharp color changes.

____Constants____: __`bottom`__: The bottom side of the image.

__`bottom left`__: The bottom left corner of the image.

__`bottom right`__: The bottom right corner of the image.

__`left`__: The left side of the image.

__`top`__: The top side of the image.

__`top left`__: The top left corner of the image.

__`top right`__: The top right corner of the image.

__`right`__: The right side of the image.

____Discussion____: The parameters are the same as `[-webkit-linear-gradient](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tsnjvfvjvomzr)` except the color stops are repeated. If a parameter is omitted, the default value is used.

The specified color stops are repeated infinitely in both directions by aligning them end-to-end. For example, this gradient:

```
-webkit-repeating-linear-gradient(red 10px, blue 50px)
```

is interpreted as:

```
-webkit-repeating-linear-gradient(..., red -30px, blue 10px, red 10px, blue 50px, red 50px, blue 90px, ...)
```

Note that the boundary between the last color stop and the first color stop may result in a sharp color change. To avoid this, use the same color in the first and last color stop as in:

```
-webkit-repeating-linear-gradient(red, blue 10%, red 20%)
```

____Availability____: Available in Safari 5.1 and later.

Available in iOS 5.0 and later.

Generates a radial gradient where the specified color stops repeat in both directions to fill the image.

```
-webkit-radial-gradient(start_position, [shape ||  size] | [length | percentage], color_stop,...)
```

____Parameters____: __`start_position`__: The starting point of the radial gradient. This parameter allows you to move the origin of the shape. The position can be specified in terms of pixels or percentages of the image or using the keywords `top`, `left`, `center`, `right`, or `bottom`. The default is `center`.

__`shape`__: The shape of the radient. Possible values are `circle` and `ellipse`. The default is `ellipse`.

__`size`__: The size of the radient. Possible values are `closest-side`, `closest-corner`, `farthest-side`, `farthest-corner`, `contain`, and `cover`. The default is `cover`.

__`length`__: Specifies the shape of an eclipse by providing two lengths: the length of the horizontal and vertical axes of the ellipse. The axis length is the length from the center of the ellipse to the edge, not the diameter. The lengths must be non-negative.

__`percentage`__: Specifies the shape of an eclipse by providing two percentage values: the percentage of the horizontal and vertical axes of the eclipse relative to the width and height of the box. The percentages must be non-negative.

__`color_stop`__: A color for the gradient at a particular point in its progression. You can specify multiple color stops including a start and end color.

Color stops are expressed as two values with the following syntax: _color_ | _stop_.

__`color`__: The color of the gradient at the stop. This parameter is mandatory.

__`stop`__: The point in the gradient that should have the specified color value. The position can be specified in pixels or as a percentage of the gradient line. When a position is not specified, the browser distributes the color stop evenly between the adjacent color stops. Color stops at the same position result in sharp color changes.

____Discussion____: The parameters are the same as `[-webkit-radial-gradient](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tsnjvfvjvomzs)` except the color stops are repeated. If a parameter is omitted, the default value is used.

For example, you can create a bulls-eye effect as follows:

```
-webkit-repeating-radial-gradient(
   transparent, rgba(0, 0, 0, 0.3) 50px);
```

____Availability____: Available in Safari 5.1 and later.

Available in iOS 5.0 and later.

Timing functions specify the easing technique for animations.

Specifies a cubic Bézier curve.

`cubic-bezier(P1x,P1y,P2x,P2y)`

____Parameters____: __`P1x, P1y`__: First point in the Bézier curve.

__`P2x, P2y`__: Second point in the Bézier curve.

____Discussion____: A cubic Bézier curve is defined by four control points, `P0` through `P3`. `P0` and `P3` are always set to `(0,0)` and `(1,1)`. This function is used to set the values for the points in between, points `P1` and `P2`. Each point is specified by both an x and y value.

____Availability____: Available in Safari 3.1 and later.

Available in iOS 2.0 and later.

Defines steps from one frame to another, not a smooth transition.

`steps(number, point)`

____Parameters____: __`number`__: The number of intervals in the function. Must be greater than `0`.

__`point`__: The point at which the change of values occur within the interval. Possible values are `start` or `end`. The default value is `end`.

____Discussion____: Stepping functions are appropriate for progress indicators. A stepping function is defined by a number of equal duration intervals and whether the change in output percentage happens at the start or end of the interval.

____Availability____: Available in iOS 5.0 and later.

Transform functions can be passed to the `-webkit-transform` property.

Specifies a 2D transformation in the form of a transformation matrix of six values.

`matrix(m11, m12, m21, m22, tX, tY)`

____Parameters____: ___m11, m12, m21, m22___: Elements of a 2 x 2 matrix in column-major order.

|  |  |
| --- | --- |
| 1,1 | 2,1 |
| 1,2 | 2,2 |

___tX, tY___: The x and y translation elements.

____Discussion____: Passing `matrix(a,b,c,d,e,f)` is equivalent to applying the transformation matrix `[a b c d e f]`.

____Availability____: Available in Safari 3.1 and later.

Available in iOS 2.0 and later.

Specifies a 3D transformation as a 4 x 4 matrix.

`matrix3d(m00, m01, m02, m03, m10, m11, m12, m13, m20, m21, m22, m23, m30, m31, m31, m33)`

____Parameters____: ___m00, m01, m02, m03, m10, m11, m12, m13, m20, m21, m22, m23, m30, m31, m31, m33___: Defines a 4 x 4 homogeneous matrix of 16 values in column-major order (`0,0`; `0,1`; `0,2`; ...).

|  |  |  |  |
| --- | --- | --- | --- |
| 0,0 | 1,0 | 2,0 | 3,0 |
| 0,1 | 1,1 | 2,1 | 3,1 |
| 0,2 | 1,2 | 2,2 | 3,2 |
| 0,3 | 1,3 | 2,3 | 3,3 |

____Availability____: Available in Safari 4.0.3 and later running on Mac OS X v10.6 and later.

Available in iOS 2.0 and later.

Specifies a perspective projection matrix.

`perspective(depth)`

____Parameters____: ___depth___: The distance, in pixels, of the z=0 plane from the viewer.

____Discussion____: This matrix maps a viewing cube onto a pyramid whose base is infinitely far away from the viewer and whose peak represents the viewer's position.

The viewable area is the region bounded by the four edges of the viewport (the portion of the browser window used for rendering the webpage between the viewer’s position and a point at a distance of infinity from the viewer).

Lower values for this property give a more flattened pyramid and therefore a more pronounced perspective effect. A value of 1000 pixels gives a moderate amount of foreshortening, and a value of 200 pixels gives an extreme amount.

____Availability____: Available in Safari 4.0.3 and later running on Mac OS X v10.6 and later.

Available in iOS 2.0 and later.

Specifies a 2D rotation around the origin of the element.

`rotate(angle)`

____Parameters____: ___angle___: The rotation angle. The angle may be specified using `deg`, `rad` or `grad` units.

____Discussion____: The rotation operation corresponds to the matrix `[cos(angle) sin(angle) -sin(angle) cos(angle) 0 0]`. The origin of the element is specified using the `-webkit-transform-origin` property.

____Availability____: Available in Safari 3.1 and later.

Available in iOS 2.0 and later.

Specifies a clockwise 3D rotation.

`rotate3d(x, y, z, angle)`

____Parameters____: ___x, y, z___: The `[x,y,z]` direction vector for the rotation.

If the direction vector is not of unit length, it will be normalized. If the direction vector cannot be normalized, such as `[0, 0, 0]`, the rotation will not be applied.

___angle___: The rotation angle. The angle may be specified using `deg`, `rad` or `grad` units.

____Availability____: Available in Safari 4.0.3 and later running on Mac OS X v10.6 and later.

Available in iOS 2.0 and later.

Specifies a clockwise rotation by the given angle about the x-axis.

`rotateX(angle)`

____Parameters____: ___angle___: The rotation angle. The angle may be specified using `deg`, `rad` or `grad` units.

____Availability____: Available in Safari 4.0.3 and later running on Mac OS X v10.6 and later. Available in iOS 2.0 and later.

Specifies a clockwise rotation by the given angle about the y-axis.

`rotateY(angle)`

____Parameters____: ___angle___: The rotation angle. The angle may be specified using `deg`, `rad` or `grad` units.

____Availability____: Available in Safari 4.0.3 and later running on Mac OS X v10.6 and later.

Available in iOS 2.0 and later.

Specifies a clockwise rotation by the given angle about the z-axis.

`rotateZ(angle)`

____Parameters____: ___angle___: The angle of the rotation. The angle may be specified using `deg`, `rad` or `grad` units.

____Availability____: Available in Safari 4.0.3 and later running on Mac OS X v10.6 and later.

Available in iOS 2.0 and later.

Specifies a 2D scale operation.

`scale(scaleX [, scaleY])`

____Parameters____: ___scaleX___: The scaling factor to apply in the x direction.

___scaleY___: The scaling factor to apply in the y direction. If not specified, defaults to _scaleX_.

____Availability____: Available in Safari 3.1 and later.

Available in iOS 2.0 and later.

Specifies a 3D scale operation.

`scale3d(scaleX, scaleY, scaleZ)`

____Parameters____: ___scaleX___: The scaling factor to apply in the x direction.

___scaleY___: The scaling factor to apply in the y direction.

___scaleZ___: The scaling factor to apply in the z direction.

____Availability____: Available in Safari 4.0.3 and later running on Mac OS X v10.6 and later.

Available in iOS 2.0 and later.

Scales in the x direction.

`scaleX(sx)`

____Parameters____: ___sx___: The scaling factor to apply to the x direction.

____Discussion____: This function specifies a scale operation using the `[sx, 1, 1]` scaling vector.

____Availability____: Available in Safari 4.0.3 and later running on Mac OS X v10.6 and later.

Available in iOS 2.0 and later.

Scales in the y direction.

`scaleY(sy)`

____Parameters____: __sy__: The scaling factor to apply to the y direction.

____Discussion____: This function specifies a scale operation using the `[1,sy,1]` scaling vector.

____Availability____: Available in Safari 4.0.3 and later running on Mac OS X v10.6 and later.

Available in iOS 2.0 and later.

Scales in the z direction.

scaleZ(sz)

____Parameters____: ___sz___: The scaling factor to apply to the z direction.

____Discussion____: This function specifies a scale operation using the `[1,1,sz]` scaling vector.

____Availability____: Available in Safari 4.0.3 and later running on Mac OS X v10.6 and later.

Available in iOS 2.0 and later.

Specifies a skew transformation along the x and y axes by given angles.

`skew(angleX [, angleY])`

____Parameters____: ___angleX___: The angle of the skew along the x-axis. The angle may be specified using `deg`, `rad` or `grad` units.

___angleY___: The angle of the skew along the y-axis. The angle may be specified using `deg`, `rad` or `grad` units. If not specified, defaults to `0`.

____Availability____: Available in Safari 3.1 and later.

Available in iOS 2.0 and later.

Specifies a skew transformation along the x-axis by the given angle.

`skewX(angle)`

____Parameters____: ___angle___: The angle of the skew. The angle may be specified using `deg`, `rad` or `grad` units.

____Availability____: Available in Safari 3.1 and later. Available in iOS 2.0 and later.

Specifies a skew transformation along the x-axis by the given angle.

`skewY(angle)`

____Parameters____: ___angle___: The angle of the skew. The angle may be specified using `deg`, `rad` or `grad` units.

____Availability____: Available in Safari 3.1 and later.

Available in iOS 2.0 and later.

Specifies a 2D translation vector.

`translate(deltaX [, deltaY])`

____Parameters____: ___deltaX___: The number of units to translate along the x-axis. This value may be a percentage or a length.

___deltaY___: The number of units to translate along the y-axis. If not specified, the y translation defaults to `0`. This value may be a percentage or a length.

____Availability____: Available in Safari 3.1 and later.

Available in iOS 2.0 and later.

Specifies a 3D translation vector.

`translate3d(deltaX, deltaY, deltaZ)`

____Parameters____: ___deltaX___: The number of units to translate along the x-axis. This value may be a percentage or a length.

___deltaY___: The number of units to translate along the y-axis. This value may be a percentage or a length.

___deltaZ___: The number of units to translate along the z-axis. This value may be a percentage or a length.

____Availability____: Available in Safari 4.0.3 and later running on Mac OS X v10.6 and later. Available in iOS 2.0 and later.

Specifies a translation in the x direction.

`translateX(deltaX)`

____Parameters____: ___deltaX___: The number of units to translate along the x-axis. This value may be a percentage or a length.

____Availability____: Available in Safari 3.1 and later.

Available in iOS 2.0 and later.

Specifies a translation in the y direction.

`translateY(deltaY)`

____Parameters____: ___deltaY___: The number of units to translate along the y-axis. This value may be a percentage or a length.

____Availability____: Available in Safari 3.1 and later. Available in iOS 2.0 and later.

Specifies a translation in the z direction.

`translateZ(deltaZ)`

____Parameters____: ___deltaZ___: The number of units to translate along the z-axis. This value may be a percentage or a length.

____Availability____: Available in Safari 4.0.3 and later running on Mac OS X v10.6 and later.

Available in iOS 2.0 and later.

Filters are visual effects that can be applied to images and other HTML elements. These functions can be concatenated in any order as parameters to the `-webkit-filter` property. These functions can be animated over time with the `-webkit-animation` property.

Applies a Gaussian blur to the element.

```
blur(radius)
```

____Parameters____: __`radius`__: The blur radius, in pixels.

____Discussion____: The radius is a specific CSS length and does not accept percentage values.

____Availability____: Available in Safari 6.0 and later.

Applies a linear multiplier to the image, making it brighter or darker.

```
brightness(amount)
```

____Parameters____: __`amount`__: The amount of brightness, as a percentage.

____Discussion____: An amount of `-100%` will create an image that is completely black. An amount of `100%` will create an image that is completely white. An amount of `0%` leaves the input unchanged.

____Availability____: Available in Safari 6.0 and later.

Adjusts the contrast of the element.

```
contrast(amount)
```

____Parameters____: __`amount`__: The amount of contrast, as a percentage.

____Discussion____: An amount of `0%` will create an image that is completely gray. An amount of `100%` leaves the image unchanged. Amounts in between linearly affect the contrast.

____Availability____: Available in Safari 6.0 and later.

Applies a drop shadow effect to the image.

```
drop-shadow(h-off v-off blur color)
```

____Parameters____: __`h-off`__: The horizontal offset of the shadow, in pixels.

__`v-off`__: The vertical offset of the shadow, in pixels.

__`blur`__: The blur radius of the shadow, in pixels.

__`color`__: The color of the shadow.

____Discussion____: The function accepts the same parameters as the `-webkit-box-shadow` property, with the exception that the `inset` keyword is not allowed.

____Availability____: Available in Safari 6.0 and later.

Desaturates the image.

```
grayscale(amount)
```

____Parameters____: __`amount`__: The percentage of desaturation.

____Discussion____: An amount of `100%` is completely grayscale. An amount of `0%` leaves the image unchanged.

____Availability____: Available in Safari 6.0 and later.

Desaturates the image.

```
hue-rotate(angle)
```

____Parameters____: __`angle`__: The number of degrees around the color circle the image’s color samples will be adjusted.

____Discussion____: An angle of `0deg` leaves the image unchanged.

____Availability____: Available in Safari 6.0 and later.

Inverts the colors of the image.

```
invert(amount)
```

____Parameters____: __`amount`__: The percentage of inversion.

____Discussion____: An amount of `100%` is completely inverted. An amount of `0%` leaves the image unchanged. Amounts in between are linear multipliers on the effect.

____Availability____: Available in Safari 6.0 and later.

Applies transparency to the image.

```
opacity(amount)
```

____Parameters____: __`amount`__: The percentage of opacity.

____Discussion____: An amount of `0%` is completely transparent. An amount of `100%` leaves the image unchanged.

____Availability____: Available in Safari 6.0 and later.

Saturates the image.

```
saturate(amount)
```

____Parameters____: __`amount`__: The percentage of saturation.

____Discussion____: An amount of `0%` is completely unsaturated. An amount of `100%` leaves the image unchanged. Amounts over `100%` are allowed, providing super-saturated results.

____Availability____: Available in Safari 6.0 and later.

Applies a sepia effect to the image.

```
sepia(amount)
```

____Parameters____: __`amount`__: The percentage of sepia effect to apply.

____Discussion____: An amount of `100%` is completely sepia. An amount of `0%` leaves the input unchanged. Amounts in between are linear multipliers on the effect.

____Availability____: Available in Safari 6.0 and later.

Specifies a canvas for drawing programmatically with Javascript.

```
-webkit-canvas(canvas)
```

____Parameters____: __`canvas`__: The name of the canvas.

____Discussion____: The `-webkit-canvas()` function can be used in any place an image URL is used.

Canvases specified with the `-webkit-canvas()` function can be accessed in Javascript with the method `getCSSCanvasContext()`, which returns a `CanvasRenderingContext` object. The identifier passed to `getCSSCanvasContext()` should be the same as the value for `canvas`.

Specifying a new width or height for the canvas in subsequent calls to `getCSSCanvasContext()` clears the canvas buffer.

____Availability____: Available in Safari 4.0 and later.

[Next](Document%20Revision%20History.md)[Previous](Supported%20CSS%20Rules.md)

