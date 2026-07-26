---
title: 'CTFramesetterGetTypesetter(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctframesettergettypesetter(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctframesettergettypesetter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctframesettergettypesetter%28_%3A%29.json'
content_hash: 'sha256:e9520eb99bab2ff0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFramesetterGetTypesetter(_:)

<sub>Function</sub>

Returns the typesetter object being used by the framesetter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFramesetterGetTypesetter(_ framesetter: CTFramesetter) -> CTTypesetter
```

## Parameters

- `framesetter` — The framesetter from which a typesetter is requested.

## Return Value

A reference to a CTTypesetter object if the call was successful; otherwise, `NULL`. The framesetter maintains a reference to the returned object, which should not be released by the caller.

## Discussion

Each framesetter uses a typesetter internally to perform line breaking and other contextual analysis based on the characters in a string; this function returns the typesetter being used by a particular framesetter in case the caller would like to perform other operations on that typesetter.

## See Also

### Creating Frames

- [CTFramesetterCreateFrame](<ctframesettercreateframe(________).md>) — Creates an immutable frame using a framesetter.
