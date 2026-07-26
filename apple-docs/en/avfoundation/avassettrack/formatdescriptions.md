---
title: formatDescriptions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassettrack/formatdescriptions
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/formatdescriptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/formatdescriptions.json'
content_hash: 'sha256:5f4fbd4810785d57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# formatDescriptions

<sub>Instance Property</sub>

The format descriptions of the media samples that a track references.

> [!warning] Deprecated
> Load the value of [formatDescriptions](../avpartialasyncproperty/formatdescriptions.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var formatDescriptions: [Any] { get }
```

## Discussion

The array contains [CMFormatDescription](../../coremedia/cmformatdescription.md) objects that indicate the format of media samples the track references.

Asset tracks typically present uniform media (for example, media that uses the same encoding settings) and contain a single format description. However, in some cases, an asset track may contain multiple format descriptions. For example, an H.264-encoded video track may have some segments that use the Main profile and others that use the High profile. Also, an individual [AVCompositionTrack](../avcompositiontrack.md), which subclasses [AVAssetTrack](../avassettrack.md), may contain audio or video segments using different codecs.

You can use [CMFormatDescription](../../coremedia/cmformatdescription.md) to access low-level details about the media the track references. For example, you can retrieve the details of track’s media type and subtype as the code below shows:

```swift
extension AVAssetTrack {
    var mediaFormat: String {
        var format = ""
        let descriptions = self.formatDescriptions as! [CMFormatDescription]
        for (index, formatDesc) in descriptions.enumerated() {
            // Get a string representation of the media type.
            let type =
                CMFormatDescriptionGetMediaType(formatDesc).toString()
            // Get a string representation of the media subtype.
            let subType =
                CMFormatDescriptionGetMediaSubType(formatDesc).toString()
            // Format the string as type/subType, such as vide/avc1 or soun/aac.
            format += "\(type)/\(subType)"
            // Comma-separate if there's more than one format description.
            if index < descriptions.count - 1 {
                format += ","
            }
        }
        return format
    }
}
 
extension FourCharCode {
    // Create a string representation of a FourCC.
    func toString() -> String {
        let bytes: [CChar] = [
            CChar((self >> 24) & 0xff),
            CChar((self >> 16) & 0xff),
            CChar((self >> 8) & 0xff),
            CChar(self & 0xff),
            0
        ]
        let result = String(cString: bytes)
        let characterSet = CharacterSet.whitespaces
        return result.trimmingCharacters(in: characterSet)
    }
}
```
