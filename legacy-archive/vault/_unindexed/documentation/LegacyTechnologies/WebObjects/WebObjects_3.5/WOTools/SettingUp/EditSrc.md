---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/SettingUp/EditSrc.htm
archived_at: '2026-07-15T07:57:39.974482Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](SetUpTOC.md) [!Previous Section](Existing.md)

# Editing Your Project's Source Files

Every component in your project has a code file whose name is the name of the component followed by the appropriate extension (__.java__ for Java, __.m__ for Objective-C, and __.wos__ for WebScript). Your project may use different languages for different components.
Each component's code specifies the component's behavior. Each component is actually a subclass of the class WOComponent (or WebComponent, in Java). This class has standard methods (such as __awake__ and __init__) that you may want to override (see [_WebObjects Developer's Guid_](../../DevGuide/DevGuideTOC.md)e for more information on these methods). You can also write your own methods and bind them to dynamic elements in your component (see ["Working With Dynamic Elements"](../DynamicElements/DynElTOC.md#apple-gqytc), as well as the [_Dynamic Elements Reference_](../../Reference/DynamicElements/DynamicElementsTOC.md), for information on binding dynamic elements).

In addition to the component's code, each project has an _application code file_ (__Application.java__, __Application.m__, or __Application.wos__) and a _session code file_ (__Session.java__, __Session.m__, or __Session.wos__). These files implement
When you first create your project using the Wizard, you specify the language you want to use (see ["Choosing the Programming Language"](ProgLang.md#apple-he2tsna)). This language applies to the application and session code, as well as to the code for your initial component, Main. Other components may be written in different languages.

The location of your code in the project suitcases varies somewhat depending on the language used:

- If you use Java or Objective-C, all code files appear in the Classes suitcase. On disk, they live at the top level of the project directory.
- If you use WebScript, the __Application.wos__ and __Session.wos__ files appear in the Resources suitcase. On disk, they live a the top level of the project directory. The component scripts (_ComponentName_.__wos__) appear in the component (_ComponentName___.wo__) in the project and on disk.

To edit your code, select the file name in the project browser. The code appears in the bottom pane of the browser.!
To save changes in your code, choose File !Save.
__Note:__ WebObjects Builder gets information from Project Builder about variables and methods in your code. If you add or delete a variable or method, WebObjects Builder doesn't get the updated information until you save the file.

[!Table of Contents](SetUpTOC.md) [!Next Section](DecFiles.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
