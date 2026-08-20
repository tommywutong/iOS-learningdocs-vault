---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOGenerationRef/Java/eogeneration/Classes/EOActionController.html
archived_at: '2026-07-15T08:13:51.659043Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration/Art/up.gif)](../../WebObjectsTOC.md)

# EOActionController

> **__Inherits from:__**
> : [EOTitlesController](EOTitlesController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvi2lunrsxgq3pnz2he33mnrsxe): [EOAssociationController](EOAssociationController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4q3pnz2he33mnrsxe): [EOWidgetController](EOWidgetController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvo2lem5sxiq3pnz2he33mnrsxe): EOComponentController (eoapplication) : [EOController (eoapplication)](EOController-2.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza): Object

> **__Implements:__**
> : java.awt.event.ComponentListener

> **__Package:__**
> : com.webobjects.eogeneration.client

---

## Class Description

---

Documentation for this class is forthcoming. For information on using this class, see the book _Getting Started with Direct to Java Client_.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| `ACTIONCONTROLLER` | `widgetController` |

## Method Types

---

> **All methods**
> : [EOActionController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixukt2bmn2gs33oinxw45dsn5wgyzls): [actionKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixwcy3unfxw4s3fpe): [buttonPosition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixwe5luorxw4udponuxi2lpny): [canBeTransient](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixwgyloijsvi4tbnzzwszlooq): [componentDidBecomeVisible](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixwg33nobxw4zloorcgszccmvrw63lfkzuxg2lcnrsq): [componentHidden](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixwg33nobxw4zlooregszdemvxa): [componentMoved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixwg33nobxw4zloorgw65tfmq): [componentResized](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixwg33nobxw4zloorjgk43jpjswi): [componentShown](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixwg33nobxw4zloorjwq33xny): [connectionWasBroken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixwg33onzswg5djn5xfoyltijzg623fny): [connectionWasEstablished](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixwg33onzswg5djn5xfoyltivzxiylcnruxg2dfmq): [defaultActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixwizlgmf2wy5cbmn2gs33oom): [disposeAssociations](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixwi2ltobxxgzkbonzw6y3jmf2gs33oom): [disposeIfTransient](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixwi2ltobxxgzkjmzkheyloonuwk3tu): [newAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixw4zlxifzxg33dnfqxi2lpny): [newTitlesDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixw4zlxkruxi3dfoncgc5dbknxxk4tdmu): [newWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixw4zlxk5uwiz3foq): [preferredWidgetAutosizingMask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixxa4tfmzsxe4tfmrlwszdhmv2ec5lun5zws6tjnztu2yltnm): [setActionKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixxgzluifrxi2lpnzfwk6i): [setButtonPosition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixxgzluij2xi5dpnzig643joruw63q): [setTitlesEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixxgzlukruxi3dfoncw45djor4u4ylnmu): [setUsesAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixxgzlukvzwk42bmn2gs33o): [setUsesButton](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixxgzlukvzwk42cov2hi33o): [startListeningToWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixxg5dboj2ey2ltorsw42lom5kg6v3jmrtwk5a): [stopListeningToWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixxg5dpobggs43umvxgs3thkrxvo2lem5sxi): [titlesEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixxi2lunrsxgrlooruxi6komfwwk): [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixxi32torzgs3th): [usesAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixxk43fonawg5djn5xa): [usesButton](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrxi2lpnzbw63tuojxwy3dfoixxk43fonbhk5dun5xa)

## Constructors

---

### EOActionController

`public EOActionController( com.webobjects.eoapplication.EOXMLUnarchiver anEOXMLUnarchiver)`

Description forthcoming.

`public EOActionController()`

Description forthcoming.

---

## Instance Methods

---

### actionKey

`public String actionKey()`

Description forthcoming.

---

### buttonPosition

`public int buttonPosition()`

Description forthcoming.

---

### canBeTransient

`public boolean canBeTransient()`

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

### connectionWasBroken

`protected void connectionWasBroken()`

Description forthcoming.

---

### connectionWasEstablished

`protected void connectionWasEstablished()`

Description forthcoming.

---

### defaultActions

`protected NSArray defaultActions()`

Description forthcoming.

---

### disposeAssociations

`protected void disposeAssociations()`

Description forthcoming.

---

### disposeIfTransient

`protected boolean disposeIfTransient()`

Description forthcoming.

---

### newAssociation

`protected com.webobjects.eointerface.EOAssociation newAssociation( javax.swing.JComponent aJComponent, com.webobjects.eointerface.EODisplayGroup anEODisplayGroup, String aString, com.webobjects.eointerface.EODisplayGroup anEODisplayGroup)`

Description forthcoming.

---

### newTitlesDataSource

`public com.webobjects.eocontrol.EODataSource newTitlesDataSource()`

Description forthcoming.

---

### newWidget

`protected javax.swing.JComponent newWidget()`

Description forthcoming.

---

### preferredWidgetAutosizingMask

`protected int preferredWidgetAutosizingMask()`

Description forthcoming.

---

### setActionKey

`public void setActionKey(String aString)`

Description forthcoming.

---

### setButtonPosition

`public void setButtonPosition(int anInt)`

Description forthcoming.

---

### setTitlesEntityName

`public void setTitlesEntityName(String aString)`

Description forthcoming.

---

### setUsesAction

`public void setUsesAction(boolean aBoolean)`

Description forthcoming.

---

### setUsesButton

`public void setUsesButton(boolean aBoolean)`

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

### titlesEntityName

`public String titlesEntityName()`

Description forthcoming.

---

### toString

`public String toString()`

Description forthcoming.

---

### usesAction

`public boolean usesAction()`

Description forthcoming.

---

### usesButton

`public boolean usesButton()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration/Art/up.gif)](../../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
