---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Intro/AppExecutables.html
archived_at: '2026-07-15T07:47:07.886450Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Start.book.md) [!Previous Section](Components.md)

## Application Executables

Applications that don't contain compiled code use __WODefaultApp__ (located in __NextLibrary/Executables__). This application uses the resources you provide to respond to user requests.
If you incorporate compiled code into your WebObjects application, you must also provide the application executable. You must write a __main()__ function, compile the source code, and link it with the WebObjects framework. You place your executable in __NextLibrary/WOApps__. See "Creating a Compiled Application" in the book _Getting Started With WebObjects_ for more information.
__Note:__  If you place the application executable in __NextLibrary/WOApps__, you can also place the __.woa__ there as well. For more information, see the description of __WOApps__ in "[Where Things Go](WhereThingsGo.md#apple-g42ds)."

[!Table of Contents](Start.book.md) [!Next Section](ConnectingAppToWeb.md)
