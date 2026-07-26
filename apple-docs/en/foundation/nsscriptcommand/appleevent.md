---
title: appleEvent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommand/appleevent
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommand/appleevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommand/appleevent.json'
content_hash: 'sha256:80cc6bb17ae7143e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommand](../nsscriptcommand.md)

# appleEvent

<sub>Instance Property</sub>

If the receiver was constructed by Cocoa scripting’s built-in Apple event handling, returns the Apple event descriptor from which it was constructed.

<sub>Mac Catalyst, macOS</sub>

```swift
@NSCopying var appleEvent: NSAppleEventDescriptor? { get }
```

## Discussion

The effects of mutating or retaining this descriptor are undefined, although it may be copied.
