---
title: 'makeSignpostID(from:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignposter/makesignpostid(from:)'
source_url: 'https://developer.apple.com/documentation/os/ossignposter/makesignpostid(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/makesignpostid%28from%3A%29.json'
content_hash: 'sha256:046e43fd7981415f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# makeSignpostID(from:)

<sub>Instance Method</sub>

Returns an identifier that the signposter derives from the specified object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeSignpostID(from object: AnyObject) -> OSSignpostID
```

## Parameters

- `object` — The object the signposter uses to match the begin and end calls of a signposted interval.

## Return Value

A signpost ID that you use to match an interval’s signposts.

## Discussion

> [!warning] Warning
> Don’t use this method to generate an identifier for a signposted interval that crosses process boundaries. Instead, use the [makeSignpostID()](<makesignpostid().md>) method.

The signposter uses a signpost ID to pair the beginning and the end of a signposted interval, which is necessary because multiple intervals with the same configuration and scope can be in-flight simultaneously.

Use this method instead of [init(log:object:)](<../ossignpostid/init(log_object_).md>).

## See Also

### Generating Signpost IDs

- [makeSignpostID()](<makesignpostid().md>) — Returns an identifier that’s unique within the scope of the signposter.
- [OSSignpostID](../ossignpostid.md) — An identifier that disambiguates signposted intervals.
