---
title: 'subscript(unchecked:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/outputspan/subscript(unchecked:)'
source_url: 'https://developer.apple.com/documentation/swift/outputspan/subscript(unchecked:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/outputspan/subscript%28unchecked%3A%29.json'
content_hash: 'sha256:2eb0d184eb4c0477'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OutputSpan](../outputspan.md)

# subscript(unchecked:)

<sub>Instance Subscript</sub>

Accesses the element at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(unchecked index: OutputSpan<Element>.Index) -> Element { borrow mutate }
```

## Parameters

- `index` — A valid index into this span.

## Overview

This subscript does not validate `index`; this is an unsafe operation.

> [!abstract] Complexity
> O(1)
