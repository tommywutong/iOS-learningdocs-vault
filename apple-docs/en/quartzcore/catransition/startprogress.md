---
title: startProgress
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catransition/startprogress
source_url: 'https://developer.apple.com/documentation/quartzcore/catransition/startprogress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransition/startprogress.json'
content_hash: 'sha256:3481e18bcac6fe85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransition](../catransition.md)

# startProgress

<sub>Instance Property</sub>

Indicates the start point of the receiver as a fraction of the entire transition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var startProgress: Float { get set }
```

## Discussion

Legal values are numbers between 0.0 and 1.0. For example, to start the transition half way through its progress set `startProgress` to 0.5. The default value is 0.

## See Also

### Related Documentation

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)

### Transition start and end point

- [endProgress](endprogress.md) — Indicates the end point of the receiver as a fraction of the entire transition.
