---
title: makeSignpostID()
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/ossignposter/makesignpostid()
source_url: 'https://developer.apple.com/documentation/os/ossignposter/makesignpostid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/makesignpostid%28%29.json'
content_hash: 'sha256:5ef25e62b4173f86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# makeSignpostID()

<sub>Instance Method</sub>

Returns an identifier that’s unique within the scope of the signposter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeSignpostID() -> OSSignpostID
```

## Return Value

A signpost ID that you use to match an interval’s signposts.

## Discussion

The signposter uses a signpost ID to pair the beginning and the end of a signposted interval, which is necessary because multiple intervals with the same configuration and scope can be in-flight simultaneously.

Use this method instead of [init(log:)](<../ossignpostid/init(log_).md>).

## See Also

### Generating Signpost IDs

- [makeSignpostID(from:)](<makesignpostid(from_).md>) — Returns an identifier that the signposter derives from the specified object.
- [OSSignpostID](../ossignpostid.md) — An identifier that disambiguates signposted intervals.
