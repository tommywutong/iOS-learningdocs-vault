---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Compiled/Deploy.html
archived_at: '2026-07-15T07:48:15.934991Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](compiled.book.md) [!Previous Section](RunApp.md)

# Deploy the application

When your application is ready to be deployed, move it from the document root to _<NextRoot>___/NextLibrary/WOApps__.
You place the directory in __WOApps__ to ensure its privacy; if you place the __.woa__ under the document root and outside users have read access on __.wos,__ __.wod,__ or __.java__ files, they have access to the application's source.
If the application imports any images or sounds, you must leave a "sparse" copy of the application in the document root so that the client's browser can find these resources. In this case "sparse" means that the application's directory structure is reproduced in the document root, but the only files it contains are the static resources that the server must dispense to a client's browser.
__Note:__  You can't autostart an application installed in __WOApps__. It must be started from the command line as described in the section "[Run the application](RunApp.md#apple-ha2di)."

[!Table of Contents](compiled.book.md) [!Next Section](ObjCNotes.md)
