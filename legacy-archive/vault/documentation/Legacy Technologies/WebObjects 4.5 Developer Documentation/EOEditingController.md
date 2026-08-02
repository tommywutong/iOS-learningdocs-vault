---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Classes/EOEditingController.html
archived_at: '2026-07-15T08:11:43.749580Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOGeneration Reference

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

# EOEditingController

> **__Inherits
> from:__**
> : EODocumentController (eoapplication)
> :
> EOEntityController (eoapplication) :
> EOComponentController (eoapplication) :
> EOController (eoapplication) :
> Object

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
| None (abstract class) | None |

## Method Types

---

> **All methods**
> : [EOEditingController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6rkpivsgs5djnztug33oorzg63dmmvza)
> : [canPerformActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6y3bnzigk4tgn5zg2qldoruw63somfwwkza)
> : [connectionWasBroken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6y3pnzxgky3unfxw4v3bonbhe33lmvxa)
> : [connectionWasEstablished](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6y3pnzxgky3unfxw4v3boncxg5dbmjwgs43imvsa)
> : [defaultActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6zdfmzqxk3duifrxi2lpnzzq)
> : [delete](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6zdfnrsxizi)
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6zdjonyg643f)
> : [disposeIfTransient](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6zdjonyg643fjftfi4tbnzzwszlooq)
> : [entityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6zlooruxi6komfwwk)
> : [fetchesOnConnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc6ztforrwqzltj5xeg33onzswg5a)
> : [insert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc62loonsxe5a)
> : [mandatoryRelationshipPaths](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc63lbnzsgc5dpoj4vezlmmf2gs33oonugs4cqmf2gq4y)
> : [masterDetailAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc63lbon2gk4semv2gc2lmifzxg33dnfqxi2lpny)
> : [newDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc63tfo5cgs43qnrqxsr3sn52xa)
> : [openWithTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc633qmvxfo2lunbkgc43l)
> : [relationshipPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc64tfnrqxi2lpnzzwq2lqkbqxi2a)
> : [setEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc643forcw45djor4u4ylnmu)
> : [setMandatoryRelationshipPaths](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc643forgwc3temf2g64tzkjswyylunfxw443infyfaylunbzq)
> : [setMasterDetailAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc643forgwc43umvzeizlumfuwyqltonxwg2lboruw63q)
> : [setRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorzg63dmmvzc643forjgk3dboruw63ttnbuxaudborua)

## Constructors

---

### EOEditingController

`public EOEditingController(
com.apple.client.eoapplication.EOXMLUnarchiver anEOXMLUnarchiver)`

---

## Instance Methods

---

### canPerformActionNamed

`public boolean canPerformActionNamed(String aString)`

---

### connectionWasBroken

`protected void connectionWasBroken()`

---

### connectionWasEstablished

`protected void connectionWasEstablished()`

---

### defaultActions

`protected NSArray defaultActions()`

---

### delete

`public boolean delete()`

---

### dispose

`public void dispose()`

---

### disposeIfTransient

`protected boolean disposeIfTransient()`

---

### entityName

`public String entityName()`

---

### fetchesOnConnect

`public boolean fetchesOnConnect()`

---

### insert

`public boolean insert()`

---

### mandatoryRelationshipPaths

`protected NSArray mandatoryRelationshipPaths()`

---

### masterDetailAssociation

`public com.apple.client.eointerface.EOMasterDetailAssociation masterDetailAssociation()`

---

### newDisplayGroup

`public com.apple.client.eointerface.EODisplayGroup newDisplayGroup()`

---

### openWithTask

`public boolean openWithTask()`

---

### relationshipPath

`public String relationshipPath()`

---

### setEntityName

`public void setEntityName(String aString)`

---

### setMandatoryRelationshipPaths

`public void setMandatoryRelationshipPaths(NSArray aNSArray)`

---

### setMasterDetailAssociation

`public void setMasterDetailAssociation(com.apple.client.eointerface.EOMasterDetailAssociation anEOMasterDetailAssociation)`

---

### setRelationshipPath

`public void setRelationshipPath(String aString)`

---

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

__DRAFT__
