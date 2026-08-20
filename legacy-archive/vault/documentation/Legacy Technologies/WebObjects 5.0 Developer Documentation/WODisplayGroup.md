---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Classes/WODisplayGroup.html
archived_at: '2026-07-15T08:15:15.511570Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# WODisplayGroup

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : NSKeyValueCoding: NSKeyValueCoding.ErrorHandling: NSInlineObservable: NSDisposable: EOKeyValueArchiving: EOKeyValueArchiving.Awaking

> **__Package:__**
> : com.webobjects.appserver

---

## Class Description

---

A WODisplayGroup is the basic user interface manager for a WebObjects application that accesses a database. It collects objects from an EODataSource (defined in EOControl), filters and sorts them, and maintains a selection in the filtered subset. You bind WebObjects dynamic elements to WODisplayGroup attributes and methods to display information from the database on your web page.

A WODisplayGroup manipulates its EODataSource by sending it fetchObjects, insertObject, and other messages, and registers itself as an editor and message handler of the EODataSource's EOEditingContext (also defined in EOControl). The EOEditingContext then monitors the WODisplayGroup for changes to objects.

Most of a WODisplayGroup's interactions are with its EODataSource and its EOEditingContext. See the EODataSource, and EOEditingContext class specifications in the _Enterprise Objects Framework Reference_ for more information on these interactions.

## The Delegate

The WODisplayGroup delegate offers a number of methods, and WODisplayGroup invokes them as appropriate. Besides displayGroupDisplayArrayForObjects, there are methods that inform the delegate that the WODisplayGroup has fetched, created an object (or failed to create one), inserted or deleted an object, changed the selection, or set a value for a property. There are also methods that request permission from the delegate to perform most of these same actions. The delegate can return `true` to permit the action or `false` to deny it. See each method's description in the WODisplayGroup.Delegates interface specification for more information.

## Constants

---

|  |  |
| --- | --- |
| __Class Variable__ | __Description__ |
| DisplayGroupWillFetchNotification | This class variable contains a String that names the notification posted at the beginning of WODisplayGroup's __fetch()__ method. |

## Interfaces Implemented

---

> : NSDisposable: [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonyg643f): : NSKeyValueCoding: [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc65dbnnsvmylmovsum33sjnsxs): [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc65tbnr2wkrtpojfwk6i): : NSKeyValueCoding.ErrorHandling: [handleQueryWithUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62dbnzsgyzkrovsxe6kxnf2gqvlomjxxk3tejnsxs): [handleTakeValueForUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62dbnzsgyzkumfvwkvtbnr2wkrtpojkw4ytpovxgis3fpe): [unableToSetNullForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc65lomfrgyzkun5jwk5coovwgyrtpojfwk6i): : EOKeyValueArchiving: [decodeWithKeyValueUnarchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjonygyylzi5zg65lqf5sgky3pmrsvo2lunbfwk6kwmfwhkzkvnzqxey3inf3gk4q): [encodeWithKeyValueArchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zlomnxwizkxnf2gqs3fpflgc3dvmvaxey3inf3gk4q): : EOKeyValueArchiving.Awaking: [awakeFromKeyValueUnarchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ylxmfvwkrtsn5wuwzlzkzqwy5lfkvxgc4tdnbuxmzls):

## Method Types

---

> **Constructor**
> : [WODisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6v2piruxg4dmmf4uo4tpovya)
>
> **Configuring behavior**
> : [setFetchesOnLoad](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fordgk5ddnbsxgt3ojrxwcza): [fetchesOnLoad](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ztforrwqzltj5xey33bmq): [setSelectsFirstObjectAfterFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forjwk3dfmn2hgrtjojzxit3cnjswg5cbmz2gk4sgmv2gg2a): [selectsFirstObjectAfterFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5dtizuxe43uj5rguzldorawm5dfojdgk5ddna): [setGlobalDefaultForValidatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjonygyylzi5zg65lqf5zwk5chnrxweylmirswmylvnr2em33skzqwy2lemf2gk42dnbqw4z3fonew23lfmruwc5dfnr4q): [globalDefaultForValidatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjonygyylzi5zg65lqf5twy33cmfweizlgmf2wy5cgn5zfmylmnfsgc5dfonbwqylom5sxgslnnvswi2lborswy6i): [setValidatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forlgc3djmrqxizltinugc3thmvzus3lnmvsgsylumvwhs): [validatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc65tbnruwiylumvzug2dbnztwk42jnvwwkzdjmf2gk3dz)
>
> **Setting the data source**
> : [setDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forcgc5dbknxxk4tdmu): [dataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdborqvg33vojrwk)
>
> **Setting the qualifier and sort ordering**
> : [setQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forixkylmnftgszls): [qualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztjmvza): [setSortOrderings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forjw64tuj5zgizlsnfxgo4y): [sortOrderings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643poj2e64temvzgs3thom)
>
> **Managing queries**
> : [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq): [queryMatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlborrwq): [queryMax](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlbpa): [queryMin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstljny): [queryOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpoi): [allQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ylmnrixkylmnftgszlsj5ygk4tborxxe4y): [relationalQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64tfnrqxi2lpnzqwyulvmfwgsztjmvze64dfojqxi33som): [stringQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643uojuw4z2rovqwy2lgnfsxet3qmvzgc5dpojzq): [setGlobalDefaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjonygyylzi5zg65lqf5zwk5chnrxweylmirswmylvnr2fg5dsnfxgotlborrwqrtpojwwc5a): [globalDefaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjonygyylzi5zg65lqf5twy33cmfweizlgmf2wy5ctorzgs3thjvqxiy3iizxxe3lboq): [setDefaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forcgkztbovwhiu3uojuw4z2nmf2gg2cgn5zg2ylu): [defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbdg64tnmf2a): [setGlobalDefaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjonygyylzi5zg65lqf5zwk5chnrxweylmirswmylvnr2fg5dsnfxgotlborrwqt3qmvzgc5dpoi): [globalDefaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjonygyylzi5zg65lqf5twy33cmfweizlgmf2wy5ctorzgs3thjvqxiy3ij5ygk4tborxxe): [setDefaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forcgkztbovwhiu3uojuw4z2nmf2gg2cpobsxeylun5za): [defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbhxazlsmf2g64q): [qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztziruxg4dmmf4uo4tpovya): [qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztzirqxiyktn52xey3f): [inQueryMode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62lokf2wk4tzjvxwizi): [setInQueryMode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forew4ulvmvzhstlpmrsq)
>
> **Fetching objects from the data source**
> : [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ztforrwq)
>
> **Getting the objects**
> : [allObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ylmnrhwe2tfmn2hg): [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y)
>
> **Batching the results**
> : [setNumberOfObjectsPerBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forhhk3lcmvze6zspmjvgky3uonigk4scmf2gg2a): [numberOfObjectsPerBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc63tvnvrgk4spmzhwe2tfmn2hgudfojbgc5ddna): [hasMultipleBatches](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62dbongxk3dunfygyzkcmf2gg2dfom): [displayNextBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzjzsxq5ccmf2gg2a): [displayPreviousBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzkbzgk5tjn52xgqtborrwq): [batchCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ytborrwqq3povxhi): [setCurrentBatchIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forbxk4tsmvxhiqtborrwqslomrsxq): [currentBatchIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6y3vojzgk3tuijqxiy3ijfxgizly): [indexOfFirstDisplayedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62lomrsxqt3gizuxe43uiruxg4dmmf4wkzcpmjvgky3u): [indexOfLastDisplayedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62lomrsxqt3gjrqxg5cenfzxa3dbpfswit3cnjswg5a): [displayBatchContainingSelectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzijqxiy3iinxw45dbnfxgs3thknswyzldorswit3cnjswg5a)
>
> **Updating display of values**
> : [redisplay](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64tfmruxg4dmmf4q): [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt)
>
> **Setting the objects**
> : [setObjectArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forhwe2tfmn2ec4tsmf4q)
>
> **Changing the selection**
> : [clearSelection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6y3mmvqxeu3fnrswg5djn5xa): [selectNext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5comv4hi): [selectObjectsIdenticalTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5cpmjvgky3uonewizlooruwgylmkrxq): [selectObjectsIdenticalToSelectFirstOnNoMatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5cpmjvgky3uonewizlooruwgylmkrxvgzlmmvrxirtjojzxit3ojzxu2ylumnua): [selectObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5cpmjvgky3u): [selectPrevious](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5cqojsxm2lpovzq): [setSelectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forjwk3dfmn2gkzcpmjvgky3u): [setSelectedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forjwk3dfmn2gkzcpmjvgky3uom): [setSelectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forjwk3dfmn2gs33ojfxgizlymvzq)
>
> **Examining the selection**
> : [selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5djn5xes3temv4gk4y): [selectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2a): [selectedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2hg)
>
> **Inserting and deleting objects**
> : [insertObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62loonsxe5cpmjvgky3uif2es3temv4a): [insertNewObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62loonsxe5comv3u6ytkmvrxiqlujfxgizly): [insert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62loonsxe5a): [setInsertedObjectDefaultValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forew443foj2gkzcpmjvgky3uirswmylvnr2fmylmovsxg): [insertedObjectDefaultValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62loonsxe5dfmrhwe2tfmn2eizlgmf2wy5cwmfwhkzlt): [deleteObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfnrsxizkpmjvgky3uif2es3temv4a): [deleteSelection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfnrsxizktmvwgky3unfxw4): [delete](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfnrsxizi)
>
> **Setting up a detail display group**
> : [hasDetailDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62dboncgk5dbnfweiylumfjw65lsmnsq): [setMasterObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forgwc43umvze6ytkmvrxi): [masterObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc63lbon2gk4spmjvgky3u): [setDetailKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forcgk5dbnfwewzlz): [detailKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdforqws3clmv4q)
>
> **Working with named fetch specifications**
> : [queryBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhsqtjnzsgs3thom)
>
> **Setting the delegate**
> : [setDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forcgk3dfm5qxizi): [delegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfnrswoylumu)

## Constructors

---

### WODisplayGroup

`public WODisplayGroup()`

Creates and returns a new WODisplayGroup. The WODisplayGroup then needs to have an EODataSource (defined in EOControl) set with [setDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forcgc5dbknxxk4tdmu).

---

## Static Methods

---

### decodeWithKeyValueUnarchiver

`public static Object decodeWithKeyValueUnarchiver( com.webobjects.eocontrol.EOKeyValueUnarchiver unarchiver)`

Conformance to EOKeyValueArchiving.

---

### globalDefaultForValidatesChangesImmediately

`public static boolean globalDefaultForValidatesChangesImmediately()`

Returns the class default controlling whether changes are immediately validated.

__See Also:__ [validatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc65tbnruwiylumvzug2dbnztwk42jnvwwkzdjmf2gk3dz)

---

### globalDefaultStringMatchFormat

`public static String globalDefaultStringMatchFormat()`

Returns the default string match format for the class.

__See Also:__ [defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbdg64tnmf2a)

---

### globalDefaultStringMatchOperator

`public static String globalDefaultStringMatchOperator()`

Returns the default string match operator for the class.

__See Also:__ [defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbhxazlsmf2g64q)

---

### setGlobalDefaultForValidatesChangesImmediately

`public static void setGlobalDefaultForValidatesChangesImmediately(boolean flag)`

Sets according to _flag_ the class default controlling whether changes are immediately validated.

__See Also:__ [setValidatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forlgc3djmrqxizltinugc3thmvzus3lnmvsgsylumvwhs)

---

### setGlobalDefaultStringMatchFormat

`public static void setGlobalDefaultStringMatchFormat(String format)`

Sets the default string match format for the class.

__See Also:__ [setDefaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forcgkztbovwhiu3uojuw4z2nmf2gg2cgn5zg2ylu)

---

### setGlobalDefaultStringMatchOperator

`public static void setGlobalDefaultStringMatchOperator(String operator)`

Sets the default string match operator for the class.

__See Also:__ [setDefaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forcgkztbovwhiu3uojuw4z2nmf2gg2cpobsxeylun5za)

---

## Instance Methods

---

### allObjects

`public NSArray allObjects()`

Returns all of the objects collected by the receiver.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ztforrwq)

---

### allQualifierOperators

`public NSArray allQualifierOperators()`

Returns an array containing all of the relational operators supported by EOControl's EOQualifier, including: =, !=, <, <=, >, >=, "__like__" and "__contains__".

__See Also:__ [queryOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpoi), [relationalQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64tfnrqxi2lpnzqwyulvmfwgsztjmvze64dfojqxi33som), [stringQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643uojuw4z2rovqwy2lgnfsxet3qmvzgc5dpojzq)

---

### awakeFromKeyValueUnarchiver

`public void awakeFromKeyValueUnarchiver( com.webobjects.eocontrol.EOKeyValueUnarchiver unarchiver)`

Conformance to EOKeyValueArchiving.Awaking.

---

### batchCount

`public int batchCount()`

The number of batches to display. For example, if the displayed objects array contains two hundred records and the batch size is ten, __batchCount__ returns twenty (twenty batches of ten records each).

__See Also:__ [currentBatchIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6y3vojzgk3tuijqxiy3ijfxgizly), [displayNextBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzjzsxq5ccmf2gg2a), [displayPreviousBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzkbzgk5tjn52xgqtborrwq), [hasMultipleBatches](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62dbongxk3dunfygyzkcmf2gg2dfom), [numberOfObjectsPerBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc63tvnvrgk4spmzhwe2tfmn2hgudfojbgc5ddna)

---

### clearSelection

`public boolean clearSelection()`

Invokes [setSelectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forjwk3dfmn2gs33ojfxgizlymvzq) to clear the selection, returning `true` on success and `false` on failure.

---

### currentBatchIndex

`public int currentBatchIndex()`

Returns the index of the batch currently being displayed. The total batch count equals the number of displayed objects divided by the batch size. For example, if the WODisplayGroup has one hundred objects to display and the batch size is twenty, there are five batches. The first batch has a batch index of 1.

__See Also:__ [batchCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ytborrwqq3povxhi), [numberOfObjectsPerBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc63tvnvrgk4spmzhwe2tfmn2hgudfojbgc5ddna), [setCurrentBatchIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forbxk4tsmvxhiqtborrwqslomrsxq)

---

### dataSource

`public com.webobjects.eocontrol.EODataSource dataSource()`

Returns the receiver's EODataSource (defined in the EOControl framework).

__See Also:__ [hasDetailDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62dboncgk5dbnfweiylumfjw65lsmnsq), [setDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forcgc5dbknxxk4tdmu)

---

### defaultStringMatchFormat

`public String defaultStringMatchFormat()`

Returns the format string that specifies how pattern matching will be performed on string values in the [queryMatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlborrwq) dictionary. If a key in the __queryMatch__ dictionary does not have an associated operator in the [queryOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpoi) dictionary, then its value is matched using pattern matching, and the format string returned by this method specifies how it will be matched.

__See Also:__ [defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbhxazlsmf2g64q), [setDefaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forcgkztbovwhiu3uojuw4z2nmf2gg2cgn5zg2ylu), [globalDefaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjonygyylzi5zg65lqf5twy33cmfweizlgmf2wy5ctorzgs3thjvqxiy3iizxxe3lboq)

---

### defaultStringMatchOperator

`public String defaultStringMatchOperator()`

Returns the operator used to perform pattern matching for string values in the [queryMatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlborrwq) dictionary. If a key in the __queryMatch__ dictionary does not have an associated operator in the [queryOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpoi) dictionary, then the operator returned by this method is used to perform pattern matching. Unless the default is changed, this method returns caseInsensitiveLike.

__See Also:__ [defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbdg64tnmf2a), [setDefaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forcgkztbovwhiu3uojuw4z2nmf2gg2cpobsxeylun5za), [globalDefaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjonygyylzi5zg65lqf5twy33cmfweizlgmf2wy5ctorzgs3thjvqxiy3ij5ygk4tborxxe)

---

### delegate

`public Object delegate()`

Returns the receiver's delegate.

__See Also:__ [setDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forcgk3dfm5qxizi)

---

### delete

`public Object delete()`

Uses [deleteSelection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfnrsxizktmvwgky3unfxw4) to attempt to delete the selected objects and then causes the page to reload. Returns `null` to force reloading of the web page.

__See Also:__ [deleteObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfnrsxizkpmjvgky3uif2es3temv4a)

---

### deleteObjectAtIndex

`public boolean deleteObjectAtIndex(int index)`

Attempts to delete the object at _index_, returning `true` if successful and `false` if not. Checks with the delegate using the method displayGroupShouldDeleteObject. If the delegate returns `false`, this method fails and returns `false`. If successful, it sends the delegate a displayGroupDidDeleteObject message.

This method performs the delete by sending the private method __deleteObject__ to the EODataSource (defined in the EOControl framework). If that message raises an exception, this method fails and returns `false`.

__See Also:__ [delete](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfnrsxizi), [deleteSelection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfnrsxizktmvwgky3unfxw4)

---

### deleteSelection

`public boolean deleteSelection()`

Attempts to delete the selected objects, returning `true` if successful and `false` if not.

__See Also:__ [delete](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfnrsxizi), [deleteObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfnrsxizkpmjvgky3uif2es3temv4a)

---

### detailKey

`public String detailKey()`

For detail display groups, returns the key to the master object that specifies what this detail display group represents. That is, if you send the object returned by the [masterObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc63lbon2gk4spmjvgky3u) method a [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc65tbnr2wkrtpojfwk6i) message with this key, you obtain the objects controlled by this display group.

This method returns `null` if the receiver is not a detail display group or if the detail key has not yet been set. You typically create a detail display group by dragging a to-many relationship from EOModeler to an open component in WebObjects Builder.

__See Also:__ [hasDetailDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62dboncgk5dbnfweiylumfjw65lsmnsq), [masterObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc63lbon2gk4spmjvgky3u), [setDetailKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forcgk5dbnfwewzlz)

---

### displayBatchContainingSelectedObject

`public Object displayBatchContainingSelectedObject()`

Displays the batch containing the selection and sets the current batch index to that batch's index. Returns `null` to force the page to reload.

__See Also:__ [displayNextBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzjzsxq5ccmf2gg2a), [displayPreviousBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzkbzgk5tjn52xgqtborrwq), [setCurrentBatchIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forbxk4tsmvxhiqtborrwqslomrsxq)

---

### displayedObjects

`public NSArray displayedObjects()`

Returns the objects that should be displayed or otherwise made available to the user, as filtered by the receiver's delegate, by the receiver's qualifier and sort ordering.

If batching is in effect, __displayedObjects__ returns the current batch of objects.

__See Also:__ [allObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ylmnrhwe2tfmn2hg), [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt), [qualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztjmvza), [setSortOrderings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forjw64tuj5zgizlsnfxgo4y), displayGroupDisplayArrayForObjects (delegate method)

---

### displayNextBatch

`public Object displayNextBatch()`

Increments the current batch index, displays that batch of objects, and clears the selection. If the batch currently being displayed is the last batch, this method displays the first batch of objects. Returns `null` to force the page to reload.

__See Also:__ [batchCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ytborrwqq3povxhi), [currentBatchIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6y3vojzgk3tuijqxiy3ijfxgizly), [displayBatchContainingSelectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzijqxiy3iinxw45dbnfxgs3thknswyzldorswit3cnjswg5a), [displayPreviousBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzkbzgk5tjn52xgqtborrwq)

---

### displayPreviousBatch

`public Object displayPreviousBatch()`

Decrements the current batch index, displays that batch of objects, and clears the selection. If the batch currently being displayed is the first batch, this method displays the last batch of objects. Returns `null` to force the page to reload.

__See Also:__ [batchCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ytborrwqq3povxhi), [currentBatchIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6y3vojzgk3tuijqxiy3ijfxgizly), [displayBatchContainingSelectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzijqxiy3iinxw45dbnfxgs3thknswyzldorswit3cnjswg5a), [displayNextBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzjzsxq5ccmf2gg2a)

---

### __dispose__

`public void dispose()`

Conformance to NSDisposable.

---

### editingContextPresentErrorMessage

`public void editingContextPresentErrorMessage( com.webobjects.eocontrol.EOEditingContext editingContext, String message)`

Invoked by the supplied EOEditingContext as part of the EOEditingContext.MessageHandlers interface, this method presents an attention panel with the supplied String as the message to display.

---

### encodeWithCoder

`public void encodeWithCoder(NSCoder coder)`

Encodes the receiver using the supplied NSCoder.

---

### encodeWithKeyValueArchiver

`public void encodeWithKeyValueArchiver( com.webobjects.eocontrol.EOKeyValueArchiver archiver)`

Conformance to EOKeyValueArchiving.

---

### __endEditing__

`public boolean endEditing()`

Attempts to end any editing taking place. If there's no editing association or if the editing association responds `true` to an __endEditing__ message, returns `true`. Otherwise returns `false`.

---

### fetch

`public Object fetch()`

Attempts to fetch objects from the EODataSource (defined in the EOControl framework).

Before fetching, this method sends displayGroupShouldFetch to the delegate. If this method was successful, it then sends a __fetchObjects__ message to the receiver's EODataSource to replace the object array, and if successful sends the delegate a displayGroupDidFetchObjects message.

This method returns `null` to force the page to reload.

__See Also:__ [allObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ylmnrhwe2tfmn2hg), [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt)

---

### fetchesOnLoad

`public boolean fetchesOnLoad()`

Returns `true` if the receiver fetches automatically after the component that contains it is loaded, `false` if it must be told explicitly to fetch. The default is `true`. You can set this behavior in WebObjects Builder using the Display Group Options panel. Note that if the display group fetches on load, it performs the fetch each time the component is loaded into the web browser.

__See Also:__ [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ztforrwq), [setFetchesOnLoad](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fordgk5ddnbsxgt3ojrxwcza)

---

### __finishInitialization__

`protected void finishInitialization()`

Invoked from the WODisplayGroup constructor and from __awakeFromNib__ to finish initializing a newly created display group. You should never invoke this method directly. Sets the receiver's editing context to it's data source's editing context (if available), registers the receiver for ObjectsChangedInEditingContextNotifications and InvalidatedAllObjectsInStoreNotifications, establishes the receiver as an editor for the editing context, and establishes the receiver as the editing context's message handler (unless the editing context already has a message handler).

---

### hasDetailDataSource

`public boolean hasDetailDataSource()`

Returns `true` if the display group's data source is an EODetailDataSource (defined in the EOControl framework), and `false` otherwise. If you drag a to-many relationship from EOModeler to an open component in WebObjects Builder, you create a display group that has an EODetailDataSource. You can also set this up using the Display Group Options panel in WebObjects Builder.

__See Also:__ [detailKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdforqws3clmv4q), [masterObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc63lbon2gk4spmjvgky3u)

---

### handleQueryWithUnboundKey

`public Object handleQueryWithUnboundKey(String key)`

Conformance to NSKeyValueCoding.ErrorHandling.

---

### handleTakeValueForUnboundKey

`public void handleTakeValueForUnboundKey(Object value, String key)`

Conformance to NSKeyValueCoding.ErrorHandling.

---

### hasMultipleBatches

`public boolean hasMultipleBatches()`

Returns `true` if the batch count is greater than 1. A display group displays its objects in batches if the [numberOfObjectsPerBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc63tvnvrgk4spmzhwe2tfmn2hgudfojbgc5ddna) method returns a number that is less than the number of objects in the [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y) array.

__See Also:__ [batchCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ytborrwqq3povxhi), [setNumberOfObjectsPerBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forhhk3lcmvze6zspmjvgky3uonigk4scmf2gg2a)

---

### indexOfFirstDisplayedObject

`public int indexOfFirstDisplayedObject()`

Returns the index of the first object displayed by the current batch. For example, if the current batch is displaying items 11 through 20, this method returns 11.

__See Also:__ [indexOfLastDisplayedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62lomrsxqt3gjrqxg5cenfzxa3dbpfswit3cnjswg5a)

---

### indexOfLastDisplayedObject

`public int indexOfLastDisplayedObject()`

Returns the index of the last object display by the current batch. For example, if the current batch is displaying items 11 through 20, this method returns 20.

__See Also:__ [indexOfFirstDisplayedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62lomrsxqt3gizuxe43uiruxg4dmmf4wkzcpmjvgky3u)

---

### initWithCoder

`public Object initWithCoder(NSCoder coder)`

Initializes a newly allocated instance from the supplied NSCoder. Returns `this`.

---

### inQueryMode

`public boolean inQueryMode()`

Returns `true` to indicate that the receiver is in query mode, `false` otherwise. In query mode, controls in the user interface that normally display values become empty, allowing users to type queries directly into them (this is also known as a "Query by Example" interface). In effect, the receiver's "displayedObjects" are replaced with an empty [queryMatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlborrwq) dictionary. When [qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztziruxg4dmmf4uo4tpovya) or [qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztzirqxiyktn52xey3f) is subsequently invoked, the query is performed and the display reverts to displaying values-this time, the objects returned by the query.

__See Also:__ [setInQueryMode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forew4ulvmvzhstlpmrsq)

---

### insert

`public Object insert()`

Invokes [insertNewObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62loonsxe5comv3u6ytkmvrxiqlujfxgizly) with an index just past the first index in the selection, or at the end if there's no selection.

This method returns `null` to force the page to reload.

---

### insertedObjectDefaultValues

`public NSDictionary insertedObjectDefaultValues()`

Returns the default values to be used for newly inserted objects. The keys into the dictionary are the properties of the entity that the display group manages. If the dictionary returned by this method is empty, the [insert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62loonsxe5a) method adds an object that is initially empty. Because the object is empty, the display group has no value to display on the HTML page for that object, meaning that there is nothing for the user to select and modify. Use the [setInsertedObjectDefaultValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forew443foj2gkzcpmjvgky3uirswmylvnr2fmylmovsxg) method to set up a default value so that there is something to display on the page.

---

### insertNewObjectAtIndex

`public Object insertNewObjectAtIndex(int index)`

Asks the receiver's EODataSource (defined in the EOControl framework) to create a new object by sending it a __createObject__ message, then inserts the new object using [insertObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62loonsxe5cpmjvgky3uif2es3temv4a). If a new object can't be created, this method sends the delegate a displayGroupCreateObjectFailedForDataSource message.

If the object is successfully created, this method then sets the default values specified by [insertedObjectDefaultValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62loonsxe5dfmrhwe2tfmn2eizlgmf2wy5cwmfwhkzlt).

__See Also:__ [insert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62loonsxe5a)

---

### insertObjectAtIndex

`public void insertObjectAtIndex( Object anObject, int index)`

Inserts _anObject_ into the receiver's EODataSource and displayed objects at the specified index, if possible. This method checks with the delegate before actually inserting, using displayGroupShouldInsertObject. If the delegate refuses, _anObject_ isn't inserted. After successfully inserting the object, this method informs the delegate with a displayGroupD:idInsertObject message, and selects the newly inserted object.

Raises an exception if _index_ is out of bounds.

__See Also:__ [insertNewObjectAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62loonsxe5comv3u6ytkmvrxiqlujfxgizly), [insert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62loonsxe5a)

---

### __localKeys__

`public NSArray localKeys()`

Returns the additional keys that EOAssociations can be bound to. A WODisplayGroup's basic keys are typically those of the attributes and relationships of its objects, as defined by their EOClassDescription through an EOEntity in the model. Local keys are typically used to form associations with key paths, with arbitrary methods of objects, or with properties of objects not associated with an EOEntity.

---

### masterObject

`public Object masterObject()`

Returns the master object for a detail display group (a display group that represents a detail in a master-detail relationship). A detail display group is one that uses an EODetailDataSource (defined in the EOControl framework). You create a detail display group by dragging a to-many relationship from EOModeler to an open component in WebObjects Builder. If the display group is not a detail display group or does not have a master object set, this method returns null.

__See Also:__ [detailKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdforqws3clmv4q), [hasDetailDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62dboncgk5dbnfweiylumfjw65lsmnsq), [setMasterObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forgwc43umvze6ytkmvrxi)

---

### numberOfObjectsPerBatch

`public int numberOfObjectsPerBatch()`

Returns the batch size. You can set the batch size using [setNumberOfObjectsPerBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forhhk3lcmvze6zspmjvgky3uonigk4scmf2gg2a) or using WebObjects Builder's Display Group Options panel.

---

### objectsChangedInEditingContext

`public void objectsChangedInEditingContext(NSNotification notification)`

Redisplays the changed objects in the display group unless the display group's delegate method __displayGroupShouldRedisplay__ indicates that a redisplay should not take place.

---

### objectsInvalidatedInEditingContext

`public void objectsInvalidatedInEditingContext(NSNotification notification)`

Refetches all objects in the receiving display group unless the display group's delegate method __displayGroupShouldRefetch__ indicates that a refetch should not take place.

---

### qualifier

`public com.webobjects.eocontrol.EOQualifier qualifier()`

Returns the receiver's qualifier, which it uses to filter its array of objects for display when the delegate doesn't do so itself.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [setQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forixkylmnftgszls), [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt)

---

### qualifierFromQueryValues

`public com.webobjects.eocontrol.EOQualifier qualifierFromQueryValues()`

Builds a qualifier constructed from entries in these query dictionaries: [queryMatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlborrwq), [queryMax](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlbpa), [queryMin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstljny), and [queryOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpoi).

__See Also:__ [qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztzirqxiyktn52xey3f), [qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztziruxg4dmmf4uo4tpovya)

---

### qualifyDataSource

`public void qualifyDataSource()`

Takes the result of [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq) and applies to the receiver's data source. The receiver then sends itself a [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ztforrwq) message. If the receiver is in query mode, query mode is exited. This method differs from [qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztziruxg4dmmf4uo4tpovya) as follows: whereas __qualifyDisplayGroup__ performs in-memory filtering of already fetched objects, __qualifyDataSource__ triggers a new qualified fetch against the database.

__See Also:__ [queryMatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlborrwq), [queryMax](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlbpa),, [queryMin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstljny), [queryOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpoi)

---

### qualifyDisplayGroup

`public void qualifyDisplayGroup()`

Takes the result of the [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq) and applies to the receiver using [setQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forixkylmnftgszls). The method [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt) is invoked to refresh the display. If the receiver is in query mode, query mode is exited.

__See Also:__ [qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztzirqxiyktn52xey3f), [queryMatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlborrwq), [queryMax](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlbpa), - [queryMin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstljny), [queryOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpoi)

---

### queryBindings

`public NSMutableDictionary queryBindings()`

Returns a dictionary containing the actual values that the user wants to query upon. You use this method to perform a query stored in the model file. Bind keys in this dictionary to elements on your component that specify query values, then pass this dictionary to the fetch specification that performs the fetch.

---

### queryMatch

`public NSMutableDictionary queryMatch()`

Returns a dictionary of query values to match. The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq) method uses this dictionary along with the [queryMax](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlbpa) and [queryMin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstljny) dictionaries to construct qualifiers.

Use the [queryOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpoi) dictionary to specify the type of matching (=, <, >, __like__, and so on) for each key in the __queryMatch__ dictionary.

If the __queryOperator__ dictionary does not contain a key contained in the __queryMatch__ dictionary, the default is to match the value exactly (=) if the value is a number or a date and to perform pattern matching if the value is a String. In the case of string values, the [defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbdg64tnmf2a) and [defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbhxazlsmf2g64q) specify exactly how the pattern matching will be performed.

__See Also:__ [allQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ylmnrixkylmnftgszlsj5ygk4tborxxe4y), [qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztzirqxiyktn52xey3f), [qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztziruxg4dmmf4uo4tpovya), [relationalQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64tfnrqxi2lpnzqwyulvmfwgsztjmvze64dfojqxi33som)

---

### queryMax

`public NSMutableDictionary queryMax()`

Returns a dictionary of "less than" query values. The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq) method uses this dictionary along with the [queryMatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlborrwq) and [queryMin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstljny) dictionaries to construct qualifiers.

__See Also:__ [qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztzirqxiyktn52xey3f), [qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztziruxg4dmmf4uo4tpovya), [queryOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpoi)

---

### queryMin

`public NSMutableDictionary queryMin()`

Returns a dictionary of "greater than" query values. The [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq) method uses this dictionary along with the [queryMatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlborrwq) and __queryMin__ dictionaries to construct qualifiers.

__See Also:__ [qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztzirqxiyktn52xey3f), [qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztziruxg4dmmf4uo4tpovya), [queryOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpoi)

---

### queryOperator

`public NSMutableDictionary queryOperator()`

Returns a dictionary of operators to use on items in the [queryMatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlborrwq) dictionary. If a key in the __queryMatch__ dictionary also exists in __queryOperator__, that operator for that key is used. The [allQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ylmnrixkylmnftgszlsj5ygk4tborxxe4y) method returns the operator strings you can use as values in this dictionary.

__See Also:__ [qualifierFromQueryValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztjmvzem4tpnvixkzlspflgc3dvmvzq), [queryMax](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlbpa), [queryMin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstljny), [relationalQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64tfnrqxi2lpnzqwyulvmfwgsztjmvze64dfojqxi33som)

---

### redisplay

`public void redisplay()`

Sends out a contents changed notification.

---

### relationalQualifierOperators

`public NSArray relationalQualifierOperators()`

Returns an array containing all of the relational operators supported by EOControl's EOQualifier: =, !=, <, <=, >, and >=. In other words, returns all of the EOQualifier operators except for the ones that work exclusively on strings (such as "__like__" and "__contains__").

__See Also:__ [allQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ylmnrixkylmnftgszlsj5ygk4tborxxe4y), [queryOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpoi), [stringQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643uojuw4z2rovqwy2lgnfsxet3qmvzgc5dpojzq)

---

### selectedObject

`public Object selectedObject()`

Returns the first selected object in the displayed objects array, or `null` if there's no such object.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5djn5xes3temv4gk4y), [selectedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2hg)

---

### selectedObjects

`public NSArray selectedObjects()`

Returns the objects selected in the receiver's displayed objects array.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5djn5xes3temv4gk4y), [selectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2a)

---

### selectionIndexes

`public NSArray selectionIndexes()`

Returns the selection as an array of integers . The integers are indexes into the array returned by [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y).

__See Also:__ [selectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2a), [selectedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2hg), [setSelectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forjwk3dfmn2gs33ojfxgizlymvzq)

---

### selectNext

`public Object selectNext()`

Attempts to select the object just after the currently selected one. The selection is altered in this way:

- If there are no objects, does nothing.
- If there's no selection, selects the object at index zero.
- If the first selected object is the last object in the displayed objects array, selects the first object.
- Otherwise selects the object after the first selected object.

This method returns `null` to force the page to reload.

__See Also:__ [selectPrevious](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5cqojsxm2lpovzq), [setSelectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forjwk3dfmn2gs33ojfxgizlymvzq)

---

### selectObject

`public boolean selectObject(Object anObject)`

Attempts to select the object equal to _anObject_ in the receiver's displayed objects array, returning `true` if successful and `false` otherwise. _anObject_ is equal to an object in the displayed objects array if its address is the same as the object in the array.

__See Also:__ [selectNext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5comv4hi), [selectPrevious](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5cqojsxm2lpovzq)

---

### selectObjectsIdenticalTo

`public boolean selectObjectsIdenticalTo(NSArray objectSelection)`

Attempts to select the objects in the receiver's displayed objects array whose addresses are equal to those of objects, returning `true` if successful and `false` otherwise.

__See Also:__ [setSelectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forjwk3dfmn2gs33ojfxgizlymvzq), [selectObjectsIdenticalToSelectFirstOnNoMatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5cpmjvgky3uonewizlooruwgylmkrxvgzlmmvrxirtjojzxit3ojzxu2ylumnua)

---

### selectObjectsIdenticalToSelectFirstOnNoMatch

`public boolean selectObjectsIdenticalToSelectFirstOnNoMatch( NSArray objects, boolean flag)`

Selects the objects in the receiver's displayed objects array whose addresses are equal to those of _objects_, returning `true` if successful and `false` otherwise. If no objects in the displayed _objects_ array match objects and _flag_ is `true`, attempts to select the first object in the displayed objects array.

__See Also:__ [setSelectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forjwk3dfmn2gs33ojfxgizlymvzq), [selectObjectsIdenticalTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5cpmjvgky3uonewizlooruwgylmkrxq)

---

### selectPrevious

`public Object selectPrevious()`

Attempts to select the object just before the presently selected one. The selection is altered in this way:

- If there are no objects, does nothing.
- If there's no selection, selects the object at index zero.
- If the first selected object is at index zero, selects the last object.
- Otherwise selects the object before the first selected object.

This method returns `null` to force the page to reload.

__See Also:__ [selectNext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5comv4hi), [redisplay](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64tfmruxg4dmmf4q)

---

### selectsFirstObjectAfterFetch

`public boolean selectsFirstObjectAfterFetch()`

Returns `true` if the receiver automatically selects its first displayed object after a fetch if there was no selection, `false` if it leaves an empty selection as-is.

WODisplayGroups by default do select the first object after a fetch when there was no previous selection.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ztforrwq), [setSelectsFirstObjectAfterFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forjwk3dfmn2hgrtjojzxit3cnjswg5cbmz2gk4sgmv2gg2a)

---

### setCurrentBatchIndex

`public void setCurrentBatchIndex(int anInt)`

Displays the _anInt_ batch of objects. The total batch count equals the number of displayed objects divided by the batch size. For example, if the WODisplayGroup has one hundred objects to display and the batch size is twenty, there are five batches. The first batch has a batch index of 1. setCurrentBatchIndex(3) would display the third batch of objects (objects 41 to 60 in this example).

If _anInt_ is greater than the number of batches, this method displays the first batch.

__See Also:__ [batchCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ytborrwqq3povxhi), [currentBatchIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6y3vojzgk3tuijqxiy3ijfxgizly), [displayBatchContainingSelectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzijqxiy3iinxw45dbnfxgs3thknswyzldorswit3cnjswg5a), [displayNextBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzjzsxq5ccmf2gg2a), [displayPreviousBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzkbzgk5tjn52xgqtborrwq), [numberOfObjectsPerBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc63tvnvrgk4spmzhwe2tfmn2hgudfojbgc5ddna)

---

### setDataSource

`public void setDataSource( com.webobjects.eocontrol.EODataSource aDataSource)`

Sets the receiver's EODataSource (defined in the EOControl framework) to _aDataSource_. In the process, it performs these actions:

- Unregisters itself as an editor and message handler for the previous EODataSource's EOEditingContext (also defined in EOControl), if necessary, and registers itself with _aDataSource_'s EOEditingContext. If the new EOEditingContext already has a message handler, however, the receiver doesn't assume that role.
- Clears the receiver's array of objects.
- Sends displayGroupDidChangeDataSource to the delegate if there is one.

__See Also:__ [dataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdborqvg33vojrwk)

---

### setDefaultStringMatchFormat

`public void setDefaultStringMatchFormat(String format)`

Sets how pattern matching will be performed on String values in the [queryMatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlborrwq) dictionary. This format is used for properties listed in the __queryMatch__ dictionary that have String values and that do not have an associated entry in the [queryOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpoi) dictionary. In these cases, the value is matched using pattern matching and format specifies how it will be matched.

The default format string for pattern matching is "__%@\*__" which means that the string value in the __queryMatch__ dictionary is used as a prefix (this default can be overridden on a class basis using [setGlobalDefaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjonygyylzi5zg65lqf5zwk5chnrxweylmirswmylvnr2fg5dsnfxgotlborrwqrtpojwwc5a)). For example, if the __queryMatch__ dictionary contains a value "Jo" for the key "Name", the query returns all records whose name values begin with "Jo".

__See Also:__ [defaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbdg64tnmf2a), [setDefaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forcgkztbovwhiu3uojuw4z2nmf2gg2cpobsxeylun5za), [setGlobalDefaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjonygyylzi5zg65lqf5zwk5chnrxweylmirswmylvnr2fg5dsnfxgotlborrwqrtpojwwc5a)

---

### setDefaultStringMatchOperator

`public void setDefaultStringMatchOperator(String operator)`

Sets the operator used to perform pattern matching for String values in the [queryMatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlborrwq) dictionary. This operator is used for properties listed in the __queryMatch__ dictionary that have String values and that do not have an associated entry in the [queryOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhst3qmvzgc5dpoi) dictionary. In these cases, the operator operator is used to perform pattern matching.

The default value for the query match operator is __caseInsensitiveLike__, which means that the query does not consider case when matching letters (this default can be overridden on a class basis using [setGlobalDefaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjonygyylzi5zg65lqf5zwk5chnrxweylmirswmylvnr2fg5dsnfxgotlborrwqt3qmvzgc5dpoi)). The other possible value for this operator is __like__, which matches the case of the letters exactly.

__See Also:__ [allQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ylmnrixkylmnftgszlsj5ygk4tborxxe4y), [defaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfmzqxk3dukn2he2lom5gwc5ddnbhxazlsmf2g64q), [relationalQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64tfnrqxi2lpnzqwyulvmfwgsztjmvze64dfojqxi33som), [setDefaultStringMatchFormat](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forcgkztbovwhiu3uojuw4z2nmf2gg2cgn5zg2ylu), [setGlobalDefaultStringMatchOperator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjonygyylzi5zg65lqf5zwk5chnrxweylmirswmylvnr2fg5dsnfxgotlborrwqt3qmvzgc5dpoi)

---

### setDelegate

`public void setDelegate(Object anObject)`

Sets the receiver's delegate to _anObject_.

__See Also:__ [delegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdfnrswoylumu), WODisplayGroup.Delegate

---

### setDetailKey

`public void setDetailKey(String detailKey)`

Sets the detail key to _detailKey_ for a detail display group. The detail key is the key that retrieves from the master object the objects that this display group manages. You must set a detail key before you set a master object.

If the receiver is not a detail display group, this method has no effect. A display group is a detail display group if its data source is an EODetailDataSource (defined in the EOControl framework). You typically create a detail display group by dragging a to-many relationship from EOModeler to an open component in WebObjects Builder. Doing so sets the detail key and master object, so you rarely need to use this method.

__See Also:__ [hasDetailDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62dboncgk5dbnfweiylumfjw65lsmnsq), [detailKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdforqws3clmv4q), [setMasterObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forgwc43umvze6ytkmvrxi)

---

### setFetchesOnLoad

`public void setFetchesOnLoad(boolean flag)`

Controls whether the receiver automatically fetches its objects after being loaded. If _flag_ is `true` it does; if _flag_ is `false` the receiver must be told explicitly to fetch. The default is `false`. You can also set this behavior in WebObjects Builder in the Display Group Options panel.

__See Also:__ [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ztforrwq), [fetchesOnLoad](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ztforrwqzltj5xey33bmq)

---

### setInQueryMode

`public void setInQueryMode(boolean flag)`

Sets according to _flag_ whether the receiver is in query mode. In query mode, controls in the user interface that normally display values become empty, allowing users to type queries directly into them (this is also known as a "Query by Example" interface). In effect, the receiver's "displayedObjects" are replaced with an empty [queryMatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmvzhstlborrwq) dictionary. When [qualifyDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztziruxg4dmmf4uo4tpovya) or [qualifyDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztzirqxiyktn52xey3f) is subsequently invoked, the query is performed and the display reverts to displaying values-this time, the objects returned by the query.

__See Also:__ [inQueryMode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62lokf2wk4tzjvxwizi)

---

### setInsertedObjectDefaultValues

`public void setInsertedObjectDefaultValues(NSDictionary defaultValues)`

Sets default values to be used for newly inserted objects. When you use the [insert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62loonsxe5a) method to add an object, that object is initially empty. Because the object is empty, there is no value to be displayed on the HTML page, meaning there is nothing for the user to select and modify. You use this method to provide at least one field that can be displayed for the newly inserted object. The possible keys into the dictionary are the properties of the entity managed by this display group.

__See Also:__ [insertedObjectDefaultValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62loonsxe5dfmrhwe2tfmn2eizlgmf2wy5cwmfwhkzlt)

---

### setLocalKeys

`public void setLocalKeys(NSArray newKeySet)`

Sets the additional keys to which EOAssociations can be bound to the strings in supplied NSArray.

---

### setMasterObject

`public void setMasterObject(Object masterObject)`

Sets the master object to _masterObject_ for detail display groups and then performs a fetch if the display group is set to fetch on load. The master object owns the objects controlled by this display group.

Before you use this method, you should use the [setDetailKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forcgk5dbnfwewzlz) to set the key to this relationship. You typically create a detail display group by dragging a to-Many relationship from EOModeler to an open component in WebObjects Builder. Doing so sets the master object and detail key, so you typically do not have to use this method.

If the receiver is not a detail display group, this method has no effect.

__See Also:__ [hasDetailDataSource](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc62dboncgk5dbnfweiylumfjw65lsmnsq), [masterObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc63lbon2gk4spmjvgky3u)

---

### setNumberOfObjectsPerBatch

`public void setNumberOfObjectsPerBatch(int count)`

Sets the number of objects the receiver displays at a time. For example, suppose you are displaying one hundred records. Instead of displaying all of these at once, you can set the batch size so that the page displays a more manageable number (for example, 10). WebObjects Builder allows you to set the number of objects per batch on the Display Group Options panel.

__See Also:__ [batchCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ytborrwqq3povxhi), [displayNextBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzjzsxq5ccmf2gg2a), [displayPreviousBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzkbzgk5tjn52xgqtborrwq), [numberOfObjectsPerBatch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc63tvnvrgk4spmzhwe2tfmn2hgudfojbgc5ddna)

---

### setObjectArray

`public void setObjectArray(NSArray objects)`

Sets the receiver's objects to _objects_, regardless of what its EODataSource (defined in the EOControl framework) provides. This method doesn't affect the EODataSource's objects at all; specifically, it results in neither inserts nor deletes of objects in the EODataSource. objects should contain objects with the same property names or methods as those accessed by the receiver. This method is used by __fetch__ to set the array of fetched objects; you should rarely need to invoke it directly.

After setting the object array, this method restores as much of the original selection as possible. If there's no match and the receiver selects after fetching, then the first object is selected.

__See Also:__ [allObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ylmnrhwe2tfmn2hg), [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ztforrwq), [selectsFirstObjectAfterFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5dtizuxe43uj5rguzldorawm5dfojdgk5ddna)

---

### setQualifier

`public void setQualifier(com.webobjects.eocontrol.EOQualifier aQualifier)`

Sets the receiver's qualifier to _aQualifier_. This qualifier is used to filter the receiver's array of objects for display. Use [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt) to apply the qualifier.

If the receiver's delegate responds to displayGroupDisplayArrayForObjects, that method is used instead of the qualifier to filter the objects.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [qualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztjmvza)

---

### setSelectedObject

`public void setSelectedObject(Object anObject)`

Sets the first selected object in the displayed objects array to _anObject_.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5djn5xes3temv4gk4y), [selectedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2hg)

---

### setSelectedObjects

`public void setSelectedObjects(NSArray objects)`

Sets the objects selected in the receiver's displayed objects array to _objects_.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5djn5xes3temv4gk4y), [selectedObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2a)

---

### setSelectionIndexes

`public boolean setSelectionIndexes(NSArray selection)`

Selects the objects at selection in the receiver's array if possible, returning `true` if successful and `false` if not (in which case the selection remains unaltered). _selection_ is an array of Integers. This method is the primitive method for altering the selection; all other such methods invoke this one to make the change.

This method checks the delegate with a displayGroupShouldChangeSelectionToIndexes message. If the delegate returns `false`, this method also fails and returns `false`. If the receiver successfully changes the selection, its observers each receive a subjectChanged message and, if necessary, a displayGroupDidChangeSelectedObjects message.

|  |
| --- |
| __Note:__ The selection set here is only a programmatic selection; the objects on the screen are not highlighted in any way. |

__See Also:__ [allObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ylmnrhwe2tfmn2hg)

---

### setSelectsFirstObjectAfterFetch

`public void setSelectsFirstObjectAfterFetch(boolean flag)`

Controls whether the receiver automatically selects its first displayed object after a fetch when there were no selected objects before the fetch. If _flag_ is `true` it does; if _flag_ is `false` then no objects are selected.

WODisplayGroups by default do select the first object after a fetch when there was no previous selection.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [fetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ztforrwq), [selectsFirstObjectAfterFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5dtizuxe43uj5rguzldorawm5dfojdgk5ddna)

---

### setSortOrderings

`public void setSortOrderings(NSArray keySortOrderArray)`

Sets the EOSortOrdering objects (defined in the EOControl framework) that [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt) uses to sort the displayed objects to orderings. Use __updateDisplayedObjects__ to apply the sort orderings.You can also set this value using the WebObjects Builder Display Group Options panel.

If the receiver's delegate responds to __displayGroupDisplayArrayForObjects__, that method is used instead of the sort orderings to order the objects.

__See Also:__ [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [sortOrderings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643poj2e64temvzgs3thom), [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt)

---

### setValidatesChangesImmediately

`public void setValidatesChangesImmediately(boolean flag)`

Controls the receiver's behavior on encountering a validation error. In the Web context, this method has no effect.

WODisplayGroups by default don't validate changes immediately (although this default can be overridden on a class basis; see [setGlobalDefaultForValidatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjonygyylzi5zg65lqf5zwk5chnrxweylmirswmylvnr2em33skzqwy2lemf2gk42dnbqw4z3fonew23lfmruwc5dfnr4q)).

__See Also:__ - saveChanges (in EOControl's EOEditingContext), - tryToSaveChanges (EOEditingContext Additions), [validatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc65tbnruwiylumvzug2dbnztwk42jnvwwkzdjmf2gk3dz), [setGlobalDefaultForValidatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjonygyylzi5zg65lqf5zwk5chnrxweylmirswmylvnr2em33skzqwy2lemf2gk42dnbqw4z3fonew23lfmruwc5dfnr4q)

---

### sortOrderings

`public NSArray sortOrderings()`

Returns an array of EOSortOrdering objects (defined in the EOControl framework) that [updateDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc65lqmrqxizkenfzxa3dbpfswit3cnjswg5dt) uses to sort the displayed objects, as returned by the [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y) method.

__See Also:__ [setSortOrderings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forjw64tuj5zgizlsnfxgo4y)

---

### stringQualifierOperators

`public NSArray stringQualifierOperators()`

Returns an array containing all of the relational operators supported by EOControl's EOQualifier that work exclusively on strings: "starts with", "contains", "ends with", "is", and "like".

__See Also:__ [allQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ylmnrixkylmnftgszlsj5ygk4tborxxe4y), [relationalQualifierOperators](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64tfnrqxi2lpnzqwyulvmfwgsztjmvze64dfojqxi33som)

---

### takeValueForKey

`public void takeValueForKey(Object value, String key)`

Conformance to NSKeyValueCoding.

---

### toString

`public String toString()`

Returns a String containing a string representation of the receiver.

---

### unableToSetNullForKey

`public void unableToSetNullForKey(String key)`

Conformance to NSKeyValueCoding.ErrorHandling.

---

### __undoManager__

`public NSUndoManager undoManager()`

Returns the receiver's undo manager.

---

### updateDisplayedObjects

`public void updateDisplayedObjects()`

Recalculates the receiver's displayed objects arrays and redisplays. If the delegate responds to displayGroupDisplayArrayForObjects, it's sent this message and the returned array is set as the WODisplayGroup's displayed objects. Otherwise, the receiver applies its qualifier and sort ordering to its array of objects. In either case, any objects that were selected before remain selected in the new displayed object's array.

__See Also:__ [redisplay](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64tfmruxg4dmmf4q), [allObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6ylmnrhwe2tfmn2hg), [displayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc6zdjonygyylzmvse6ytkmvrxi4y), [qualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc64lvmfwgsztjmvza), [selectedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643fnrswg5dfmrhwe2tfmn2hg), [sortOrderings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643poj2e64temvzgs3thom)

---

### validatesChangesImmediately

`public boolean validatesChangesImmediately()`

Returns `true` if the receiver immediately handles validation errors, or leaves them for the EOEditingContext (defined in the EOControl framework) to handle when saving changes.

By default, WODisplayGroups don't validate changes immediately.

__See Also:__ [setValidatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2piruxg4dmmf4uo4tpovyc643forlgc3djmrqxizltinugc3thmvzus3lnmvsgsylumvwhs), [globalDefaultForValidatesChangesImmediately](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6rdjonygyylzi5zg65lqf5twy33cmfweizlgmf2wy5cgn5zfmylmnfsgc5dfonbwqylom5sxgslnnvswi2lborswy6i)

---

### valueForKey

`public Object valueForKey(String key)`

Conformance to NSKeyValueCoding.

---

### __willChange__

`public void willChange()`

Notifies observers that the receiver will change.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
