---
title: CTRunDelegateGetWidthCallback
framework: Core Text
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctrundelegategetwidthcallback
source_url: 'https://developer.apple.com/documentation/coretext/ctrundelegategetwidthcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrundelegategetwidthcallback.json'
content_hash: 'sha256:5fb38b80e5acd3d1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunDelegateGetWidthCallback

<sub>Type Alias</sub>

Defines a pointer to a function that determines the typographic width of glyphs in the run.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CTRunDelegateGetWidthCallback = (UnsafeMutableRawPointer) -> CGFloat
```

## Parameters

- `refCon` — The reference-constant value supplied to the [CTRunDelegateCreate](<ctrundelegatecreate(____).md>) function when the run delegate was created.

## Return Value

The typographic width of glyphs in the run associated with the run delegate.  A value of 0.0 indicates that the glyphs should not be drawn.

## Discussion

You would declare the get-width function like this if you were to name it `MyGetWidthCallback`:

## See Also

### Callbacks

- [CTRunDelegateGetAscentCallback](ctrundelegategetascentcallback.md) — Defines a pointer to a function that determines typographic ascent of glyphs in the run.
- [CTRunDelegateGetDescentCallback](ctrundelegategetdescentcallback.md) — Defines a pointer to a function that determines typographic descent of glyphs in the run.
- [CTRunDelegateDeallocateCallback](ctrundelegatedeallocatecallback.md) — Defines a pointer to a function that is invoked when a CTRunDelegate object is deallocated.
