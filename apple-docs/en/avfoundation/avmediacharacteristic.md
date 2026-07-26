---
title: AVMediaCharacteristic
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediacharacteristic
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediacharacteristic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediacharacteristic.json'
content_hash: 'sha256:36e397f962ec2079'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMediaCharacteristic

<sub>Structure</sub>

A structure that defines media data characteristics.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVMediaCharacteristic
```

## Discussion

QuickTime Movie and MPEG-4 video files may contain tracks that provide tagged media characteristics to indicate a purpose, trait, or feature of the track’s media. For example, an audio track that mixes original program content with additional narrative descriptions of visual action may have the media characteristic `public.accessibility.describes-video` to distinguish it from other audio tracks stored in the same file that don’t contain additional narrative.

You inspect the tagged media characteristics of a track as shown below:

```objc
NSArray *userDataItems = [myAVAssetTrack metadataForFormat:AVMetadataFormatQuickTimeUserData];
NSArray *trackTaggedMediaCharacteristics = [AVMetadataItem metadataItemsFromArray: userDataItems
        withKey: AVMetadataQuickTimeUserDataKeyTaggedCharacteristic
        keySpace: AVMetadataKeySpaceQuickTimeUserData];
for (AVMetadataItem *metadataItem in trackTaggedMediaCharacteristics) {
     NSString *thisTrackMediaCharacteristic = [metadataItem stringValue];
}
```

You write tagged media characteristics to files of type [AVFileTypeQuickTimeMovie](avfiletype/mov.md) and [AVFileTypeAppleM4V](avfiletype/m4v.md) by using an instance of [AVAssetWriter](avassetwriter.md). You indicate tagged characteristics for a track by setting metadata on its associated asset writer input as shown below:

```objc
AVMutableMetadataItem *myTaggedMediaCharacteristic = [[AVMutableMetadataItem alloc] init];
[myTaggedMediaCharacteristic setKey:AVMetadataQuickTimeUserDataKeyTaggedCharacteristic];
[myTaggedMediaCharacteristic setKeySpace:AVMetadataKeySpaceQuickTimeUserData];
[myTaggedMediaCharacteristic setValue:aMeaningfulCharacteristicAsNSString];
[myMutableArrayOfMetadata addObject:myTaggedMediaCharacteristic];
[myAssetWriterInput setMetadata:myMutableArrayOfMetadata];
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Visual

- [AVMediaCharacteristicVisual](avmediacharacteristic/visual.md) — A media characteristic that indicates that a track or media selection option includes visual content.
- [AVMediaCharacteristicContainsAlphaChannel](avmediacharacteristic/containsalphachannel.md) — A media characteristic that indicates that a track contains an alpha channel.
- [AVMediaCharacteristicContainsHDRVideo](avmediacharacteristic/containshdrvideo.md) — A media characteristic that indicates that a track contains HDR video.
- [AVMediaCharacteristicFrameBased](avmediacharacteristic/framebased.md) — A media characteristic that indicates that a track or media selection option includes frame-based content.
- [AVMediaCharacteristicUsesWideGamutColorSpace](avmediacharacteristic/useswidegamutcolorspace.md) — A media characteristic that indicates that a track uses a wide-gamut color space.
- [AVMediaCharacteristicContainsStereoMultiviewVideo](avmediacharacteristic/containsstereomultiviewvideo.md) — A media characteristic that indicates that a track contains stereoscopic video captured in a multiview compression format.
- [AVMediaCharacteristicCarriesVideoStereoMetadata](avmediacharacteristic/carriesvideostereometadata.md) — A media characteristic that indicates that the stereoscopic video track carries additional information related to the stereoscopic video.
- [AVMediaCharacteristicIndicatesHorizontalFieldOfView](avmediacharacteristic/indicateshorizontalfieldofview.md) — A media characteristic that indicates the video track carries information related to the horizontal field of view.
- [AVMediaCharacteristicIndicatesNonRectilinearProjection](avmediacharacteristic/indicatesnonrectilinearprojection.md) — A media characteristic that indicates the video track carries information related to how it should be projected for display.

### Audible

- [AVMediaCharacteristicAudible](avmediacharacteristic/audible.md) — A media characteristic that indicates that a track or media selection option includes audible content.
- [AVMediaCharacteristicDubbedTranslation](avmediacharacteristic/dubbedtranslation.md) — A media characteristic that indicates that a track or media selection option contains audio language or dialect translation of the original content.
- [AVMediaCharacteristicVoiceOverTranslation](avmediacharacteristic/voiceovertranslation.md) — A media characteristic that indicates that a track or media selection option contains a language translation and verbal interpretation of spoken dialog.
- [AVMediaCharacteristicEnhancesSpeechIntelligibility](avmediacharacteristic/enhancesspeechintelligibility.md) — A media characteristic that indicates a track or media selection option includes audio processed to enhance the intelligibility of speech.
- [AVMediaCharacteristicDescribesMusicAndSoundForAccessibility](avmediacharacteristic/describesmusicandsoundforaccessibility.md) — A media characteristic that indicates that a track or media selection option includes legible content in the language of its specified locale.
- [AVMediaCharacteristicTactileMinimal](avmediacharacteristic/tactileminimal.md) — A media characteristic that indicates that a track or media selection option includes haptic content.

### Legible

- [AVMediaCharacteristicLegible](avmediacharacteristic/legible.md) — A media characteristic that indicates that a track or media selection option includes legible content.
- [AVMediaCharacteristicEasyToRead](avmediacharacteristic/easytoread.md) — A media characteristic that indicates a track or media selection option provides legible content that’s edited for easy reading.
- [AVMediaCharacteristicDescribesVideoForAccessibility](avmediacharacteristic/describesvideoforaccessibility.md) — A media characteristic that indicates the media includes audible content that describes the visual portion of the presentation.
- [AVMediaCharacteristicContainsOnlyForcedSubtitles](avmediacharacteristic/containsonlyforcedsubtitles.md) — A media characteristic that indicates that a track or media selection option presents only forced subtitles.
- [AVMediaCharacteristicLanguageTranslation](avmediacharacteristic/languagetranslation.md) — A media characteristic that indicates that a track or media selection option contains a language or dialect translation of the original content.
- [AVMediaCharacteristicTranscribesSpokenDialogForAccessibility](avmediacharacteristic/transcribesspokendialogforaccessibility.md) — A media characteristic that indicates that a media selection option includes legible content that transcribes spoken dialog.

### Content

- [AVMediaCharacteristicIsOriginalContent](avmediacharacteristic/isoriginalcontent.md) — A media characteristic that indicates that a track or media selection option contains original content.
- [AVMediaCharacteristicIsMainProgramContent](avmediacharacteristic/ismainprogramcontent.md) — A media characteristic that indicates a track or media selection option includes content its author indicates is essential to the asset’s presentation.
- [AVMediaCharacteristicIsAuxiliaryContent](avmediacharacteristic/isauxiliarycontent.md) — A media characteristic that indicates a track or media selection option includes content its author indicates is auxiliary to the asset’s presentation.
- [AVMediaCharacteristicMachineGenerated](avmediacharacteristic/machinegenerated.md) — A media characteristic that indicates that a track was generated in an automated fashion by a machine.

### Initializers

- [init(_:)](<avmediacharacteristic/init(__).md>) — Creates a media characteristic.
- [init(rawValue:)](<avmediacharacteristic/init(rawvalue_).md>) — Creates a media characteristic with a string value.

## See Also

### Media types

- [AVMediaType](avmediatype.md) — An identifier for various media types.
