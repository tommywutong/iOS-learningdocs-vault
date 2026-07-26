---
title: CGAffineTransform
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgaffinetransform
source_url: 'https://developer.apple.com/documentation/coregraphics/cgaffinetransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgaffinetransform.json'
content_hash: 'sha256:56f954f1a5bee972'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGAffineTransform

<sub>API Collection</sub>

An affine transformation matrix for use in drawing 2D graphics.

## Overview

A transformation specifies how points in one coordinate system map to points in another coordinate system. An affine transformation is a special type of mapping that preserves parallel lines in a path but does not necessarily preserve lengths or angles. Scaling, rotation, and translation are the most commonly used manipulations supported by affine transforms, but skewing is also possible.

For more information on how to create, concatenate, and apply affine transformations, see [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).

You typically do not need to create an affine transform directly—[CGContext](cgcontext.md) describes functions that modify the current affine transform. If you don’t plan to reuse an affine transform, you may want to use [CGContextScaleCTM](<cgcontext/scaleby(x_y_).md>), [CGContextRotateCTM](<cgcontext/rotate(by_).md>), [CGContextTranslateCTM](<cgcontext/translateby(x_y_).md>), or [CGContextConcatCTM](<cgcontext/concatenate(__).md>).

## Topics

### Creating an Affine Transformation Matrix

- [CGAffineTransformMake](<cgaffinetransformmake(____________).md>) — Returns an affine transformation matrix constructed from values you provide.
- [CGAffineTransformMakeRotation](<cgaffinetransformmakerotation(__).md>) — Returns an affine transformation matrix constructed from a rotation value you provide.
- [CGAffineTransformMakeScale](<cgaffinetransformmakescale(____).md>) — Returns an affine transformation matrix constructed from scaling values you provide.
- [CGAffineTransformMakeTranslation](<cgaffinetransformmaketranslation(____).md>) — Returns an affine transformation matrix constructed from translation values you provide.

### Modifying Affine Transformations

- [CGAffineTransformTranslate](<cgaffinetransformtranslate(______).md>) — Returns an affine transformation matrix constructed by translating an existing affine transform.
- [CGAffineTransformScale](<cgaffinetransformscale(______).md>) — Returns an affine transformation matrix constructed by scaling an existing affine transform.
- [CGAffineTransformRotate](<cgaffinetransformrotate(____).md>) — Returns an affine transformation matrix constructed by rotating an existing affine transform.
- [CGAffineTransformInvert](<cgaffinetransforminvert(__).md>) — Returns an affine transformation matrix constructed by inverting an existing affine transform.
- [CGAffineTransformConcat](<cgaffinetransformconcat(____).md>) — Returns an affine transformation matrix constructed by combining two existing affine transforms.

### Applying Affine Transformations

- [CGPointApplyAffineTransform](<cgpointapplyaffinetransform(____).md>) — Returns the point resulting from an affine transformation of an existing point.
- [CGSizeApplyAffineTransform](<cgsizeapplyaffinetransform(____).md>) — Returns the height and width resulting from a transformation of an existing height and width.
- [CGRectApplyAffineTransform](<cgrectapplyaffinetransform(____).md>) — Applies an affine transform to a rectangle.

### Evaluating Affine Transforms

- [CGAffineTransformIsIdentity](<cgaffinetransformisidentity(__).md>) — Checks whether an affine transform is the identity transform.
- [CGAffineTransformEqualToTransform](<cgaffinetransformequaltotransform(____).md>) — Checks whether two affine transforms are equal.

### Data Types

- [CGAffineTransform](../corefoundation/cgaffinetransform.md)

### Constants

- [CGAffineTransformIdentity](cgaffinetransformidentity.md) — The identity transform.

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
