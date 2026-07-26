---
title: CGBitmapContextReleaseDataCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgbitmapcontextreleasedatacallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgbitmapcontextreleasedatacallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgbitmapcontextreleasedatacallback.json'
content_hash: 'sha256:c6322d12d899f308'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGBitmapContextReleaseDataCallback

<sub>Type Alias</sub>

A callback function used to release data associate with the bitmap context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGBitmapContextReleaseDataCallback = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Void
```

## Discussion

The `releaseInfo` parameter contains the contextual data that you passed to the `CGContext/init(data:width:height:bitsPerComponent:bytesPerRow:space:bitmapInfo:releaseCallback:releaseInfo:)` function. The `data` parameter contains a pointer to the bitmap data for you to release.
