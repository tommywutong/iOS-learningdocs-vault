---
title: Shape Fill Mode Values
framework: Core Animation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/shape-fill-mode-values
source_url: 'https://developer.apple.com/documentation/quartzcore/shape-fill-mode-values'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/shape-fill-mode-values.json'
content_hash: 'sha256:a464d582b0330ded'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md) · [CAShapeLayer](cashapelayer.md)

# Shape Fill Mode Values

<sub>API Collection</sub>

These constants specify the possible fill modes for [fillRule](cashapelayer/fillrule.md).

## Topics

### Constants

- [kCAFillRuleNonZero](cashapelayerfillrule/nonzero.md) — Specifies the non-zero winding rule. Count each left-to-right path as +1 and each right-to-left path as -1. If the sum of all crossings is 0, the point is outside the path. If the sum is nonzero, the point is inside the path and the region containing it is filled.
- [kCAFillRuleEvenOdd](cashapelayerfillrule/evenodd.md) — Specifies the even-odd winding rule. Count the total number of path crossings. If the number of crossings is even, the point is outside the path. If the number of crossings is odd, the point is inside the path and the region containing it should be filled.

## See Also

### Constants

- [Line Join Values](line-join-values.md) — These constants specify the shape of the joints between connected segments of a stroked path.
- [Line Cap Values](line-cap-values.md) — These constants specify the shape of endpoints for an open path when stroked.
