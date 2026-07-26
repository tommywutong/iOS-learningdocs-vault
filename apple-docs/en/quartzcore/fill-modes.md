---
title: Fill Modes
framework: Core Animation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/fill-modes
source_url: 'https://developer.apple.com/documentation/quartzcore/fill-modes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/fill-modes.json'
content_hash: 'sha256:a1cf3cb9359360ec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md) · [CAMediaTiming](camediatiming.md)

# Fill Modes

<sub>API Collection</sub>

These constants determine how the timed object behaves once its active duration has completed. They are used with the [fillMode](camediatiming/fillmode.md) property.

## Topics

### Constants

- [kCAFillModeRemoved](camediatimingfillmode/removed.md) — The receiver is removed from the presentation when the animation is completed.
- [kCAFillModeForwards](camediatimingfillmode/forwards.md) — The receiver remains visible in its final state when the animation is completed.
- [kCAFillModeBackwards](camediatimingfillmode/backwards.md) — The receiver clamps values before zero to zero when the animation is completed.
- [kCAFillModeBoth](camediatimingfillmode/both.md) — The receiver clamps values at both ends of the object’s time space
