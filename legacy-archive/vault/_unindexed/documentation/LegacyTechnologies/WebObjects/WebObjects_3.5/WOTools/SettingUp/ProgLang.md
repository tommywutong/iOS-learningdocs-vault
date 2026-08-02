---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/SettingUp/ProgLang.htm
archived_at: '2026-07-15T07:57:47.019433Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](SetUpTOC.md) [!Previous Section](Assist.md)

## Choosing the Programming Language

WebObjects supports three languages:

- Java
- Objective-C
- WebScript

Java and Objective-C are _compiled_ languages. WebScript, which is based on Objective-C, is a _scripted_ language. A scripted language allows you to make changes to your application while it is running. When you use compiled code, your application runs faster, but you must build your application before running it.
Java files have the extension __.java__, Objective-C files have the extension __.m__, and WebScript files have the extension __.wos__.
The language you choose in the Wizard applies to the following files:

- The Main _component_. A component in WebObjects represents a page in your application (or possibly part of a page). When you create your project, Project Builder provides you with an initial component called Main. The component's code file implements the behavior of the component.
- The _application_ and _session_ code files. Application code contains variables and methods that affect the entire application. Session code contains variables and methods that affect a single user's session.

If, for example, you specify Java as your primary language, the Wizard will create the files __Application.java__, __Session.java__, and __Main.java__ for you. You can mix languages in a project by choosing a different language when you create other components.

[!Table of Contents](SetUpTOC.md) [!Next Section](Struct.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
