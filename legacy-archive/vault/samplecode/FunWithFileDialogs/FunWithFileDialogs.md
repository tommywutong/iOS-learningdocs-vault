---
title: FunWithFileDialogs
apple_id: DTS10000678
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-04-30'
source_url: https://developer.apple.com/library/archive/samplecode/FunWithFileDialogs/Introduction/Intro.html
archived_at: '2026-07-18T03:09:40.822657Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](README.txt.md)

# FunWithFileDialogs

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-04-30 Demo of the AWT FileChooser and Swing Aqua JFileChooser, and available Mac-specific runtime options. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Mac OS X Mac OS X 10.2 or later, Java 1.4.1 or later |

This sample demonstrates the behavior of the AWT FileChooser and Swing Aqua JFileChooser dialogs in Mac OS X, and the available runtime options to handle Mac-specific conditions in each class. They are: JFileChooser.packageIsTraversable (JFileChooser) JFileChooser.appBundleIsTraversable (JFileChooser) apple.awt.use-file-dialog-packages (FileDialog) This sample is for developers looking to handle Mac OS X-specific conditions in their AWT/Swing applications. Keep in mind that the FileDialog can still be used in Swing applications safely (and is recommended because it employs the native "Column" view), and that the runtime properties in question can be set on the fly as long as it's done before the relevant dialog instance is shown. They are neither permanent nor global. Requirements: Mac OS X 10.2 or later, Java 1.4.1 or later Keywords: filedialog java jfilechooser

[Next](README.txt.md)

