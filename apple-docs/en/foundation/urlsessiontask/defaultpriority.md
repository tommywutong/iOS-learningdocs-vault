---
title: defaultPriority
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/defaultpriority
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/defaultpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/defaultpriority.json'
content_hash: 'sha256:7268cbd755771534'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# defaultPriority

<sub>Type Property</sub>

The default URL session task priority, used implicitly for any task you have not prioritized.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let defaultPriority: Float
```

## Discussion

The floating point value of this constant is `0.5`.

## See Also

### Priority constants

- [NSURLSessionTaskPriorityLow](lowpriority.md) — A low URL session task priority, with a floating point value above the minimum of `0` and below the default value.
- [NSURLSessionTaskPriorityHigh](highpriority.md) — A high URL session task priority, with a floating point value above the default value and below the maximum of `1.0`.
