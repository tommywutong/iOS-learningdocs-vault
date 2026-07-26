---
title: rangeContainerObject
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptexecutioncontext/rangecontainerobject
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext/rangecontainerobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptexecutioncontext/rangecontainerobject.json'
content_hash: 'sha256:f5c17163578cd308'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptExecutionContext](../nsscriptexecutioncontext.md)

# rangeContainerObject

<sub>Instance Property</sub>

Sets the top-level container object for a range-specifier evaluation to a give object.

<sub>Mac Catalyst, macOS</sub>

```swift
var rangeContainerObject: Any? { get set }
```

## Parameters

- `container` — The top-level container object for a range-specifier evaluation.

## Discussion

Instances of `NSRangeSpecifier` contain object specifiers representing the first or last element in a range of elements, and these specifiers are evaluated in the context of `container`.

## See Also

### Getting and setting the container object

- [topLevelObject](toplevelobject.md) — Sets the top-level object for an object-specifier evaluation.
- [objectBeingTested](objectbeingtested.md) — Sets the top-level container object currently being tested in a “whose” qualifier to a given object.
