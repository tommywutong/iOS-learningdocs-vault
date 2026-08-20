---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Classes/EOOneValueEnumerationCntr.html
archived_at: '2026-07-15T08:11:43.892338Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOGeneration Reference

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

# EOOneValueEnumerationController

> **__Inherits
> from:__**
> : [EOEnumerationController](EOEnumerationController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuk3tvnvsxeylunfxw4q3pnz2he33mnrsxe) : [EOTitlesController](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Classes/EOTitlesController.html#//apple_ref/java/cl/EOTitlesController) : [EOAssociationController](EOAssociationController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4q3pnz2he33mnrsxe) : [EOWidgetController](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Classes/EOWidgetController.html#//apple_ref/java/cl/EOWidgetController) :
> EOComponentController (eoapplication) :
> EOController (eoapplication) :
> Object

> **__Implements:__**
> : ActionListener
> : (java.awt.event package)
> : EOWidgetController.QueryWidget

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
| `ONEVALUEENUMERATIONCONTROLLER` | `widgetController` |

## Method Types

---

> **All methods**
> : [EOOneValueEnumerationController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpivhu63tfkzqwy5lfivxhk3lfojqxi2lpnzbw63tuojxwy3dfoi)
> : [actionPerformed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpmfrxi2lpnzigk4tgn5zg2zle)
> : [canPerformActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpmnqw4udfojtg64tnifrxi2lpnzhgc3lfmq)
> : [deselect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpmrsxgzlmmvrxi)
> : [isQueryWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpnfzvc5lfoj4vo2lem5sxi)
> : [newAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpnzsxoqltonxwg2lboruw63q)
> : [newWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpnzsxov3jmrtwk5a)
> : [setIsQueryWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rponsxisltkf2wk4tzk5uwiz3foq)
> : [startListeningToWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpon2gc4tujruxg5dfnzuw4z2un5lwszdhmv2a)
> : [stopListeningToWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpj5xgkvtbnr2wkrloovwwk4tboruw63sdn5xhi4tpnrwgk4rpon2g64cmnfzxizlonfxgovdpk5uwiz3foq)

## Constructors

---

### EOOneValueEnumerationController

`public EOOneValueEnumerationController(
com.apple.client.eoapplication.EOXMLUnarchiver anEOXMLUnarchiver)`

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

`protected com.apple.client.eointerface.EOAssociation newAssociation(
javax.swing.JComponent aJComponent,
com.apple.client.eointerface.EODisplayGroup anEODisplayGroup,
String aString,
com.apple.client.eointerface.EODisplayGroup anEODisplayGroup)`

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

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

__DRAFT__
