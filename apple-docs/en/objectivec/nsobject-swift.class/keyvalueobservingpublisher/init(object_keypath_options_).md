---
title: 'init(object:keyPath:options:)'
framework: Objective-C Runtime
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher/init(object:keypath:options:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher/init(object:keypath:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher/init%28object%3Akeypath%3Aoptions%3A%29.json'
content_hash: 'sha256:22972586fcd3daa7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Objective-C Runtime](../../../objectivec.md) · [NSObject](../../nsobject-swift.class.md) · [KeyValueObservingPublisher](../keyvalueobservingpublisher.md)

# init(object:keyPath:options:)

<sub>Initializer</sub>

Creates a key-value observing publisher for the given combination of object and key path, using publishing behavior options you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(object: Subject, keyPath: KeyPath<Subject, Value>, options: NSKeyValueObservingOptions)
```

## Parameters

- `object` — The object that contains the property to publish.

- `keyPath` — The key path, relative to the object receiving this message, of the property to publish.

- `options` — Options that determine which elements the publisher produces. Set this parameter to `[]` to receive new elements when the observed property changes.

## Discussion

This publisher produces a new element every time the observed property changes.
