---
title: activate()
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchobject/activate()
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchobject/activate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchobject/activate%28%29.json'
content_hash: 'sha256:85902ef666a5fa3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchObject](../dispatchobject.md)

# activate()

<sub>Instance Method</sub>

Activates the dispatch object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func activate()
```

## Discussion

Once a dispatch object has been activated, it cannot change its target queue.

## See Also

### Activating, Suspending, and Resuming

- [dispatch_resume](<resume().md>) — Resumes the invocation of block objects on a dispatch object.
- [dispatch_suspend](<suspend().md>) — Suspends the invocation of block objects on a dispatch object.
