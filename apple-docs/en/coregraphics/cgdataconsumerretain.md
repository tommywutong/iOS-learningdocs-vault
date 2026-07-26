---
title: CGDataConsumerRetain
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataconsumerretain
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataconsumerretain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataconsumerretain.json'
content_hash: 'sha256:0841fbe1bbdb8c52'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDataConsumerRetain

<sub>Function</sub>

Increments the retain count of a data consumer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGDataConsumerRefCGDataConsumerRetain(CGDataConsumerRef consumer);
```

## Parameters

- `consumer` — The data consumer to retain.

## Return Value

The same data consumer you passed in as the `consumer` parameter.

## Discussion

This function is equivalent to [CFRetain](../corefoundation/cfretain.md), except that it does not cause an error if the `consumer` parameter is `NULL`.

## See Also

### Retaining and Releasing Data Consumers

- [CGDataConsumerRelease](cgdataconsumerrelease.md) — Decrements the retain count of a data consumer.
