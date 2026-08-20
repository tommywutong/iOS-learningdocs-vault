---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOApplicationRef/Java/Classes/EOApplet.html
archived_at: '2026-07-15T08:13:42.548527Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# EOApplet

> **__Inherits from:__**
> : javax.swing.JApplet

> **__Package:__**
> : com.webobjects.eoapplication

---

## Class Description

---

EOApplet is the default Applet class embedded in WebObjects pages containing a WOJavaClientApplet dynamic element. EOApplet's only task is to read all the application's arguments (passed as HTML parameters) and forward them to the initialization code in EOApplication. For maximum flexibility, any application specific code should be implemented in EOApplication's __finishInitialization__ method rather than EOApplet's __init__ method.

In the controller hierarchy, the applet is represented by an EOAppletController, which becomes a client subcontroller of the EOApplication object.

EOApplet is used in Java Client applications only; there is no equivalent class on the server.

## Constructors

---

### EOApplet

`public EOApplet()`

Description forthcoming.

---

## Instance Methods

---

### __destroy__

`public void destroy()`

Description forthcoming.

---

### init

`public void init()`

Instantiates an EOAppletController for the controller hierarchy and invokes EOApplication's __startApplication__ using parameters retrieved via Applet's __getParameter__.

---

© 2001 Apple Computer, Inc. (Last Published April 14, 2001)

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
