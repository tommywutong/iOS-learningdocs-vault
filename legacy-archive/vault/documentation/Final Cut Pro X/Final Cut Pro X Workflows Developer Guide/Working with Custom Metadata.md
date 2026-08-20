---
title: Final Cut Pro X Workflows Developer Guide
apple_id: TP40013781
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/FinalCutProX/Conceptual/FinalCutProXWorkflowsGuide/WorkingwithCustomMetadata/WorkingwithCustomMetadata.html
archived_at: '2026-07-15T07:32:30.157391Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Final Cut Pro X Workflows Developer Guide](About%20Final%20Cut%20Pro%20X%20Workflows.md)


[Next](Appendix%20A-%20ProVideo%20Asset%20Management%20Suite.md)[Previous](Exporting.md)

# Working with Custom Metadata

Final Cut Pro X can incorporate custom metadata described in an FCPXML document. (Refer to the _[Final Cut Pro X XML Format](https://developer.apple.com/library/archive/documentation/FinalCutProX/Reference/FinalCutProXXMLFormat/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011227)_ documentation for more details.) These custom metadata items do not appear in the Info Inspector until you add the respective fields to a metadata view. Refer to the [Final Cut Pro X Help](http://help.apple.com/finalcutpro/) for more information.

Final Cut Pro X supports a mechanism for adding metadata definitions and view sets through external metadata definition files. This mechanism allows production facilities and third-party applications to install such definition files on each Final Cut Pro X station where the metadata definitions and view sets are needed.

The definition file is a plist file that Final Cut Pro X reads and uses to augment the interface with facility-specific views. You should put this plist file in one of the following locations so Final Cut Pro X can find it:

- `/Library/Application Support/ProApps/Metadata Definitions/`
- `~/Library/Application Support/ProApps/Metadata Definitions/`

The plist file has the following structure:

- Root (Dictionary)

  - __com.apple.proapps.MetadataDefinitions__ — Definition (Dictionary)
  - __com.apple.proapps.MetadataViewSets__ — View Set (Dictionary)
- Definition (Dictionary)—The key is the Metadata identifier key (for example, `com.yourCompany.yourApp.yourCustomMetadata`).

  - __displayName__ (String)—The name to be displayed in the Name field of the Final Cut Pro X Inspector and Metadata View Set Editor.
  - __displayDescription__ (String)—The description to be displayed in the Description field of the Final Cut Pro X Metadata View Set Editor.
  - __type__ (String)—The data type of this metadata, for example, string, boolean, integer, float (these are the same Metadata types as are used in FCPXML).
  - __source__ (String)—The source of the metadata (for example, ‘EXIF’, ‘Apple’, ‘BBC’, ‘<your company name>’) to be displayed in the Origin field of the Final Cut Pro X Metadata View Set Editor.
  - __editable__ (Boolean)—Whether the user can modify this metadata.
- View Set (Dictionary)

  - __displayName__ (String)
  - __keys__ (String Array)—An array of metadata identifiers (in reverse DNS style).

Listing 3-1 shows an example metadata definition file.

__Listing 3-1__  Example metadata definition file

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>com.apple.proapps.MetadataDefinitions</key>
    <dict>
      <key>com.yourCompany.yourApp.yourCustomMetadata</key>
      <dict>
        <key>displayDescription</key>
        <string>Description of your custom metadata</string>
        <key>displayName</key>
        <string>Your custom metadata</string>
        <key>source</key>
        <string>custom</string>
        <key>type</key>
        <string>string</string>
      </dict>
    </dict>
    <key>com.apple.proapps.MetadataViewSets</key>
    <array>
      <dict>
        <key>displayName</key>
        <string>Your Application's Set</string>
        <key>keys</key>
        <array>
          <string>com.yourCompany.yourApp.yourCustomMetadata</string>
        </array>
      </dict>
    </array>
  </dict>
</plist>
￼
```

[Next](Appendix%20A-%20ProVideo%20Asset%20Management%20Suite.md)[Previous](Exporting.md)

