---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOGenerationRef/Java/eogeneration.client/Classes/EOFormController.html
archived_at: '2026-07-15T08:13:50.699772Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration.client/Art/up.gif)](../../WebObjectsTOC.md)

# EOFormController

> **__Inherits from:__**
> : [EOEditingController](EOEditingController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhukzdjoruw4z2dn5xhi4tpnrwgk4q): EODocumentController : [EOAssociationController](EOAssociationController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4q3pnz2he33mnrsxe): [EOWidgetController](EOWidgetController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvo2lem5sxiq3pnz2he33mnrsxe): EOComponentController (eoapplication) : [EOController (eoapplication)](EOController-2.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza): Object

> **__Implements:__**
> : EOModalDialogController.ModalActions: (eoapplication package): EOControllerFactory.Insert: EOControllerFactory.Open: EOControllerFactory.SelectByInserting

> **__Package:__**
> : com.webobjects.eogeneration.client

---

## Class Description

---

Documentation for this class is forthcoming. For information on using this class, see the book _Getting Started with Direct to Java Client_.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| `FORMCONTROLLER` | `entityController` |

## Method Types

---

> **All methods**
> : [EOFormController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpivhum33snvbw63tuojxwy3dfoi): [canPerformActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpmnqw4udfojtg64tnifrxi2lpnzhgc3lfmq): [canRevert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpmnqw4utfozsxe5a): [canSave](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpmnqw4u3bozsq): [cancel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpmnqw4y3fnq): [defaultActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpmrswmylvnr2ecy3unfxw44y): [delete](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpmrswyzlumu): [finishSelecting](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpmzuw42ltnbjwk3dfmn2gs3th): [insert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpnfxhgzlsoq): [insertNewObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpnfxhgzlsorhgk52pmjvgky3u): [insertNewObjectWithRelationshipPathsFilled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpnfxhgzlsorhgk52pmjvgky3uk5uxi2csmvwgc5djn5xhg2djobigc5diondgs3dmmvsa): [insertWithTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpnfxhgzlsorlws5dikrqxg2y): [modalDialogShouldClose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpnvxwiylmiruwc3dpm5jwq33vnrseg3dponsq): [ok](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpn5vq): [openObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpn5ygk3spmjvgky3uk5uxi2chnrxweylmjfca): [openWithTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpn5ygk3sxnf2gqvdbonvq): [prepareToSelectByInserting](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpobzgk4dbojsvi32tmvwgky3uij4us3ttmvzhi2lom4): [provideSelectedObjectGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rpobzg65tjmrsvgzlmmvrxizlej5rguzldordwy33cmfwesra): [save](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdn5xhi4tpnrwgk4rponqxmzi)

## Constructors

---

### EOFormController

`public EOFormController( com.webobjects.eoapplication.EOXMLUnarchiver anEOXMLUnarchiver)`

Description forthcoming.

`public EOFormController()`

Description forthcoming.

---

## Instance Methods

---

### canPerformActionNamed

`public boolean canPerformActionNamed(String aString)`

Description forthcoming.

---

### canRevert

`public boolean canRevert()`

Description forthcoming.

---

### canSave

`public boolean canSave()`

Description forthcoming.

---

### cancel

`public void cancel()`

Description forthcoming.

---

### defaultActions

`protected NSArray defaultActions()`

Description forthcoming.

---

### delete

`public boolean delete()`

Description forthcoming.

---

### finishSelecting

`public void finishSelecting()`

Description forthcoming.

---

### insert

`public boolean insert()`

Description forthcoming.

---

### insertNewObject

`public boolean insertNewObject()`

Description forthcoming.

---

### insertNewObjectWithRelationshipPathsFilled

`public boolean insertNewObjectWithRelationshipPathsFilled(NSDictionary aNSDictionary)`

Description forthcoming.

---

### insertWithTask

`public boolean insertWithTask()`

Description forthcoming.

---

### modalDialogShouldClose

`public boolean modalDialogShouldClose()`

Description forthcoming.

---

### ok

`public boolean ok()`

Description forthcoming.

---

### openObjectWithGlobalID

`public void openObjectWithGlobalID(com.webobjects.eocontrol.EOGlobalID anEOGlobalID)`

Description forthcoming.

---

### openWithTask

`public boolean openWithTask()`

Description forthcoming.

---

### prepareToSelectByInserting

`public void prepareToSelectByInserting()`

Description forthcoming.

---

### provideSelectedObjectGlobalID

`public com.webobjects.eocontrol.EOGlobalID provideSelectedObjectGlobalID()`

Description forthcoming.

---

### save

`public boolean save()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration.client/Art/up.gif)](../../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
