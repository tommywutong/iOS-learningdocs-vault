---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOGenerationRef/Java/eogeneration.client/Classes/EOTableController.html
archived_at: '2026-07-15T08:13:50.948380Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration.client/Art/up.gif)](../../WebObjectsTOC.md)

# EOTableController

> **__Inherits from:__**
> : [EOAssociationController](EOAssociationController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4q3pnz2he33mnrsxe) : [EOController (eoapplication)](EOController-2.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza): Object

> **__Implements:__**
> : ComponentListener: (java.awt.event package): MouseListener (java.awt.event package): EOWidgetController.TableWidget

> **__Package:__**
> : com.webobjects.eogeneration.client

---

## Class Description

---

Documentation for this class is forthcoming. For information on using this class, see the book _Getting Started with Direct to Java Client_.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| `TABLECONTROLLER` | `widgetController` |

## Method Types

---

> **All methods**
> : [EOTableController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5cu6vdbmjwgkq3pnz2he33mnrsxe): [allowsMultipleSelection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5qwy3dpo5zu25lmoruxa3dfknswyzldoruw63q): [componentDidBecomeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5rw63lqn5xgk3tuiruwiqtfmnxw2zkwnfzwsytmmu): [componentHidden](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5rw63lqn5xgk3tujbuwizdfny): [componentMoved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5rw63lqn5xgk3tujvxxmzle): [componentResized](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5rw63lqn5xgk3tukjsxg2l2mvsa): [componentShown](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5rw63lqn5xgk3tuknug653o): [mouseClicked](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5ww65ltmvbwy2ldnnswi): [mouseEntered](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5ww65ltmvcw45dfojswi): [mouseExited](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5ww65ltmvcxq2lumvsa): [mousePressed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5ww65ltmvihezltonswi): [mouseReleased](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5ww65ltmvjgk3dfmfzwkza): [newWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5xgk52xnfsgozlu): [setAllowsMultipleSelection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5zwk5cbnrwg653tjv2wy5djobwgku3fnrswg5djn5xa): [startListeningToWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5zxiylsorggs43umvxgs3thkrxvo2lem5sxi): [stopListeningToWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5zxi33qjruxg5dfnzuw4z2un5lwszdhmv2a): [table](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf52gcytmmu)

## Constructors

---

### EOTableController

`public EOTableController( com.webobjects.eoapplication.EOXMLUnarchiver anEOXMLUnarchiver)`

Description forthcoming.

`public EOTableController()`

Description forthcoming.

---

## Instance Methods

---

### allowsMultipleSelection

`public boolean allowsMultipleSelection()`

Description forthcoming.

---

### componentDidBecomeVisible

`protected void componentDidBecomeVisible()`

Description forthcoming.

---

### componentHidden

`public void componentHidden(java.awt.event.ComponentEvent aComponentEvent)`

Description forthcoming.

---

### componentMoved

`public void componentMoved(java.awt.event.ComponentEvent aComponentEvent)`

Description forthcoming.

---

### componentResized

`public void componentResized(java.awt.event.ComponentEvent aComponentEvent)`

Description forthcoming.

---

### componentShown

`public void componentShown(java.awt.event.ComponentEvent aComponentEvent)`

Description forthcoming.

---

### mouseClicked

`public void mouseClicked(java.awt.event.MouseEvent aMouseEvent)`

Description forthcoming.

---

### mouseEntered

`public void mouseEntered(java.awt.event.MouseEvent aMouseEvent)`

Description forthcoming.

---

### mouseExited

`public void mouseExited(java.awt.event.MouseEvent aMouseEvent)`

Description forthcoming.

---

### mousePressed

`public void mousePressed(java.awt.event.MouseEvent aMouseEvent)`

Description forthcoming.

---

### mouseReleased

`public void mouseReleased(java.awt.event.MouseEvent aMouseEvent)`

Description forthcoming.

---

### __newAssociation__

`protected com.webobjects.eointerface.EOAssociation newAssociation( javax.swing.JComponent aJComponent, com.webobjects.eointerface.EODisplayGroup aDisplayGroup, String aString com.webobjects.eointerface.EODisplayGroup anotherDisplayGroup)`

Description forthcoming.

---

### newWidget

`protected javax.swing.JComponent newWidget()`

Description forthcoming.

---

### setAllowsMultipleSelection

`public void setAllowsMultipleSelection(boolean aBoolean)`

Description forthcoming.

---

### __setSortsByColumnOrder__

`public void setSortsByColumnOrder(boolean flag)`

Description forthcoming.

---

### __sortsByColumnOrder__

`public boolean sortsByColumnOrder()`

Description forthcoming.

---

### startListeningToWidget

`protected void startListeningToWidget()`

Description forthcoming.

---

### stopListeningToWidget

`protected void stopListeningToWidget()`

Description forthcoming.

---

### table

`public com.webobjects.eointerface.swing.EOTable table()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration.client/Art/up.gif)](../../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
