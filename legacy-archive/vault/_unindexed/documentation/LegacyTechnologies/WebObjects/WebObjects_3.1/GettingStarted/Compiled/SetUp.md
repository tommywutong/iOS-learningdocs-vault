---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Compiled/SetUp.html
archived_at: '2026-07-15T07:48:29.474135Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](compiled.book.md) [!Previous Section](Deciding.md)

# Set up Project Builder and WebObjects Builder

Before you can write a compiled WebObjects application, you must set up Project Builder so that it recognizes the WebObjects application project type. Before you can write an application in Java, you must tell WebObjects Builder that you want to use Java to write the component logic. You only need to perform these steps once. After that, you can create as many WebObjects applications as you need.

- Launch Project Builder by choosing it from the OpenStep Enterprise program group in the Start menu.
- Choose Tools ! Preferences to open the Preferences panel.
- Choose Bundles from the pop-up list in the Preferences panel.
- Click the Add button.
- Select _<NextRoot>___/NextDeveloper/PBBundles/WebObjectsSupport.bundle__, and click Open.
!- Exit Project Builder.

You must exit and relaunch Project Builder for the bundle to be loaded.

- Launch WebObjects Builder by choosing WebObjects Builder from the WebObjects program group in the Start menu.
- Choose Tools ! Preferences to open the Preferences panel.
- Click the Language tab.
- Choose the Java option, and then close the Preferences panel.
!

When Java is selected as the WebObjects Builder language preference, WebObjects Builder creates __.java__ files instead of __.wos__ files in each component.
__Note:__  WebObjects Builder's language preference specifies that all new components will be created using that language. If you change the language preference and then add a new component to an existing application, the new component uses a different language than the rest of the application. To prevent this from happening, always set the language preference before you create the application.

[!Table of Contents](compiled.book.md) [!Next Section](NewProject.md)
