---
title: Transforms
framework: Core Animation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/transforms
source_url: 'https://developer.apple.com/documentation/quartzcore/transforms'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/transforms.json'
content_hash: 'sha256:5885657b59ad3ddd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# Transforms

<sub>API Collection</sub>

Define transform matrices to apply affine transformations to layers in Core Animation.

## Topics

### Creating Transforms

- [CATransform3DMakeTranslation](<catransform3dmaketranslation(______).md>) — Returns a transform that translates by `(tx, ty, tz)`.
- [CATransform3DMakeScale](<catransform3dmakescale(______).md>) — Returns a transform that scales by `(sx, sy, sz)`.
- [CATransform3DMakeRotation](<catransform3dmakerotation(________).md>) — Returns a transform that rotates by `angle` radians about the vector `(x, y, z)`.

### Chaining Transforms

- [CATransform3DConcat](<catransform3dconcat(____).md>) — Concatenates `b` to `a` and returns the result: `t = a * b`.
- [CATransform3DTranslate](<catransform3dtranslate(________).md>) — Translates `t` by `(tx, ty, tz)` and returns the result: `t` `= translate(tx, ty, tz) * t`.
- [CATransform3DScale](<catransform3dscale(________).md>) — Scales `t` by `(sx, sy, sz)` and returns the result: `t = scale(sx, sy, sz) * t`.
- [CATransform3DRotate](<catransform3drotate(__________).md>) — Rotates `t` by `angle` radians about the vector `(x, y, z)` and returns the result.

### Inverting a Transform

- [CATransform3DInvert](<catransform3dinvert(__).md>) — Inverts `t` and returns the result.

### Determining Transform Properties

- [CATransform3DIsAffine](<catransform3disaffine(__).md>) — Returns a Boolean value that indicates whether a transform can be exactly represented by an affine transform.
- [CATransform3DIsIdentity](<catransform3disidentity(__).md>) — Returns a Boolean value that indicates whether the transform is the identity transform.
- [CATransform3DEqualToTransform](<catransform3dequaltotransform(____).md>) — Returns a Boolean value that indicates whether the two transforms are exactly equal.

### Converting to and from Core Graphics Affine Transforms

- [CATransform3DMakeAffineTransform](<catransform3dmakeaffinetransform(__).md>) — Returns a transform with the same effect as affine transform `m`.
- [CATransform3DGetAffineTransform](<catransform3dgetaffinetransform(__).md>) — Returns the affine transform represented by `t`.

### Data Types

- [CATransform3D](catransform3d.md) — The standard transform matrix used throughout Core Animation.

### Constants

- [CATransform3DIdentity](catransform3didentity.md) — The identity transform: `[1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1]`.
