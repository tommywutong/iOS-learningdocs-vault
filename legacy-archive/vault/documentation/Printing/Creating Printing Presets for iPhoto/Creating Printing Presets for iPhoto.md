---
title: Creating Printing Presets for iPhoto
apple_id: TP40000859
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Printing/Conceptual/PresetDraft/presets_intro/presets_intro.html
archived_at: '2026-07-18T01:52:26.792630Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Document%20Revision%20History.md)

# Creating Printing Presets for iPhoto

This document shows you how to create a printing
presets file that can be used with the iPhoto application. _Printing
presets_ are printer-specific collections of settings which
have associated metadata. The metadata describes the situation in
which the printer settings should be applied by the printing system.
For example, a given preset might be appropriate when printing high-resolution
photo images to glossy paper. The _metadata_ describes
this situation in a general manner, while the printer specific settings
describe which key-value pairs achieve the desired effect on a given
printer.

If you are a printer vendor who wants to support printing
presets you should read this document. This document

- gives an
  overview of printing presets files
- describes the format of a printing presets file
- tells you where to install a printing preset file for a printer
  module
- provides an example of a printing presets file

Apple’s iPhoto application helps users to save, organize,
and share photos by simplifying the user experience. Before iPhoto,
users needed to understand the interrelationships between paper
type and other print settings to get the best printing results.
With iPhoto, this is no longer true. The simplified Print dialog
in iPhoto presents users with a Presets pop-up menu. The Presets
setting determines which set of printing presets are used for the print
job. This saves the user from the need to navigate to different
panes in the Print dialog to make settings for paper type, resolution,
and so forth.

When iPhoto was introduced, Apple supplied printing presets
files for many printer models. Developers can provide a printing
presets file for a printer by creating a file whose contents follow
the format specified in the next section. The Apple-supplied printing presets
file is used only if a printer module does not have a printing presets
files supplied by the printer vendor.

The printing presets file uses XML format and can be viewed
by using the PropertyListEditor application provided in the `/Developer/Applications` directory. Printing
presets files are named using printer module’s ID with the `.xml` extension.
For example:

`com.abccompany.printer.ZQ3700.xml`

where `com.abccompany.printer.ZQ3700` is
the printer module ID.

A printing presets file describes an array of dictionaries.
Each dictionary is a collection of key-value pairs that describes
a single preset value—a combination of general metadata and printer
specific settings.

The preset dictionary can have the following keys:

- `com.apple.print.preset.id` The
  id of the preset. The value of this key is used to look up a localized
  name for the setting. The id must match an Apple-defined id. If
  the key does not match an Apple-defined key then the preset specified
  by the key will not be made available in the application’s Print
  dialog. The set of Apple defined keys is located in:

  `/System/Library/Frameworks/ApplicationServices.framework/Frameworks/PrintCore.framework/Resources/KnownPresets.xml`

  The
  following lists the current Apple-defined preset ids. Apple is in
  the process of defining additional preset ids.

  - Photo with Paper Auto-Detect

    - graphicsType - Photo
    - quality - mid
    - media-front-coating - autodetect
  - Photo with Paper Auto-Detect - Fine

    - graphicsType
      - Photo
    - quality - high
    - media-front-coating - autodetect
  - Photo on Plain Paper

    - graphicsType
      - Photo
    - quality - mid
    - media-front-coating - none
  - Photo on Plain Paper - Fine

    - graphicsType
      - Photo
    - quality - high
    - media-front-coating - none
  - Photo on Photo Paper

    - graphicsType
      - Photo
    - quality - mid
    - media-front-coating - glossy
  - Photo on Photo Paper - Fine

    - graphicsType
      - Photo
    - quality - high
    - media-front-coating - glossy
  - Photo on Matte Paper

    - graphicsType
      - Photo
    - quality - mid
    - media-front-coating - matte
  - Photo on Matte Paper - Fine

    - graphicsType
      - Photo
    - quality - high
    - media-front-coating - matte
- `com.apple.print.preset.graphicsType` The
  type of graphics for which this preset is tuned. The only currently
  defined value for this key is "Photo". The list of values
  for this key could expand in the near future.
- `com.apple.print.preset.quality` If
  this key is present it specifies the relative output quality of
  his preset. The values are "low", "mid", and
  "high". This is a new key and it is not used in the Apple
  supplied preset files in 10.1.2. In 10.1.2 this quality setting
  is implied by the preset id. Apple recommends that printer manufacturers
  include this key in their presets where appropriate.
- c`om.apple.print.preset.media-front-coating` If
  present the value of this key value specifies the media coating
  to be used with the associated settings. Defined values include
  "none" (plain), "glossy", "high-gloss",
  "semi-gloss", "satin", "matte", and "autodetect".
  This is a new key and it is not used in the Apple supplied preset
  files in OS X version 10.1.2. In version 10.1.2 the quality
  setting is implied by the preset id. Apple recommends that printer
  manufacturers include this key in their presets where appropriate.
- `com.apple.print.preset.model` This
  key is only needed by printer modules that support multiple printers
  where the printers have different settings; that is where a single
  preset can not satisfy all of the printer modules. In this case
  each preset can include this key to differentiate the presets for
  each supported printer model. If this key exists, then the preset
  will only be used if the value of this key matches the current printer's
  model.
- `com.apple.print.preset.settings` A
  dictionary containing a set of printer specific settings. When this
  preset is activated the key-value pairs from this dictionary are added
  to the current job’s print settings (`PMPrintSettings`).
  The print settings are added to a default print settings ticket.
  Because a printer module should treat a missing key as having a
  default value, the presets do not need to contain key-value pairs
  for default settings. You can reduce the size of the presets file
  by not including entries for values that are the same as printer
  module default values.

After you create a printing presets file for your printer
module, you need to name the file `Presets.xml` and
put it in the Resources directory of the printer module. The XML
file is not localizable so you must put the printing presets file
at the top level of the Resources directory; do not put the file
in any of the language (`.lproj` )
sub-directories.

The complete path for your printing presets file must be:

`/Library/Printers/vendor/.../vendorPM.plugin/Contents/Resources/Presets.xml`

For example, the location of ABC printer company’s printing
presets file for the SpiffyPrint model BL2300 printer would be:

`/Library/Printers/ABC/SpiffyPrint/BL2300PM.plugin/Contents/Resources/Presets.xml`

As long as your file is installed in the correct location,
the printing systems uses your printing presets file even if Apple
provides a file for your printer module. In other words, your printing
presets file takes precedence over a file supplied by Apple.

Apple-supplied printing presets files are located in this
directory:

`/System/Library/Frameworks/ApplicationServices.framework/Frameworks/PrintCore.framework/Resources/`

Listing
1-1 shows a sample printing presets file. You
can find other examples of properly formatted printing preset files
in the this directory:

`/System/Library/Frameworks/ApplicationServices.framework/Frameworks/PrintCore.framework/Resources/`

You can use the PropertyListEditor application to view the
files.

__Listing 1-1__  A sample printing presets file.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist SYSTEM "file://localhost/System/Library/DTDs/PropertyList.dtd">
<plist version="0.9">
<array>

    <dict>
        <key>com.apple.print.preset.id</key>
        <string>Photo on Plain Paper</string>
        <key>com.apple.print.preset.graphicsType</key>
        <string>Photo</string>
        <key>com.apple.print.preset.quality</key>
        <string>mid</string>
        <key> media-front-coating </key>
        <string>none</string>
        <key>com.apple.print.preset.settings</key>
        <dict>
            <key>com.xx.setting.A1</key>
            <integer>0</integer>
            <key>com.xx.setting.A2</key>
            <string>plain-12bond</string>
        </dict>
    </dict>

    <dict>
        <key>com.apple.print.preset.id</key>
        <string>Photo on Matte Paper</string>
        <key>com.apple.print.preset.graphicsType</key>
        <string>Photo</string>
         <key>com.apple.print.preset.quality</key>
            <string>mid</string>
         <key> media-front-coating </key>
         <string>matte</string>
        <key>com.apple.print.preset.settings</key>
        <dict>
            <key>com.xx.setting.A1</key>
            <integer>21</integer>
            <key>com.xx.setting.A2</key>
            <string>32 bump</string>
        </dict>
    </dict>

</array>
</plist>
```

[Next](Document%20Revision%20History.md)

