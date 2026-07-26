---
title: Legacy Signpost Symbols
framework: os
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/os/legacy-signpost-symbols
source_url: 'https://developer.apple.com/documentation/os/legacy-signpost-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/legacy-signpost-symbols.json'
content_hash: 'sha256:a8d59196fa6f5484'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md) · [Logging](logging.md)

# Legacy Signpost Symbols

<sub>API Collection</sub>

Migrate your code away from using these legacy symbols.

## Topics

### Measure Events

- [os_signpost(_:dso:log:name:signpostID:)](<os_signpost(__dso_log_name_signpostid_)-2oz8u.md>) — Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments. _(deprecated)_
- [os_signpost(_:dso:log:name:signpostID:_:_:)](<os_signpost(__dso_log_name_signpostid_____)-2om9b.md>) — Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments, and includes a detailed message. _(deprecated)_
- [OSSignpostType](ossignposttype.md) — The different kinds of signpost. _(deprecated)_
- [os_signpost(_:dso:log:name:signpostID:)](<os_signpost(__dso_log_name_signpostid_)-12m3v.md>) — Logs the beginning of an animation as a point-of-interest in your code, without a message. _(deprecated)_
- [os_signpost(_:dso:log:name:signpostID:_:_:)](<os_signpost(__dso_log_name_signpostid_____)-nez5.md>) — Logs the beginning of an animation as a point-of-interest in your code, and includes the specified message in the logs. _(deprecated)_
- [OSSignpostAnimationBegin](ossignpostanimationbegin.md) — The signpost options to use when measuring animations. _(deprecated)_
- [AnimationFormatString](animationformatstring.md) — A namespace for utilities specific to animation-related signposts. _(deprecated)_
- [os_signpost_id_t](os_signpost_id_t.md) — An identifier you use to distinguish between signposts that have the same name and destination log.

## See Also

### Measure Events

- [Recording Performance Data](recording-performance-data.md) — Add signposts to record interesting time-based events.
- [OSSignposter](ossignposter.md) — An object for measuring task performance using the unified logging system.
- [OSSignpostType](ossignposttype.md) — The different kinds of signpost. _(deprecated)_
- [os_signpost_id_t](os_signpost_id_t.md) — An identifier you use to distinguish between signposts that have the same name and destination log.
