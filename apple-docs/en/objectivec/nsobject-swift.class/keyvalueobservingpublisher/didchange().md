---
title: didChange()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher/didchange()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher/didchange()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher/didchange%28%29.json'
content_hash: 'sha256:a8362751bf7878b7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Objective-C Runtime](../../../objectivec.md) · [NSObject](../../nsobject-swift.class.md) · [KeyValueObservingPublisher](../keyvalueobservingpublisher.md)

# didChange()

<sub>Instance Method</sub>

Returns a publisher that emits values when a KVO-compliant property changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func didChange() -> Publishers.Map<NSObject.KeyValueObservingPublisher<Subject, Value>, Void>
```

## Return Value

A key-value observing publisher.
