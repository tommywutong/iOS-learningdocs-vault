---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOGenerationRef/Java/eogeneration/Classes/EOEditingController.html
archived_at: '2026-07-15T08:13:51.941583Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration/Art/up.gif)](../../WebObjectsTOC.md)

# EOEditingController

> **__Inherits from:__**
> : EODocumentController (eoapplication) : EOEntityController (eoapplication) : EOComponentController (eoapplication) : [EOController (eoapplication)](EOController-2.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza): Object

> **__Package:__**
> : com.webobjects.eogeneration.client

---

## Class Description

---

Documentation for this class is forthcoming. For information on using this class, see the book _Getting Started with Direct to Java Client_.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| None (abstract class) | None |

## Method Types

---

> **All methods**
> : [EOEditingController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6rkpivsgs5djnztug33oorzg63dmmvza): [canPerformActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6y3bnzigk4tgn5zg2qldoruw63somfwwkza): [connectionWasBroken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6y3pnzxgky3unfxw4v3bonbhe33lmvxa): [connectionWasEstablished](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6y3pnzxgky3unfxw4v3boncxg5dbmjwgs43imvsa): [defaultActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6zdfmzqxk3duifrxi2lpnzzq): [delete](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6zdfnrsxizi): [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6zdjonyg643f): [disposeIfTransient](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6zdjonyg643fjftfi4tbnzzwszlooq): [entityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6zlooruxi6komfwwk): [fetchesOnConnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6ztforrwqzltj5xeg33onzswg5a): [insert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc62loonsxe5a): [mandatoryRelationshipPaths](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc63lbnzsgc5dpoj4vezlmmf2gs33oonugs4cqmf2gq4y): [masterDetailAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc63lbon2gk4semv2gc2lmifzxg33dnfqxi2lpny): [newDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc63tfo5cgs43qnrqxsr3sn52xa): [openWithTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc633qmvxfo2lunbkgc43l): [relationshipPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc64tfnrqxi2lpnzzwq2lqkbqxi2a): [setEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc643forcw45djor4u4ylnmu): [setMandatoryRelationshipPaths](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc643forgwc3temf2g64tzkjswyylunfxw443infyfaylunbzq): [setMasterDetailAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc643forgwc43umvzeizlumfuwyqltonxwg2lboruw63q): [setRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc643forjgk3dboruw63ttnbuxaudborua)

## Constructors

---

### EOEditingController

`public EOEditingController( com.webobjects.eoapplication.EOXMLUnarchiver anEOXMLUnarchiver)`

Description forthcoming.

`public EOEditingController()`

Description forthcoming.

---

## Instance Methods

---

### canPerformActionNamed

`public boolean canPerformActionNamed(String aString)`

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

### delete

`public boolean delete()`

Description forthcoming.

---

### dispose

`public void dispose()`

Description forthcoming.

---

### disposeIfTransient

`protected boolean disposeIfTransient()`

Description forthcoming.

---

### entityName

`public String entityName()`

Description forthcoming.

---

### fetchesOnConnect

`public boolean fetchesOnConnect()`

Description forthcoming.

---

### insert

`public boolean insert()`

Description forthcoming.

---

### mandatoryRelationshipPaths

`protected NSArray mandatoryRelationshipPaths()`

Description forthcoming.

---

### masterDetailAssociation

`public com.webobjects.eointerface.EOMasterDetailAssociation masterDetailAssociation()`

Description forthcoming.

---

### newDisplayGroup

`public com.webobjects.eointerface.EODisplayGroup newDisplayGroup()`

Description forthcoming.

---

### openWithTask

`public boolean openWithTask()`

Description forthcoming.

---

### relationshipPath

`public String relationshipPath()`

Description forthcoming.

---

### setEntityName

`public void setEntityName(String aString)`

Description forthcoming.

---

### setMandatoryRelationshipPaths

`public void setMandatoryRelationshipPaths(NSArray aNSArray)`

Description forthcoming.

---

### setMasterDetailAssociation

`public void setMasterDetailAssociation( com.webobjects.eointerface.EOMasterDetailAssociation anEOMasterDetailAssociation)`

Description forthcoming.

---

### setRelationshipPath

`public void setRelationshipPath(String aString)`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration/Art/up.gif)](../../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
