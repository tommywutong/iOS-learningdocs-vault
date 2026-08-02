---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOApplication.framework/Java/Classes/EOInspectorController.html
archived_at: '2026-07-15T08:11:36.540647Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOApplication Reference

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

# EOInspectorController

> **__Inherits
> from:__**
> : [EOWindowController](EOWindowController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvo2lomrxxoq3pnz2he33mnrsxe) : [EOComponentController](EOComponentController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33nobxw4zloorbw63tuojxwy3dfoi) : [EOController](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza) :
> Object

> **__Implements:__**
> : EOComponentController.ResetUserInterface

> **__Package:__**
> : com.apple.client.eoapplication

---

## Class Description

---

Documentation for this class is forthcoming.
For information on using this class, see the book _Getting Started
with Direct to Java Client_.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| `INSPECTORCONTROLLER` | `windowController` |

## Method Types

---

> **All methods**
> : [EOInspectorController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfxhg4dfmn2g64sdn5xhi4tpnrwgk4rpivhus3ttobswg5dpojbw63tuojxwy3dfoi)
> : [activateWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfxhg4dfmn2g64sdn5xhi4tpnrwgk4rpmfrxi2lwmf2gkv3jnzsg65y)
> : [addComponentOfSubcontroller](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfxhg4dfmn2g64sdn5xhi4tpnrwgk4rpmfsgiq3pnvyg63tfnz2e6zstovrgg33oorzg63dmmvza)
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfxhg4dfmn2g64sdn5xhi4tpnrwgk4rpmruxg4dponsq)
> : [generateBorderSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfxhg4dfmn2g64sdn5xhi4tpnrwgk4rpm5sw4zlsmf2gkqtpojsgk4stnf5gk)
> : [generateComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfxhg4dfmn2g64sdn5xhi4tpnrwgk4rpm5sw4zlsmf2gkq3pnvyg63tfnz2a)
> : [inspectorIdentifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfxhg4dfmn2g64sdn5xhi4tpnrwgk4rpnfxhg4dfmn2g64sjmrsw45djmzuwk4q)
> : [integrationComponentDidBecomeInvisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfxhg4dfmn2g64sdn5xhi4tpnrwgk4rpnfxhizlhojqxi2lpnzbw63lqn5xgk3tuiruwiqtfmnxw2zkjnz3gs43jmjwgk)
> : [integrationComponentDidBecomeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfxhg4dfmn2g64sdn5xhi4tpnrwgk4rpnfxhizlhojqxi2lpnzbw63lqn5xgk3tuiruwiqtfmnxw2zkwnfzwsytmmu)
> : [resetUserInterface](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfxhg4dfmn2g64sdn5xhi4tpnrwgk4rpojsxgzlukvzwk4sjnz2gk4tgmfrwk)
> : [setInspectorIdentifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfxhg4dfmn2g64sdn5xhi4tpnrwgk4rponsxisloonygky3un5zeszdfnz2gsztjmvza)
> : [subcontrollerMinimumSizeDidChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfxhg4dfmn2g64sdn5xhi4tpnrwgk4rpon2wey3pnz2he33mnrsxetljnzuw25lnknuxuzkenfseg2dbnztwk)

## Constructors

---

### EOInspectorController

`public EOInspectorController(EOXMLUnarchiver anEOXMLUnarchiver)`

---

## Instance Methods

---

### activateWindow

`public void activateWindow()`

---

### addComponentOfSubcontroller

`protected void addComponentOfSubcontroller(EOComponentController anEOComponentController)`

---

### dispose

`public void dispose()`

---

### generateBorderSize

`protected java.awt.Dimension generateBorderSize()`

---

### generateComponent

`protected void generateComponent()`

---

### inspectorIdentifier

`public String inspectorIdentifier()`

---

### integrationComponentDidBecomeInvisible

`protected void integrationComponentDidBecomeInvisible()`

---

### integrationComponentDidBecomeVisible

`protected void integrationComponentDidBecomeVisible()`

---

### resetUserInterface

`public void resetUserInterface()`

---

### setInspectorIdentifier

`public void setInspectorIdentifier(String aString)`

---

### subcontrollerMinimumSizeDidChange

`public void subcontrollerMinimumSizeDidChange(
EOComponentController anEOComponentController,
javax.swing.JComponent aJComponent,
java.awt.Dimension aDimension)`

---

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

__DRAFT__
