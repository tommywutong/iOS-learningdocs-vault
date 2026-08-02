---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Classes/EOListController.html
archived_at: '2026-07-15T08:11:43.854793Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOGeneration Reference

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

# EOListController

> **__Inherits
> from:__**
> : [EOEditingController](EOEditingController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhukzdjoruw4z2dn5xhi4tpnrwgk4q) :
> EODocumentController (eoapplication) :
> EOEntityController (eoapplication) :
> EOComponentController (eoapplication) :
> EOController (eoapplication) :
> Object

> **__Implements:__**
> : EOModalDialogController.ModalActions
> : (eoapplication package)
> : EOTableController.DefaultAction
> : EOControllerFactory.Select
> : EOControllerFactory.List

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
| `LISTCONTROLLER` | `entityController` |

## Method Types

---

> **All methods**
> : [EOListController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpivhuy2ltorbw63tuojxwy3dfoi)
> : [canPerformActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpmnqw4udfojtg64tnifrxi2lpnzhgc3lfmq)
> : [cancel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpmnqw4y3fnq)
> : [defaultAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpmrswmylvnr2ecy3unfxw4)
> : [defaultActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpmrswmylvnr2ecy3unfxw44y)
> : [delete](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpmrswyzlumu)
> : [finishSelecting](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpmzuw42ltnbjwk3dfmn2gs3th)
> : [insert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpnfxhgzlsoq)
> : [insertWithTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpnfxhgzlsorlws5dikrqxg2y)
> : [isDocumentForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpnfzui33dovwwk3tuizxxer3mn5rgc3cjiq)
> : [listObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpnruxg5cpmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4)
> : [modalDialogShouldClose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpnvxwiylmiruwc3dpm5jwq33vnrseg3dponsq)
> : [ok](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpn5vq)
> : [openWithTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpn5ygk3sxnf2gqvdbonvq)
> : [prepareToSelect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpobzgk4dbojsvi32tmvwgky3u)
> : [provideSelectedObjectGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpobzg65tjmrsvgzlmmvrxizlej5rguzldordwy33cmfwesra)
> : [provideSelectedObjectsGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpobzg65tjmrsvgzlmmvrxizlej5rguzldorzuo3dpmjqwyskeom)
> : [save](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rponqxmzi)

## Constructors

---

### EOListController

`public EOListController(
com.apple.client.eoapplication.EOXMLUnarchiver anEOXMLUnarchiver)`

---

## Instance Methods

---

### canPerformActionNamed

`public boolean canPerformActionNamed(String aString)`

---

### cancel

`public void cancel()`

---

### defaultAction

`public void defaultAction()`

---

### defaultActions

`protected NSArray defaultActions()`

---

### delete

`public boolean delete()`

---

### finishSelecting

`public void finishSelecting()`

---

### insert

`public boolean insert()`

---

### insertWithTask

`public boolean insertWithTask()`

---

### isDocumentForGlobalID

`public boolean isDocumentForGlobalID(
com.apple.client.eocontrol.EOGlobalID anEOGlobalID,
String aString)`

---

### listObjectsWithFetchSpecification

`public void listObjectsWithFetchSpecification(com.apple.client.eocontrol.EOFetchSpecification anEOFetchSpecification)`

---

### modalDialogShouldClose

`public boolean modalDialogShouldClose()`

---

### ok

`public boolean ok()`

---

### openWithTask

`public boolean openWithTask()`

---

### prepareToSelect

`public void prepareToSelect(
boolean aBoolean,
boolean aBoolean)`

---

### provideSelectedObjectGlobalID

`public com.apple.client.eocontrol.EOGlobalID provideSelectedObjectGlobalID()`

---

### provideSelectedObjectsGlobalIDs

`public NSArray provideSelectedObjectsGlobalIDs()`

---

### save

`public boolean save()`

---

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

__DRAFT__
