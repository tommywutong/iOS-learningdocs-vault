---
title: objectBeingTested
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptexecutioncontext/objectbeingtested
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext/objectbeingtested'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptexecutioncontext/objectbeingtested.json'
content_hash: 'sha256:031840e309094f1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptExecutionContext](../nsscriptexecutioncontext.md)

# objectBeingTested

<sub>Instance Property</sub>

Sets the top-level container object currently being tested in a “whose” qualifier to a given object.

<sub>Mac Catalyst, macOS</sub>

```swift
var objectBeingTested: Any? { get set }
```

## Parameters

- `object` — The top-level container object currently being tested.

## See Also

### Getting and setting the container object

- [topLevelObject](toplevelobject.md) — Sets the top-level object for an object-specifier evaluation.
- [rangeContainerObject](rangecontainerobject.md) — Sets the top-level container object for a range-specifier evaluation to a give object.
