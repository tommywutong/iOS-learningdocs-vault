---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Classes/EOTableController.html
archived_at: '2026-07-15T08:11:44.092886Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOGeneration Reference

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

# EOTableController

> **__Inherits
> from:__**
> : [EOWidgetController](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Classes/EOWidgetController.html#//apple_ref/java/cl/EOWidgetController) :
> EOComponentController (eoapplication) :
> EOController (eoapplication) :
> Object

> **__Implements:__**
> : ComponentListener
> : (java.awt.event package)
> : MouseListener (java.awt.event package)
> : EOAssociationConnector (eoapplication package)
> : EOWidgetController.TableWidget

> **__Package:__**
> : com.apple.client.eogeneration

---

## Class Description

---

Documentation for this class is forthcoming.
For information on using this class, see the book _Getting Started
with Direct to Java Client_.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| `TABLECONTROLLER` | `widgetController` |

## Method Types

---

> **All methods**
> : [EOTableController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5cu6vdbmjwgkq3pnz2he33mnrsxe)
> : [allowsMultipleSelection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5qwy3dpo5zu25lmoruxa3dfknswyzldoruw63q)
> : [componentDidBecomeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5rw63lqn5xgk3tuiruwiqtfmnxw2zkwnfzwsytmmu)
> : [componentHidden](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5rw63lqn5xgk3tujbuwizdfny)
> : [componentMoved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5rw63lqn5xgk3tujvxxmzle)
> : [componentResized](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5rw63lqn5xgk3tukjsxg2l2mvsa)
> : [componentShown](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5rw63lqn5xgk3tuknug653o)
> : [connectionWasBroken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5rw63tomvrxi2lpnzlwc42cojxwwzlo)
> : [connectionWasEstablished](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5rw63tomvrxi2lpnzlwc42fon2gcytmnfzwqzle)
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5sgs43qn5zwk)
> : [disposeIfTransient](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5sgs43qn5zwkslgkrzgc3ttnfsw45a)
> : [mouseClicked](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5ww65ltmvbwy2ldnnswi)
> : [mouseEntered](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5ww65ltmvcw45dfojswi)
> : [mouseExited](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5ww65ltmvcxq2lumvsa)
> : [mousePressed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5ww65ltmvihezltonswi)
> : [mouseReleased](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5ww65ltmvjgk3dfmfzwkza)
> : [newWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5xgk52xnfsgozlu)
> : [setAllowsMultipleSelection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5zwk5cbnrwg653tjv2wy5djobwgku3fnrswg5djn5xa)
> : [startListeningToWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5zxiylsorggs43umvxgs3thkrxvo2lem5sxi)
> : [stopListeningToWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf5zxi33qjruxg5dfnzuw4z2un5lwszdhmv2a)
> : [table](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf52gcytmmu)
> : [takeResposibilityForConnectionOfAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxw45dsn5wgyzlsf52gc23fkjsxg4dponuwe2lmnf2hsrtpojbw63tomvrxi2lpnzhwmqltonxwg2lboruw63q)

## Constructors

---

### EOTableController

`public EOTableController(
com.apple.client.eoapplication.EOXMLUnarchiver anEOXMLUnarchiver)`

---

## Instance Methods

---

### allowsMultipleSelection

`public boolean allowsMultipleSelection()`

---

### componentDidBecomeVisible

`protected void componentDidBecomeVisible()`

---

### componentHidden

`public void componentHidden(java.awt.event.ComponentEvent aComponentEvent)`

---

### componentMoved

`public void componentMoved(java.awt.event.ComponentEvent aComponentEvent)`

---

### componentResized

`public void componentResized(java.awt.event.ComponentEvent aComponentEvent)`

---

### componentShown

`public void componentShown(java.awt.event.ComponentEvent aComponentEvent)`

---

### connectionWasBroken

`protected void connectionWasBroken()`

---

### connectionWasEstablished

`protected void connectionWasEstablished()`

---

### dispose

`public void dispose()`

---

### disposeIfTransient

`protected boolean disposeIfTransient()`

---

### mouseClicked

`public void mouseClicked(java.awt.event.MouseEvent aMouseEvent)`

---

### mouseEntered

`public void mouseEntered(java.awt.event.MouseEvent aMouseEvent)`

---

### mouseExited

`public void mouseExited(java.awt.event.MouseEvent aMouseEvent)`

---

### mousePressed

`public void mousePressed(java.awt.event.MouseEvent aMouseEvent)`

---

### mouseReleased

`public void mouseReleased(java.awt.event.MouseEvent aMouseEvent)`

---

### newWidget

`protected javax.swing.JComponent newWidget()`

---

### setAllowsMultipleSelection

`public void setAllowsMultipleSelection(boolean aBoolean)`

---

### startListeningToWidget

`protected void startListeningToWidget()`

---

### stopListeningToWidget

`protected void stopListeningToWidget()`

---

### table

`public com.apple.client.eointerface.EOTable table()`

---

### takeResposibilityForConnectionOfAssociation

`public void takeResposibilityForConnectionOfAssociation(com.apple.client.eointerface.EOAssociation anEOAssociation)`

---

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

__DRAFT__
