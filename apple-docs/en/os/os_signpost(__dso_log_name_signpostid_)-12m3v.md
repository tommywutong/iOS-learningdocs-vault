---
title: 'os_signpost(_:dso:log:name:signpostID:)'
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/os/os_signpost(_:dso:log:name:signpostid:)-12m3v'
source_url: 'https://developer.apple.com/documentation/os/os_signpost(_:dso:log:name:signpostid:)-12m3v'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_signpost%28_%3Adso%3Alog%3Aname%3Asignpostid%3A%29-12m3v.json'
content_hash: 'sha256:fe69742ce8127180'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_signpost(_:dso:log:name:signpostID:)

<sub>Function</sub>

Logs the beginning of an animation as a point-of-interest in your code, without a message.

> [!warning] Deprecated
> Use [beginAnimationInterval(_:id:)](<ossignposter/beginanimationinterval(__id_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func os_signpost(_ animationBegin: OSSignpostAnimationBegin, dso: UnsafeRawPointer = #dsohandle, log: OSLog, name: StaticString, signpostID: OSSignpostID = .exclusive)
```

## Parameters

- `animationBegin` — The type of animation signpost to create.

- `log` — The log object to write the signpost to.

- `name` — The name of the signpost.

- `signpostID` — A signpost identifier you use to disambiguate between signposts with the same name. If you specify [invalid](ossignpostid/invalid.md) or [null](ossignpostid/null.md) for this parameter, this method does nothing.

## See Also

### Measure Events

- [os_signpost(_:dso:log:name:signpostID:)](<os_signpost(__dso_log_name_signpostid_)-2oz8u.md>) — Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments. _(deprecated)_
- [os_signpost(_:dso:log:name:signpostID:_:_:)](<os_signpost(__dso_log_name_signpostid_____)-2om9b.md>) — Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments, and includes a detailed message. _(deprecated)_
- [OSSignpostType](ossignposttype.md) — The different kinds of signpost. _(deprecated)_
- [os_signpost(_:dso:log:name:signpostID:_:_:)](<os_signpost(__dso_log_name_signpostid_____)-nez5.md>) — Logs the beginning of an animation as a point-of-interest in your code, and includes the specified message in the logs. _(deprecated)_
- [OSSignpostAnimationBegin](ossignpostanimationbegin.md) — The signpost options to use when measuring animations. _(deprecated)_
- [AnimationFormatString](animationformatstring.md) — A namespace for utilities specific to animation-related signposts. _(deprecated)_
- [os_signpost_id_t](os_signpost_id_t.md) — An identifier you use to distinguish between signposts that have the same name and destination log.
