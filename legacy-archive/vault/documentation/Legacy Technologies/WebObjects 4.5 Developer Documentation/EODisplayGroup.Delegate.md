---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Protocols/EODisplayGroupDelegate.html
archived_at: '2026-07-15T08:11:45.246548Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EODisplayGroup.Delegate

> __(informal interface)__

> **__Package:__**
> : com.apple.client.eointerface
> : com.apple.yellow.eointerface

---

## Interface Description

---

The EODisplayGroup.Delegate interface defines
methods that an EODisplayGroup can invoke in its delegate. Delegates
are not required to provide implementations for all of the methods
in the interface, and you don't have to use the implements keyword
to specify that the object implements the Delegates interface. Instead,
declare and implement any subset of the methods declared in the interface that
you need, and use the EODisplayGroup method [setDelegate](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forcgk3dfm5qxizi) method to assign your
object as the delegate. A display group can determine if the delegate
doesn't implement a delegate method and only attempts to invoke
the methods the delegate actually implements.

## Method Types

---

> **Fetching objects**
> : [displayGroupShouldFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4ctnbxxk3deizsxiy3i)
> : [displayGroupDidFetchObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cenfsemzlumnue6ytkmvrxi4y)
> : [displayGroupShouldRefetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4ctnbxxk3dekjswmzlumnua)
>
> **Inserting, updating,
> and deleting objects**
> : [displayGroupShouldInsertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4ctnbxxk3dejfxhgzlsorhwe2tfmn2a)
> : [displayGroupDidInsertObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cenfses3ttmvzhit3cnjswg5a)
> : [displayGroupCreateObjectFailed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cdojswc5dfj5rguzldordgc2lmmvsa)
> : [displayGroupDidSetValueForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cenfsfgzlukzqwy5lfizxxet3cnjswg5a)
> : [displayGroupShouldDeleteObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4ctnbxxk3deirswyzlumvhwe2tfmn2a)
> : [displayGroupDidDeleteObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cenfseizlmmv2gkt3cnjswg5a)
>
> **Managing the display**
> : [displayGroupShouldDisplayAlert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4ctnbxxk3deiruxg4dmmf4uc3dfoj2a)
> : [displayGroupShouldRedisplay](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4ctnbxxk3dekjswi2ltobwgc6i)
> : [displayGroupDisplayArrayForObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cenfzxa3dbpfaxe4tbpfdg64spmjvgky3uom)
>
> **Managing the selection**
> : [displayGroupShouldChangeSelection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4ctnbxxk3deinugc3thmvjwk3dfmn2gs33o)
> : [displayGroupDidChangeSelection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cenfseg2dbnztwku3fnrswg5djn5xa)
> : [displayGroupDidChangeSelectedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cenfseg2dbnztwku3fnrswg5dfmrhwe2tfmn2hg)
>
> **Changing the data source**
> : [displayGroupDidChangeDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpiruxg4dmmf4uo4tpovyc4rdfnrswoylumuxwi2ltobwgc6khojxxk4cenfseg2dbnztwkrdborqvg33vojrwk)

## Instance Methods

---

### displayGroupCreateObjectFailed

`public abstract void displayGroupCreateObjectFailed(
EODisplayGroup  aDisplayGroup,
com.apple.yellow.eocontrol.EODataSource  aDataSource)`

Invoked from [insertNewObjectAtIndex](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc62loonsxe5comv3u6ytkmvrxiqlujfxgizly) to inform
the delegate that  _aDisplayGroup_ has
failed to create a new object for  _aDataSource._
If the delegate doesn't implement this method, the EODisplayGroup instead
runs an alert panel to inform the user of the failure.

---

### displayGroupDidChangeDataSource

`public abstract void displayGroupDidChangeDataSource(EODisplayGroup  aDisplayGroup)`

Informs the delegate that  _aDisplayGroup_ 's
EODataSource has changed.

---

### displayGroupDidChangeSelectedObjects

`public abstract void displayGroupDidChangeSelectedObjects(EODisplayGroup  aDisplayGroup)`

Informs the delegate that  _aDisplayGroup_ 's
set of selected objects has changed, regardless of whether the selection
indexes have changed.

---

### displayGroupDidChangeSelection

`public abstract void displayGroupDidChangeSelection(EODisplayGroup  aDisplayGroup)`

Informs the delegate that  _aDisplayGroup_ 's
selection has changed.

---

### displayGroupDidDeleteObject

`public abstract void displayGroupDidDeleteObject(
EODisplayGroup  aDisplayGroup,
Object  anObject)`

Informs the delegate that  _aDisplayGroup_ has
deleted  _anObject._

---

### displayGroupDidFetchObjects

`public abstract void displayGroupDidFetchObjects(
EODisplayGroup  aDisplayGroup,
NSArray  objects)`

Informs the delegate that  _aDisplayGroup_ has
fetched  _objects._

---

### displayGroupDidInsertObject

`public abstract void displayGroupDidInsertObject(
EODisplayGroup  aDisplayGroup,
Object  anObject)`

Informs the delegate that  _aDisplayGroup_ has
inserted  _anObject._

---

### displayGroupDidSetValueForObject

`public abstract void displayGroupDidSetValueForObject(
EODisplayGroup  aDisplayGroup,
Object  value,
Object  anObject,
String  key)`

Informs the delegate that  _aDisplayGroup_ has
altered a property value of  _anObject._  _key_ identifies
the property, and  _value_ is its new
value.

---

### displayGroupDisplayArrayForObjects

`public abstract NSArray displayGroupDisplayArrayForObjects(
EODisplayGroup  aDisplayGroup,
NSArray  objects)`

Invoked from [updateDisplayedObjects](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt),
this method allows the delegate to filter and sort  _aDisplayGroup_ 's
array of objects to limit which ones get displayed.  _objects_ contains
all of  _aDisplayGroup_ 's objects.
The delegate should filter any objects that shouldn't be shown
and sort the remainder, returning a new array containing this group
of objects. You can use EOQualifier's `filteredArrayUsingQualifier` and
EOSortOrdering's `sortedArrayUsingKeyOrderArray` methods in EOControl
to create the new array.

If the delegate doesn't implement this method, the EODisplayGroup
uses its own qualifier and sort ordering to update its displayed
objects array.

__See Also:__
[sortOrderings](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643poj2e64temvzgs3thom), [qualifier](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64lvmfwgsztjmvza), [displayedObjects](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y)

---

### displayGroupShouldChangeSelection

`public abstract boolean displayGroupShouldChangeSelection(
EODisplayGroup  aDisplayGroup,
NSArray  newIndexes)`

Allows the delegate to prevent a change in selection
by  _aDisplayGroup._  _newIndexes_ is
the proposed new selection, an array of Numbers. If the delegate
returns true, the selection changes; if the delegate returns false,
the selection remains as it is.

---

### displayGroupShouldDeleteObject

`public abstract boolean displayGroupShouldDeleteObject(
EODisplayGroup  aDisplayGroup,
Object  anObject)`

Allows the delegate to prevent  _aDisplayGroup_ from
deleting  _anObject._ If the delegate
returns true,  _anObject_ is deleted;
if the delegate returns false, the deletion is abandoned.

---

### displayGroupShouldDisplayAlert

`public abstract boolean displayGroupShouldDisplayAlert(
EODisplayGroup  aDisplayGroup,
String  title,
String  message)`

Allows the delegate to prevent  _aDisplayGroup_ from
displaying an attention panel with  _title_ and  _message._
The delegate can return true to allow  _aDisplayGroup_ to
display the panel, or false to prevent it from doing so (perhaps
displaying a different attention panel).

---

### displayGroupShouldFetch

`public abstract boolean displayGroupShouldFetch(EODisplayGroup  aDisplayGroup)`

Allows the delegate to prevent  _aDisplayGroup_ from
fetching. If the delegate returns true,  _aDisplayGroup_ performs
the fetch; if the delegate returns false,  _aDisplayGroup_ abandons
the fetch.

---

### displayGroupShouldInsertObject

`public abstract boolean displayGroupShouldInsertObject(
EODisplayGroup  aDisplayGroup,
Object  anObject,
int  anIndex)`

Allows the delegate to prevent  _aDisplayGroup_ from
inserting  _anObject_ at  _anIndex._
If the delegate returns true,  _anObject_ is
inserted; if the delegate returns false, the insertion is abandoned.

---

### displayGroupShouldRedisplay

`public abstract boolean displayGroupShouldRedisplay(
EODisplayGroup  aDisplayGroup,
NSNotification  aNotification)`

Invoked whenever  _aDisplayGroup_ receives
an `ObjectsChangedInEditingContextNotification`,
this method allows the delegate to suppress redisplay based on the
nature of the change that has occurred. If the delegate returns true,  _aDisplayGroup_ redisplays;
if it returns false,  _aDisplayGroup_ doesn't.  _aNotification_ supplies
the EOEditingContext that has changed, as well as which objects
have changed and how. See the EOEditingContext class specification
for information on `ObjectsChangedInEditingContextNotification`.

__See Also:__
[redisplay](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc64tfmruxg4dmmf4q)

---

### displayGroupShouldRefetch

`public abstract boolean displayGroupShouldRefetch(
EODisplayGroup  aDisplayGroup,
NSNotification  aNotification)`

Invoked whenever  _aDisplayGroup_ receives
an `InvalidatedAllObjectsInStoreNotification`,
this method allows the delegate to suppress refetching of the invalidated
objects. If the delegate returns true,  _aDisplayGroup_ immediately
refetches its objects. If the delegate returns false,  _aDisplayGroup_ doesn't immediately
fetch, instead delaying until absolutely necessary.  _aNotification_ is
an NSNotification. See the EOObjectStore and EOEditingContext class
specifications for information on this notification.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
