---
title: Final Cut Pro X - Metadata in MP4
apple_id: DTS40014018
resource_type: Technical Note
platform: macOS
topic: Apple Applications
technology: null
published: '2013-12-18'
source_url: https://developer.apple.com/library/archive/technotes/tn2174/_index.html
archived_at: '2026-07-26T19:54:13.027451Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2174

# Final Cut Pro X - Metadata in MP4

Final Cut Pro X recognizes timecode and certain metadata in MP4 files, as much as it does in QuickTime Movie (MOV) files. This document describes the format of timecode and chapter markers stored as a track in MP4 files. It also discusses how metadata Final Cut Pro X supports are stored in MP4 files as user data items.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvke4vcbi4yq)[MP4 File Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvke4vcbi4za)[Timecode and Chapter Markers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvke4vcbi4zq)[Timecode Track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvke4vcbi42a)[Timecode Media Information](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvke4vcbi42c2vcjjvcugt2eivpu2rkejfav6skoizhvetkbkreu6tq)[Timecode Samples](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvke4vcbi42c2vcjjvcugt2eivpvgqknkbgekuy)[Timecode Track Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvke4vcbi42c2vcjjvcugt2eivpviusbinfv6usfizcverkoincq)[Chapter Marker Track](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvke4vcbi4ytg)[Chapter Marker Media Information](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvke4vcbi4ytglkdjbavavcfkjpu2qksjncvex2nivcesqk7jfhemt2sjvaviskpjy)[Chapter Marker Sample Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvke4vcbi4ytglkdjbavavcfkjpu2qksjncvex2tifgvatcfl5de6usnifka)[Chapter Marker Track Header Box](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvke4vcbi4ytglkdjbavavcfkjpu2qksjncvex2ukjaugs27jbcucrcfkjpuet2y)[Chapter Marker Track Reference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvke4vcbi4ytglkdjbavavcfkjpu2qksjncvex2ukjaugs27kjcumrksivhegri)[Clip Metadata](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvke4vcbi4yti)[References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvjekrsfkjcu4q2fkm)[Appendix A: 3GPP User Data Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvke4vcbi4ytk)[Appendix B: Video Editing User Data Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvke4vcbi4ytm)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

Consumer/Prosumer level Camcorders and Still Cameras (DSLRs and DSCs) require a self-contained media file format to carry captured audio/video footage and metadata. The QuickTime File Format [1] fills this need very nicely, however there is an increased level of interest among camera manufacturers for a specification based-on the standard such as MP4.

This document addresses such interest by defining the format of the timecode and chapter marker tracks in the MP4 File Format [2], borrowing relevant definitions from the QuickTime File Format. In addition Apple recommends using the User Data container for storing non-temporal metadata in an MP4 file with the keys defined in the 3GPP standard [5]. The document also defines additional metadata keys intended for use with video editing applications such as Final Cut Pro X.

[Back to Top](#)

## MP4 File Format

The MP4 File Format is a multimedia container file format defined as part of the MPEG-4 standard. The official name of the standard is ISO/IEC 14496-14:2003 [2], often times referred to as MPEG-4 Part 14. It defines how to store video and audio streams encoded with certain codecs, such as MPEG-4 Part 2 or MPEG-4 Part 10 (H.264/AVC) and Advanced Audio Coding (AAC). The MP4 File Format is also used to store subtitle text in the MPEG-4 Timed Text format (MPEG-4 Part 17 [3]).

The MP4 File Format has general provisions for carrying temporal metadata using the definitions in the ISO Base Media File Format (MPEG-4 Part 12 [4]), but there is no concrete specification to store timecode information or chapter markers. There is very limited non-temporal or clip metadata (only copyright) defined specifically for MP4.

[Back to Top](#)

## Timecode and Chapter Markers

Apple recommends that developers and manufacturers use the following two track types to store timecode and chapter markers in an MP4 file:

- Timecode Track
- Chapter Marker Track

These track types are already available in the QuickTime File Format. The MP4 File Format design is similar to the QuickTime File Format, therefore it's natural to borrow these constructs defined in the QuickTime File Format to support the features in the MP4 File Format. It may, however, be appropriate to drop legacy QuickTime specific constructs that are awkward in the context of the ISO specification.

[Back to Top](#)

## Timecode Track

The timecode track in an MP4 file uses the constructs defined in the QuickTime File Format, with some minor modifications.

- The text formatting information to display the timecode is dropped.
- The Null Media Header box (`nmhd`) box is used instead of the Generic Media Header box (`gmhd`).

The rest of the QuickTime Timecode track functionality, such as 64-bit timecode support, is preserved.

### Timecode Media Information

The following sections describe the boxes under the Media box (`mdia`) that indicate a timecode track.

#### Handler Reference Box

The handler type is `tmcd` in the Handler Reference box (`hdlr`) under the Media box (`mdia`), as defined in the QuickTime File Format Specification [1]. This indicates that the track contains timecode information.

#### Media Information Header Box

For a timecode track, the Null Media Header box (`nmhd`) is used as the media information header. This is in contrast to the Generic Media Header box (`gmhd`) used in the QuickTime Timecode track.

Unlike the QuickTime Timecode track, there is no Timecode Media Information box (`tcmi`). The information in this box is about formatting the timecode as text. Given the timecode is metadata, the formatting information is no longer considered relevant, and therefore dropped.

#### Timecode Sample Entry

The timecode track sample entry uses the same structure as the Timecode Sample Description defined in the QuickTime Movie File Format specification [1], except for the source reference field. The Timecode Sample Entry definition is presented in Listing 1 with the same notation used in the MP4 specification [2].

__Listing 1__  Timecode Sample Entry definition

```swift
class TimecodeSampleEntry(codingName) extends SampleEntry(codingName) {
   const unsigned int(32) reserved = 0;
   unsigned int(32) flags;
   int(32) timescale;
   int(32) frameDuration;
   int(8) numFrames;
   const unsigned int(8) reserved = 0;
}
```

The `codingName` field is one of the following:

- `tmcd` — For 32-bit timecode samples.
- `tc64` — For 64-bit timecode samples.

The `flags` field contains the following flags:

- Drop frame (`0x0000001`) — Indicates whether the timecode is a drop frame. It's a drop frame if the flag is set.
- 24 hour max (`0x0000002`) — Indicates whether the timecode wraps after 24 hours. It wraps if the flag is set.
- Negative times OK (`0x0000004`) — Indicates whether negative time values are allowed. Negative values are allowed if the flag is set.
- Counter (`0x0000008`) — Indicates whether the timecode value this track represents is a tape counter value. It's a tape counter value if the flag is set.

The `timescale` field specifies the time scale for the `frameDuration` field.

The `frameDuration` field indicates how long each frame lasts in real time.

The `numFrames` field contains the number of frames per second for the timecode format. If the timecode is a counter, this is the number of frames for each counter tick.

This is exactly the same as the QuickTime Timecode Sample Description, except that the source reference extension is dropped.

### Timecode Samples

The sample format is the same as the QuickTime Timecode Track. There is no need for transcoding when the data is going from one format to the other.

### Timecode Track Reference

Apple does not recommend using track references that indicate particular association to other media tracks. Generally, a timecode track represents the timecode for the entire captured movie, and therefore no track reference is required.

[Back to Top](#)

## Chapter Marker Track

The Chapter Marker track stores text chapter markers in an MP4 file as a disabled text track, with a track reference that identifies the track as a chapter marker track. It uses the constructs defined in the QuickTime File Format Specification with minor modifications.

### Chapter Marker Media Information

The following sections describe the boxes under the Media box (`mdia`) that indicate a chapter marker track.

#### Handler Reference Box

The handler type is set to `text` in the Handler Reference box (`hdlr`) under the Media box (`mdia`). This indicates that the track contains text data.

#### Media Information Header Box

For a Chapter Marker track, the Null Media Header box (`nmhd`) is used as the media information header. This is in contrast to the Generic Media Header box (`gmhd`) box used in the QuickTime Text Track.

#### Chapter Maker Sample Entry

To store information specific to Chapter Marker samples, the `TextSampleEntry` defined in the MPEG-4 Timed Text Format [3], originally defined in 3GPP Timed Text Format [6], is used. Because chapter markers are considered as metadata and not part of the presentation, all the text formatting information, such as font, style, text box, color, and justification, are ignored.

### Chapter Marker Sample Format

A Chapter Marker sample is a series of Unicode characters, either in UTF-16 or UTF-8, preceded by a 16-bit unsigned integer that indicates the number of bytes that the series takes up. If the size of the media sample is greater than the number of bytes indicated, the extra data is ignored. If UTF-16 is used, there must be a BOM (Byte Order Mark) at the beginning of the series indicating format and byte order of Unicode characters.

This is a subset of the MPEG-4 Timed Text Sample Format [3]. There is no formatting information. It's simple enough to transcode a MPEG-4 Timed Text track into the Chapter Marker track by simply stripping off the formatting information.

### Chapter Marker Track Header Box

To indicate that the text samples in the chapter marker track aren't part of the presentation, the chapter marker track should be disabled. To do so, set the `track_enabled` flag, which is the zero bit of the flags field, to 0.

### Chapter Marker Track Reference

A track reference of type `chap` from an enabled track to the Chapter Marker track must exist, as it is with a Chapter Marker track in a QuickTime Movie.

[Back to Top](#)

## Clip Metadata

For clip (or non-temporal) metadata, Apple recommends using the User Data container and store metadata items as user data items with user data keys, each of which is a four character code. This provides sufficient functionality to carry text-oriented metadata items with language identification. The 3GPP file format [5] defines more than a dozen user data keys, and Apple recommends to follow those definitions. The following three keys are currently supported by Final Cut Pro X:

- `titl` – The title for the media.
- `cprt` – The information about the organization holding the copyright for the media file.
- `auth` – The author of the media.

[Appendix A: 3GPP User Data Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvke4vcbi4ytk) lists the metadata keys defined in the 3GPP Release 12 [5]. Refer to the specification [5] for the definitions of custom data types.

Apple also defines additional user data keys for video applications such as Final Cut Pro X, such as the manufacturer and the model name of the camera. [Appendix B: Video Editing User Data Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrhawugsbrfvke4vcbi4ytm) contains a list of those user data keys. Note the string value for the creation date key is expected to be in the ISO 8601 date string format [7].

Unlike with the QuickTime Metadata keys, there isn't a safe way to introduce private keys for user data keys. For an MP4 file, private metadata should be stored in a UUID box as defined in the ISO Base Media file format [4].

[Back to Top](#)

## References

[1] [QuickTime File Format Specification, 2012](https://developer.apple.com/library/mac/documentation/QuickTime/QTFF/), Apple Inc.

[2] [MPEG-4 Part 14: MP4 file format; ISO/IEC 14496-14:2003](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=38538), International Organization for Standardization

[3] [MPEG-4 Part 17: Streaming text format; ISO/IEC 14496-17:2006](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=39478), International Organization for Standardization

[4] [MPEG-4 Part 12: ISO base media file format; ISO/IEC 14496-12:2012](http://www.iso.org/iso/home/store/catalogue_ics/catalogue_detail_ics.htm?csnumber=61988), International Organization for Standardization

[5] [3GPP TS 26.244 v12.1.0: 3GPP file format (3GP) (Release 12)](http://www.3gpp.org/ftp/Specs/html-info/26244.htm), 3rd Generation Partnership Project

[6] [3GPP TS 26.245 V12.0.0: 3GPP Timed text format (Release 12)](http://www.3gpp.org/ftp/Specs/html-info/26245.htm), 3rd Generation Partnership Project

[7] [Data elements and interchange formats - Information interchange - Representation of dates and times; ISO 8601:2004](http://www.iso.org/iso/catalogue_detail?csnumber=40874), International Organization of Standardization

[Back to Top](#)

## Appendix A: 3GPP User Data Keys

Refer to [5] for definition of custom data types.

__Table 1__  3GPP User Data Keys

| Key | Name | Type | Description |
| titl | title | string | Title of the media. |
| dscp | description | string | Caption or description for the media. |
| cprt | copyright | string | Notice about the organization holding the copyright for the media. |
| perf | performer | string | Performer or artist for the media. |
| auth | Author | string | Author of the media. |
| gnre | genre | string | Genre (category or style) of the media. |
| rtng | rating | custom | Media rating, including the rating entity and the rating criteria. |
| clsf | classification | custom | Classification of the media, including the classification entity and an index that indicates the classification table. |
| kywd | keyword | list of strings | Media keywords. |
| loci | location | custom | Location information, including location name, role, longitude, latitude, altitude, astronomical body, and notes. |
| albm | album | custom | Album title and track number for the media. |
| yrrc | recording year | integer | Recording year for the media. |
| coll | collection | string | Name of the collection from which the media comes from. |
| urat | user rating | integer | User's star rating for the media. |
| thmb | thumbnail | custom | Thumbnail image of the media. |

[Back to Top](#)

## Appendix B: Video Editing User Data Keys

__Table 2__  Video Editing User Data Keys

| Key | Name | Type | Description |
| manu | manufacturer | string | Name of the camera manufacturer. |
| modl | model name | string | Model name of the camera. |
| slno | serial no | string | Serial number of the camera. |
| clid | clip ID | string | Identifier of the clip. |
| clfn | clip file name | string | Name of the clip file. |
| cmid | camera ID | string | Camera identifier. |
| cmnm | camera name | string | Name that identifies the camera. |
| reel | reel | string | Name of the tape reel. |
| scen | scene | string | Name of the scene for the clip. |
| shot | shot | string | Name that identifies the shot. |
| angl | angle | string | Name of the camera angle thorough which the clip was shot. |
| date | creation date | string | Date and time, formatted according to ISO 8601, when the clip recording started. |

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-12-18 | New document that describes the format of timecode and other metadata Final Cut Pro X recognizes in MP4 files. |

