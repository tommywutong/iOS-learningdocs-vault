---
title: distantFuture
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchtime/distantfuture
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchtime/distantfuture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchtime/distantfuture.json'
content_hash: 'sha256:d2795ac00ba9fa8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchTime](../dispatchtime.md)

# distantFuture

<sub>Type Property</sub>

A time in the distant future.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let distantFuture: DispatchTime
```

## Discussion

You can pass this value to methods that schedule work to have the system wait indefinitely for a particular event to occur or condition to be met.

## See Also

### Getting Well-Known Times

- [now()](<now().md>) — Returns the current time.
