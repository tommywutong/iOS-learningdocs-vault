---
title: AnimationFormatString
framework: os
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/os/animationformatstring
source_url: 'https://developer.apple.com/documentation/os/animationformatstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/animationformatstring.json'
content_hash: 'sha256:5644393d8d4482c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# AnimationFormatString

<sub>Enumeration</sub>

A namespace for utilities specific to animation-related signposts.

> [!warning] Deprecated
> Use [OSSignposter](ossignposter.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum AnimationFormatString
```

## Topics

### Getting an Animation-Related Log Message

- [OSLogMessage](animationformatstring/oslogmessage.md) — A log message that includes an animation tag.

## See Also

### Measure Events

- [os_signpost(_:dso:log:name:signpostID:)](<os_signpost(__dso_log_name_signpostid_)-2oz8u.md>) — Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments. _(deprecated)_
- [os_signpost(_:dso:log:name:signpostID:_:_:)](<os_signpost(__dso_log_name_signpostid_____)-2om9b.md>) — Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments, and includes a detailed message. _(deprecated)_
- [OSSignpostType](ossignposttype.md) — The different kinds of signpost. _(deprecated)_
- [os_signpost(_:dso:log:name:signpostID:)](<os_signpost(__dso_log_name_signpostid_)-12m3v.md>) — Logs the beginning of an animation as a point-of-interest in your code, without a message. _(deprecated)_
- [os_signpost(_:dso:log:name:signpostID:_:_:)](<os_signpost(__dso_log_name_signpostid_____)-nez5.md>) — Logs the beginning of an animation as a point-of-interest in your code, and includes the specified message in the logs. _(deprecated)_
- [OSSignpostAnimationBegin](ossignpostanimationbegin.md) — The signpost options to use when measuring animations. _(deprecated)_
- [os_signpost_id_t](os_signpost_id_t.md) — An identifier you use to distinguish between signposts that have the same name and destination log.
