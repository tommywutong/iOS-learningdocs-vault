---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOGenerationRef/Java/eogeneration/Classes/EOOneValueEnumerationCont.html
archived_at: '2026-07-15T08:13:52.206643Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration/Art/up.gif)](../../WebObjectsTOC.md)

# EOOneValueEnumerationController

> **__Inherits from:__**
> : [EOEnumerationController](EOEnumerationController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuk3tvnvsxeylunfxw4q3pnz2he33mnrsxe): [EOTitlesController](EOTitlesController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvi2lunrsxgq3pnz2he33mnrsxe): [EOAssociationController](EOAssociationController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4q3pnz2he33mnrsxe): [EOWidgetController](EOWidgetController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvo2lem5sxiq3pnz2he33mnrsxe): EOComponentController (eoapplication) : [EOController (eoapplication)](EOController-2.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza): Object

> **__Implements:__**
> : ActionListener: (java.awt.event package): EOWidgetController.QueryWidget

> **__Package:__**
> : com.webobjects.eogeneration.client

---

## Class Description

---

Documentation for this class is forthcoming. For information on using this class, see the book _Getting Started with Direct to Java Client_.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| `ONEVALUEENUMERATIONCONTROLLER` | `widgetController` |

## Method Types

---

> **All methods**
> : [EOOneValueEnumerationController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpivhu63tfkzqwy5lfivxhk3lfojqxi2lpnzbw63tuojxwy3dfoi): [actionPerformed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpmfrxi2lpnzigk4tgn5zg2zle): [canPerformActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpmnqw4udfojtg64tnifrxi2lpnzhgc3lfmq): [deselect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpmrsxgzlmmvrxi): [isQueryWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpnfzvc5lfoj4vo2lem5sxi): [newAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpnzsxoqltonxwg2lboruw63q): [newWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpnzsxov3jmrtwk5a): [setIsQueryWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rponsxisltkf2wk4tzk5uwiz3foq): [startListeningToWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpon2gc4tujruxg5dfnzuw4z2un5lwszdhmv2a): [stopListeningToWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpon2g64cmnfzxizlonfxgovdpk5uwiz3foq)

## Constructors

---

### EOOneValueEnumerationController

`public EOOneValueEnumerationController( com.webobjects.eoapplication.EOXMLUnarchiver anEOXMLUnarchiver)`

---

## Instance Methods

---

### actionPerformed

`public void actionPerformed(java.awt.event.ActionEvent anActionEvent)`

---

### canPerformActionNamed

`public boolean canPerformActionNamed(String aString)`

---

### deselect

`public void deselect()`

---

### isQueryWidget

`public boolean isQueryWidget()`

---

### newAssociation

`protected com.webobjects.eointerface.EOAssociation newAssociation( javax.swing.JComponent aJComponent, com.webobjects.eointerface.EODisplayGroup anEODisplayGroup, String aString, com.webobjects.eointerface.EODisplayGroup anEODisplayGroup)`

---

### newWidget

`protected javax.swing.JComponent newWidget()`

---

### setIsQueryWidget

`public void setIsQueryWidget(boolean aBoolean)`

---

### startListeningToWidget

`protected void startListeningToWidget()`

---

### stopListeningToWidget

`protected void stopListeningToWidget()`

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration/Art/up.gif)](../../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
