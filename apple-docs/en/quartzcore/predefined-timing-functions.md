---
title: Predefined Timing Functions
framework: Core Animation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/predefined-timing-functions
source_url: 'https://developer.apple.com/documentation/quartzcore/predefined-timing-functions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/predefined-timing-functions.json'
content_hash: 'sha256:2d418202d26d80f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md) · [CAMediaTimingFunction](camediatimingfunction.md)

# Predefined Timing Functions

<sub>API Collection</sub>

Constants that specify system-provided timing functions, used by [+ functionWithName:](<camediatimingfunction/init(name_).md>).

## Topics

### Constants

- [kCAMediaTimingFunctionLinear](camediatimingfunctionname/linear.md) — Linear pacing, which causes an animation to occur evenly over its duration.
- [kCAMediaTimingFunctionEaseIn](camediatimingfunctionname/easein.md) — Ease-in pacing, which causes an animation to begin slowly and then speed up as it progresses.
- [kCAMediaTimingFunctionEaseOut](camediatimingfunctionname/easeout.md) — Ease-out pacing, which causes an animation to begin quickly and then slow as it progresses.
- [kCAMediaTimingFunctionEaseInEaseOut](camediatimingfunctionname/easeineaseout.md) — Ease-in-ease-out pacing, which causes an animation to begin slowly, accelerate through the middle of its duration, and then slow again before completing.
- [kCAMediaTimingFunctionDefault](camediatimingfunctionname/default.md) — The system default timing function. Use this function to ensure that the timing of your animations matches that of most system animations.
