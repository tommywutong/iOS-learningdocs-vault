---
title: OSSignpostAnimationBegin
framework: os
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/os/ossignpostanimationbegin
source_url: 'https://developer.apple.com/documentation/os/ossignpostanimationbegin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignpostanimationbegin.json'
content_hash: 'sha256:e14589d07b04effa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# OSSignpostAnimationBegin

<sub>Enumeration</sub>

The signpost options to use when measuring animations.

> [!warning] Deprecated
> Use [OSSignposter](ossignposter.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum OSSignpostAnimationBegin
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Getting the Animation Options

- [OSSignpostAnimationBegin.animationBegin](ossignpostanimationbegin/animationbegin.md) — A signpost that marks the start of an animation.

## See Also

### Measure Events

- [os_signpost(_:dso:log:name:signpostID:)](<os_signpost(__dso_log_name_signpostid_)-2oz8u.md>) — Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments. _(deprecated)_
- [os_signpost(_:dso:log:name:signpostID:_:_:)](<os_signpost(__dso_log_name_signpostid_____)-2om9b.md>) — Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments, and includes a detailed message. _(deprecated)_
- [OSSignpostType](ossignposttype.md) — The different kinds of signpost. _(deprecated)_
- [os_signpost(_:dso:log:name:signpostID:)](<os_signpost(__dso_log_name_signpostid_)-12m3v.md>) — Logs the beginning of an animation as a point-of-interest in your code, without a message. _(deprecated)_
- [os_signpost(_:dso:log:name:signpostID:_:_:)](<os_signpost(__dso_log_name_signpostid_____)-nez5.md>) — Logs the beginning of an animation as a point-of-interest in your code, and includes the specified message in the logs. _(deprecated)_
- [AnimationFormatString](animationformatstring.md) — A namespace for utilities specific to animation-related signposts. _(deprecated)_
- [os_signpost_id_t](os_signpost_id_t.md) — An identifier you use to distinguish between signposts that have the same name and destination log.
