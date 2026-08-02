---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Classes/EOQueryController.html
archived_at: '2026-07-15T08:11:43.913531Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOGeneration Reference

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

# EOQueryController

> **__Inherits
> from:__**
> : EOEntityController (eoapplication)
> :
> EOComponentController (eoapplication) :
> EOController (eoapplication) :
> Object

> **__Implements:__**
> : EOControllerFactory.Query
> : EOQueryController.QueryObjectDisplay

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
| `QUERYCONTROLLER` | `entityController` |

## Method Types

---

> **All methods**
> : [EOQueryController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5cu6ulvmvzhsq3pnz2he33mnrsxe)
> : [append](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5qxa4dfnzsa)
> : [clear](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5rwyzlboi)
> : [connectionWasEstablished](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5rw63tomvrxi2lpnzlwc42fon2gcytmnfzwqzle)
> : [controllerDidLoadArchive](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcgszcmn5qwiqlsmnugs5tf)
> : [defaultActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5sgkztbovwhiqldoruw63tt)
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5sgs43qn5zwk)
> : [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5sw4zcfmruxi2lom4)
> : [fetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5tgk5ddnbjxazldnftgsy3boruw63q)
> : [fetchesOnConnect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5tgk5ddnbsxgt3oinxw43tfmn2a)
> : [find](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5tgs3te)
> : [findAll](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5tgs3teifwgy)
> : [newQueryDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5xgk52rovsxe6kenfzxa3dbpfdxe33voa)
> : [newQueryEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5xgk52rovsxe6kfmruxi2lom5bw63tumv4hi)
> : [objectForOutletPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5xwe2tfmn2em33sj52xi3dforigc5di)
> : [prepareForNewTask](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5yhezlqmfzgkrtpojhgk52umfzww)
> : [qualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5yxkylmnftgszls)
> : [queryDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5yxkzlspfcgs43qnrqxsr3sn52xa)
> : [queryEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5yxkzlspfcwi2lunfxgoq3pnz2gk6du)
> : [queryObjectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5yxkzlspfhwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33o)
> : [setQueryDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5zwk5crovsxe6kenfzxa3dbpfdxe33voa)
> : [setQueryEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wk4tzinxw45dsn5wgyzlsf5zwk5crovsxe6kfmruxi2lom5bw63tumv4hi)

## Constructors

---

### EOQueryController

`public EOQueryController(com.apple.client.eoapplication.EOXMLUnarchiver anEOXMLUnarchiver)`

---

## Instance Methods

---

### append

`public void append()`

---

### clear

`public void clear()`

---

### connectionWasEstablished

`protected void connectionWasEstablished()`

---

### controllerDidLoadArchive

`protected void controllerDidLoadArchive(NSDictionary aNSDictionary)`

---

### defaultActions

`protected NSArray defaultActions()`

---

### dispose

`public void dispose()`

---

### endEditing

`public boolean endEditing()`

---

### fetchSpecification

`protected com.apple.client.eocontrol.EOFetchSpecification fetchSpecification()`

---

### fetchesOnConnect

`public boolean fetchesOnConnect()`

---

### find

`public void find()`

---

### findAll

`public void findAll()`

---

### newQueryDisplayGroup

`public com.apple.client.eointerface.EODisplayGroup newQueryDisplayGroup()`

---

### newQueryEditingContext

`public com.apple.client.eocontrol.EOEditingContext newQueryEditingContext()`

---

### objectForOutletPath

`public Object objectForOutletPath(
com.apple.client.eoapplication.EOArchive anEOArchive,
String aString)`

---

### prepareForNewTask

`public void prepareForNewTask(boolean aBoolean)`

---

### qualifier

`protected com.apple.client.eocontrol.EOQualifier qualifier()`

---

### queryDisplayGroup

`public com.apple.client.eointerface.EODisplayGroup queryDisplayGroup()`

---

### queryEditingContext

`public com.apple.client.eocontrol.EOEditingContext queryEditingContext()`

---

### queryObjectsWithFetchSpecification

`public void queryObjectsWithFetchSpecification(com.apple.client.eocontrol.EOFetchSpecification anEOFetchSpecification)`

---

### setQueryDisplayGroup

`public void setQueryDisplayGroup(com.apple.client.eointerface.EODisplayGroup anEODisplayGroup)`

---

### setQueryEditingContext

`public void setQueryEditingContext(com.apple.client.eocontrol.EOEditingContext anEOEditingContext)`

---

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

__DRAFT__
