---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WODisplayGroup.html
archived_at: '2026-07-15T08:11:47.508929Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WODisplayGroup

> __Inherits
> from:__  NSObject

> __Conforms to:__  NSCoding
> NSObject (NSObject)

> __Declared in:__  WebObjects/WODisplayGroup.h

---

## Class Description

---

A WODisplayGroup is the basic user interface manager for a
WebObjects application that accesses a database. It collects objects
from an EODataSource (defined in EOControl), filters and sorts them,
and maintains a selection in the filtered subset. You bind WebObjects
dynamic elements to WODisplayGroup attributes and methods to display
information from the database on your web page.

A WODisplayGroup manipulates its EODataSource by sending it
fetchObjects, insertObject:, and other messages, and registers itself
as an editor and message handler of the EODataSource's EOEditingContext
(also defined in EOControl). The EOEditingContext then monitors
the WODisplayGroup for changes to objects.

Most of a WODisplayGroup's interactions are with its EODataSource
and its EOEditingContext. See the EODataSource, and EOEditingContext
class specifications in the _Enterprise Objects Framework Reference_ for
more information on these interactions.

## The Delegate

The WODisplayGroup delegate offers a number of methods, and
WODisplayGroup invokes them as appropriate. Besides displayGroup:displayArrayForObjects:,
there are methods that inform the delegate that the WODisplayGroup
has fetched, created an object (or failed to create one), inserted
or deleted an object, changed the selection, or set a value for
a property. There are also methods that request permission from
the delegate to perform most of these same actions. The delegate
can return YES to permit the action or NO to deny it. See each method's
description in the WODisplayGroup.Delegates protocol specification
for more information.

## Adopted Protocols

---

> NSCoding: - encodeWithCoder:
> : - initWithCoder:

## Method Types

---

> **Creating instances**
> : [- init](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3tjoq)
>
> **Configuring behavior**
> : [- setFetchesOnLoad:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluizsxiy3imvzu63smn5qwioq)
> : [- fetchesOnLoad](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwmzlumnugk42pnzgg6yle)
> : [- setSelectsFirstObjectAfterFetch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluknswyzldorzum2lson2e6ytkmvrxiqlgorsxertforrwqoq)
> : [- selectsFirstObjectAfterFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxi42gnfzhg5cpmjvgky3uifthizlsizsxiy3i)
> : [+ setGlobalDefaultForValidatesChangesImmediately:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hui2ltobwgc6khojxxk4bponsxir3mn5rgc3cemvtgc5lmordg64swmfwgszdborsxgq3imfxgozltjfww2zlenfqxizlmpe5a)
> : [+ globalDefaultForValidatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hui2ltobwgc6khojxxk4bpm5wg6ytbnrcgkztbovwhirtpojlgc3djmrqxizltinugc3thmvzus3lnmvsgsylumvwhs)
> : [- setValidatesChangesImmediately:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlukzqwy2lemf2gk42dnbqw4z3fonew23lfmruwc5dfnr4tu)
> : [- validatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxmylmnfsgc5dfonbwqylom5sxgslnnvswi2lborswy6i)
>
> **Setting the data source**
> : [- setDataSource:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluirqxiyktn52xey3fhi)
> : [- dataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwiylumfjw65lsmnsq)
>
> **Setting the qualifier
> and sort ordering**
> : [- setQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlukf2wc3djmzuwk4r2)
> : [- qualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfoi)
> : [- setSortOrderings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluknxxe5cpojsgk4tjnztxgoq)
> : [- sortOrderings](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxg33sorhxezdfojuw4z3t)
>
> **Managing queries**
> : [- qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom)
> : [- queryMatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2ylumnua)
> : [- queryMax](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2yly)
> : [- queryMin](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u22lo)
> : [- queryOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33s)
> : [- allQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwc3dmkf2wc3djmzuwk4spobsxeylun5zhg)
> : [- relationalQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxezlmmf2gs33omfwfc5lbnruwm2lfojhxazlsmf2g64tt)
> : [- stringQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxg5dsnfxgoulvmfwgsztjmvze64dfojqxi33som)
> : [+ setGlobalDefaultStringMatchFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hui2ltobwgc6khojxxk4bponsxir3mn5rgc3cemvtgc5lmorjxi4tjnztu2ylumnuem33snvqxioq)
> : [+ globalDefaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hui2ltobwgc6khojxxk4bpm5wg6ytbnrcgkztbovwhiu3uojuw4z2nmf2gg2cgn5zg2ylu)
> : [- setDefaultStringMatchFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluirswmylvnr2fg5dsnfxgotlborrwqrtpojwwc5b2)
> : [- defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3iizxxe3lboq)
> : [+ setGlobalDefaultStringMatchOperator:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hui2ltobwgc6khojxxk4bponsxir3mn5rgc3cemvtgc5lmorjxi4tjnztu2ylumnue64dfojqxi33shi)
> : [+ globalDefaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hui2ltobwgc6khojxxk4bpm5wg6ytbnrcgkztbovwhiu3uojuw4z2nmf2gg2cpobsxeylun5za)
> : [- setDefaultStringMatchOperator:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluirswmylvnr2fg5dsnfxgotlborrwqt3qmvzgc5dpoi5a)
> : [- defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3ij5ygk4tborxxe)
> : [- qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm6kenfzxa3dbpfdxe33voa)
> : [- qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm6kemf2gcu3povzggzi)
> : [- inQueryMode](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3srovsxe6knn5sgk)
> : [- setInQueryMode:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlujfxfc5lfoj4u233emu5a)
>
> **Fetching objects from
> the data source**
> : [- fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwmzlumnua)
>
> **Getting the objects**
> : [- allObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwc3dmj5rguzldorzq)
> : [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg)
>
> **Batching the results**
> : [- setNumberOfObjectsPerBatch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlujz2w2ytfojhwmt3cnjswg5dtkbsxeqtborrwqoq)
> : [- numberOfObjectsPerBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxw45lnmjsxet3gj5rguzldorzvazlsijqxiy3i)
> : [- hasMultipleBatches](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwqyltjv2wy5djobwgkqtborrwqzlt)
> : [- displayNextBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6komv4hiqtborrwq)
> : [- displayPreviousBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6kqojsxm2lpovzueylumnua)
> : [- batchCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxweylumnueg33vnz2a)
> : [- setCurrentBatchIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluin2xe4tfnz2eeylumnues3temv4du)
> : [- currentBatchIndex](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwg5lsojsw45ccmf2gg2cjnzsgk6a)
> : [- indexOfFirstDisplayedObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3temv4e6zsgnfzhg5cenfzxa3dbpfswit3cnjswg5a)
> : [- indexOfLastDisplayedObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3temv4e6zsmmfzxirdjonygyylzmvse6ytkmvrxi)
> : [- displayBatchContainingSelectedObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6kcmf2gg2cdn5xhiyljnzuw4z2tmvwgky3umvse6ytkmvrxi)
>
> **Updating display of values**
> : [- redisplay](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxezlenfzxa3dbpe)
> : [- updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y)
>
> **Setting the objects**
> : [- setObjectArray:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluj5rguzldoraxe4tbpe5a)
>
> **Changing the selection**
> : [- clearSelection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwg3dfmfzfgzlmmvrxi2lpny)
> : [- selectNext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxittfpb2a)
> : [- selectObjectsIdenticalTo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxit3cnjswg5dtjfsgk3tunfrwc3cun45a)
> : [- selectObjectsIdenticalTo:selectFirstOnNoMatch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxit3cnjswg5dtjfsgk3tunfrwc3cun45hgzlmmvrxirtjojzxit3ojzxu2ylumnudu)
> : [- selectObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxit3cnjswg5b2)
> : [- selectPrevious](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxiudsmv3gs33vom)
> : [- setSelectedObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluknswyzldorswit3cnjswg5b2)
> : [- setSelectedObjects:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluknswyzldorswit3cnjswg5dthi)
> : [- setSelectionIndexes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluknswyzldoruw63sjnzsgk6dfom5a)
>
> **Examining the selection**
> : [- selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxi2lpnzew4zdfpbsxg)
> : [- selectedObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldoq)
> : [- selectedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldorzq)
>
> **Inserting and deleting
> objects**
> : [- insertObject: atIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WODisplayGroup.html#//apple_ref/occ/instm/WODisplayGroup/insertObject:%20atIndex:)
> : [- insertObjectAtIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3ttmvzhit3cnjswg5cborew4zdfpa5a)
> : [- insert](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3ttmvzhi)
> : [- setInsertedObjectDefaultValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlujfxhgzlsorswit3cnjswg5cemvtgc5lmorlgc3dvmvztu)
> : [- insertedObjectDefaultValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3ttmvzhizlej5rguzldorcgkztbovwhivtbnr2wk4y)
> : [- deleteObjectAtIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlmmv2gkt3cnjswg5cborew4zdfpa5a)
> : [- deleteSelection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlmmv2gku3fnrswg5djn5xa)
> : [- delete](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlmmv2gk)
>
> **Setting up a detail display
> group**
> : [- hasDetailDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwqyltirsxiyljnrcgc5dbknxxk4tdmu)
> : [- setMasterObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlujvqxg5dfojhwe2tfmn2du)
> : [- masterObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxw2yltorsxet3cnjswg5a)
> : [- setDetailKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluirsxiyljnrfwk6j2)
> : [- detailKey](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlumfuwys3fpe)
>
> **Working with named fetch
> specifications**
> : [- queryBindings](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4ue2lomruw4z3t)
>
> **Setting the delegate**
> : [- setDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluirswyzlhmf2gkoq)
> : [- delegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlmmvtwc5df)

## Class Methods

---

### globalDefaultForValidatesChangesImmediately

`+ (BOOL)globalDefaultForValidatesChangesImmediately`

Returns the class default controlling
whether changes are immediately validated.

__See
Also:__  [- validatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxmylmnfsgc5dfonbwqylom5sxgslnnvswi2lborswy6i)

---

### globalDefaultStringMatchFormat

`+ (NSString *)globalDefaultStringMatchFormat`

Returns the default string match format
for the class.

__See Also:__  [- defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3iizxxe3lboq)

---

### globalDefaultStringMatchOperator

`+ (NSString *)globalDefaultStringMatchOperator`

Returns the default string match operator
for the class.

__See Also:__  [- defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3ij5ygk4tborxxe)

---

### setGlobalDefaultForValidatesChangesImmediately:

`+ (void)setGlobalDefaultForValidatesChangesImmediately:(BOOL)flag`

Sets according to _flag_ the
class default controlling whether changes are immediately validated.

__See
Also:__  [- setValidatesChangesImmediately:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlukzqwy2lemf2gk42dnbqw4z3fonew23lfmruwc5dfnr4tu)

---

### setGlobalDefaultStringMatchFormat:

`+ (void)setGlobalDefaultStringMatchFormat:(NSString
*)format`

Sets the default string match format for
the class.

__See Also:__  [- setDefaultStringMatchFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluirswmylvnr2fg5dsnfxgotlborrwqrtpojwwc5b2)

---

### setGlobalDefaultStringMatchOperator:

`+ (void)setGlobalDefaultStringMatchFormat:(NSString
*)operator`

Sets the default string match operator
for the class.

__See Also:__  [- setDefaultStringMatchOperator:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluirswmylvnr2fg5dsnfxgotlborrwqt3qmvzgc5dpoi5a)

---

## Instance Methods

---

### allObjects

`- (NSArray *)allObjects`

Returns all of the objects collected by the
receiver.

__See Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwmzlumnua)

---

### allQualifierOperators

`- (NSArray *)allQualifierOperators`

Returns an array containing all of the relational
operators supported by EOControl's EOQualifier: =, !=, <, <=,
>, >=, "__like__" and "__caseInsensitiveLike__".

__See
Also:__  [- queryOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33s), [- relationalQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxezlmmf2gs33omfwfc5lbnruwm2lfojhxazlsmf2g64tt), [- stringQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxg5dsnfxgoulvmfwgsztjmvze64dfojqxi33som)

---

### batchCount

`- (unsigned)batchCount`

The number of batches to display. For example,
if the displayed objects array contains two hundred records and
the batch size is ten, __batchCount__ returns
twenty (twenty batches of ten records each).

__See
Also:__  [- currentBatchIndex](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwg5lsojsw45ccmf2gg2cjnzsgk6a), [- displayNextBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6komv4hiqtborrwq), [- displayPreviousBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6kqojsxm2lpovzueylumnua), [- hasMultipleBatches](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwqyltjv2wy5djobwgkqtborrwqzlt), [- numberOfObjectsPerBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxw45lnmjsxet3gj5rguzldorzvazlsijqxiy3i)

---

### clearSelection

`- (BOOL)clearSelection`

Invokes [setSelectionIndexes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluknswyzldoruw63sjnzsgk6dfom5a) to
clear the selection, returning YES on success and NO on failure.

---

### currentBatchIndex

`- (unsigned)currentBatchIndex`

Returns the index of the batch currently being
displayed. The total batch count equals the number of displayed
objects divided by the batch size. For example, if the WODisplayGroup
has one hundred objects to display and the batch size is twenty,
there are five batches. The first batch has a batch index of 1.

__See
Also:__  [- batchCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxweylumnueg33vnz2a), [- numberOfObjectsPerBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxw45lnmjsxet3gj5rguzldorzvazlsijqxiy3i), [- setCurrentBatchIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluin2xe4tfnz2eeylumnues3temv4du)

---

### dataSource

`- (EODataSource *)dataSource`

Returns the receiver's EODataSource (defined
in the EOControl framework).

__See Also:__  [- hasDetailDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwqyltirsxiyljnrcgc5dbknxxk4tdmu), [- setDataSource:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluirqxiyktn52xey3fhi)

---

### defaultStringMatchFormat

`- (NSString *)defaultStringMatchFormat`

Returns the format string that specifies how
pattern matching will be performed on string values in the [queryMatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2ylumnua) dictionary.
If a key in the __queryMatch__ dictionary does
not have an associated operator in the [queryOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33s) dictionary, then its
value is matched using pattern matching, and the format string returned
by this method specifies how it will be matched.

__See
Also:__  [- defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3ij5ygk4tborxxe), [- setDefaultStringMatchFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluirswmylvnr2fg5dsnfxgotlborrwqrtpojwwc5b2), [+ globalDefaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hui2ltobwgc6khojxxk4bpm5wg6ytbnrcgkztbovwhiu3uojuw4z2nmf2gg2cgn5zg2ylu)

---

### defaultStringMatchOperator

`- (NSString *)defaultStringMatchOperator`

Returns the operator used to perform pattern
matching for string values in the [queryMatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2ylumnua) dictionary. If a key in
the __queryMatch__ dictionary does not have
an associated operator in the [queryOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33s) dictionary, then the
operator returned by this method is used to perform pattern matching.
Unless the default is changed, this method returns caseInsensitiveLike.

__See
Also:__  [- defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3iizxxe3lboq), [- setDefaultStringMatchOperator:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluirswmylvnr2fg5dsnfxgotlborrwqt3qmvzgc5dpoi5a), [+ globalDefaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hui2ltobwgc6khojxxk4bpm5wg6ytbnrcgkztbovwhiu3uojuw4z2nmf2gg2cpobsxeylun5za)

---

### delegate

`- (id)delegate`

Returns the receiver's delegate.

__See
Also:__  [- setDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluirswyzlhmf2gkoq)

---

### delete

`- (id)delete`

Uses [deleteSelection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlmmv2gku3fnrswg5djn5xa) to attempt to delete
the selected objects and then causes the page to reload. Returns nil to
force reloading of the web page.

__See Also:__  [- deleteObjectAtIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlmmv2gkt3cnjswg5cborew4zdfpa5a)

---

### deleteObjectAtIndex:

`- (BOOL)deleteObjectAtIndex:(unsigned)index`

Attempts to delete the object at _index_,
returning YES if successful and NO if not. Checks with the delegate using
the method displayGroup:shouldDeleteObject:.
If the delegate returns NO, this method fails and returns NO. If
successful, it sends the delegate a displayGroup:didDeleteObject: message.

This method performs the delete by sending deleteObject to
the EODataSource (defined in the EOControl framework). If that message
raises an exception, this method fails and returns NO.

__See
Also:__  [- delete](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlmmv2gk), [- deleteSelection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlmmv2gku3fnrswg5djn5xa)

---

### deleteSelection

`- (BOOL)deleteSelection`

Attempts to delete the selected objects, returning YES if
successful and NO if not.

__See Also:__  [- delete](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlmmv2gk), [- deleteObjectAtIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlmmv2gkt3cnjswg5cborew4zdfpa5a)

---

### detailKey

`- (NSString *)detailKey`

For detail display groups, returns the key to
the master object that specifies what this detail display group
represents. That is, if you send the object returned by the [masterObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxw2yltorsxet3cnjswg5a) method
a valueForKey: message with this key, you obtain the objects controlled
by this display group.

This method returns nil if the receiver
is not a detail display group or if the detail key has not yet been set.
You typically create a detail display group by dragging a to-many
relationship from EOModeler to an open component in WebObjects Builder.

__See
Also:__  [- hasDetailDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwqyltirsxiyljnrcgc5dbknxxk4tdmu), [- masterObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxw2yltorsxet3cnjswg5a), [- setDetailKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluirsxiyljnrfwk6j2)

---

### displayBatchContainingSelectedObject

`- (id)displayBatchContainingSelectedObject`

Displays the batch containing the selection
and sets the current batch index to that batch's index. Returns nil to
force the page to reload.

__See Also:__  [- displayNextBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6komv4hiqtborrwq), [- displayPreviousBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6kqojsxm2lpovzueylumnua), [- setCurrentBatchIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluin2xe4tfnz2eeylumnues3temv4du)

---

### displayedObjects

`- (NSArray *)displayedObjects`

Returns the objects that should be displayed
or otherwise made available to the user, as filtered by the receiver's
delegate, by the receiver's qualifier and sort ordering.

If
batching is in effect, __displayedObjects__ returns
the current batch of objects.

__See
Also:__  [- allObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwc3dmj5rguzldorzq), [- updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y), [- qualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfoi), [- setSortOrderings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluknxxe5cpojsgk4tjnztxgoq), - displayGroup:displayArrayForObjects: (delegate
method)

---

### displayNextBatch

`- (id)displayNextBatch`

Increments the current batch index, displays
that batch of objects, and clears the selection. If the batch currently
being displayed is the last batch, this method displays the first
batch of objects. Returns nil to force the page to reload.

__See
Also:__  [- batchCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxweylumnueg33vnz2a), [- currentBatchIndex](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwg5lsojsw45ccmf2gg2cjnzsgk6a), [- displayBatchContainingSelectedObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6kcmf2gg2cdn5xhiyljnzuw4z2tmvwgky3umvse6ytkmvrxi), [- displayPreviousBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6kqojsxm2lpovzueylumnua)

---

### displayPreviousBatch

`- (id)displayPreviousBatch`

Decrements the current batch index, displays
that batch of objects, and clears the selection. If the batch currently
being displayed is the first batch, this method displays the last
batch of objects. Returns nil to force the page to reload.

__See
Also:__  [- batchCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxweylumnueg33vnz2a), [- currentBatchIndex](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwg5lsojsw45ccmf2gg2cjnzsgk6a), [- displayBatchContainingSelectedObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6kcmf2gg2cdn5xhiyljnzuw4z2tmvwgky3umvse6ytkmvrxi), [- displayNextBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6komv4hiqtborrwq)

---

### fetch

`- (id)fetch`

Attempts to fetch objects from the EODataSource
(defined in the EOControl framework).

Before fetching, this
method sends displayGroupShouldFetch: to
the delegate. If this method was successful, it then sends a __fetchObjects__ message
to the receiver's EODataSource to replace the object array, and
if successful sends the delegate a displayGroup:didFetchObjects: message.

This
method returns nil to force the page to reload.

__See
Also:__  [- allObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwc3dmj5rguzldorzq), [- updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y)

---

### fetchesOnLoad

`- (BOOL)fetchesOnLoad`

Returns YES if the receiver fetches automatically
after the component that contains it is loaded, NO if it must be
told explicitly to fetch. The default is YES. You can set this behavior
in WebObjects Builder using the Display Group Options panel. Note
that if the display group fetches on load, it performs the fetch each
time the component is loaded into the web browser.

__See
Also:__  [- fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwmzlumnua), [- setFetchesOnLoad:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluizsxiy3imvzu63smn5qwioq)

---

### hasDetailDataSource

`- (BOOL)hasDetailDataSource`

Returns YES if the display group's data source
is an EODetailDataSource (defined in the EOControl framework), and NO otherwise.
If you drag a to-many relationship from EOModeler to an open component
in WebObjects Builder, you create a display group that has an EODetailDataSource.
You can also set this up using the Display Group Options panel in
WebObjects Builder.

__See Also:__  [- detailKey](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlumfuwys3fpe), [- masterObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxw2yltorsxet3cnjswg5a)

---

### hasMultipleBatches

`- (BOOL)hasMultipleBatches`

Returns YES if the batch count is greater than
1. A display group displays its objects in batches if the [numberOfObjectsPerBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxw45lnmjsxet3gj5rguzldorzvazlsijqxiy3i) method returns
a number that is less than the number of objects in the [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg) array.

__See
Also:__  [- batchCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxweylumnueg33vnz2a), [- setNumberOfObjectsPerBatch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlujz2w2ytfojhwmt3cnjswg5dtkbsxeqtborrwqoq)

---

### indexOfFirstDisplayedObject

`- (unsigned)indexOfFirstDisplayedObject`

Returns the index of the first object displayed
by the current batch. For example, if the current batch is displaying
items 11 through 20, this method returns 11.

__See
Also:__  [- indexOfLastDisplayedObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3temv4e6zsmmfzxirdjonygyylzmvse6ytkmvrxi)

---

### indexOfLastDisplayedObject

`- (unsigned)indexOfLastDisplayedObject`

Returns the index of the last object display
by the current batch. For example, if the current batch is displaying
items 11 through 20, this method returns 20.

__See
Also:__  [- indexOfFirstDisplayedObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3temv4e6zsgnfzhg5cenfzxa3dbpfswit3cnjswg5a)

---

### init

`- (id)init`

Initializes the WODisplayGroup. The WODisplayGroup
then needs to have an EODataSource set with [setDataSource:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluirqxiyktn52xey3fhi).

---

### inQueryMode

`- (BOOL)inQueryMode`

Returns YES to indicate that the receiver is
in query mode, NO otherwise. In query mode, controls in the user
interface that normally display values become empty, allowing users
to type queries directly into them (this is also known as a "Query
by Example" interface). In effect, the receiver's "displayedObjects"
are replaced with an empty [queryMatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2ylumnua) dictionary. When [qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm6kenfzxa3dbpfdxe33voa) or [qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm6kemf2gcu3povzggzi) is
subsequently invoked, the query is performed and the display reverts
to displaying values-this time, the objects returned by the query.

__See
Also:__  [- setInQueryMode:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlujfxfc5lfoj4u233emu5a)

---

### insert

`- (id)insert`

Invokes [insertObjectAtIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3ttmvzhit3cnjswg5cborew4zdfpa5a) with
an index just past the first index in the selection, or at the end
if there's no selection.

This method returns nil to force
the page to reload.

---

### insertedObjectDefaultValues

`- (NSDictionary *)insertedObjectDefaultValues`

Returns the default values to be used for newly
inserted objects. The keys into the dictionary are the properties
of the entity that the display group manages. If the dictionary
returned by this method is empty, the [insert](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3ttmvzhi) method adds an object that
is initially empty. Because the object is empty, the display group
has no value to display on the HTML page for that object, meaning
that there is nothing for the user to select and modify. Use the [setInsertedObjectDefaultValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlujfxhgzlsorswit3cnjswg5cemvtgc5lmorlgc3dvmvztu) method
to set up a default value so that there is something to display
on the page.

---

### insertObjectAtIndex:

`- (id)insertObjectAtIndex:(unsigned)index`

Asks the receiver's EODataSource (defined
in the EOControl framework) to create a new object by sending it
a __createObject__ message, then inserts the
new object using [insertObject: atIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WODisplayGroup.html#//apple_ref/occ/instm/WODisplayGroup/insertObject:%20atIndex:).
If a new object can't be created, this method sends the delegate
a displayGroup:createObjectFailedForDataSource: message.

If
the object is successfully created, this method then sets the default
values specified by [insertedObjectDefaultValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3ttmvzhizlej5rguzldorcgkztbovwhivtbnr2wk4y).

__See
Also:__  [- insert](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3ttmvzhi)

---

### insertObject: atIndex:

`- (void)insertObject:(id)anObject
atIndex:(unsigned)index`

Inserts _anObject_ into
the receiver's EODataSource and displayed
objects at the specified index, if possible. This method checks
with the delegate before actually inserting, using displayGroup:shouldInsertObject:atIndex:.
If the delegate refuses, _anObject_ isn't
inserted. After successfully inserting the object, this method informs
the delegate with a displayGroup:didInsertObject: message, and
selects the newly inserted object.

Raises an NSRangeException if _index_ is
out of bounds.

__See Also:__  [- insertObjectAtIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3ttmvzhit3cnjswg5cborew4zdfpa5a), [- insert](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3ttmvzhi)

---

### masterObject

`- (id)masterObject`

Returns the master object for a detail display
group (a display group that represents a detail in a master-detail
relationship). A detail display group is one that uses an EODetailDataSource
(defined in the EOControl framework). You create a detail display
group by dragging a to-many relationship from EOModeler to an open
component in WebObjects Builder. If the display group is not a detail
display group or does not have a master object set, this method
returns nil.

__See Also:__  [- detailKey](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlumfuwys3fpe), [- hasDetailDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwqyltirsxiyljnrcgc5dbknxxk4tdmu), [- setMasterObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlujvqxg5dfojhwe2tfmn2du)

---

### numberOfObjectsPerBatch

`- (unsigned)numberOfObjectsPerBatch`

Returns the batch size. You can set the batch
size using [setNumberOfObjectsPerBatch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlujz2w2ytfojhwmt3cnjswg5dtkbsxeqtborrwqoq) or
using WebObjects Builder's Display Group Options panel.

---

### qualifier

`- (EOQualifier *)qualifier`

Returns the receiver's qualifier, which it
uses to filter its array of objects for display when the delegate doesn't
do so itself.

__See Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- setQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlukf2wc3djmzuwk4r2), [- updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y)

---

### qualifierFromQueryValues

`- (EOQualifier *)qualifierFromQueryValues`

Builds a qualifier constructed from entries
in these query dictionaries: [queryMatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2ylumnua), [queryMax](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2yly), [queryMin](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u22lo), and [queryOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33s).

__See
Also:__  [- qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm6kemf2gcu3povzggzi), [- qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm6kenfzxa3dbpfdxe33voa)

---

### qualifyDataSource

`- (void)qualifyDataSource`

Takes the result of [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom) and applies
to the receiver's data source. The receiver then sends itself
a [fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwmzlumnua) message. If
the receiver is in query mode, query mode is exited. This method differs
from [qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm6kenfzxa3dbpfdxe33voa) as
follows: whereas __qualifyDisplayGroup__ performs
in-memory filtering of already fetched objects, __qualifyDataSource__ triggers
a new qualified fetch against the database.

__See
Also:__  [- queryMatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2ylumnua), [- queryMax](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2yly),, [- queryMin](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u22lo), [- queryOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33s)

---

### qualifyDisplayGroup

`- (void)qualifyDisplayGroup`

Takes the result of the [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom) and applies
to the receiver using [setQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlukf2wc3djmzuwk4r2).
The method [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y) is invoked
to refresh the display. If the receiver is in query mode, query
mode is exited.

__See Also:__  [- qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm6kemf2gcu3povzggzi), [- queryMatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2ylumnua), [- queryMax](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2yly),
- [- queryMin](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u22lo), [- queryOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33s)

---

### queryBindings

`- (NSMutableDictionary *)queryBindings`

Returns a dictionary containing the actual values
that the user wants to query upon. You use this method to perform
a query stored in the model file. Bind keys in this dictionary to
elements on your component that specify query values, then pass
this dictionary to the fetch specification that performs the fetch.

---

### queryMatch

`- (NSMutableDictionary *)queryMatch`

Returns a dictionary of query values to match.
The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom) method uses
this dictionary along with the [queryMax](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2yly) and [queryMin](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u22lo) dictionaries to construct
qualifiers.

Use the [queryOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33s) dictionary to specify
the type of matching (=, <, >, __like__,
and so on) for each key in the __queryMatch__ dictionary.

If the __queryOperator__ dictionary
does not contain a key contained in the __queryMatch__ dictionary,
the default is to match the value exactly (=) if the value is a
number or a date and to perform pattern matching if the value is
an NSString. In the case of string values, the [defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3iizxxe3lboq) and [defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3ij5ygk4tborxxe) specify
exactly how the pattern matching will be performed.

__See
Also:__  [- allQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwc3dmkf2wc3djmzuwk4spobsxeylun5zhg), [- qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm6kemf2gcu3povzggzi), [- qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm6kenfzxa3dbpfdxe33voa), [- relationalQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxezlmmf2gs33omfwfc5lbnruwm2lfojhxazlsmf2g64tt)

---

### queryMax

`- (NSMutableDictionary *)queryMax`

Returns a dictionary of "less than" query
values. The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom) method
uses this dictionary along with the [queryMatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2ylumnua) and [queryMin](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u22lo) dictionaries to construct
qualifiers.

__See Also:__  [- qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm6kemf2gcu3povzggzi), [- qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm6kenfzxa3dbpfdxe33voa), [- queryOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33s)

---

### queryMin

`- (NSMutableDictionary *)queryMin`

Returns a dictionary of "greater than" query
values. The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom) method
uses this dictionary along with the [queryMatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2ylumnua) and __queryMin__ dictionaries
to construct qualifiers.

__See Also:__  [- qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm6kemf2gcu3povzggzi), [- qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm6kenfzxa3dbpfdxe33voa), [- queryOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33s)

---

### queryOperator

`- (NSMutableDictionary *)queryOperator`

Returns a dictionary of operators to use on
items in the [queryMatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2ylumnua) dictionary.
If a key in the __queryMatch__ dictionary also
exists in __queryOperator__, that operator
for that key is used. The [allQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwc3dmkf2wc3djmzuwk4spobsxeylun5zhg) method
returns the operator strings you can use as values in this dictionary.

__See
Also:__  [- qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfojdhe33nkf2wk4tzkzqwy5lfom), [- queryMax](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2yly), [- queryMin](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u22lo), [- relationalQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxezlmmf2gs33omfwfc5lbnruwm2lfojhxazlsmf2g64tt)

---

### redisplay

`- (void)redisplay`

Sends out a contents changed notification.

---

### relationalQualifierOperators

`- (NSArray *)relationalQualifierOperators`

Returns an array containing all of the relational
operators supported by EOControl's EOQualifier: =, !=, <, <=,
>, and >=. In other words, returns all of the EOQualifier
operators except for the ones that work exclusively on strings:
"__like__" and "__caseInsensitiveLike__".

__See
Also:__  [- allQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwc3dmkf2wc3djmzuwk4spobsxeylun5zhg), [- queryOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33s), [- stringQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxg5dsnfxgoulvmfwgsztjmvze64dfojqxi33som)

---

### selectedObject

`- (id)selectedObject`

Returns the first selected object in the displayed
objects array, or nil if there's no such object.

__See
Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxi2lpnzew4zdfpbsxg), [- selectedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldorzq)

---

### selectedObjects

`- (NSArray *)selectedObjects`

Returns the objects selected in the receiver's
displayed objects array.

__See Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxi2lpnzew4zdfpbsxg), [- selectedObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldoq)

---

### selectionIndexes

`- (NSArray *)selectionIndexes`

Returns the selection as an array of NSNumbers.
The NSNumbers are indexes into the array returned by [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg).

__See
Also:__  [- selectedObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldoq), [- selectedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldorzq), [- setSelectionIndexes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluknswyzldoruw63sjnzsgk6dfom5a)

---

### selectNext

`- (id)selectNext`

Attempts to select the object just after the
currently selected one. The selection is altered in this way:

- If there are no objects, does nothing.
- If there's no selection, selects the object at index zero.
- If the first selected object is the last object in the displayed
  objects array, selects the first object.
- Otherwise selects the object after the first selected object.

This
method returns nil to force the page to reload.

__See
Also:__  [- selectPrevious](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxiudsmv3gs33vom), [- setSelectionIndexes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluknswyzldoruw63sjnzsgk6dfom5a)

---

### selectObject:

`- (BOOL)selectObject:(id)anObject`

Attempts to select the object equal to _anObject_ in
the receiver's displayed objects array, returning YES if successful
and NO otherwise. _anObject_ is equal
to an object in the displayed objects array if its address is the
same as the object in the array.

__See Also:__  [- selectNext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxittfpb2a), [- selectPrevious](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxiudsmv3gs33vom)

---

### selectObjectsIdenticalTo:

`- (BOOL)selectObjectsIdenticalTo:(NSArray
*)objectSelection`

Attempts to select the objects in the receiver's
displayed objects array whose ids are equal to those of objects,
returning YES if successful and NO otherwise.

__See
Also:__  [- setSelectionIndexes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluknswyzldoruw63sjnzsgk6dfom5a), [- selectObjectsIdenticalTo:selectFirstOnNoMatch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxit3cnjswg5dtjfsgk3tunfrwc3cun45hgzlmmvrxirtjojzxit3ojzxu2ylumnudu)

---

### selectObjectsIdenticalTo:selectFirstOnNoMatch:

`- (BOOL)selectObjectsIdenticalTo:(NSArray
*)objects
selectFirstOnNoMatch:(BOOL)flag`

Selects the objects in the receiver's displayed
objects array whose ids are equal to those of _objects_, returning YES if
successful and NO otherwise. If no objects in the displayed _objects_ array
match objects and _flag_ is YES, attempts
to select the first object in the displayed objects array.

__See
Also:__  [- setSelectionIndexes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluknswyzldoruw63sjnzsgk6dfom5a), [- selectObjectsIdenticalTo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxit3cnjswg5dtjfsgk3tunfrwc3cun45a)

---

### selectPrevious

`- (id)selectPrevious`

Attempts to select the object just before the
presently selected one. The selection is altered in this way:

- If there are no objects, does nothing.
- If there's no selection, selects the object at index zero.
- If the first selected object is at index zero, selects the
  last object.
- Otherwise selects the object before the first selected object.

This method returns nil to force the
page to reload.

__See Also:__  [- selectNext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxittfpb2a), [- redisplay](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxezlenfzxa3dbpe)

---

### selectsFirstObjectAfterFetch

`- (BOOL)selectsFirstObjectAfterFetch`

Returns YES YES if the receiver automatically
selects its first displayed object after a fetch if there was no
selection, NO if it leaves an empty selection as-is.

WODisplayGroups
by default do select the first object after a fetch when there was
no previous selection.

__See Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwmzlumnua), [- setSelectsFirstObjectAfterFetch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluknswyzldorzum2lson2e6ytkmvrxiqlgorsxertforrwqoq)

---

### setCurrentBatchIndex:

`- (void)setCurrentBatchIndex:(unsigned)anInt`

Displays the _anInt_ batch
of objects. The total batch count equals the number of displayed
objects divided by the batch size. For example, if the WODisplayGroup
has one hundred objects to display and the batch size is twenty,
there are five batches. The first batch has a batch index of 1. setCurrentBatchIndex:3 would
display the third batch of objects (objects 41 to 60 in this example).

If _anInt_ is greater than the
number of batches, this method displays the first batch.

__See
Also:__  [- batchCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxweylumnueg33vnz2a), [- currentBatchIndex](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwg5lsojsw45ccmf2gg2cjnzsgk6a), [- displayBatchContainingSelectedObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6kcmf2gg2cdn5xhiyljnzuw4z2tmvwgky3umvse6ytkmvrxi), [- displayNextBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6komv4hiqtborrwq), [- displayPreviousBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6kqojsxm2lpovzueylumnua), [- numberOfObjectsPerBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxw45lnmjsxet3gj5rguzldorzvazlsijqxiy3i)

---

### setDataSource:

`- (void)setDataSource:(EODataSource
*)aDataSource`

Sets the receiver's EODataSource (defined
in the EOControl framework) to _aDataSource_.
In the process, it performs these actions:

- Unregisters
  itself as an editor and message handler for the previous EODataSource's EOEditingContext
  (also defined in EOControl), if necessary, and registers itself
  with _aDataSource_'s EOEditingContext.
  If the new EOEditingContext already has a message handler, however,
  the receiver doesn't assume that role.
- Clears the receiver's array of objects.
- Sends displayGroupDidChangeDataSource: to
  the delegate if there is one.

__See
Also:__  [- dataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwiylumfjw65lsmnsq)

---

### setDefaultStringMatchFormat:

`- (void)setDefaultStringMatchFormat:(NSString
*)format`

Sets how pattern matching will be performed
on NSString values in the [queryMatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2ylumnua) dictionary. This format
is used for properties listed in the __queryMatch__ dictionary
that have NSString values and that do not have an associated entry
in the [queryOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33s) dictionary.
In these cases, the value is matched using pattern matching and
format specifies how it will be matched.

The default format
string for pattern matching is "__%@\*__"
which means that the string value in the __queryMatch__ dictionary
is used as a prefix (this default can be overridden on a class basis
using [setGlobalDefaultStringMatchFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hui2ltobwgc6khojxxk4bponsxir3mn5rgc3cemvtgc5lmorjxi4tjnztu2ylumnuem33snvqxioq)).
For example, if the __queryMatch__ dictionary
contains a value "Jo" for the key "Name", the query returns
all records whose name values begin with "Jo".

__See
Also:__  [- defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3iizxxe3lboq), [- setDefaultStringMatchOperator:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluirswmylvnr2fg5dsnfxgotlborrwqt3qmvzgc5dpoi5a), [+ setGlobalDefaultStringMatchFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hui2ltobwgc6khojxxk4bponsxir3mn5rgc3cemvtgc5lmorjxi4tjnztu2ylumnuem33snvqxioq)

---

### setDefaultStringMatchOperator:

`- (void)setDefaultStringMatchOperator:(NSString
*)operator`

Sets the operator used to perform pattern matching
for NSString values in the [queryMatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2ylumnua) dictionary. This operator
is used for properties listed in the __queryMatch__ dictionary
that have NSString values and that do not have an associated entry
in the [queryOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u64dfojqxi33s) dictionary.
In these cases, the operator operator is used to perform pattern
matching.

The default value for the query match operator
is __caseInsensitiveLike__, which means that
the query does not consider case when matching letters (this default
can be overridden on a class basis using [setGlobalDefaultStringMatchOperator:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hui2ltobwgc6khojxxk4bponsxir3mn5rgc3cemvtgc5lmorjxi4tjnztu2ylumnue64dfojqxi33shi)).
The other possible value for this operator is __like__,
which matches the case of the letters exactly.

__See
Also:__  [- allQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwc3dmkf2wc3djmzuwk4spobsxeylun5zhg), [- defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlgmf2wy5ctorzgs3thjvqxiy3ij5ygk4tborxxe), [- relationalQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxezlmmf2gs33omfwfc5lbnruwm2lfojhxazlsmf2g64tt), [- setDefaultStringMatchFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluirswmylvnr2fg5dsnfxgotlborrwqrtpojwwc5b2), [+ setGlobalDefaultStringMatchOperator:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hui2ltobwgc6khojxxk4bponsxir3mn5rgc3cemvtgc5lmorjxi4tjnztu2ylumnue64dfojqxi33shi)

---

### setDelegate:

`- (void)setDelegate:(id)anObject`

Sets the receiver's delegate to _anObject_,
without retaining it.

__See Also:__  [- delegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlmmvtwc5df), WODisplayGroup Delegate

---

### setDetailKey:

`- (void)setDetailKey:(NSString
*)detailKey`

Sets the detail key to _detailKey_ for
a detail display group. The detail key is the key that retrieves
from the master object the objects that this display group manages.
You must set a detail key before you set a master object.

If
the receiver is not a detail display group, this method has no effect.
A display group is a detail display group if its data source is
an EODetailDataSource (defined in the EOControl framework). You
typically create a detail display group by dragging a to-many relationship
from EOModeler to an open component in WebObjects Builder. Doing
so sets the detail key and master object, so you rarely need to
use this method.

__See Also:__  [- hasDetailDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwqyltirsxiyljnrcgc5dbknxxk4tdmu), [- detailKey](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwizlumfuwys3fpe), [- setMasterObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlujvqxg5dfojhwe2tfmn2du)

---

### setFetchesOnLoad:

`- (void)setFetchesOnLoad:(BOOL)flag`

Controls whether the receiver automatically
fetches its objects after being loaded. If _flag_ is YES it
does; if _flag_ is NO the receiver
must be told explicitly to fetch. The default is NO. You can also
set this behavior in WebObjects Builder in the Display Group Options
panel.

__See Also:__  [- fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwmzlumnua), [- fetchesOnLoad](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwmzlumnugk42pnzgg6yle)

---

### setInQueryMode:

`- (void)setInQueryMode:(BOOL)flag`

Sets according to _flag_ whether
the receiver is in query mode. In query mode, controls in the user interface
that normally display values become empty, allowing users to type
queries directly into them (this is also known as a "Query by
Example" interface). In effect, the receiver's "displayedObjects"
are replaced with an empty [queryMatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lfoj4u2ylumnua) dictionary. When [qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm6kenfzxa3dbpfdxe33voa) or [qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm6kemf2gcu3povzggzi) is subsequently
invoked, the query is performed and the display reverts to displaying
values-this time, the objects returned by the query.

__See
Also:__  [- inQueryMode](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3srovsxe6knn5sgk)

---

### setInsertedObjectDefaultValues:

`- (void)setInsertedObjectDefaultValues:(NSDictionary
*)defaultValues`

Sets default values to be used for newly inserted
objects. When you use the [insert](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3ttmvzhi) method
to add an object, that object is initially empty. Because the object
is empty, there is no value to be displayed on the HTML page, meaning
there is nothing for the user to select and modify. You use this
method to provide at least one field that can be displayed for the
newly inserted object. The possible keys into the dictionary are
the properties of the entity managed by this display group. For
example, a component that displays a list of movie titles and allows
the user to insert new movie titles might contain these statements
to ensure that all new objects have something to display as a movie
title:
> ```
> [defaultValues setObject:@"New title" forKey:@"title"];
> [movies setInsertedObjectDefaultValues:defaultValues];
> ```

__See
Also:__  [- insertedObjectDefaultValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxws3ttmvzhizlej5rguzldorcgkztbovwhivtbnr2wk4y)

---

### setMasterObject:

`- (void)setMasterObject:(id)masterObject`

Sets the master object to _masterObject_ for
detail display groups and then performs a fetch if the display group
is set to fetch on load. The master object owns the objects controlled
by this display group.

Before you use this method, you should
use the [setDetailKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluirsxiyljnrfwk6j2) to
set the key to this relationship. You typically create a detail
display group by dragging a to-Many relationship from EOModeler
to an open component in WebObjects Builder. Doing so sets the master
object and detail key, so you typically do not have to use this
method.

If the receiver is not a detail display group,
this method has no effect.

__See Also:__  [- hasDetailDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwqyltirsxiyljnrcgc5dbknxxk4tdmu), [- masterObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxw2yltorsxet3cnjswg5a)

---

### setNumberOfObjectsPerBatch:

`- (void)setNumberOfObjectsPerBatch:(unsigned)count`

Sets the number of objects the receiver displays
at a time. For example, suppose you are displaying one hundred records.
Instead of displaying all of these at once, you can set the batch
size so that the page displays a more manageable number (for example,
10). WebObjects Builder allows you to set the number of objects
per batch on the Display Group Options panel.

__See
Also:__  [- batchCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxweylumnueg33vnz2a), [- displayNextBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6komv4hiqtborrwq), [- displayPreviousBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6kqojsxm2lpovzueylumnua), [- numberOfObjectsPerBatch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxw45lnmjsxet3gj5rguzldorzvazlsijqxiy3i)

---

### setObjectArray:

`- (void)setObjectArray:(NSArray
*)objects`

Sets the receiver's objects to _objects_,
regardless of what its EODataSource (defined in the EOControl framework)
provides. This method doesn't affect the EODataSource's objects
at all; specifically, it results in neither inserts nor deletes
of objects in the EODataSource. objects should contain objects with the
same property names or methods as those accessed by the receiver.
This method is used by __fetch__ to set the
array of fetched objects; you should rarely need to invoke it directly.

After setting the object array, this method restores as much
of the original selection as possible. If there's no match and
the receiver selects after fetching, then the first object is selected.

__See
Also:__  [- allObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwc3dmj5rguzldorzq), [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwmzlumnua), [- selectsFirstObjectAfterFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxi42gnfzhg5cpmjvgky3uifthizlsizsxiy3i)

---

### setQualifier:

`- (void)setQualifier:(EOQualifier
*)aQualifier`

Sets the receiver's qualifier to _aQualifier_.
This qualifier is used to filter the receiver's array of objects for
display. Use [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y) to apply the
qualifier.

If the receiver's delegate responds to displayGroup:displayArrayForObjects:,
that method is used instead of the qualifier to filter the objects.

__See
Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- qualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfoi)

---

### setSelectedObject:

`- (void)setSelectedObject:(id)anObject`

Sets the first selected object in the displayed
objects array to _anObject_.

__See
Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxi2lpnzew4zdfpbsxg), [- selectedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldorzq)

---

### setSelectedObjects:

`- (void)selectedObjects:(NSArray
*)objects`

Sets the objects selected in the receiver's
displayed objects array to _objects_.

__See
Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxi2lpnzew4zdfpbsxg), [- selectedObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldoq)

---

### setSelectionIndexes:

`- (BOOL)setSelectionIndexes:(NSArray
*)selection`

Selects the objects at selection in the receiver's
array if possible, returning YES if successful and NO if not (in
which case the selection remains unaltered). This method is the
primitive method for altering the selection; all other such methods
invoke this one to make the change.

This method checks the
delegate with a displayGroup:shouldChangeSelectionToIndexes: message.
If the delegate returns NO, this method also fails and returns NO.
If the receiver successfully changes the selection, its observers
each receive a displayGroupDidChangeSelection: message
and, if necessary, a displayGroupDidChangeSelectedObjects: message.

|  |
| --- |
| The selection set here is only a programmatic selection; the objects on the screen are not highlighted in any way. |

__See Also:__  [- allObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwc3dmj5rguzldorzq)

---

### setSelectsFirstObjectAfterFetch:

`- (void)setSelectsFirstObjectAfterFetch:(BOOL)flag`

Controls whether the receiver automatically
selects its first displayed object after a fetch when there were
no selected objects before the fetch. If _flag_ is YES it
does; if _flag_ is NO then no objects
are selected.

WODisplayGroups by default do select the first
object after a fetch when there was no previous selection.

__See
Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- fetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwmzlumnua), [- selectsFirstObjectAfterFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxi42gnfzhg5cpmjvgky3uifthizlsizsxiy3i)

---

### setSortOrderings:

`- (void)setSortOrderings:(NSArray
*)keySortOrderArray`

Sets the EOSortOrdering objects (defined in
the EOControl framework) that [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y) uses
to sort the displayed objects to orderings. Use __updateDisplayedObjects__ to
apply the sort orderings.You can also set this value using the WebObjects
Builder Display Group Options panel.

If the receiver's
delegate responds to __displayGroup:displayArrayForObjects:__,
that method is used instead of the sort orderings to order the objects.

__See
Also:__  [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- sortOrderings](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxg33sorhxezdfojuw4z3t), [- updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y)

---

### setValidatesChangesImmediately:

`- (void)setValidatesChangesImmediately:(BOOL)flag`

Controls the receiver's behavior on encountering
a validation error. In the Web context, this method has no effect.

WODisplayGroups by default don't validate changes immediately
(although this default can be overridden on a class basis; see [setGlobalDefaultForValidatesChangesImmediately:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hui2ltobwgc6khojxxk4bponsxir3mn5rgc3cemvtgc5lmordg64swmfwgszdborsxgq3imfxgozltjfww2zlenfqxizlmpe5a)).

__See
Also:__  - saveChanges (in EOControl's EOEditingContext),
- tryToSaveChanges (EOEditingContext Additions), [- validatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxmylmnfsgc5dfonbwqylom5sxgslnnvswi2lborswy6i), [+ setGlobalDefaultForValidatesChangesImmediately:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hui2ltobwgc6khojxxk4bponsxir3mn5rgc3cemvtgc5lmordg64swmfwgszdborsxgq3imfxgozltjfww2zlenfqxizlmpe5a)

---

### sortOrderings

`- (NSArray *)sortOrderings`

Returns an array of EOSortOrdering objects (defined
in the EOControl framework) that [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y) uses
to sort the displayed objects, as returned by the [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg) method.

__See
Also:__  [- setSortOrderings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzluknxxe5cpojsgk4tjnztxgoq)

---

### stringQualifierOperators

`- (NSArray *)stringQualifierOperators`

Returns an array containing all of the relational operators supported by EOControl's EOQualifier that work exclusively on strings: `"starts with", "contains", "ends with", "is",` and `"like"`.

__See Also:__  [allQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwc3dmkf2wc3djmzuwk4spobsxeylun5zhg), [relationalQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxezlmmf2gs33omfwfc5lbnruwm2lfojhxazlsmf2g64tt)

---

### updateDisplayedObjects

`- (void)updateDisplayedObjects`

Recalculates the receiver's displayed objects
arrays and redisplays. If the delegate responds to displayGroup:displayArrayForObjects:,
it's sent this message and the returned array is set as the WODisplayGroup's
displayed objects. Otherwise, the receiver applies its qualifier
and sort ordering to its array of objects. In either case, any objects
that were selected before remain selected in the new displayed object's
array.

__See Also:__  [- redisplay](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxezlenfzxa3dbpe), [- allObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwc3dmj5rguzldorzq), [- displayedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg), [- qualifier](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfoi), [- selectedObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlmmvrxizlej5rguzldorzq), [- sortOrderings](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxg33sorhxezdfojuw4z3t)

---

### validatesChangesImmediately

`- (BOOL)validatesChangesImmediately`

Returns YES if the receiver immediately handles
validation errors, or leaves them for the EOEditingContext (defined
in the EOControl framework) to handle when saving changes.

By
default, WODisplayGroups don't validate changes immediately.

__See
Also:__  [- setValidatesChangesImmediately:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2enfzxa3dbpfdxe33voaxxgzlukzqwy2lemf2gk42dnbqw4z3fonew23lfmruwc5dfnr4tu), [+ globalDefaultForValidatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hui2ltobwgc6khojxxk4bpm5wg6ytbnrcgkztbovwhirtpojlgc3djmrqxizltinugc3thmvzus3lnmvsgsylumvwhs)

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
