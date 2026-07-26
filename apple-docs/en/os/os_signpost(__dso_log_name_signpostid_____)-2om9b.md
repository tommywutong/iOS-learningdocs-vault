---
title: 'os_signpost(_:dso:log:name:signpostID:_:_:)'
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/os/os_signpost(_:dso:log:name:signpostid:_:_:)-2om9b'
source_url: 'https://developer.apple.com/documentation/os/os_signpost(_:dso:log:name:signpostid:_:_:)-2om9b'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_signpost%28_%3Adso%3Alog%3Aname%3Asignpostid%3A_%3A_%3A%29-2om9b.json'
content_hash: 'sha256:f8ad32ed8986c6e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_signpost(_:dso:log:name:signpostID:_:_:)

<sub>Function</sub>

Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments, and includes a detailed message.

> [!warning] Deprecated
> Use [beginInterval(_:id:_:)](<ossignposter/begininterval(__id___).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func os_signpost(_ type: OSSignpostType, dso: UnsafeRawPointer = #dsohandle, log: OSLog, name: StaticString, signpostID: OSSignpostID = .exclusive, _ format: StaticString, _ arguments: any CVarArg...)
```

## Parameters

- `type` — The type of signpost to log.

- `log` — A log object to log the signpost to.

- `name` — The name of the signpost.

- `signpostID` — A signpost identifier you use to disambiguate between signposts with the same name.

- `format` — A constant string or format string that produces a human-readable log message.

- `arguments` — Additional arguments to substitute into the `format` string parameter. Pass the expected number of arguments in the order that they appear in the string. If `format` is a constant string, don’t include any additional arguments.

## See Also

### Measure Events

- [os_signpost(_:dso:log:name:signpostID:)](<os_signpost(__dso_log_name_signpostid_)-2oz8u.md>) — Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments. _(deprecated)_
- [OSSignpostType](ossignposttype.md) — The different kinds of signpost. _(deprecated)_
- [os_signpost(_:dso:log:name:signpostID:)](<os_signpost(__dso_log_name_signpostid_)-12m3v.md>) — Logs the beginning of an animation as a point-of-interest in your code, without a message. _(deprecated)_
- [os_signpost(_:dso:log:name:signpostID:_:_:)](<os_signpost(__dso_log_name_signpostid_____)-nez5.md>) — Logs the beginning of an animation as a point-of-interest in your code, and includes the specified message in the logs. _(deprecated)_
- [OSSignpostAnimationBegin](ossignpostanimationbegin.md) — The signpost options to use when measuring animations. _(deprecated)_
- [AnimationFormatString](animationformatstring.md) — A namespace for utilities specific to animation-related signposts. _(deprecated)_
- [os_signpost_id_t](os_signpost_id_t.md) — An identifier you use to distinguish between signposts that have the same name and destination log.
