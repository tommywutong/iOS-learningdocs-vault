---
title: Core Image Kernel Language Reference
apple_id: TP40004397
resource_type: Guide
platform: iOS|macOS
topic: Graphics & Animation
technology: CoreImage
published: '2015-01-12'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/ci_gslang_ext.html
archived_at: '2026-07-15T07:39:19.649732Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Image Kernel Language Reference](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Introduction.md)

# Core Image Kernel Language

The following sections list the symbols provided by the Core Image Kernel Language:

- [Functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueqkkirfeeqkb)
- [Data Types](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueqkkjjducrsj)
- [Keywords](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueqkkijeuossk)

You can use these symbols together with any of the OpenGL Shading Language routines that Core Image supports. See [Unsupported Items](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueqkkjjbugscf) for those you can’t use.

This section describes the following functions:

- [compare](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueq2jivbukqsj)
- [cos_](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueq2jijfeqqsc)
- [cossin](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueq2jijcusr2g)
- [cossin_](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueq2jjfeukrke)
- [destCoord](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueq2jjbauirkj)
- [premultiply](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueq2jizbuoq2j)
- [sample](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueq2ji5ceqr2h)
- [samplerCoord](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueq2jjjeeussd)
- [samplerExtent](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueq2jizbuqq2e)
- [samplerOrigin](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueq2jijcesrch)
- [samplerSize](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueq2jizbugscb)
- [samplerTransform](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueq2jivducskk)
- [sin_](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueq2jjffeir2i)
- [sincos](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueq2jirduuqkb)
- [sincos_](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueq2jjfausssg)
- [tan_](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueq2jivduur2e)
- [unpremultiply](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojxfvbuqmrqgywueq2ji5ceuqsd)

**`genType compare (genType x, genType y, genType z)`**
: For each component, returns `x < 0 ? y : z`. Note that `genType` is a placeholder for an arbitrary vector type.

**`genType cos_ (genType x)`**
: Similar to `cos (x)` except that `x` must be in the [`–pi`, `pi`] range. Note that `genType` is a placeholder for an arbitrary vector type.

**`vec2 cossin (float x)`**
: Returns `vec2 (cos (x), sin (x))`.

**`vec2 cossin_ (float x)`**
: Returns `vec2 (cos (x), sin (x))`. This function expects `x` to be in the [`–pi`, `pi`] range.

**`varying vec2 destCoord ()`**
: Returns the position, in working space coordinates, of the pixel currently being computed. The destination space refers to the coordinate space of the image you are rendering.

**`vec4 premultiply (vec4 color)`**
: Multiplies the red, green, and blue components of the `color` parameter by its alpha component.

**`vec4 sample (uniform sampler src, vec2 point)`**
: Returns the pixel value produced from sampler `src` at the position `point`, where `point` is specified in sampler space.

**`varying vec2 samplerCoord (uniform sampler src)`**
: Returns the position, in sampler space, of the sampler `src` that is associated with the current output pixel (that is, after any transformation matrix associated with `src` is applied). The sample space refers to the coordinate space of that you are texturing from.

Note that if your source data is tiled, the sample coordinate will have an offset (dx/dy). You can convert a destination location to the sampler location using the `samplerTransform` function.

**`uniform vec4 samplerExtent (uniform sampler src)`**
: Returns the extent of the sampler in world coordinates, as a four-element vector [x, y, width, height].

**`uniform vec2 samplerOrigin (uniform sampler src)`**
: Equivalent to `samplerExtent (src).xy`.

**`uniform vec2 samplerSize (uniform sampler src)`**
: Equivalent to `samplerExtent (src).zw`.

**`vec2 samplerTransform (uniform sampler src, vec2 point)`**
: Returns the position in the coordinate space of the source (the first argument) that is associated with the position defined in working-space coordinates (the second argument). (Keep in mind that the working space coordinates reflect any transformations that you applied to the working space.)

For example, if you are modifying a pixel in the working space, and you need to retrieve the pixels that surround this pixel in the original image, you would make calls similar to the following, where `d` is the location of the pixel you are modifying in the working space, and `image` is the image source for the pixels.

```
samplerTransform(image, d + vec2(-1.0,-1.0));
samplerTransform(image, d + vec2(+1.0,-1.0));
samplerTransform(image, d + vec2(-1.0,+1.0));
samplerTransform(image, d + vec2(+1.0,+1.0));
```


**`genType sin_ (genType x)`**
: Similar to `sin (x)` except that `x` must be in the [`–pi`, `pi`] range. Note that `genType` is a placeholder for an arbitrary vector type.

**`vec2 sincos (float x)`**
: Returns `vec2 (sin (x), cos (x))`.

**`vec2 sincos_ (float x)`**
: Returns `vec2 (sin (x), cos (x))`. This function expects `x` to be in the [`–pi`, `pi`] range.

**`genType tan_ (genType x)`**
: Similar to `tan (x)` except that `x` must be in the [`–pi`, `pi`] range. Note that `genType` is a placeholder for an arbitrary vector type.

**`vec4 unpremultiply (vec4 color)`**
: If the alpha component of the `color` parameter is greater than 0, divides the red, green and blue components by alpha. If alpha is 0, this function returns `color`.

**`sampler`**
: Specifies a sampler passed in from CISampler that is used to get samples from data.

**`__color`**
: Specifies a type for kernel parameters that need to be color matched to the current CIContext working color space.

**`__table`**
: Specifies a flag for a sampler that fetches values from a lookup table.

The `__table` flag must precede the `sampler` type. The flag ensures that Core Image does not sample the table values using world coordinates.

For example, to use a lookup table sampler in a kernel named `shadedmaterial`, the kernel declaration would be:

`kernel vec4 shadedmaterial(sampler heightfield, __table sampler envmap, float surfaceScale, vec2 envscaling)`

Using the `__table` flag prevents the `envmap` sampler values from being transformed, even if the shaded material kernel gets inserted into a filter chain with an affine transform. If you don’t tag the sampler this way and you chain the shaded material filter to an affine transform for rotation, then looking up values in the environment map results in getting rotated values, which is not correct because the lookup table is simply a data collection.

**`kernel`**
: Specifies a kernel routine. Kernel routines are extracted and compiled by the CIKernel class. A kernel encapsulates the computation required to compute a single pixel in the output image.

Each kernel is tagged by the `kernel` keyword in its return type. The underlying return type of the kernel must be `vec4` . Core Image requires this type in order to return the output pixel for the input pixel currently being evaluated.

All parameters to the kernel are implicitly marked `uniform`. Parameters marked `out` and `inout` are not allowed.

You can pass the following types to a kernel routine:

- `sampler`: Requires a CISampler object when applied.
- `__table`: A qualifier for a `sampler` type.
- `float`, `vec2`, `vec3`, `vec4`: Requires an NSNumber or CIVector.
- `__color`: A color that will be matched to the CIContext working color space when passed into the program. It requires a CIColor object when applied. To the kernel program it appears to be a `vec4` type in premultiplied RGBA format.

Core Image does not support the OpenGL Shading Language source code preprocessor. In addition, the following are not implemented:

- Data types: `mat2`, `mat3`, `mat4`, `struct`, `arrays`
- Statements: `continue`, `break`, `discard`. Other flow control statements (`if`, `for`, `while`, `do while`) are supported only when the loop condition can be inferred at the time the code compiles.
- Expression operators: `% << >> | & ^ || && ^^ ~`
- Built-in functions: `ftransform`, `matrixCompMult`, `dfdx`, `dfdy`, `fwidth`, `noise1`, `noise2`, `noise3`, `noise4`, `refract`

[Next](Document%20Revision%20History.md)[Previous](Introduction.md)

