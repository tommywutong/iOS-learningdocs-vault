---
title: 'load(_:isolation:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avasynchronouskeyvalueloading/load(_:isolation:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/load(_:isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronouskeyvalueloading/load%28_%3Aisolation%3A%29.json'
content_hash: 'sha256:17c089937389618b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousKeyValueLoading](../avasynchronouskeyvalueloading.md)

# load(_:isolation:)

<sub>Instance Method</sub>

Loads a property asynchronously and returns the value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: macOS 26.0, iOS 26.0, tvOS 26.0, watchOS 26.0, visionOS 26.0)
func load<T>(_ property: AVAsyncProperty<Self, T>, isolation: isolated (any Actor)? = #isolation) async throws -> T
```

## Parameters

- `property` — A property to load.

- `isolation` — The isolation context.

## Return Value

The loaded property value.

## Discussion

Call this method from an asynchronous context to load the value of one or more media properties. The method returns a single result if you load one property value, and returns a tuple if you load multiple properties (up to eight) at the same time.

To load a property, pass one or more [AVAsyncProperty](../avasyncproperty.md) constants to this method as shown below.

```swift
// Load an asset's list of tracks.
let tracks = try await asset.load(.tracks)
        
// Load an asset's suitability for playback and export.
let (isPlayable, isExportable) = try await asset.load(.isPlayable, .isExportable)
```

## See Also

### Loading property values

- [load(_:_:_:isolation:)](<load(______isolation_).md>) — Loads two or more properties asynchronously and returns the values.
