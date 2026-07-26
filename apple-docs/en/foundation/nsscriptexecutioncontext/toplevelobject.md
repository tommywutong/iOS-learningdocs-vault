---
title: topLevelObject
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptexecutioncontext/toplevelobject
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext/toplevelobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptexecutioncontext/toplevelobject.json'
content_hash: 'sha256:96b428324322a340'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptExecutionContext](../nsscriptexecutioncontext.md)

# topLevelObject

<sub>Instance Property</sub>

Sets the top-level object for an object-specifier evaluation.

<sub>Mac Catalyst, macOS</sub>

```swift
var topLevelObject: Any? { get set }
```

## Parameters

- `anObject` — The top-level object for an object-specifier evaluation.

## See Also

### Getting and setting the container object

- [objectBeingTested](objectbeingtested.md) — Sets the top-level container object currently being tested in a “whose” qualifier to a given object.
- [rangeContainerObject](rangecontainerobject.md) — Sets the top-level container object for a range-specifier evaluation to a give object.
