---
title: BackgroundExporter
apple_id: DTS10003356
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2005-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/BackgroundExporter/Introduction/Intro.html
archived_at: '2026-07-18T03:01:42.306450Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# BackgroundExporter

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0.1, 2005-07-22 Updated to produce a universal binary. No code changes were required. |
| __Build Requirements:__ | Xcode 2.1, Xcode 1.2 |
| __Runtime Requirements:__ | QuickTime 6.4+, Mac OS X 10.3+ |

The technique presented in this sample may be useful in situations where exporting on separate threads isn't practical , for example in cases where a Movie contains media requiring one or more non-thread safe components to render, and the export applications UI cannot be blocked waiting for the export to happen on the main thread. As an example, earlier version of QuickTime (6.5.2) could not export Sound Media on separate threads. QuickTime 7+ no longer has this limitation.
MovieExportClient launches a background application called MovieExportServer on startup (MovieExportServer is located in the Client apps bundle). The Client let's you select a Movie, configure the QuickTime Movie exporter component and send an export request to the server application. MovieExportServer queues up requests and actually does all the work by calling ConvertMovieToDataRef on the main thread. The Server also sends progress messages back to the client for display in a status window during the export process.
A relatively straight forward approach, the techniques presented here can be expanded to perform batch processing, export from procedures or any other export activity which needs to be on the main thread but is not practical to do from the main application.
Xcode 2.1 project builds universal binary.

[Next](main.c.md)

