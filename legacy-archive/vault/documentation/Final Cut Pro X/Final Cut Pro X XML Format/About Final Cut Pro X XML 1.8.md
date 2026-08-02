---
title: Final Cut Pro X XML Format
apple_id: TP40011227
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/FinalCutProX/Reference/FinalCutProXXMLFormat/Introduction/Introduction.html
archived_at: '2026-07-27T06:57:08.433858Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](FCPXML%20Concepts.md)

# About Final Cut Pro X XML 1.8

You use the Final Cut Pro X app to create, edit, and produce high-quality video. With the Final Cut Pro X XML (FCPXML) format, you can transfer the details of your events and projects between Final Cut Pro X and third-party applications, devices, and media asset management tools that do not natively recognize Final Cut Pro X events or projects. FCPXML 1.8 requires Final Cut Pro X 10.4.1 or later.

FCPXML describes certain aspects of projects and events that are useful for other applications. It does not describe all possible data, and therefore is not a substitute for the native project and event data organized in a library bundle.

You can use Final Cut Pro X to export and import FCPXML documents to accomplish the following tasks:

- Exchange Final Cut Pro X event and project data with other applications.
- Create new Final Cut Pro X events and projects.

In this document, it is assumed that you understand XML and have used Final Cut Pro X.

__Note:__ Starting with Final Cut Pro X 10.1, project and event data is organized in a library bundle. Refer to [Managing Media with Final Cut Pro X Libraries](http://images.apple.com/final-cut-pro/docs/Media_Management.pdf) for more information on Final Cut Pro Libraries.

Starting with Final Cut Pro X 10.3, you can import XML documents into existing events and exchange objects through drag-and-drop as XML with another application that supports FCPXML. Refer to the _[Final Cut Pro X Workflows Developer Guide](../Final%20Cut%20Pro%20X%20Workflows%20Developer%20Guide/About%20Final%20Cut%20Pro%20X%20Workflows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztoobr)_ for more information.

FCPXML 1.8 includes the following changes:

- Closed captions and subtitles—New `<caption>` element for adding captions and subtitles to a clip.

  __Relevant Chapter:__ [Story Elements](Story%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjtfvjvomi)
- Caption and subtitle text blocks—Added support for describing captions and subtitles.

  __Relevant Section:__ [Titles and Captions](Adjustments%20and%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvomry)

FCPXML 1.7 includes the following changes:

- External asset identifiers—Added support for asset identifiers assigned by third parties.

  __Relevant Section:__ [Media Assets](Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjwfvjvomry)
- High Dynamic Range (HDR) projects and media—Enhanced support for project and media color space, added support for HDR library processing mode.

  __Relevant Section:__ [Media Formats](Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjwfvjvomjz)
- 360-degree projects and media—Added support for describing projection information.

  __Relevant Section:__ [Media Formats](Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjwfvjvomjz)

FCPXML 1.6 included the following changes:

- Single asset reference—New `<asset-clip>` element to add both the audio and video media components from a media file as a clip.

  __Relevant Chapter:__ [Story Elements](Story%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjtfvjvomi)
- Synchronized clips—New `<sync-clip>` element to describe clips whose contained items and anchored items are synchronized.

  __Relevant Chapter:__ [Story Elements](Story%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjtfvjvomi)
- Audio components—Added support for audio components identified in terms of their roles.

  __Relevant Section:__ [Audio Components](Story%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjtfvjvona)
- Wide-gamut color—Added support for projects using wide gamut color (Rec. 2020).

FCPXML 1.5 included the following changes:

- Collections—Added support for smart collections in Final Cut Pro X libraries.

  __Relevant Section:__ [Collections](FCPXML%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjsfvjvony)
- Video filter masks—Now applies video filters to a region defined by a collection of masks.

  __Relevant Section:__ [Masked Filters](Adjustments%20and%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvomrs)
- Color filtering and adjustments—Now describes color correction, color matching, and color balance effects using the `<filter-video>` element instead of the `<adjust-color>` and `<color-filter>` elements.

  __Relevant Section:__ [Color Filters](Adjustments%20and%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvooa)
- 3D text—Now applies three dimensional text appearance to titles.

  __Relevant Section:__ [Text Styles](Adjustments%20and%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvomrq)
- Structured parameter data—Describes three dimensional text and other effects.

  __Relevant Section:__ [Adjustment Attributes and Effect Parameters](Adjustments%20and%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvonq)
- ASC CDL color information—Now exports as an XML comment the primary color correction definition in American Society of Cinematographers Color Decision List (ASC CDL) format.

  __Relevant Content:__ See the [Note](Adjustments%20and%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvomrt) in the Color Filters section.

FCPXML 1.4 included the following changes:

- Structural changes reflecting the organization of Final Cut Pro X libraries.

  __Relevant Chapter:__ [FCPXML Concepts](FCPXML%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjsfvjvomi)
- Change in specifying keyframe animations.

  __Relevant Section:__ [Animation](Adjustments%20and%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvomq)
- Visual adjustments on a multicam clip must now be specified on individual angles instead of the entire clip.

  __Relevant Section:__ [Multicam Media](Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjwfvjvonq) and [Visual Adjustments](Adjustments%20and%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvomjw)

FCPXML 1.3 added support for the following Final Cut Pro X features:

- Adjustments

  - Color adjustments—Define and preserve color adjustments, such as balancing, matching, and correction.
  - Audio adjustments—Define audio component enhancements, such as loudness, noise and hum reduction, and equalization.
  - Video adjustments—Define the stabilization and rolling shutter reduction applied to a clip.

  __Relevant Section:__ [Adjustments](Adjustments%20and%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvomjr)
- Effects

  - Text styles—Define text style effects for titles, such as font, size, color, alignment, spacing, style, stroke, baseline, and kerning.
  - Color filtering—Apply color filter effects to a clip.

  __Relevant Section:__ [Effects](Adjustments%20and%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvooi)
- Import options—Control certain options during XML import.

  __Relevant Section:__ [Import Options](FCPXML%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjsfvjvooa)
- Collections—Group clips and projects using folders, keywords, and other search criteria.

  __Relevant Section:__ [Collections](FCPXML%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjsfvjvony)

__Note:__ In FCPXML 1.3, some attributes and elements are renamed or removed. Take care if you plan to support both 1.3 and earlier versions. In particular, the `<filter>` element is replaced by the `<filter-audio>` and `<filter-video>` elements, depending on the type of the filter. Also the `<timeMap>` element representing rate conforming (with the `rateConform` attribute) is replaced by the `<conformRate>` element. Refer to the DTDs for prior versions in [Legacy DTDs for Final Cut Pro X XML](https://developer.apple.com/library/fcp/legacydtds) for specific changes.

FCPXML 1.2 added support for the following Final Cut Pro X features:

- Audio Component Editing—Define how audio components are used (for example, channel mappings, enabled, role, effects, and mute ranges).

  __Relevant Section:__ [Audio Components](Story%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjtfvjvona)
- Metadata Export/Import—Import and export metadata associated with media assets or clips in an event or project.

  __Relevant Chapter:__ [Metadata](Metadata.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjxfvjvomi)

FCPXML 1.1 added support for the following Final Cut Pro X features:

- Multicam editing—Manage media from multiple cameras or other synchronized footage.

  __Relevant Chapter:__ [Resources](Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjwfvjvomi)
- Adjustments

  - Video and image transformation—Crop, trim, pan and zoom, distort, conform, move, resize, rotate, and blend videos and images.
  - Audio adjustment—Adjust audio volume and panning.

  __Relevant Chapter:__ [Adjustments and Effects](Adjustments%20and%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvomi)
- Retrieve ASC CDL color information—Export the first primary color correction definition in American Society of Cinematographers Color Decision List (ASC CDL) format.

  __Note:__ In FCPXML 1.5, this feature was changed and ASC CDL color information is now exported as an XML comment. See the [Note](Adjustments%20and%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmjufvjvomrt) in the Color Filters section.

## See Also

The following resources may be helpful as you work with the FCPXML format:

- [Final Cut Pro X Help](http://help.apple.com/finalcutpro/)
- [Final Cut Pro X Resources](http://www.apple.com/final-cut-pro/resources/)
- See [Legacy DTDs for Final Cut Pro X XML](https://developer.apple.com/library/fcp/legacydtds) for prior DTD versions.
- The [Extensible Markup Language (XML) 1.0](http://www.xml.com/axml/testaxml.htm) specification

[Next](FCPXML%20Concepts.md)
