---
title: Scale Value Functions
framework: Core Animation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/scale-value-functions
source_url: 'https://developer.apple.com/documentation/quartzcore/scale-value-functions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/scale-value-functions.json'
content_hash: 'sha256:f6d9cfd1cb44dd70'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md) · [CAValueFunction](cavaluefunction.md)

# Scale Value Functions

<sub>API Collection</sub>

Scale value transform functions construct a 4x4 matrix that represents the corresponding scale matrix.

## Topics

### Constants

- [kCAValueFunctionScale](cavaluefunctionname/scale.md) — A value function scales by the input value along all three axis. Animations using this value transform function must provide animation values in an `NSArray` of three `NSNumber` instances that specify the (x, y, z) scale values.
- [kCAValueFunctionScaleX](cavaluefunctionname/scalex.md) — A value function scales by the input value along the x-axis. Animations referencing this value transform function must provide a single animation value.
- [kCAValueFunctionScaleY](cavaluefunctionname/scaley.md) — A value function scales by the input value along the y-axis. Animations referencing this value function must provide a single animation value.
- [kCAValueFunctionScaleZ](cavaluefunctionname/scalez.md) — A value function that scales by the input value along the z-axis. Animations referencing this value function must provide a single animation value.

## See Also

### Constants

- [Rotate Value Functions](rotate-value-functions.md) — Rotate value transform functions construct a 4x4 matrix that represents the corresponding rotation matrix.
- [Translate Functions](translate-functions.md) — Translate value transform functions construct a 4x4 matrix that represents the corresponding translate matrix.
