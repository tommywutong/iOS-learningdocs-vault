---
title: resume()
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchobject/resume()
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchobject/resume()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchobject/resume%28%29.json'
content_hash: 'sha256:56f2e42a885fc232'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchObject](../dispatchobject.md)

# resume()

<sub>Instance Method</sub>

Resumes the invocation of block objects on a dispatch object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resume()
```

## Discussion

Calling this function decrements the suspension count of a suspended dispatch queue or dispatch event source object. While the count is greater than zero, the object remains suspended. When the suspension count returns to zero, any blocks submitted to the dispatch queue or any events observed by the dispatch source while suspended are delivered.

With one exception, each call to [dispatch_resume](<resume().md>) must balance a call to [dispatch_suspend](<suspend().md>). New dispatch event source objects returned by [dispatch_source_create](../dispatch_source_create.md) have a suspension count of 1 and must be resumed before any events are delivered. This approach allows your application to fully configure the dispatch event source object prior to delivery of the first event. In all other cases, it is undefined to call [dispatch_resume](<resume().md>) more times than [dispatch_suspend](<suspend().md>), which would result in a negative suspension count.

## See Also

### Activating, Suspending, and Resuming

- [dispatch_activate](<activate().md>) — Activates the dispatch object.
- [dispatch_suspend](<suspend().md>) — Suspends the invocation of block objects on a dispatch object.
