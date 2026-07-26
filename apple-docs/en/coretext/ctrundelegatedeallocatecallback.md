---
title: CTRunDelegateDeallocateCallback
framework: Core Text
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctrundelegatedeallocatecallback
source_url: 'https://developer.apple.com/documentation/coretext/ctrundelegatedeallocatecallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrundelegatedeallocatecallback.json'
content_hash: 'sha256:294002f9fb3fd822'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunDelegateDeallocateCallback

<sub>Type Alias</sub>

Defines a pointer to a function that is invoked when a CTRunDelegate object is deallocated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CTRunDelegateDeallocateCallback = (UnsafeMutableRawPointer) -> Void
```

## Parameters

- `refCon` — The reference-constant value supplied to the [CTRunDelegateCreate](<ctrundelegatecreate(____).md>) function when the run delegate was created.

## Discussion

You would declare the deallocation function like this if you were to name it `MyDeallocationCallback`:

## See Also

### Callbacks

- [CTRunDelegateGetAscentCallback](ctrundelegategetascentcallback.md) — Defines a pointer to a function that determines typographic ascent of glyphs in the run.
- [CTRunDelegateGetDescentCallback](ctrundelegategetdescentcallback.md) — Defines a pointer to a function that determines typographic descent of glyphs in the run.
- [CTRunDelegateGetWidthCallback](ctrundelegategetwidthcallback.md) — Defines a pointer to a function that determines the typographic width of glyphs in the run.
