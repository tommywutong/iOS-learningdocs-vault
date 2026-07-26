---
title: 'init(data:width:height:bitsPerComponent:bytesPerRow:space:bitmapInfo:releaseCallback:releaseInfo:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+（27.0 起废弃）, iPadOS 4.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.6+（27.0 起废弃）, tvOS（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/coregraphics/cgcontext/init(data:width:height:bitspercomponent:bytesperrow:space:bitmapinfo:releasecallback:releaseinfo:)-71ea9'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/init(data:width:height:bitspercomponent:bytesperrow:space:bitmapinfo:releasecallback:releaseinfo:)-71ea9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/init%28data%3Awidth%3Aheight%3Abitspercomponent%3Abytesperrow%3Aspace%3Abitmapinfo%3Areleasecallback%3Areleaseinfo%3A%29-71ea9.json'
content_hash: 'sha256:54b3cbaabf9e5195'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# init(data:width:height:bitsPerComponent:bytesPerRow:space:bitmapInfo:releaseCallback:releaseInfo:)

<sub>Initializer</sub>

> [!warning] Deprecated
> update space parameter to CGColorSpace?, bitmapInfo parameter to CGBitmapInfo

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(data: UnsafeMutableRawPointer?, width: Int, height: Int, bitsPerComponent: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: UInt32, releaseCallback: CGBitmapContextReleaseDataCallback?, releaseInfo: UnsafeMutableRawPointer?)
```
