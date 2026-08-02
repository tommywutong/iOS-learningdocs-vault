---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOApplicationRef/Java/Classes/EOActionWidgetController.html
archived_at: '2026-07-15T08:13:42.512446Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md)

# EOActionWidgetController

> **__Inherits from:__**
> : [EOComponentController](EOComponentController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33nobxw4zloorbw63tuojxwy3dfoi): [EOController](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza): Object

> **__Implements:__**
> : EOActionWidgetController.ActionCollector

> **__Package:__**
> : com.webobjects.eoapplication

---

## Class Description

---

Documentation for this class is forthcoming. For information on using this class, see the book _Getting Started with Direct to Java Client_.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| None (abstract class) | `actionWidgetController` |

## Method Types

---

> **All methods**
> : [EOActionWidgetController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvzc6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvza): [actionWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvzc6yldoruw63sxnfsgozlu): [actionWidgetContainer](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvzc6yldoruw63sxnfsgozluinxw45dbnfxgk4q): [actionWidgetPosition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvzc6yldoruw63sxnfsgozlukbxxg2lunfxw4): [actionWidgetToSubcontrollerAreaDistance](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvzc6yldoruw63sxnfsgozlukrxvg5lcmnxw45dsn5wgyzlsifzgkykenfzxiylomnsq): [collectedActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvzc6y3pnrwgky3umvsecy3unfxw44y): [componentDidBecomeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvzc6y3pnvyg63tfnz2ei2leijswg33nmvlgs43jmjwgk): [createWidgetForActionsAndPlaceInContainer](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvzc6y3smvqxizkxnfsgozluizxxeqldoruw63ttifxgiudmmfrwksloinxw45dbnfxgk4q): [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvzc6zdjonyg643f): [disposeActionWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvzc6zdjonyg643fifrxi2lpnzlwszdhmv2a): [generateComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvzc6z3fnzsxeylumvbw63lqn5xgk3tu): [resetActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvzc64tfonsxiqldoruw63tt): [setActionWidgetContainer](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvzc643forawg5djn5xfo2lem5sxiq3pnz2gc2lomvza): [setActionWidgetPosition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvzc643forawg5djn5xfo2lem5sxiudponuxi2lpny): [subcontrollerActionsDidChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvzc643vmjrw63tuojxwy3dfojawg5djn5xhgrdjmrbwqylom5sq): [subcontrollerConnectionDidChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvzc643vmjrw63tuojxwy3dfojbw63tomvrxi2lpnzcgszcdnbqw4z3f): [updateActionWidgetEnabling](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzlwszdhmv2eg33oorzg63dmmvzc65lqmrqxizkbmn2gs33ok5uwiz3forcw4ylcnruw4zy)

## Constructors

---

### EOActionWidgetController

`public EOActionWidgetController(EOXMLUnarchiver anEOXMLUnarchiver)`

Description forthcoming.

`public EOActionWidgetController()`

Description forthcoming.

---

## Instance Methods

---

### actionWidget

`public abstract javax.swing.JComponent actionWidget()`

Description forthcoming.

---

### actionWidgetContainer

`public javax.swing.JComponent actionWidgetContainer()`

Description forthcoming.

---

### actionWidgetPosition

`public int actionWidgetPosition()`

Description forthcoming.

---

### actionWidgetToSubcontrollerAreaDistance

`protected abstract int actionWidgetToSubcontrollerAreaDistance()`

Description forthcoming.

---

### collectedActions

`public NSArray collectedActions()`

Description forthcoming.

---

### componentDidBecomeVisible

`protected void componentDidBecomeVisible()`

Description forthcoming.

---

### createWidgetForActionsAndPlaceInContainer

`protected abstract void createWidgetForActionsAndPlaceInContainer( NSArray aNSArray, javax.swing.JComponent aJComponent, int anInt)`

Description forthcoming.

---

### dispose

`public void dispose()`

Description forthcoming.

---

### disposeActionWidget

`protected abstract void disposeActionWidget()`

Description forthcoming.

---

### generateComponent

`protected void generateComponent()`

Description forthcoming.

---

### resetActions

`public void resetActions()`

Description forthcoming.

---

### setActionWidgetContainer

`public void setActionWidgetContainer(javax.swing.JComponent aJComponent)`

Description forthcoming.

---

### setActionWidgetPosition

`public void setActionWidgetPosition(int anInt)`

Description forthcoming.

---

### subcontrollerActionsDidChange

`public void subcontrollerActionsDidChange(EOController anEOController)`

Description forthcoming.

---

### subcontrollerConnectionDidChange

`public void subcontrollerConnectionDidChange(EOController anEOController)`

Description forthcoming.

---

### updateActionWidgetEnabling

`protected abstract void updateActionWidgetEnabling()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 14, 2001)

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
