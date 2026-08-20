---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/HowWOWorks/ScriptedClasses.html
archived_at: '2026-07-15T07:46:56.708056Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.mif.book.md)
[!Previous Section](StartingRRLoop.md)

# __A Note on Scripted Classes__

The following sections discuss in detail the roles performed by the application (WOApplication), session (WOSession) and component (WOComponent) objects in request handling. In WebObjects, the behavior of these objects can be scripted or compiled. In the latter case, you would might create a subclass of, say, WOSession, and then implement the request-handling methods. Scripted behavior, however, is more common in WebObjects than compiled behavior. In a scripted application, you write WebScript code (or another supported scripting language) in an application's __Application.wos__ and __Session.wos__ files, and in each component's ".wos" files. At run time, the application uses a special subclass of WOApplication and WOSession---and a unique WOComponent subclass for each component---to generate instances. It makes the code it finds in the associated ".wos" files the implementation code of these subclasses.

For more on scripting, including the script files allowed in a WebObjects application, see the chapter "[Using WebScript](../WebScript/WebScript.mif.book.md)."

[!Table of Contents](HowWOWorks.mif.book.md)
[!Next Section](PhasesRRLoop.md)
