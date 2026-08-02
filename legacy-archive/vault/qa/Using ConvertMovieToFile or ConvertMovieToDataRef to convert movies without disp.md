---
title: Using ConvertMovieToFile or ConvertMovieToDataRef to convert movies without
  displaying the settings dialog
apple_id: DTS10003524
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2005-03-22'
source_url: https://developer.apple.com/library/archive/qa/qa1418/_index.html
archived_at: '2026-07-18T02:30:35.448730Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1418

# Using ConvertMovieToFile or ConvertMovieToDataRef to convert movies without displaying the settings dialog

## Q:  I have a source movie in DV format and I need to convert it to a MPEG-4 file and set some of the attributes like compression quality, image size, frame rate, and so on. However, I'd like to do this programatically without displaying the settings dialog. Is this possible?

A: Yes. The recommended technique for performing a conversion without displaying the dialog involves a two-stage process in which you create a set of settings "presets" which are retrieved later to configure the exporter. Here's an overview:

First, create a simple tool (separate from your real application) to manufacture any number of exporter settings presets which can be retrieved later to configure the exporter. Here's how:

Write a simple application which brings up the exporter dialog. Now use the dialog to configure the desired settings for your file export and save these settings to a file so they can be easily retrieved later. You can create any number of different exporter settings presets in this manner to suit your particular needs.

Here's the detailed steps:

- Find and open the desired export component.
- Call `MovieExportDoUserDialog` to bring up the settings dialog.
- Adjust the export settings in the dialog as appropriate, and dismiss the dialog.
- Call `MovieExportGetSettingsAsAtomContainer` to retrieve and save the newly configured exporter settings.
- Close the exporter component.

This technique is demonstrated in [Technical Q&A QTMTB62, 'Batch Exporting movie sound tracks with ConvertMovieToFile'](https://developer.apple.com/qa/qtmtb/qtmtb62.html) and in the [QTDataExchange](https://developer.apple.com/samplecode/Sample_Code/QuickTime/Importers_and_Exporters/qtdataexchange.htm) and [BackgroundExporter](https://developer.apple.com/samplecode/BackgroundExporter/BackgroundExporter.html) sample code projects.

Finally, in your real application, retrieve the desired settings preset, configure the export component with these saved settings and perform the conversion with the fully configured export component.

Here's the detailed steps:

- Find and open the desired export component.
- Call `MovieExportSetSettingsFromAtomContainer` with the AtomContainer for the previously saved settings to configure the exporter
- Call  `ConvertMovieToFile`  or `ConvertMovieToDataRef` to perform the conversion, passing the fully configured export component as the last parameter to this function.

This technique is also demonstrated in [Technical Q&A QTMTB62, 'Batch Exporting movie sound tracks with ConvertMovieToFile'](https://developer.apple.com/qa/qtmtb/qtmtb62.html) and in the [QTDataExchange](https://developer.apple.com/samplecode/Sample_Code/QuickTime/Importers_and_Exporters/qtdataexchange.htm) and [BackgroundExporter](https://developer.apple.com/samplecode/BackgroundExporter/BackgroundExporter.html) sample code projects.

Alternately, you can manually configure the exporter using the various `QTAtom` routines.

To use this technique, first get the default settings from the exporter, use the functions which operate on QuickTime atoms to locate the atoms associated with the desired settings, then update the atoms for the new settings. Next, configure the exporter with the new settings. Finally, call  `ConvertMovieToFile`  or `ConvertMovieToDataRef` to perform the conversion, passing the fully configured export component as the last parameter to this function.

Here's the detailed steps:

- Find and open the desired export component.
- Call `MovieExportGetSettingsAsAtomContainer` to retrieve the default settings from the export component
- Use the `QTAtom` routines to locate the particular atoms
- Change the atom settings as desired
- Call `MovieExportSetSettingsFromAtomContainer` to set the exporter settings
- Call  `ConvertMovieToFile`  or `ConvertMovieToDataRef` to perform the conversion, passing the fully configured export component as the last parameter to this function.

This technique is demonstrated in [Technical Q&A QA1147, 'Programmatic configuration of a Movie Export Component'](https://developer.apple.com/qa/qa2001/qa1147.html).

As noted above, only part of the settings atoms used to configure the exporters are documented. Therefore, it may not be possible to fully configure the exporter using this technique.

However, the definitions for the settings atoms used with the [Standard Image Compression Dialog component](https://developer.apple.com/documentation/QuickTime/RM/CompressDecompress/ImageComprDialog/index.html) and functions such as [SCSetInfo](https://developer.apple.com/documentation/QuickTime/APIREF/scsetinfo.htm) can be found in the QuickTimeComponents.h header file.

Atoms for the visual settings can be found in the `kQTSettingsVideo` ('`vide`') container atom. Atoms for the audio settings can be found in the `kQTSettingsSound` ('`soun`') container atom.

For example, the spatial compression parameters used with the [Standard Image Compression Dialog component](https://developer.apple.com/documentation/QuickTime/RM/CompressDecompress/ImageComprDialog/index.html) are stored in the '`vide`' container atom in an atom with ID `scSpatialSettingsType` ('`sptl`') and data in an `SCSpatialSettings` structure:


```
struct SCSpatialSettings {
  CodecType           codecType;
  CodecComponent      codec;
  short               depth;
  CodecQ              spatialQuality;
};
```

Similarly, temporal compression parameters are stored in an atom with ID `scTemporalSettingsType` ('`tprl`') and data in an `SCTemporalSettings` structure:


```
struct SCTemporalSettings {
  CodecQ              temporalQuality;
  Fixed               frameRate;
  long                keyFrameRate;
};
```

Compression data rate settings are stored in an atom with ID `scDataRateSettingsType` ('`drat`') and data in an `SCDataRateSettings` structure:


```
struct SCDataRateSettings {
  long                dataRate;
  long                frameDuration;
  CodecQ              minSpatialQuality;
  CodecQ              minTemporalQuality;
};
```


- [Technical Q&A QTMTB62, 'Batch Exporting movie sound tracks with ConvertMovieToFile'](https://developer.apple.com/qa/qtmtb/qtmtb62.html)
- [Technical Q&A QA1147, 'Programmatic configuration of a Movie Export Component'](https://developer.apple.com/qa/qa2001/qa1147.html)
- [QTDataExchange sample code](https://developer.apple.com/samplecode/Sample_Code/QuickTime/Importers_and_Exporters/qtdataexchange.htm)
- [BackgroundExporter sample code](https://developer.apple.com/samplecode/BackgroundExporter/BackgroundExporter.html)
- [Finding Movie Export Components](https://developer.apple.com/quicktime/icefloe/dispatch006.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-03-22 | New document that describes how to perform movie export using ConvertMovieToFile or ConvertMovieToDataRef without displaying the dialog |

