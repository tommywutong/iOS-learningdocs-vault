---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOGenerationRef/Java/eogeneration.client/Classes/EOListController.html
archived_at: '2026-07-15T08:13:50.743762Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration.client/Art/up.gif)](../../WebObjectsTOC.md)

# EOListController

> **__Inherits from:__**
> : [EOEditingController](EOEditingController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhukzdjoruw4z2dn5xhi4tpnrwgk4q): EODocumentController (eoapplication) : EOEntityController (eoapplication) : EOComponentController (eoapplication) : [EOController (eoapplication)](EOController-2.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza): Object

> **__Implements:__**
> : EOModalDialogController.ModalActions: (eoapplication package): EOTableController.DefaultAction: EOControllerFactory.Select: EOControllerFactory.List

> **__Package:__**
> : com.webobjects.eogeneration.client

---

## Class Description

---

Documentation for this class is forthcoming. For information on using this class, see the book _Getting Started with Direct to Java Client_.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| `LISTCONTROLLER` | `entityController` |

## Method Types

---

> **All methods**
> : [EOListController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpivhuy2ltorbw63tuojxwy3dfoi): [canPerformActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpmnqw4udfojtg64tnifrxi2lpnzhgc3lfmq): [cancel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpmnqw4y3fnq): [defaultAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpmrswmylvnr2ecy3unfxw4): [defaultActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpmrswmylvnr2ecy3unfxw44y): [delete](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpmrswyzlumu): [finishSelecting](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpmzuw42ltnbjwk3dfmn2gs3th): [insert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpnfxhgzlsoq): [insertWithTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpnfxhgzlsorlws5dikrqxg2y): [isDocumentForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpnfzui33dovwwk3tuizxxer3mn5rgc3cjiq): [listObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpnruxg5cpmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4): [modalDialogShouldClose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpnvxwiylmiruwc3dpm5jwq33vnrseg3dponsq): [ok](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpn5vq): [openWithTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpn5ygk3sxnf2gqvdbonvq): [prepareToSelect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpobzgk4dbojsvi32tmvwgky3u): [provideSelectedObjectGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpobzg65tjmrsvgzlmmvrxizlej5rguzldordwy33cmfwesra): [provideSelectedObjectsGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rpobzg65tjmrsvgzlmmvrxizlej5rguzldorzuo3dpmjqwyskeom): [save](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjruxg5cdn5xhi4tpnrwgk4rponqxmzi)

## Constructors

---

### EOListController

`public EOListController( com.webobjects.eoapplication.EOXMLUnarchiver anEOXMLUnarchiver)`

Description forthcoming.

`public EOListController()`

Description forthcoming.

---

## Instance Methods

---

### canPerformActionNamed

`public boolean canPerformActionNamed(String aString)`

Description forthcoming.

---

### cancel

`public void cancel()`

Description forthcoming.

---

### defaultAction

`public void defaultAction()`

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

### insertWithTask

`public boolean insertWithTask()`

Description forthcoming.

---

### isDocumentForGlobalID

`public boolean isDocumentForGlobalID( com.webobjects.eocontrol.EOGlobalID anEOGlobalID, String aString)`

Description forthcoming.

---

### listObjectsWithFetchSpecification

`public void listObjectsWithFetchSpecification(com.webobjects.eocontrol.EOFetchSpecification anEOFetchSpecification)`

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

### openWithTask

`public boolean openWithTask()`

Description forthcoming.

---

### prepareToSelect

`public void prepareToSelect( boolean aBoolean, boolean aBoolean)`

Description forthcoming.

---

### provideSelectedObjectGlobalID

`public com.webobjects.eocontrol.EOGlobalID provideSelectedObjectGlobalID()`

Description forthcoming.

---

### provideSelectedObjectsGlobalIDs

`public NSArray provideSelectedObjectsGlobalIDs()`

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
