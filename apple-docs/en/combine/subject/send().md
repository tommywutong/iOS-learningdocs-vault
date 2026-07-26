---
title: send()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/subject/send()
source_url: 'https://developer.apple.com/documentation/combine/subject/send()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subject/send%28%29.json'
content_hash: 'sha256:ace28bfbd3ecf3ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Subject](../subject.md)

# send()

<sub>Instance Method</sub>

Sends a void value to the subscriber.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func send()
```

## Discussion

Use `Void` inputs and outputs when you want to signal that an event has occurred, but don’t need to send the event itself.

## See Also

### Delivering elements to subscribers

- [send(_:)](<send(__).md>) — Sends a value to the subscriber.
