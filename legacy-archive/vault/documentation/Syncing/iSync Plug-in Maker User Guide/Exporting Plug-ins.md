---
title: iSync Plug-in Maker User Guide
apple_id: TP40003921
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2011-06-13'
source_url: https://developer.apple.com/library/archive/documentation/Syncing/Conceptual/TramontanePluginBuilderUserGuide/Exporting/Exporting.html
archived_at: '2026-07-18T02:07:49.535911Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iSync Plug-in Maker User Guide](Introduction%20to%20iSync%20Plug-in%20Maker%20User%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Testing%20Plug-ins.md)

# Exporting Plug-ins

When you are ready to export your plug-in or modem script, click the Export button in the toolbar. An alert panel appears asking if you have tested the plug-in. Click Yes if you completed the testing phase or Cancel if you want to continue testing the plug-in.

If you click Yes, a sheet appears allowing you to enter a filename and select an export format from a pop-up menu, as shown in Figure 4-1. Enter the filename, choose a format, and click Export.

__Figure 4-1__  Exporting sheet

![Exporting sheet](attachments/art/exporting2.jpg)

Which format you choose depends on how you want to ship your plug-in and if you want to export the modem script separately. For example, if you want to ship the plug-in as a downloadable package, you might choose "Disk image with installer." If the plug-in is part of another product, then you might choose "iSync plug-in" and include the file in the product package. If you want to just export the modem script choose “Modem Script bundle.“ The possible export formats are described in Table 4-1.

__Table 4-1__  Export formats

| Format | Description |
| iSync plug-in | Exports the plug-in in a bundle format that can be loaded by iSync. This bundle includes the iSync plug-in only, not the modem script bundle.  For example, choose this format if you want to run some manual tests on your local computer. See _[iSync Manual Test Suite Guide](../../Apple%20Applications/iSync%20Manual%20Test%20Suite%20Guide/Introduction%20to%20iSync%20Manual%20Test%20Suite%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diobu)_ for manual tests that you should run before shipping your plug-in.  iSync looks in `~/Library/PhonePlugins` and then `/Library/PhonePlugins` for phone plug-in files. Move your phone plug-in file to one of these folders. Create the folder if it doesn’t exist. |
| Modem Script bundle | Exports the modem script as a bundle independent of the iSync plug-in. Choose this option if you are just adding CCL support for a device. |
| Installer package | Exports the plug-in as an installer package. Choose this format if you are releasing the plug-in separately. For example, choose this format if you make the plug-in available on a CD or DVD. Select the appropriate options below the “Export format” menu to include just the iSync plug-in, just the modem script, or both in the installer package. |
| Disk image with installer | Exports the plug-in as an installer in a convenient disk image that is ready for release. For example, choose this option if you want to make the plug-in downloadable. Select the appropriate options below the “Export format” menu to include just the iSync plug-in, just the modem script, or both in the disk image. |

[Next](Document%20Revision%20History.md)[Previous](Testing%20Plug-ins.md)

