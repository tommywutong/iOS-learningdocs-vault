---
title: CTRunDelegateGetDescentCallback
framework: Core Text
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctrundelegategetdescentcallback
source_url: 'https://developer.apple.com/documentation/coretext/ctrundelegategetdescentcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrundelegategetdescentcallback.json'
content_hash: 'sha256:1bca22c1515d4231'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunDelegateGetDescentCallback

<sub>Type Alias</sub>

Defines a pointer to a function that determines typographic descent of glyphs in the run.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CTRunDelegateGetDescentCallback = (UnsafeMutableRawPointer) -> CGFloat
```

## Parameters

- `refCon` — The reference-constant value supplied to the [CTRunDelegateCreate](<ctrundelegatecreate(____).md>) function when the run delegate was created.

## Return Value

The typographic descent of glyphs in the run associated with the run delegate.

## Discussion

You would declare the get-descent function like this if you were to name it `MyGetDescentCallback`:

## See Also

### Callbacks

- [CTRunDelegateGetAscentCallback](ctrundelegategetascentcallback.md) — Defines a pointer to a function that determines typographic ascent of glyphs in the run.
- [CTRunDelegateGetWidthCallback](ctrundelegategetwidthcallback.md) — Defines a pointer to a function that determines the typographic width of glyphs in the run.
- [CTRunDelegateDeallocateCallback](ctrundelegatedeallocatecallback.md) — Defines a pointer to a function that is invoked when a CTRunDelegate object is deallocated.
