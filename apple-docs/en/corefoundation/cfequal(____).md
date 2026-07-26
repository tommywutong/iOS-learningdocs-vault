---
title: 'CFEqual(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfequal(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfequal(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfequal%28_%3A_%3A%29.json'
content_hash: 'sha256:99323acf434e5d64'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFEqual(_:_:)

<sub>Function</sub>

Determines whether two Core Foundation objects are considered equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFEqual(_ cf1: CFTypeRef!, _ cf2: CFTypeRef!) -> Bool
```

## Parameters

- `cf1` — A CFType object to compare to `cf2`.

- `cf2` — A CFType object to compare to `cf1`.

## Return Value

`true` if `cf1` and `cf2` are of the same type and considered equal, otherwise `false`.

## Discussion

Equality is something specific to each Core Foundation opaque type. For example, two CFNumber objects are equal if the numeric values they represent are equal. Two CFString objects are equal if they represent identical sequences of characters, regardless of encoding.
