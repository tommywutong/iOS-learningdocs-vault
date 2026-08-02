---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOApplication.framework/Java/Classes/EOApplet.html
archived_at: '2026-07-15T08:11:36.228727Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOApplication Reference

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

# EOApplet

> **__Inherits
> from:__**
> : javax.swing.JApplet

> **__Package:__**
> : com.apple.client.eoapplication

---

## Class Description

---

EOApplet is the default
Applet class embedded in WebObjects pages containing a WOJavaClientApplet
dynamic element. EOApplet's only task is
to read all the application's arguments (passed as HTML parameters)
and forward them to the initialization code in EOApplication. For maximum
flexibility, any application specific code should be implemented
in EOApplication's __finishInitialization__ method
rather than EOApplet's __init__ method.

In the controller hierarchy, the applet is represented by
an EOAppletController, which becomes a client subcontroller
of the EOApplication object.

EOApplet is used in Java Client applications
only; there is no equivalent class on the server.

## Instance Methods

---

### init

`public void init()`

Instantiates
an EOAppletController for the controller
hierarchy and invokes EOApplication's __startApplication__ using
parameters retrieved via Applet's __getParameter__.

---

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

__DRAFT__
