---
title: 'run(forKey:object:arguments:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/caaction/run(forkey:object:arguments:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/caaction/run(forkey:object:arguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caaction/run%28forkey%3Aobject%3Aarguments%3A%29.json'
content_hash: 'sha256:cd8ed983f4941949'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAAction](../caaction.md)

# run(forKey:object:arguments:)

<sub>Instance Method</sub>

Called to trigger the action specified by the identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func run(forKey event: String, object anObject: Any, arguments dict: [AnyHashable : Any]?)
```

## Parameters

- `event` — The identifier of the action. The identifier may be a key or key path relative to `anObject`, an arbitrary external action, or one of the action identifiers defined in [CALayer](../calayer.md).

- `anObject` — The layer on which the action should occur.

- `dict` — A dictionary containing parameters associated with this event. May be `nil`.

## See Also

### Related Documentation

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
