---
title: AVURLAsset
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avurlasset
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlasset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlasset.json'
content_hash: 'sha256:1600c44666f4e7e7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVURLAsset

<sub>Class</sub>

An asset that represents media at a local or remote URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVURLAsset
```

## Overview

This class is a concrete subclass of [AVAsset](avasset.md). When you create an asset as shown below, the system creates and returns an instance of [AVURLAsset](avurlasset.md).

```swift
// A local or remote asset URL.
guard let url: URL = Bundle.main.url(forResource: "Image",
                                     withExtension: "png") else { return }
let asset = AVAsset(url: url)
```

In many cases, this is an appropriate way to create asset instances, but you can also directly instantiate an [AVURLAsset](avurlasset.md) when you need more fine-grained control over its initialization. The initializer for [AVURLAsset](avurlasset.md) accepts an options dictionary, which you use to customize the asset’s initialization for your particular purpose. For example, if you’re creating an asset for an HLS stream, you may want to prevent it from retrieving its media when it connects over a cellular network. You can do this by providing the initialization option and value as shown below.

```swift
let url: URL = // A remote asset URL.
let options = [AVURLAssetAllowsCellularAccessKey: false]
let asset = AVURLAsset(url: url, options: options)
```

## Relationships

- **Inherits From**: [AVAsset](avasset.md)

- **Inherited By**: [AVFragmentedAsset](avfragmentedasset.md)

- **Conforms To**: [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md), [AVContentKeyRecipient](avcontentkeyrecipient.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSItemProviderReading](../foundation/nsitemproviderreading.md), [NSItemProviderWriting](../foundation/nsitemproviderwriting.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an asset

- [init(url:)](<avurlasset/init(url_).md>) — Creates an asset that models the media at the specified URL.
- [- initWithURL:options:](<avurlasset/init(url_options_)-2x8uu.md>) — Creates an asset that models the media resource at the specified URL.
- [Initialization options](avurlasset-initialization-options.md) — Specify options to configure the initialization of a media asset.

### Loading tracks

- [tracks](avpartialasyncproperty/tracks-44ptx.md) — The tracks an asset contains.
- [- findCompatibleTrackForCompositionTrack:completionHandler:](<avurlasset/findcompatibletrack(for_completionhandler_).md>) — Loads an asset track from which you can insert any time range into the composition track.

### Loading variants

- [variants](avpartialasyncproperty/variants.md) — An array of variants that an asset contains.

### Determining supported media types

- [+ audiovisualTypes](<avurlasset/audiovisualtypes().md>) — Returns an array of the file types the asset supports. _(deprecated)_
- [+ audiovisualMIMETypes](<avurlasset/audiovisualmimetypes().md>) — Returns an array of the MIME types the asset supports.
- [+ isPlayableExtendedMIMEType:](<avurlasset/isplayableextendedmimetype(__).md>) — Returns a Boolean value that indicates whether the asset is playable with the specified codecs and container type.
- [audiovisualContentTypes](avurlasset/audiovisualcontenttypes.md) — Provides the content types the AVURLAsset class understands.

### Assisting with resource loading

- [resourceLoader](avurlasset/resourceloader.md) — The resource loader for the asset.
- [mayRequireContentKeysForMediaDataProcessing](avurlasset/mayrequirecontentkeysformediadataprocessing.md) — A Boolean value that indicates whether you can add this asset as a content key recipient to a content key session.

### Working with offline assets

- [assetCache](avurlasset/assetcache.md) — The asset’s associated asset cache, if it exists.

### Accessing the media URL

- [URL](avurlasset/url.md) — A URL to the asset’s media.

### Accessing asset variants

- [variants](avurlasset/variants.md) — An array of variants that an asset contains. _(deprecated)_

### Accessing compatible tracks

- [- compatibleTrackForCompositionTrack:](<avurlasset/compatibletrack(for_).md>) — Returns an asset track from which you can insert any time range into a given composition track. _(deprecated)_

### Accessing the session identifier

- [httpSessionIdentifier](avurlasset/httpsessionidentifier.md) — A session identifier that the asset sends in HTTP requests that it makes.

### Accessing Media Extension properties

- [mediaExtensionProperties](avurlasset/mediaextensionproperties.md) — The properties of the media extension format reader that decodes the asset.
- [AVMediaExtensionProperties](avmediaextensionproperties.md) — An object that describes a Media Extension.

### Initializers

- [init(URL:options:)](<avurlasset/init(url_options_)-1t08s.md>)
- [init(URL:options:)](<avurlasset/init(url_options_)-4zhx7.md>)

## See Also

### Assets

- [AVAsset](avasset.md) — An object that models timed audiovisual media.
- [AVAssetTrack](avassettrack.md) — An object that models a track of media that an asset contains.
- [AVAssetTrackSegment](avassettracksegment.md) — An object that represents a time range segment of an asset track.
- [AVAssetTrackGroup](avassettrackgroup.md) — A group of related tracks in an asset.
