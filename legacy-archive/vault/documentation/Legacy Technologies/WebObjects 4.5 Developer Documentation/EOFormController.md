---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Classes/EOFormController.html
archived_at: '2026-07-15T08:11:43.798650Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOGeneration Reference

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

# EOFormController

> **__Inherits
> from:__**
> : [EOEditingController](EOEditingController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhukzdjoruw4z2dn5xhi4tpnrwgk4q) :
> EODocumentController : [EOAssociationController](EOAssociationController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4q3pnz2he33mnrsxe) : [EOWidgetController](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Classes/EOWidgetController.html#//apple_ref/java/cl/EOWidgetController) :
> EOComponentController (eoapplication) :
> EOController (eoapplication) :
> Object

> **__Implements:__**
> : EOModalDialogController.ModalActions
> : (eoapplication package)
> : EOControllerFactory.Insert
> : EOControllerFactory.Open
> : EOControllerFactory.SelectByInserting

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
| `FORMCONTROLLER` | `entityController` |

## Method Types

---

> **All methods**
> : [EOFormController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpivhum33snvbw63tuojxwy3dfoi)
> : [canPerformActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpmnqw4udfojtg64tnifrxi2lpnzhgc3lfmq)
> : [canRevert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpmnqw4utfozsxe5a)
> : [canSave](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpmnqw4u3bozsq)
> : [cancel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpmnqw4y3fnq)
> : [defaultActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpmrswmylvnr2ecy3unfxw44y)
> : [delete](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpmrswyzlumu)
> : [finishSelecting](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpmzuw42ltnbjwk3dfmn2gs3th)
> : [insert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpnfxhgzlsoq)
> : [insertNewObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpnfxhgzlsorhgk52pmjvgky3u)
> : [insertNewObjectWithRelationshipPathsFilled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpnfxhgzlsorhgk52pmjvgky3uk5uxi2csmvwgc5djn5xhg2djobigc5diondgs3dmmvsa)
> : [insertWithTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpnfxhgzlsorlws5dikrqxg2y)
> : [modalDialogShouldClose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpnvxwiylmiruwc3dpm5jwq33vnrseg3dponsq)
> : [ok](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpn5vq)
> : [openObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpn5ygk3spmjvgky3uk5uxi2chnrxweylmjfca)
> : [openWithTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpn5ygk3sxnf2gqvdbonvq)
> : [prepareToSelectByInserting](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpobzgk4dbojsvi32tmvwgky3uij4us3ttmvzhi2lom4)
> : [provideSelectedObjectGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpobzg65tjmrsvgzlmmvrxizlej5rguzldordwy33cmfwesra)
> : [save](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rponqxmzi)

## Constructors

---

### EOFormController

`public EOFormController(
com.apple.client.eoapplication.EOXMLUnarchiver anEOXMLUnarchiver)`

---

## Instance Methods

---

### canPerformActionNamed

`public boolean canPerformActionNamed(String aString)`

---

### canRevert

`protected boolean canRevert()`

---

### canSave

`protected boolean canSave()`

---

### cancel

`public void cancel()`

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

### insertNewObject

`public boolean insertNewObject()`

---

### insertNewObjectWithRelationshipPathsFilled

`public boolean insertNewObjectWithRelationshipPathsFilled(NSDictionary aNSDictionary)`

---

### insertWithTask

`public boolean insertWithTask()`

---

### modalDialogShouldClose

`public boolean modalDialogShouldClose()`

---

### ok

`public boolean ok()`

---

### openObjectWithGlobalID

`public void openObjectWithGlobalID(com.apple.client.eocontrol.EOGlobalID anEOGlobalID)`

---

### openWithTask

`public boolean openWithTask()`

---

### prepareToSelectByInserting

`public void prepareToSelectByInserting()`

---

### provideSelectedObjectGlobalID

`public com.apple.client.eocontrol.EOGlobalID provideSelectedObjectGlobalID()`

---

### save

`public boolean save()`

---

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

__DRAFT__
