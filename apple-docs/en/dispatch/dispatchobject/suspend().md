---
title: suspend()
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchobject/suspend()
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchobject/suspend()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchobject/suspend%28%29.json'
content_hash: 'sha256:a1edb1aa4504bea3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchObject](../dispatchobject.md)

# suspend()

<sub>Instance Method</sub>

Suspends the invocation of block objects on a dispatch object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func suspend()
```

## Discussion

By suspending a dispatch object, your application can temporarily prevent the execution of any blocks associated with that object. The suspension occurs after completion of any blocks running at the time of the call. Calling this function increments the suspension count of the object, and calling [dispatch_resume](<resume().md>) decrements it. While the count is greater than zero, the object remains suspended, so you must balance each [dispatch_suspend](<suspend().md>) call with a matching [dispatch_resume](<resume().md>) call.

Any blocks submitted to a dispatch queue or events observed by a dispatch source are delivered once the object is resumed.

> [!important] Important
> It is a programmer error to release an object that is currently suspended, because suspension implies that there is still work to be done. Therefore, always balance calls to this method with a corresponding call to [dispatch_resume](<resume().md>) before disposing of the object. The behavior when releasing the last reference to a dispatch object while it is in a suspended state is undefined.

## See Also

### Activating, Suspending, and Resuming

- [dispatch_activate](<activate().md>) — Activates the dispatch object.
- [dispatch_resume](<resume().md>) — Resumes the invocation of block objects on a dispatch object.
