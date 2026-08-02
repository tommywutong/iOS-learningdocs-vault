---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOApplication.framework/Java/Classes/EOAppletController.html
archived_at: '2026-07-15T08:11:36.243453Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOApplication Reference

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

# EOAppletController

> **__Inherits
> from:__**
> : [EOComponentController](EOComponentController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33nobxw4zloorbw63tuojxwy3dfoi) : [EOController](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza) : Object

> **__Package:__**
> : com.apple.client.eoapplication

---

## Class Description

---

This class represents an EOApplet as
a controller in the controller hierarchy. When the application is running
as an applet, this controller is the direct descendent of the EOApplication
in the controller hierarchy. It performs the analogous function
as a EOWindowController when the application
is running as a Java application.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| None (abstract class) | None |

## Method Types

---

> **All methods**
> : [EOAppletController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3dforbw63tuojxwy3dfoixukt2bobygyzluinxw45dsn5wgyzls)
> : [applet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3dforbw63tuojxwy3dfoixwc4dqnrsxi)
> : [setApplet](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3dforbw63tuojxwy3dfoixxgzluifyha3dfoq)
> : [setVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3dforbw63tuojxwy3dfoixxgzlukzuxg2lcnrsq)
> : [showInSupercontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3dforbw63tuojxwy3dfoixxg2dpo5ew4u3vobsxey3pnz2he33mnrsxe)

## Constructors

---

### EOAppletController

`public EOAppletController(EOApplet applet)`

Creates an
applet controller for _applet_.

---

## Instance Methods

---

### applet

`public EOApplet applet()`

Returns the
receiver's applet.

---

### setApplet

`protected void setApplet(EOApplet applet)`

Sets the
receiver's applet to _applet_.

---

### setVisible

`public void setVisible(boolean flag)`

Sets the
visibility of the applet according to _flag_.
Since applets can not be made invisible, this method does nothing
if _visible_ is `false`.

---

### showInSupercontroller

`public boolean showInSupercontroller()`

Properly
integrates the content of the applet (usually a component of a EOInterfaceController).

---

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

__DRAFT__
