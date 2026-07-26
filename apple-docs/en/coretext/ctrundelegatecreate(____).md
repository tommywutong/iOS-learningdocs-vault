---
title: 'CTRunDelegateCreate(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctrundelegatecreate(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctrundelegatecreate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrundelegatecreate%28_%3A_%3A%29.json'
content_hash: 'sha256:c7fe33b426bca18a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunDelegateCreate(_:_:)

<sub>Function</sub>

Creates an immutable instance of a run delegate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTRunDelegateCreate(_ callbacks: UnsafePointer<CTRunDelegateCallbacks>, _ refCon: UnsafeMutableRawPointer?) -> CTRunDelegate?
```

## Parameters

- `callbacks` — A structure holding pointers to the callbacks for this run delegate.

- `refCon` — A constant value associated with the run delegate to identify it.

## Return Value

If  successful, a reference to an immutable CTRunDelegate object. Otherwise, returns `NULL`.

## Discussion

The run-delegate object can be used for reserving space in a line or for eliding the glyphs for a range of text altogether.
