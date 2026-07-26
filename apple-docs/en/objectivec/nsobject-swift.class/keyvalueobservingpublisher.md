---
title: NSObject.KeyValueObservingPublisher
framework: Objective-C Runtime
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher.json'
content_hash: 'sha256:ec9973cc81f67040'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# NSObject.KeyValueObservingPublisher

<sub>Structure</sub>

A Combine publisher that produces a new element whenever the observed value changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct KeyValueObservingPublisher<Subject, Value> where Subject : NSObject
```

## Overview

Use this publisher to integrate a property that’s compliant with key-value observing into a Combine publishing chain. You can create a publisher of this type with the [NSObject](../nsobject-swift.class.md) instance method `publisher(for:options:)`, passing in the key path and a set of [NSKeyValueObservingOptions](../../foundation/nskeyvalueobservingoptions.md).

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Publisher](../../combine/publisher.md)

## Topics

### Creating a KVO Publisher

- [init(object:keyPath:options:)](<keyvalueobservingpublisher/init(object_keypath_options_).md>) — Creates a key-value observing publisher for the given combination of object and key path, using publishing behavior options you provide.

### Inspecting KVO Publisher Properties

- [object](keyvalueobservingpublisher/object.md) — The object that contains the property to publish.
- [keyPath](keyvalueobservingpublisher/keypath.md) — The key path, relative to the object receiving this message, of the property to publish.
- [options](keyvalueobservingpublisher/options.md) — Options that determine which elements the publisher produces.

### Instance Methods

- [didChange()](<keyvalueobservingpublisher/didchange().md>) — Returns a publisher that emits values when a KVO-compliant property changes.
