---
title: AVAsyncProperty
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avasyncproperty
source_url: 'https://developer.apple.com/documentation/avfoundation/avasyncproperty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasyncproperty.json'
content_hash: 'sha256:9b7cc9fc4e558452'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAsyncProperty

<sub>Class</sub>

An asynchronous property that constrains its type and value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVAsyncProperty<Root, Value>
```

## Overview

This class subclasses [AVPartialAsyncProperty](avpartialasyncproperty.md) to provide a type constraint on the property value.

## Relationships

- **Inherits From**: [AVPartialAsyncProperty](avpartialasyncproperty.md)

- **Conforms To**: [CustomStringConvertible](../swift/customstringconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the status

- [Status](avasyncproperty/status.md) — Loaded status values for asynchronous properties.

## See Also

### Property loading

- [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md) — A protocol that defines the interface to load media data asynchronously.
- [AVPartialAsyncProperty](avpartialasyncproperty.md) — An asynchronous property that constrains its type.
- [AVAnyAsyncProperty](avanyasyncproperty.md) — A base class for asynchronous properties.
