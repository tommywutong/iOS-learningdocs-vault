---
title: Translate Functions
framework: Core Animation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/translate-functions
source_url: 'https://developer.apple.com/documentation/quartzcore/translate-functions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/translate-functions.json'
content_hash: 'sha256:8a7050a9405dad15'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md) · [CAValueFunction](cavaluefunction.md)

# Translate Functions

<sub>API Collection</sub>

Translate value transform functions construct a 4x4 matrix that represents the corresponding translate matrix.

## Topics

### Constants

- [kCAValueFunctionTranslate](cavaluefunctionname/translate.md) — A value function that translates by the input values along all three axis. Animations using this value transform function must provide animation values in an `NSArray` of three `NSNumber` instances that specify the (x, y, z) translate values.
- [kCAValueFunctionTranslateX](cavaluefunctionname/translatex.md) — A value function translates by the input value along the x-axis. Animations referencing this value function must provide a single input value.
- [kCAValueFunctionTranslateY](cavaluefunctionname/translatey.md) — A value function translates by the input value along the y-axis. Animations referencing this value function must provide a single input value.
- [kCAValueFunctionTranslateZ](cavaluefunctionname/translatez.md) — A value function translates by the input value along the z-axis. Animations referencing this value function must provide a single input value.

## See Also

### Constants

- [Rotate Value Functions](rotate-value-functions.md) — Rotate value transform functions construct a 4x4 matrix that represents the corresponding rotation matrix.
- [Scale Value Functions](scale-value-functions.md) — Scale value transform functions construct a 4x4 matrix that represents the corresponding scale matrix.
