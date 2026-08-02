---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface/Interfaces/EODisplayGroup.Delegate.html
archived_at: '2026-07-15T08:13:55.538098Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md) 

# EODisplayGroup.Delegate

> **__Package:__**
> : com.webobjects.eointerface

---

## Interface Description

---

Documentation for this interface is forthcoming.

## Method Types

---

> **All methods**
>
> : [displayGroupCreateObjectFailed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cdojswc5dfj5rguzldordgc2lmmvsa): [displayGroupDidChangeDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cenfseg2dbnztwkrdborqvg33vojrwk): [displayGroupDidChangeSelectedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cenfseg2dbnztwku3fnrswg5dfmrhwe2tfmn2hg): [displayGroupDidChangeSelection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cenfseg2dbnztwku3fnrswg5djn5xa): [displayGroupDidDeleteObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cenfseizlmmv2gkt3cnjswg5a): [displayGroupDidFetchObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cenfsemzlumnue6ytkmvrxi4y): [displayGroupDidInsertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cenfses3ttmvzhit3cnjswg5a): [displayGroupDidSetValueForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cenfsfgzlukzqwy5lfizxxet3cnjswg5a): [displayGroupDisplayArrayForObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cenfzxa3dbpfaxe4tbpfdg64spmjvgky3uom): [displayGroupShouldChangeSelection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4ctnbxxk3deinugc3thmvjwk3dfmn2gs33o): [displayGroupShouldDeleteObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4ctnbxxk3deirswyzlumvhwe2tfmn2a): [displayGroupShouldDisplayAlert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4ctnbxxk3deiruxg4dmmf4uc3dfoj2a): [displayGroupShouldFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4ctnbxxk3deizsxiy3i): [displayGroupShouldInsertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4ctnbxxk3dejfxhgzlsorhwe2tfmn2a): [displayGroupShouldRedisplay](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4ctnbxxk3dekjswi2ltobwgc6i): [displayGroupShouldRefetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4ctnbxxk3dekjswmzlumnua)

## Instance Methods

---

### displayGroupCreateObjectFailed

`public abstract void displayGroupCreateObjectFailed( EODisplayGroup anEODisplayGroup, com.webobjects.eocontrol.EODataSource anEODataSource)`

Description forthcoming.

---

### displayGroupDidChangeDataSource

`public abstract void displayGroupDidChangeDataSource(EODisplayGroup anEODisplayGroup)`

Description forthcoming.

---

### displayGroupDidChangeSelectedObjects

`public abstract void displayGroupDidChangeSelectedObjects(EODisplayGroup anEODisplayGroup)`

Description forthcoming.

---

### displayGroupDidChangeSelection

`public abstract void displayGroupDidChangeSelection(EODisplayGroup anEODisplayGroup)`

Description forthcoming.

---

### displayGroupDidDeleteObject

`public abstract void displayGroupDidDeleteObject( EODisplayGroup anEODisplayGroup, Object anObject)`

Description forthcoming.

---

### displayGroupDidFetchObjects

`public abstract void displayGroupDidFetchObjects( EODisplayGroup anEODisplayGroup, NSArray objects)`

Description forthcoming.

---

### displayGroupDidInsertObject

`public abstract void displayGroupDidInsertObject( EODisplayGroup anEODisplayGroup, Object anObject)`

Description forthcoming.

---

### displayGroupDidSetValueForObject

`public abstract void displayGroupDidSetValueForObject( EODisplayGroup anEODisplayGroup, Object value, Object anObject, String key)`

Description forthcoming.

---

### displayGroupDisplayArrayForObjects

`public abstract NSArray displayGroupDisplayArrayForObjects( EODisplayGroup anEODisplayGroup, NSArray objects)`

Description forthcoming.

---

### displayGroupShouldChangeSelection

`public abstract boolean displayGroupShouldChangeSelection( EODisplayGroup anEODisplayGroup, NSArray newIndexes)`

Description forthcoming.

---

### displayGroupShouldDeleteObject

`public abstract boolean displayGroupShouldDeleteObject( EODisplayGroup anEODisplayGroup, Object anObject)`

Description forthcoming.

---

### displayGroupShouldDisplayAlert

`public abstract boolean displayGroupShouldDisplayAlert( EODisplayGroup anEODisplayGroup, String title, String message)`

Description forthcoming.

---

### displayGroupShouldFetch

`public abstract boolean displayGroupShouldFetch(EODisplayGroup anEODisplayGroup)`

Description forthcoming.

---

### displayGroupShouldInsertObject

`public abstract boolean displayGroupShouldInsertObject( EODisplayGroup anEODisplayGroup, Object anObject, int index)`

Description forthcoming.

---

### displayGroupShouldRedisplay

`public abstract boolean displayGroupShouldRedisplay( EODisplayGroup anEODisplayGroup, NSNotification aNSNotification)`

Description forthcoming.

---

### displayGroupShouldRefetch

`public abstract boolean displayGroupShouldRefetch( EODisplayGroup anEODisplayGroup, NSNotification aNSNotification)`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
