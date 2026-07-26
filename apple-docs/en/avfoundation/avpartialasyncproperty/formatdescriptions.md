---
title: formatDescriptions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/formatdescriptions
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/formatdescriptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/formatdescriptions.json'
content_hash: 'sha256:d80d0e10d5db9a28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# formatDescriptions

<sub>Type Property</sub>

The format descriptions of the media samples that a track references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var formatDescriptions: AVAsyncProperty<Root, [CMFormatDescription]> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

The array contains [CMFormatDescription](../../coremedia/cmformatdescription.md) objects that indicate the format of media samples the track references.

Asset tracks typically present uniform media (for example, media that uses the same encoding settings) and contain a single format description. However, in some cases, an asset track may contain multiple format descriptions. For example, an H.264-encoded video track may have some segments that use the Main profile and others that use the High profile. Also, an individual [AVCompositionTrack](../avcompositiontrack.md), which subclasses [AVAssetTrack](../avassettrack.md), may contain audio or video segments using different codecs.

You can use [CMFormatDescription](../../coremedia/cmformatdescription.md) to access low-level details about the media the track references. For example, you can retrieve the details of track’s media type and subtype as the code below shows:

```swift
extension AVAssetTrack {
    var mediaFormat: String {
        get async throws {
            var format = ""
            let descriptions = try await load(.formatDescriptions)
            for (index, formatDesc) in descriptions.enumerated() {
                // Get a string representation of the media type.
                let type = CMFormatDescriptionGetMediaType(formatDesc).toString()
                // Get a string representation of the media subtype.
                let subType = CMFormatDescriptionGetMediaSubType(formatDesc).toString()
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

## See Also

### Loading track information

- [isPlayable](isplayable-6txa5.md) — A Boolean value that indicates whether the track is playable in the current environment.
- [isDecodable](isdecodable.md) — A Boolean value that indicates whether the track is decodable in the current environment.
- [isEnabled](isenabled.md) — A Boolean value that indicates whether the track is in an enabled state.
- [isSelfContained](isselfcontained.md) — A Boolean value that indicates whether the track references sample data only within its container file.
- [totalSampleDataLength](totalsampledatalength.md) — The total number of bytes of sample data the track requires.
- [mediaCharacteristics](mediacharacteristics.md) — The media characteristics for the track.
