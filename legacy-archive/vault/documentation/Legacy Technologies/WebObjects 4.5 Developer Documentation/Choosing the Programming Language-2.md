---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.4.html
archived_at: '2026-07-15T08:10:35.086923Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Creating%20WebObjects%20Application%20Projects.md) [!](Choosing%20Assistance.md) [!](The%20Structure%20of%20a%20WebObjects%20Application%20Project.md)

---

#   Choosing the Programming Language

WebObjects supports three languages:

- 

  Java
- 

  Objective-C
- 

  WebScript

Java and Objective-C are _compiled_
languages. WebScript, which is based on Objective-C, is a _scripted_
language. A scripted language allows you to make changes to your application without compiling. When you use compiled code, your application runs faster, but you must continually build your application before running it.

Java files have the extension __.java__
, Objective-C files have the extension __.m__
, and WebScript files have the extension __.wos__
.

The language you choose in the Wizard applies to the following files:

- 

  The Main _component_
  . A component in WebObjects represents a page in your application (or possibly part of a page). When you create your project, Project Builder provides you with an initial component called Main. The component's code file implements the behavior of the component.
- 

  The _application_
  and _session_
  code files. Application code contains variables and methods that affect the entire application. Session code contains variables and methods that affect a single user's session.

  If, for example, you specify Java as your primary language, the Wizard will create the files __Application.java__
  , __Session.java__
  , and __Main.java__
  for you. You can mix languages in a project by choosing a different language when you create individual components.

  ---

  © 1999 Apple Computer, Inc. – (Last Updated July 27 99)

  [!](Creating%20WebObjects%20Application%20Projects.md) [!](Choosing%20Assistance.md) [!](The%20Structure%20of%20a%20WebObjects%20Application%20Project.md)

  Copyright © 2016 Apple Inc. All rights reserved.

  - [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
  - [Privacy Policy](http://www.apple.com/privacy/)
