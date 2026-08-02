---
title: ImportExport
apple_id: DTS10000957
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2006-05-11'
source_url: https://developer.apple.com/library/archive/samplecode/ImportExport/Introduction/Intro.html
archived_at: '2026-07-18T03:12:50.276598Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](src-ImportExport.java.md)

# ImportExport

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2006-05-11 Support for XCode 2. Modified project layout for platform independent distribution and compilation. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydaojvg4wvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | XCode 2.2, or Java 2 SDK for Windows, and QuickTime 7 |
| __Runtime Requirements:__ | Java 1.5 and QuickTime 7, or later, recommended |

Demonstrates how to export a movie, using the standard user dialog to customise export settings. There are two ways this can be done - by far the easiest way is to use the Movie.convertToFile call which will allow you to show the default progress proc. This provides simple visual feedback to the user of the progress of the export. Alternatively an application can call the MovieExporter directly to export movie data and define its own custom progress handling. A movie export should take place on an independant thread, so as not to block the Java AWT event thread, since an export can take some time.

Also shown is how to create reference movies, which contain references to an existing movie, or movies, rather than an independent copy of the movie data. This movie may be "flattened" later on. Flattening is a process that copies the referenced movie data into the reference movie, making it a standalone copy.

[Next](src-ImportExport.java.md)

