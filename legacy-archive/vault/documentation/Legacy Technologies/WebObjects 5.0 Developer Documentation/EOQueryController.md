---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOGenerationRef/Java/eogeneration.client/Classes/EOQueryController.html
archived_at: '2026-07-15T08:13:50.779361Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration.client/Art/up.gif)](../../WebObjectsTOC.md)

# EOQueryController

> **__Inherits from:__**
> : EOEntityController (eoapplication) : EOComponentController (eoapplication) : [EOController (eoapplication)](EOController-2.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza): Object

> **__Implements:__**
> : EOWidgetController.DefaultAction: EOControllerFactory.Query: EOQueryObjectDisplay

> **__Package:__**
> : com.webobjects.eogeneration.client

---

## Class Description

---

Documentation for this class is forthcoming. For information on using this class, see the book _Getting Started with Direct to Java Client_.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| `QUERYCONTROLLER` | `entityController` |

## Method Types

---

> **All methods**
> : [EOQueryController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5cu6ulvmvzhsq3pnz2he33mnrsxe): [append](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5qxa4dfnzsa): [clear](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5rwyzlboi): [connectionWasEstablished](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5rw63tomvrxi2lpnzlwc42fon2gcytmnfzwqzle): [controllerDidLoadArchive](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcgszcmn5qwiqlsmnugs5tf): [defaultActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5sgkztbovwhiqldoruw63tt): [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5sgs43qn5zwk): [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5sw4zcfmruxi2lom4): [fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5tgk5ddnbjxazldnftgsy3boruw63q): [fetchesOnConnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5tgk5ddnbsxgt3oinxw43tfmn2a): [find](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5tgs3te): [findAll](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5tgs3teifwgy): [newQueryDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5xgk52rovsxe6kenfzxa3dbpfdxe33voa): [newQueryEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5xgk52rovsxe6kfmruxi2lom5bw63tumv4hi): [objectForOutletPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5xwe2tfmn2em33sj52xi3dforigc5di): [prepareForNewTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5yhezlqmfzgkrtpojhgk52umfzww): [qualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5yxkylmnftgszls): [queryDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5yxkzlspfcgs43qnrqxsr3sn52xa): [queryEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5yxkzlspfcwi2lunfxgoq3pnz2gk6du): [queryObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5yxkzlspfhwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33o): [setQueryDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5zwk5crovsxe6kenfzxa3dbpfdxe33voa): [setQueryEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5zwk5crovsxe6kfmruxi2lom5bw63tumv4hi)

## Constructors

---

### EOQueryController

`public EOQueryController(com.webobjects.eoapplication.EOXMLUnarchiver anEOXMLUnarchiver)`

Description forthcoming.

`public EOQueryController()`

Description forthcoming.

---

## Instance Methods

---

### append

`public void append()`

Description forthcoming.

---

### clear

`public void clear()`

Description forthcoming.

---

### connectionWasEstablished

`protected void connectionWasEstablished()`

Description forthcoming.

---

### controllerDidLoadArchive

`protected void controllerDidLoadArchive(NSDictionary aNSDictionary)`

Description forthcoming.

---

### __defaultAction__

`public void defaultAction()`

Description forthcoming.

---

### defaultActions

`protected NSArray defaultActions()`

Description forthcoming.

---

### dispose

`public void dispose()`

Description forthcoming.

---

### endEditing

`public boolean endEditing()`

Description forthcoming.

---

### fetchSpecification

`public com.webobjects.eocontrol.EOFetchSpecification fetchSpecification()`

Description forthcoming.

---

### fetchesOnConnect

`public boolean fetchesOnConnect()`

Description forthcoming.

---

### find

`public void find()`

Description forthcoming.

---

### findAll

`public void findAll()`

Description forthcoming.

---

### newQueryDisplayGroup

`public com.webobjects.eointerface.EODisplayGroup newQueryDisplayGroup()`

Description forthcoming.

---

### newQueryEditingContext

`public com.webobjects.eocontrol.EOEditingContext newQueryEditingContext()`

Description forthcoming.

---

### objectForOutletPath

`public Object objectForOutletPath( com.webobjects.eoapplication.EOArchive anEOArchive, String aString)`

Description forthcoming.

---

### prepareForNewTask

`public void prepareForNewTask(boolean aBoolean)`

Description forthcoming.

---

### qualifier

`public com.webobjects.eocontrol.EOQualifier qualifier()`

Description forthcoming.

---

### queryDisplayGroup

`public com.webobjects.eointerface.EODisplayGroup queryDisplayGroup()`

Description forthcoming.

---

### queryEditingContext

`public com.webobjects.eocontrol.EOEditingContext queryEditingContext()`

Description forthcoming.

---

### queryObjectsWithFetchSpecification

`public void queryObjectsWithFetchSpecification(com.webobjects.eocontrol.EOFetchSpecification anEOFetchSpecification)`

Description forthcoming.

---

### setQueryDisplayGroup

`public void setQueryDisplayGroup(com.webobjects.eointerface.EODisplayGroup anEODisplayGroup)`

Description forthcoming.

---

### setQueryEditingContext

`public void setQueryEditingContext(com.webobjects.eocontrol.EOEditingContext anEOEditingContext)`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration.client/Art/up.gif)](../../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
