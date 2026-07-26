---
title: keyPath
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher/keypath
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher/keypath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher/keypath.json'
content_hash: 'sha256:9904e7692fc925ba'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Objective-C Runtime](../../../objectivec.md) · [NSObject](../../nsobject-swift.class.md) · [KeyValueObservingPublisher](../keyvalueobservingpublisher.md)

# keyPath

<sub>Instance Property</sub>

The key path, relative to the object receiving this message, of the property to publish.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let keyPath: KeyPath<Subject, Value>
```

## See Also

### Inspecting KVO Publisher Properties

- [object](object.md) — The object that contains the property to publish.
- [options](options.md) — Options that determine which elements the publisher produces.
