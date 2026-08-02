---
title: Final Cut Pro X XML Format
apple_id: TP40011227
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/FinalCutProX/Reference/FinalCutProXXMLFormat/Metadata/Metadata.html
archived_at: '2026-07-27T06:57:08.616860Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Final Cut Pro X XML Format](About%20Final%20Cut%20Pro%20X%20XML%201.8.md)


[Next](Appendix%20A-%20FCPXML%20Supported%20Identifiers.md)[Previous](Adjustments%20and%20Effects.md)

# Metadata

Final Cut Pro X maintains various metadata item values (such as Camera Name, Reel, Copyright). Metadata typically comes from the media and may be of interest to other applications, but is not critical for Final Cut Pro X to perform its tasks.

On export, Final Cut Pro X includes only the metadata items in the selected metadata view. On import, Final Cut Pro X uses the values specified in the FCPXML for editable metadata items; the values for non-editable metadata items are ignored during import, and are instead retrieved from the media asset.

See [Metadata Keys](Appendix%20A-%20FCPXML%20Supported%20Identifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmznknlti) for a complete list of metadata items that are editable through Final Cut Pro X.

## Elements

Table 5-1 lists the FCPXML metadata elements.

__Table 5-1__  Metadata elements

| Element | Description |
| `<metadata>` | A container for a collection of `<md>` elements. |
| `<md>` | Specifies an individual metadata item. This element has the following attributes:   - `key`—A structured Final Cut Pro X key string that identifies the metadata item (for example, `com.apple.proapps.mio.cameraName`). - `value`—The value of the metadata item. When the value is an array, an `<array>` element is used instead. - `editable`—Indicates whether the metadata item is editable (`1`=Yes, `0`=No). The default is 0. Most metadata items are not editable, and this attribute may be omitted. If editable, Final Cut Pro X applies the new value for the metadata item on import. - `type`—Defines the metadata item value type. - `displayName`—The metadata item name that appears in Final Cut Pro X. - `description`—The metadata item description that appears in Final Cut Pro X. - `source`—The metadata item origin. |
| `<array>` | A container for a collection of `<string>` elements that define the value(s) for an array of strings. |
| `<string>` | Defines one metadata value in an array of strings. |

The following is an example of metadata with primitive data types:

```
<metadata>
    <md key="com.apple.proapps.mio.cameraName" value="The Big Camera"/>
    <md key="com.apple.proapps.spotlight.kMDItemCopyright"
            value="© 2009 All Rights Reserved"/>
    <md key="com.apple.proapps.studio.reel" value="R945"/>
    <md key="com.apple.proapps.studio.scene" value="Deep Water"/>
</metadata>
```

The following is an example of metadata with complex data types:

```
<metadata>
    <md key="com.apple.proapps.spotlight.kMDItemCodecs" displayName="Codecs">
        <array>
            <string>AAC</string>
            <string>H.264</string>
        </array>
    </md>
</metadata>
```

## Keys and Sources

Metadata items Final Cut Pro X maintains are grouped based on where they come from (their source). The source is indicated by the `<md>` element’s `source` attribute (for example, `studio`) or the prefix of the `key` attribute (for example, `com.apple.proapps.studio`).

The sources and key prefixes currently used are:

**__Camera__**
: Metadata from a camera or capturing device that Final Cut Pro X or the device driver/plug-in picks up. These are not editable, except for `com.apple.proapps.mio.cameraName`.
: _Key Prefixes:_
: - `com.apple.proapps.mio`
- `org.smpte.mxf`
: _Example:_
: - `com.apple.proapps.mio.cameraName`

**__Exif__**
: Metadata from files with Exif information (for example, a JPEG file).
: _Key Prefix:_
: - `com.apple.proapps.exif.{Exif}`
: _Example:_
: - `com.apple.proapps.exif.{Exif}.FocalLength`

**__Image__**
: Metadata from an image file (for example, TIFF or PNG), or camera specific metadata saved with the image.
: _Key Prefixes:_
: - `com.apple.proapps.image.{TIFF}`
- `com.apple.proapps.image.{CIFF}`
- `com.apple.proapps.image.{GIF}`
- `com.apple.proapps.image.{PNG}`
- `com.apple.proapps.image.{DNG}`
- `com.apple.proapps.image.{GPS}`
- A prefix that identifies the camera manufacturer.
: _Examples:_
: - `com.apple.proapps.image.{TIFF}.WhitePoint`
- `com.apple.proapps.image.{CIFF}.FocusMode`
- `com.apple.proapps.image.{PNG}.Gamma`
- `com.apple.proapps.image.{GPS}.MapDatum`

**__IPTC__**
: International Press Telecommunication Council defined photo metadata.
: _Key Prefix:_
: - `com.apple.proapps.iptc.{IPTC}`
: _Example:_
: - `com.apple.proapps.iptc.{IPTC}.Headline`

**__Share__**
: Metadata added to a share output.
: _Key Prefix:_
: - `com.apple.proapps.share`
- `com.apple.quicktime`
: _Example:_
: - `com.apple.proapps.share.id`
- `com.apple.quicktime.copyright`

**__Spotlight__**
: Spotlight metadata.
: _Key Prefix:_
: - `com.apple.proapps.spotlight`
: _Example:_
: - `com.apple.proapps.spotlight.kMDItemCopyright`

**__Studio__**
: Final Cut Pro X-defined metadata. See [Metadata Keys](Appendix%20A-%20FCPXML%20Supported%20Identifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrxfvbuqmznknlti) for a list of editable Studio keys. Additional _Studio_ keys exist that are not editable.
: _Key Prefix:_
: - `com.apple.proapps.studio`
: _Examples:_
: - `com.apple.proapps.studio.reel`
- `com.apple.proapps.studio.scene`

**__Custom__**
: Metadata the user added in Final Cut Pro X (has prefix: `com.apple.proapps.custom`), or metadata that comes from a third-party application or camera (prefix is a Reverse DNS string that identifies a third-party application or a camera manufacturer).
: _Key Prefixes:_
: - `com.apple.proapps.custom`
- A prefix that identifies a third-party application or a camera manufacturer.
: _Examples:_
: - `com.apple.proapps.custom.mycustommetadata`
- `com.yourCompany.yourApp.yourCustomMetadata`

The following is an example of custom metadata items:

```
<metadata>
    <md key="com.yourCompany.yourApp.yourCustomMetadata"
          value="This is your custom metadata" type="string"
          displayName="Your Custom Metadata" source="Your Application"/>
    <md key="com.apple.proapps.custom.mycustommetadata"
          value="This is my custom metadata" type="string" editable="1"
          displayName="myCustomMetadata" source="custom source"/>
</metadata>
```

[Next](Appendix%20A-%20FCPXML%20Supported%20Identifiers.md)[Previous](Adjustments%20and%20Effects.md)
