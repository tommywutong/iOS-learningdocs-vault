---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EODatabaseContext.html
archived_at: '2026-07-15T08:11:33.511633Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EODatabaseContext

> __Inherits
> from:__  EOCooperatingObjectStore : EOObjectStore : NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  EOAccess/EODatabaseContext.h

---

## Class Description

---

An EODatabaseContext object is an EOObjectStore (EOControl)
for accessing relational databases, creating and saving objects
based on EOEntity definitions in an EOModel.

An EODatabaseContext represents a single connection to a database
server, and it determines the updating and locking strategy used
by its EODatabaseChannel objects. An EODatabaseContext has a corresponding
EODatabase object. If the server supports multiple concurrent transactions,
the EODatabase object may have several database contexts. If the
server and adaptor support it, a database context may in turn have
several database channels, which handle access to the data on the
server.

For a more information on EODatabaseContext, see the sections:

- ["EODatabaseContext's Interaction with Other Classes"](EODatabaseContext-3.md#apple-ijduurkcijbuq)
- ["Creating and Using an EODatabaseContext"](EODatabaseContext-3.md#apple-ijduuqsci5dem)
- ["Fetching and Saving Objects"](EODatabaseContext-3.md#apple-ijduuqseijeuk)
- ["Using a Custom Query"](EODatabaseContext-3.md#apple-ijduurcjijeuo)
- ["Faulting"](EODatabaseContext-3.md#apple-ijduurcjjfdus)
- ["Delegate Methods"](EODatabaseContext-3.md#apple-ijduuq2kinbuk)
- ["Snapshots"](EODatabaseContext-3.md#apple-ijduurcdjjaum)
- ["Updating And Locking Strategies"](EODatabaseContext-3.md#apple-inbuuq2hjjauo)

## Constants

---

In EODatabaseContext.h, EOAccess defines
an enumeration type, `EOUpdateStrategy`,
to identify update strategies. It's constants and the other constants
defined in the EODatabaseContext.h are described
in the following table:

|  |  |  |
| --- | --- | --- |
| __Constant__ | __Type__ | __Description__ |
| EOUpdateWithOptimisticLocking | `EOUpdateStrategy` | Identifies the locking strategy as optimistic. |
| EOUpdateWithPessimisticLocking | `EOUpdateStrategy` | Identifies the locking strategy as pessimistic |
| EOUpdateWithNoLocking | `EOUpdateStrategy` | Identifies the locking strategy as no locking |
| EOCustomQueryExpressionHintKey | NSString | A key in an EOFetchSpecification's hint dictionary |
| EOStoredProcedureNameHintKey | NSString | A key in an EOFetchSpecification's hint dictionary |
| EODatabaseContextKey | NSString | A key in an `EOGenericAdaptorException`'s userInfo dictionary |
| EODatabaseOperationsKey | NSString | A key in an `EOGenericAdaptorException`'s userInfo dictionary |
| EOFailedDatabaseOperationKey | NSString | A key in an `EOGenericAdaptorException`'s userInfo dictionary |

In addition, EODatabaseContext defines a constant for the
name of the notification it posts. For more information on the notification,
see ["Notifications"](#apple-irauoscdjfees).

## Method Types

---

> **Initializing instances**
> : [- initWithDatabase:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfxgs5cxnf2gqrdborqweyltmu5a)
>
> **Fetching objects**
> : [- objectsWithFetchSpecification:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpn5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63r2mvsgs5djnztug33oorsxq5b2)
> : [- objectsForSourceGlobalID:relationshipName:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpn5rguzldorzum33sknxxk4tdmvdwy33cmfwesrb2ojswyylunfxw443infye4ylnmu5gkzdjoruw4z2dn5xhizlyoq5a)
> : [- arrayFaultWithSourceGlobalID:relationshipName:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmfzheylzizqxk3duk5uxi2ctn52xey3fi5wg6ytbnreuiotsmvwgc5djn5xhg2djobhgc3lfhjswi2lunfxgoq3pnz2gk6duhi)
> : [- faultForGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzqxk3duizxxer3mn5rgc3cjiq5gkzdjoruw4z2dn5xhizlyoq5a)
> : [- faultForRawRow:entityNamed:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzqxk3duizxxeutbo5jg65z2mvxhi2lupfhgc3lfmq5gkzdjoruw4z2dn5xhizlyoq5a)
> : [- batchFetchRelationship:forSourceObjects:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmjqxiy3iizsxiy3ikjswyylunfxw443infyduztpojjw65lsmnsu6ytkmvrxi4z2mvsgs5djnztug33oorsxq5b2)
> : [- missingObjectGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnvuxg43jnztu6ytkmvrxir3mn5rgc3cjirzq)
>
> **Enabling shared object
> loading**
> : [+ setSharedObjectLoadingEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuiylumfrgc43finxw45dfpb2c643forjwqylsmvse6ytkmvrxitdpmfsgs3thivxgcytmmvsdu)
> : [+ isSharedObjectLoadingEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuiylumfrgc43finxw45dfpb2c62ltknugc4tfmrhwe2tfmn2ey33bmruw4z2fnzqwe3dfmq)
>
> **Accessing the adaptor
> context**
> : [- adaptorContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmfsgc4dun5zeg33oorsxq5a)
>
> **Managing the database
> connection**
> : [+ forceConnectionWithModel:connectionDictionaryOverrides:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuiylumfrgc43finxw45dfpb2c6ztpojrwkq3pnzxgky3unfxw4v3jorue233emvwduy3pnzxgky3unfxw4rdjmn2gs33omfzhst3wmvzhe2lemvztuzlenf2gs3thinxw45dfpb2du)
> : [- handleDroppedConnection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnbqw4zdmmvche33qobswiq3pnzxgky3unfxw4)
>
> **Accessing the database
> object**
> : [- database](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmrqxiylcmfzwk)
>
> **Accessing the coordinator**
> : [- coordinator](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmnxw64tenfxgc5dpoi)
>
> **Managing channels**
> : [- availableChannel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmf3gc2lmmfrgyzkdnbqw43tfnq)
> : [- registerChannel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswo2ltorsxeq3imfxg4zlmhi)
> : [- registeredChannels](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswo2ltorsxezleinugc3tomvwhg)
> : [- unregisterChannel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpovxhezlhnfzxizlsinugc3tomvwdu)
> : [- hasBusyChannels](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnbqxgqtvon4ug2dbnzxgk3dt)
>
> **Accessing the delegate**
> : [- setDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponsxirdfnrswoylumu5a)
> : [- delegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmrswyzlhmf2gk)
> : [+ setDefaultDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuiylumfrgc43finxw45dfpb2c643forcgkztbovwhirdfnrswoylumu5a)
> : [+ defaultDelegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuiylumfrgc43finxw45dfpb2c6zdfmzqxk3duirswyzlhmf2gk)
>
> **Committing or discarding
> changes**
> : [- saveChangesInEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponqxmzkdnbqw4z3fonew4rlenf2gs3thinxw45dfpb2du)
> : [- invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfxhmylmnfsgc5dfifwgyt3cnjswg5dt)
> : [- invalidateObjectsWithGlobalIDs:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfxhmylmnfsgc5dfj5rguzldorzvo2lunbdwy33cmfwesrdthi)
> : [- rollbackChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojxwy3dcmfrwwq3imfxgozlt)
> : [- commitChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmnxw23ljorbwqylom5sxg)
> : [- prepareForSaveWithCoordinator:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpobzgk4dbojsum33sknqxmzkxnf2gqq3pn5zgi2lomf2g64r2mvsgs5djnztug33oorsxq5b2)
> : [- recordUpdateForObject:changes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrkxazdborsum33sj5rguzldoq5gg2dbnztwk4z2)
> : [- recordChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrbwqylom5sxgsloivsgs5djnztug33oorsxq5a)
> : [- refaultObject:withGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswmylvnr2e6ytkmvrxiotxnf2gqr3mn5rgc3cjiq5gkzdjoruw4z2dn5xhizlyoq5a)
>
> **Determining if the EODatabaseContext
> is responsible for a particular operation**
> : [- ownsObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpn53w442pmjvgky3uhi)
> : [- ownsGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpobsxeztpojwug2dbnztwk4y)
> : [- handlesFetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnbqw4zdmmvzumzlumnufg4dfmnuwm2ldmf2gs33ohi)
>
> **Recording snapshots**
> : [- recordSnapshot:forGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrjw4ylqonug65b2mzxxer3mn5rgc3cjiq5a)
> : [- recordSnapshots:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrjw4ylqonug65dthi)
> : [- recordSnapshot:forSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrjw4ylqonug65b2mzxxeu3povzggzkhnrxweylmjfcdu4tfnrqxi2lpnzzwq2lqjzqw2zj2)
> : [- recordToManySnapshots:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrkg6tlbnz4vg3tbobzwq33uom5a)
>
> **Forgetting snapshots**
> : [- forgetSnapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forjw4ylqonug65cgn5zeo3dpmjqwyskehi)
> : [- forgetSnapshotsForGlobalIDs:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forjw4ylqonug65dtizxxer3mn5rgc3cjirztu)
>
> **Accessing snapshots**
> : [- localSnapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwgylmknxgc4dtnbxxirtpojdwy33cmfwesrb2)
> : [- localSnapshotForSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwgylmknxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyskehjzgk3dboruw63ttnbuxattbnvstu)
> : [- snapshotForGlobalID:after:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponxgc4dtnbxxirtpojdwy33cmfwesrb2mfthizlshi)
> : [- snapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponxgc4dtnbxxirtpojdwy33cmfwesrb2)
> : [- snapshotForSourceGlobalID:relationshipName:after:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyskehjzgk3dboruw63ttnbuxattbnvstuylgorsxeoq)
> : [- snapshotForSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyskehjzgk3dboruw63ttnbuxattbnvstu)
>
> **Initializing objects**
> : [- initializeObject:withGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfxgs5djmfwgs6tfj5rguzldoq5ho2lunbdwy33cmfwesrb2mvsgs5djnztug33oorsxq5b2)
>
> **Obtaining an EODatabaseContext**
> : [+ registeredDatabaseContextForModel:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuiylumfrgc43finxw45dfpb2c64tfm5uxg5dfojswirdborqweyltmvbw63tumv4hirtpojgw6zdfnq5gkzdjoruw4z2dn5xhizlyoq5a)
>
> **Locking objects**
> : [- setUpdateStrategy:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponsxivlqmrqxizktorzgc5dfm54tu)
> : [- updateStrategy](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpovygiylumvjxi4tborswo6i)
> : [- registerLockedObjectWithGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswo2ltorsxetdpmnvwkzcpmjvgky3uk5uxi2chnrxweylmjfcdu)
> : [- isObjectLockedWithGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfzu6ytkmvrxitdpmnvwkzcxnf2gqr3mn5rgc3cjiq5a)
> : [- isObjectLockedWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfzu6ytkmvrxitdpmnvwkzcxnf2gqr3mn5rgc3cjiq5gkzdjoruw4z2dn5xhizlyoq5a)
> : [- forgetAllLocks](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forawy3cmn5rww4y)
> : [- forgetLocksForObjectsWithGlobalIDs:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forgg6y3londg64spmjvgky3uonlws5dii5wg6ytbnreui4z2)
> : [- lockObjectWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwg22pmjvgky3uk5uxi2chnrxweylmjfcduzlenf2gs3thinxw45dfpb2du)
>
> **Returning information
> about objects**
> : [- valuesForKeys:object:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpozqwy5lfondg64slmv4xgotpmjvgky3uhi)
>
> **Setting the context class**
> : [+ contextClassToRegister](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuiylumfrgc43finxw45dfpb2c6y3pnz2gk6duinwgc43tkrxvezlhnfzxizls)
> : [+ setContextClassToRegister:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuiylumfrgc43finxw45dfpb2c643forbw63tumv4hiq3mmfzxgvdpkjswo2ltorsxeoq)
>
> **Thread safety**
> : [- lock](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwg2y)
> : [- unlock](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpovxgy33dnm)

## Class Methods

---

### contextClassToRegister

`+ (Class)contextClassToRegister`

Returns the class that is registered with an
EOObjectStoreCoordinator when the coordinator broadcasts an `EOCooperatingObjectStoreNeeded` notification.
By default this is EODatabaseContext, but you can use [setContextClassToRegister:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuiylumfrgc43finxw45dfpb2c643forbw63tumv4hiq3mmfzxgvdpkjswo2ltorsxeoq) to specify
your own subclass of EODatabaseContext.

When an EOObjectStoreCoordinator
sends an `EOCooperatingObjectStoreNeeded` notification
for an EOEntity in the default model group, if __contextClassToRegister__ is
non-nil (and it should be-it makes no sense to set __contextClassToRegister__ to nil),
an instance of the that class is created, the EOModel for the EOEntity
is registered, and the context class is registered with the requesting EOObjectStoreCoordinator.

---

### defaultDelegate

`+ (id)defaultDelegate`

Returns the default delegate-the object assigned
as delegate to new EODatabaseContext instances.

---

### forceConnectionWithModel:connectionDictionaryOverrides:editingContext:

`+ (EODatabaseContext *)forceConnectionWithModel:(EOModel
*)amodel
connectionDictionaryOverrides:(NSDictionary
*)overrides
editingContext:(EOEditingContext
*)anEditingContext`

Forces the stack of objects in the EOAccess
layer to be instantiated, if necessary, and then makes a connection
to the database. If there is an existing connection for _amodel_,
it is first closed and then reconnected. The new connection dictionary
is effectively made up of the model's connection dictionary, overlaid
with _overrides_. All compatible models
in the model's group also are associated with the new connection
(so they share the same adaptor). Returns the EODatabaseContext
associated with the model for _anEditingContext_.

---

### isSharedObjectLoadingEnabled

`+ (BOOL)isSharedObjectLoadingEnabled`

Returns `YES` if
database contexts automatically load enterprise objects into the
default shared editing context when they load models; `NO` otherwise.
The objects loaded into the shared editing context are those identified
by entities' shared fetch specifications.

__See
Also:__  [- sharedObjectFetchSpecificationNames](EOEntity-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwqylsmvse6ytkmvrxirtforrwqu3qmvrwsztjmnqxi2lpnzhgc3lfom) ( [EOEntity](EOEntity-3.md#apple-irauuq2ginduu))

---

### registeredDatabaseContextForModel:editingContext:

`+ (EODatabaseContext *)registeredDatabaseContextForModel:(EOModel
*)aModel
editingContext:(EOEditingContext
*)anEditingContext`

Finds the EOObjectStoreCoordinator (EOControl)
for _anEditingContext_ and checks to
see if it already contains an EODatabaseContext cooperating store
for _aModel_. If it does, it returns
that EODatabaseContext. Otherwise it instantiates a new EODatabaseContext,
adds it to the EOObjectStoreCoordinator, and returns the EODatabaseContext.

---

### setContextClassToRegister:

`+ (void)setContextClassToRegister:(Class)contextClass`

Sets to _contextClass_ the
"contextClassToRegister." For more discussion of this topic,
see the method description for [contextClassToRegister](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuiylumfrgc43finxw45dfpb2c6y3pnz2gk6duinwgc43tkrxvezlhnfzxizls).

---

### setDefaultDelegate:

`+ (void)setDefaultDelegate:(id)defaultDelegate`

Sets the default delegate to _defaultDelegate_-the
object assigned as delegate to new instances of EODatabaseContext.

---

### setSharedObjectLoadingEnabled:

`+ (void)setSharedObjectLoadingEnabled:(BOOL)flag`

Sets according to _flag_ whether
database contexts automatically load enterprise objects into the
default shared editing context when they load models. The default
is `YES` (the database
automatically loads shared objects). The objects loaded into the
shared editing context are those identified by entities' shared
fetch specifications.

__See Also:__  [- sharedObjectFetchSpecificationNames](EOEntity-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5zwqylsmvse6ytkmvrxirtforrwqu3qmvrwsztjmnqxi2lpnzhgc3lfom) ( [EOEntity](EOEntity-3.md#apple-irauuq2ginduu))

---

## Instance Methods

---

### adaptorContext

`- (EOAdaptorContext *)adaptorContext`

Returns the EOAdaptorContext used by the EODatabaseContext
for communication with the database server.

---

### arrayFaultWithSourceGlobalID:relationshipName:editingContext:

`- (NSArray *)arrayFaultWithSourceGlobalID:(EOGlobalID
*)globalID
relationshipName:(NSString *)name
editingContext:(EOEditingContext
*)anEditingContext`

Overrides the inherited implementation to create
a to-many fault for _anEditingContext_. _name_ must correspond
to an EORelationship in the EOEntity for the specified _globalID_.

__See
Also:__  [- faultForGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzqxk3duizxxer3mn5rgc3cjiq5gkzdjoruw4z2dn5xhizlyoq5a)

---

### availableChannel

`- (EODatabaseChannel *)availableChannel`

Returns an EODatabaseChannel that's registered
with the receiver and that isn't busy. If the method can't find
a channel that meets these criteria, it posts an [EODatabaseChannelNeededNotification](#apple-irauorcgirdem) in
the hopes that someone will provide a new channel. After posting
the notification, the receiver checks its list of channels again.
If there are still no available channels, the receiver creates an
EODatabaseChannel itself. However, if the list is not empty and
there are no available channels, the method returns nil.

__See
Also:__  [- registerChannel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswo2ltorsxeq3imfxg4zlmhi), [- registeredChannels](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswo2ltorsxezleinugc3tomvwhg), [- unregisterChannel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpovxhezlhnfzxizlsinugc3tomvwdu)

---

### batchFetchRelationship:forSourceObjects:editingContext:

`- (void)batchFetchRelationship:(EORelationship
*)relationship
forSourceObjects:(NSArray *)objects
editingContext:(EOEditingContext
*)anEditingContext`

Clear all the faults for the _relationship_ of _anEditingContext_'s _objects_ and
performs a single, efficient, fetch (at most two fetches, if the
relationship is many-to-many). This method provides a way to fetch the
same relationship for multiple objects. For example, given an array
of Employee objects, this method can fetch all of their departments
with one round trip to the server, rather than asking the server
for each of the employee's departments individually.

---

### commitChanges

`- (void)commitChanges`

Overrides the inherited implementation to instruct
the adaptor to commit the transaction. If the commit is successful,
any primary and foreign key changes are written back to the saved
objects, database locks are released, and an `EOCooperatingObjectStoreNeeded` (defined
in EOControl's EOObjectStore) is posted describing the committed
changes. Raises an exception if the adaptor is unable to commit
the transaction; the error message indicates the nature of the problem.
You should never need to invoke this method directly.

__See
Also:__  [- ownsGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpobsxeztpojwug2dbnztwk4y), [- rollbackChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojxwy3dcmfrwwq3imfxgozlt)

---

### coordinator

`- (EOObjectStoreCoordinator *)coordinator`

Returns the receiver's EOObjectStoreCoordinator
(EOControl) or nil if there is none.This
method is only valid during a save operation.

---

### database

`- (EODatabase *)database`

Returns the receiver's EODatabase.

__See
Also:__  [- initWithDatabase:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfxgs5cxnf2gqrdborqweyltmu5a)

---

### delegate

`- (id)delegate`

Returns the receiver's delegate.

__See
Also:__  [- setDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponsxirdfnrswoylumu5a)

---

### faultForGlobalID:editingContext:

`- (id)faultForGlobalID:(EOGlobalID
*)globalID
editingContext:(EOEditingContext
*)anEditingContext`

Overrides the inherited implementationto
create a to-one fault for the object identified by _globalID_ and
register it in _anEditingContext._

__See
Also:__  [- arrayFaultWithSourceGlobalID:relationshipName:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmfzheylzizqxk3duk5uxi2ctn52xey3fi5wg6ytbnreuiotsmvwgc5djn5xhg2djobhgc3lfhjswi2lunfxgoq3pnz2gk6duhi)

---

### faultForRawRow:entityNamed:editingContext:

`- (id <EOEnterpriseObject>)faultForRawRow:(id)row
entityNamed:(NSString *)entityName
editingContext:(EOEditingContext
*)context`

Returns a fault for a raw row. _row_ is
the raw data, typically in the form of an NSDictionary. _entityName_ is
the name of the appropriate entity for the EO you want to create
(as a fault). _editingContext_ is the EOEditingContext
in which to create the fault

---

### forgetAllLocks

`- (void)forgetAllLocks`

Clears all of the receiver's locks. Doesn't
cause the locks to be forgotten in the server, only in the receiver.
This method is useful when something has happened to cause the server
to forget the locks and the receiver needs to be synced up. This
method is invoked whenever a transaction is committed or rolled
back.

__See Also:__  [- registerLockedObjectWithGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswo2ltorsxetdpmnvwkzcpmjvgky3uk5uxi2chnrxweylmjfcdu), [- isObjectLockedWithGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfzu6ytkmvrxitdpmnvwkzcxnf2gqr3mn5rgc3cjiq5a), [- isObjectLockedWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfzu6ytkmvrxitdpmnvwkzcxnf2gqr3mn5rgc3cjiq5gkzdjoruw4z2dn5xhizlyoq5a), [- forgetLocksForObjectsWithGlobalIDs:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forgg6y3londg64spmjvgky3uonlws5dii5wg6ytbnreui4z2), [- lockObjectWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwg22pmjvgky3uk5uxi2chnrxweylmjfcduzlenf2gs3thinxw45dfpb2du), - __lockObject:__ (EOEditingContext)

---

### forgetLocksForObjectsWithGlobalIDs:

`- (void)forgetLocksForObjectsWithGlobalIDs:(NSArray
*)globalIDs`

Clears the locks made for the enterprise objects
identified by each of the EOGlobalIDs in _globalIDs_. Doesn't
cause the locks to be forgotten in the server, only in the receiver.

__See
Also:__  [- registerLockedObjectWithGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswo2ltorsxetdpmnvwkzcpmjvgky3uk5uxi2chnrxweylmjfcdu), [- isObjectLockedWithGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfzu6ytkmvrxitdpmnvwkzcxnf2gqr3mn5rgc3cjiq5a), [- isObjectLockedWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfzu6ytkmvrxitdpmnvwkzcxnf2gqr3mn5rgc3cjiq5gkzdjoruw4z2dn5xhizlyoq5a), [- forgetAllLocks](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forawy3cmn5rww4y), [- lockObjectWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwg22pmjvgky3uk5uxi2chnrxweylmjfcduzlenf2gs3thinxw45dfpb2du), - __lockObject:__ (EOEditingContext)

---

### forgetSnapshotForGlobalID:

`- (void)forgetSnapshotForGlobalID:(EOGlobalID
*)globalID`

Deletes the snapshot made for the enterprise
object identified by _globalID_.

__See
Also:__  [- recordSnapshot:forGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrjw4ylqonug65b2mzxxer3mn5rgc3cjiq5a), [- localSnapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwgylmknxgc4dtnbxxirtpojdwy33cmfwesrb2), [- recordSnapshots:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrjw4ylqonug65dthi), [- snapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponxgc4dtnbxxirtpojdwy33cmfwesrb2), [- forgetSnapshotsForGlobalIDs:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forjw4ylqonug65dtizxxer3mn5rgc3cjirztu)

---

### forgetSnapshotsForGlobalIDs:

`- (void)forgetSnapshotsForGlobalIDs:(NSArray
*)globalIDs`

Deletes the snapshots made for the enterprise
objects identified by _globalIDs_,
an array of EOGlobalID objects.

__See Also:__  [- recordSnapshot:forGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrjw4ylqonug65b2mzxxer3mn5rgc3cjiq5a), [- localSnapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwgylmknxgc4dtnbxxirtpojdwy33cmfwesrb2), [- recordSnapshots:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrjw4ylqonug65dthi), [- snapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponxgc4dtnbxxirtpojdwy33cmfwesrb2)

---

### handleDroppedConnection

`- (void)handleDroppedConnection`

Cleans up after a database connection is dropped
by releasing the receiver's adaptor context and database channels,
and then creating a new adaptor context. Don't invoke this method;
it's invoked automatically by the Framework.

---

### handlesFetchSpecification:

`- (BOOL)handlesFetchSpecification:(EOFetchSpecification
*)fetchSpec`

Overrides the inherited implementation to return YES if
the receiver is responsible for fetching the objects described by
the entity name in _fetchSpec_.

__See
Also:__  [- ownsObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpn53w442pmjvgky3uhi), [- ownsGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpobsxeztpojwug2dbnztwk4y)

---

### hasBusyChannels

`- (BOOL)hasBusyChannels`

Returns YES if the receiver's EOAdaptorContext
has channels that have outstanding operations (that is, have a fetch
in progress), NO otherwise.

---

### initializeObject:withGlobalID:editingContext:

`- (void)initializeObject:(id)object
withGlobalID:(EOGlobalID *)globalID
editingContext:(EOEditingContext
*)anEditingContext`

Overrides the inherited implementation initialize _object_ for _anEditingContext_ by
filling it with properties based on row data fetched from the adaptor.
The snapshot for _globalID_ is looked
up and those attributes in the snapshot that are marked as class
properties in the EOEntity are assigned to _object_.
For relationship class properties, faults are constructed and assigned
to the object.

---

### initWithDatabase:

`- initWithDatabase:(EODatabase
*)aDatabase`

Initializes a newly allocated EODatabaseContext
with _aDatabase_ as the EODatabase
object it works with. The new EODatabaseContext retains _aDatabase_.
Returns __self__, or __nil__ if
unable to create another EOAdaptorContext for the EOAdaptor of _aDatabase_.
This is the designated initializer for the EODatabaseContext class.

---

### invalidateAllObjects

`- (void)invalidateAllObjects`

Overrides the inherited implementation to discard
all snapshots in the receiver's EODatabase, forget all locks,
and post an `EOInvalidatedAllObjectsInStoreNotification`,
as well as an `EOObjectsChangedInStoreNotification` with
the invalidated global IDs in the __userInfo__ dictionary.
Both of these notifications are defined in EOObjectStore (EOControl).
This method works by invoking [- invalidateObjectsWithGlobalIDs:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfxhmylmnfsgc5dfj5rguzldorzvo2lunbdwy33cmfwesrdthi) for
all of the snapshots in the receiver's EODatabase.

---

### invalidateObjectsWithGlobalIDs:

`- (void)invalidateObjectsWithGlobalIDs:(NSArray
*)globalIDs`

Overrides the inherited implementation to discard
the snapshots for the objects identified by the EOGlobalIDs in _globalIDs_ and
broadcasts an `EOObjectsChangedInStoreNotification` (defined
in EOObjectStore), which causes the EOEditingContext containing
objects fetched from the receiver to refault those objects. The
result is that these objects will be refetched from the database
the next time they're accessed.

---

### isObjectLockedWithGlobalID:

`- (BOOL)isObjectLockedWithGlobalID:(EOGlobalID
*)globalID`

Returns YES if the enterprise object identified
by _globalID_ is locked, NO otherwise.

__See
Also:__  [- registerLockedObjectWithGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswo2ltorsxetdpmnvwkzcpmjvgky3uk5uxi2chnrxweylmjfcdu), [- forgetAllLocks](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forawy3cmn5rww4y), [- isObjectLockedWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfzu6ytkmvrxitdpmnvwkzcxnf2gqr3mn5rgc3cjiq5gkzdjoruw4z2dn5xhizlyoq5a), [- forgetLocksForObjectsWithGlobalIDs:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forgg6y3londg64spmjvgky3uonlws5dii5wg6ytbnreui4z2), [- lockObjectWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwg22pmjvgky3uk5uxi2chnrxweylmjfcduzlenf2gs3thinxw45dfpb2du), - __lockObject:__ (EOEditingContext)

---

### isObjectLockedWithGlobalID:editingContext:

`- (BOOL)isObjectLockedWithGlobalID:(EOGlobalID
*)globalID
editingContext:(EOEditingContext
*)anEditingContext`

Overrides the EOObjectStore method __isObjectLockedWithGlobalID:editingContext:__ to
return YES if the database row corresponding to _globalID_ has
been locked in an open transaction held by the receiver.

__See
Also:__  [- registerLockedObjectWithGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswo2ltorsxetdpmnvwkzcpmjvgky3uk5uxi2chnrxweylmjfcdu), [- isObjectLockedWithGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfzu6ytkmvrxitdpmnvwkzcxnf2gqr3mn5rgc3cjiq5a), [- forgetAllLocks](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forawy3cmn5rww4y), [- forgetLocksForObjectsWithGlobalIDs:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forgg6y3londg64spmjvgky3uonlws5dii5wg6ytbnreui4z2), [- lockObjectWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwg22pmjvgky3uk5uxi2chnrxweylmjfcduzlenf2gs3thinxw45dfpb2du),
- __lockObject:__ (EOEditingContext)

---

### localSnapshotForGlobalID:

`- (NSDictionary *)localSnapshotForGlobalID:(EOGlobalID
*)globalID`

Returns the snapshot for the object identified
by _globalID_, if there is one; else
returns nil. Only searches locally (in the transaction scope), not
in the EODatabase.

__See Also:__  [- recordSnapshot:forGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrjw4ylqonug65b2mzxxer3mn5rgc3cjiq5a), [- forgetSnapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forjw4ylqonug65cgn5zeo3dpmjqwyskehi), [- recordSnapshots:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrjw4ylqonug65dthi), [- snapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponxgc4dtnbxxirtpojdwy33cmfwesrb2)

---

### localSnapshotForSourceGlobalID:relationshipName:

`- (NSArray *)localSnapshotForSourceGlobalID:(EOGlobalID
*)globalID
relationshipName:(NSString *)name`

Returns an array that is the snapshot for the
objects at the destination of the to-many relationship named _name_,
which is a property of the object identified by _globalID_.
The returned array contains the globalIDs of the destination objects.
If there is no snapshot, returns nil. Only searches locally (in
the transaction scope), not in the EODatabase.

__See
Also:__  [- recordSnapshot:forSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrjw4ylqonug65b2mzxxeu3povzggzkhnrxweylmjfcdu4tfnrqxi2lpnzzwq2lqjzqw2zj2), [- snapshotForSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyskehjzgk3dboruw63ttnbuxattbnvstu)

---

### lock

`- (void)lock`

Used internally to protect access to the receiver
in a multi-threaded environment. Do not confuse this with any methods
which work with the database locking mechanism.

__See
Also:__  [- unlock](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpovxgy33dnm)

---

### lockObjectWithGlobalID:editingContext:

`- (void)lockObjectWithGlobalID:(EOGlobalID
*)globalID
editingContext:(EOEditingContext
*)anEditingContext`

Overrides the inherited implementation to attempt
to lock the database row corresponding to _globalID_ in
the underlying database server, on behalf of _anEditingContext_.
If a transaction is not already open at the time of the lock request,
the transaction is begun and is held open until either __commitChanges__ or __invalidateAllObjects__ is
invoked. At that point all locks are released. Raises an `NSInternalInconsistencyException` if
unable to obtain the lock.

__See Also:__  [- registerLockedObjectWithGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswo2ltorsxetdpmnvwkzcpmjvgky3uk5uxi2chnrxweylmjfcdu), [- isObjectLockedWithGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfzu6ytkmvrxitdpmnvwkzcxnf2gqr3mn5rgc3cjiq5a), [- forgetAllLocks](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forawy3cmn5rww4y), [- forgetLocksForObjectsWithGlobalIDs:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forgg6y3londg64spmjvgky3uonlws5dii5wg6ytbnreui4z2), - __lockObject:__ (EOEditingContext)

---

### missingObjectGlobalIDs

`- (NSArray *)missingObjectGlobalIDs`

Returns the globalIDs of any "missing" enterprise
objects, or an empty array if no missing objects are known to the
receiver. An object is "missing" when a fault fires and the
corresponding row for the fault isn't found in the database.

To
be notified when a missing object is discovered, implement the delegate
method [databaseContext:failedToFetchObject:globalID:](EODatabaseContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2mzqws3dfmrkg6rtforrwqt3cnjswg5b2m5wg6ytbnreuioq).

If
an application tries to save a missing object, an exception is raised.

---

### objectsForSourceGlobalID:relationshipName:editingContext:

`- (NSArray *)objectsForSourceGlobalID:(EOGlobalID
*)globalID
relationshipName:(NSString *)name
editingContext:(EOEditingContext
*)anEditingContext`

Overrides the inherited implementation to service
a to-many fault. The snapshot for the source object identified by _globalID_ is
located and the EORelationship named _name_ is
used to construct a qualifier from that snapshot. This qualifier
is then used to fetch the requested objects into _anEditingContext_ using
the method [objectsWithFetchSpecification:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpn5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63r2mvsgs5djnztug33oorsxq5b2).

---

### objectsWithFetchSpecification:editingContext:

`- (NSArray *)objectsWithFetchSpecification:(EOFetchSpecification
*)fetchSpecification
editingContext:(EOEditingContext
*)anEditingContext`

Overrides the inherited implementation to fetch
objects from an external store into _anEditingContext_. The
receiver obtains an available EODatabaseChannel and issues a fetch
with _fetchSpecification_. If one of
these objects is already present in memory, by default this method
doesn't overwrite its values with the new values from the database
(you can change this behavior; see the __setRefreshesRefetchedObjects:__ method
in the EOFetchSpecification class specification).

You can fine-tune
the fetching behavior by adding hints to _fetchSpecification_'s __hints__ dictionary.
For this purpose, Enterprise Objects Framework defines the following
keys:

|  |  |
| --- | --- |
| __Constant__ | __Corresponding value in the hints dictionary__ |
| `EOCustomQueryExpressionHintKey` | An NSString specifying raw SQL with which to perform the fetch. There is no way to pass down parameters with this hint. |
| `EOStoredProcedureNameHintKey` | An NSString specifying a name for a stored procedure in the model that should be used rather than building the SQL statement. The stored procedure must query the exact same attributes in the same order as EOF would query if generating the SELECT expression dynamically. If this key is supplied, other aspects of the EOFetchSpecification such as __isDeep__, __qualifier__, and __sortOrderings__ are ignored (in that sense, this key is more of a directive than a hint). There is no way to pass down parameters with this hint. |

The class description contains additional information
on using these hints. See "Using a Custom Query."

You
can also use this method to implement "on-demand" locking by
using a _fetchSpecification_ that includes
locking. For more discussion of this subject, see "Updating And
Locking Strategies" in the class description.

Raises
an exception if an error occurs; the error message indicates the
nature of the problem.

__See Also:__  - __objectsWithFetchSpecification:__ (EOEditingContext)

---

### __ownsGlobalID:__

`- (BOOL)ownsGlobalID:(EOGlobalID
*)globalID`

Overrides the inherited implementation to return YES if
the receiver is responsible for fetching and saving the object identified
by _globalID_, NO otherwise. The receiver
is determined to be responsible if _globalID_ is
a subclass of EOKeyGlobalID and _globalID_ has
an entity from one of the receiver's EODatabase's EOModels.

__See
Also:__  [- handlesFetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnbqw4zdmmvzumzlumnufg4dfmnuwm2ldmf2gs33ohi), [- ownsObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpn53w442pmjvgky3uhi)

---

### ownsObject:

`- (BOOL)ownsObject:(id)object`

Overrides the inherited implementation to return YES if
the receiver is responsible for fetching and saving _object_, NO otherwise.
The receiver is determined to be responsible if the entity corresponding
to _object_ is in one of the receiver's
EODatabase's EOModels.

__See Also:__  [- ownsGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpobsxeztpojwug2dbnztwk4y), [- handlesFetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnbqw4zdmmvzumzlumnufg4dfmnuwm2ldmf2gs33ohi)

---

### performChanges

`- (void)performChanges`

Overrides the inherited implementation to construct
EOAdaptorOperations from the EODatabaseOperations produced during [recordChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrbwqylom5sxgsloivsgs5djnztug33oorsxq5a) and [recordUpdateForObject:changes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrkxazdborsum33sj5rguzldoq5gg2dbnztwk4z2). Invokes
the delegate method [databaseContext:willOrderAdaptorOperationsFromDatabaseOperations:](EODatabaseContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2o5uwy3cpojsgk4sbmrqxa5dpojhxazlsmf2gs33oondhe33nirqxiylcmfzwkt3qmvzgc5djn5xhgoq) to
give the delegate an opportunity to construct alternative EOAdaptorOperations
from the EODatabaseOperations. Then invokes the delegate method [databaseContext:willPerformAdaptorOperations:adaptorChannel:](EODatabaseContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2emf2gcytbonsug33oorsxq5bairswyzlhmf2gkl3emf2gcytbonsug33oorsxq5b2o5uwy3cqmvzgm33snvawiylqorxxet3qmvzgc5djn5xhgotbmrqxa5dpojbwqylonzswyoq) to
let the delegate substitute its own array of EOAdaptorOperations.
Gives the EOAdaptorOperations to an available EOAdaptorChannel for
execution. If the save succeeds, updates the snapshots in the receiver
to reflect the new state of the server. You should never need to
invoke this method directly.

This method raises an exception
if the adaptor is unable to perform the operations. The exception's userInfo
dictionary contains these keys:

|  |  |
| --- | --- |
| __Key (NSString Constant)__ | __Value__ |
| `EODatabaseContextKey` | The EODatabaseContext object that was trying to save to its underlying repository when the exception was raised. |
| `EODatabaseOperationsKey` | The list of database operations the EODatabaseContext was trying to perform when the failure occurred. |
| `EOFailedDatabaseOperationKey` | The database operation the EODatabaseContext failed to perform. |

The userInfo dictionary may also contain some of the
keys listed in the method description for the EOAdaptorChannel method __performAdaptorOperation:__.
For more information, see the EOAdaptorChannel class specification.

__See
Also:__  [- commitChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmnxw23ljorbwqylom5sxg), [- rollbackChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojxwy3dcmfrwwq3imfxgozlt)

---

### prepareForSaveWithCoordinator:editingContext:

`- (void)prepareForSaveWithCoordinator:(EOObjectStoreCoordinator
*)coordinator
editingContext:(EOEditingContext
*)anEditingContext`

Overrides the inherited implementation to do
whatever is necessary to prepare to save changes. If needed, generates
primary keys for any new objects in _anEditingContext_ that
are owned by the receiver. This method is invoked before the object
graph is analyzed and foreign key assignments are performed. You
should never need to invoke this method directly.

---

### recordChangesInEditingContext

`- (void)recordChangesInEditingContext`

Overrides the inherited implementation to construct
a list of EODatabaseOperations for all changes to objects in the
EOEditingContext that are owned by the receiver. Forwards any relationship
changes discovered but not owned by the receiver to the EOObjectStoreCoordinator.
This method is typically invoked in the course of an EOObjectStoreCoordinator
saving changes through its __saveChangesInEditingContext:__ method.
It's invoked after [prepareForSaveWithCoordinator:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpobzgk4dbojsum33sknqxmzkxnf2gqq3pn5zgi2lomf2g64r2mvsgs5djnztug33oorsxq5b2) and
before [ownsGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpobsxeztpojwug2dbnztwk4y).
You should never need to invoke this method directly.

---

### recordSnapshot:forGlobalID:

`- (void)recordSnapshot:(NSDictionary
*)snapshot
forGlobalID:(EOGlobalID *)globalID`

Records _aSnapshot_ under _globalID_.
This method only records snapshots locally (in the transaction scope).
If you want to record snapshots globally, use the corresponding
EODatabase method.

__See Also:__  [- forgetSnapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forjw4ylqonug65cgn5zeo3dpmjqwyskehi), [- localSnapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwgylmknxgc4dtnbxxirtpojdwy33cmfwesrb2), [- recordSnapshots:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrjw4ylqonug65dthi), [- snapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponxgc4dtnbxxirtpojdwy33cmfwesrb2)

---

### recordSnapshot:forSourceGlobalID:relationshipName:

`- (void)recordSnapshot:(NSArray
*)globalIDs
forSourceGlobalID:(EOGlobalID
*)globalID
relationshipName:(NSString *)name`

For the object identified by _globalID_,
records an NSArray of _globalIDs_ for
the to-many relationship named _name_.
These _globalIDs_ identify the objects
at the destination of the relationship. This method only records
snapshots locally (in the transaction scope). If you want to record
snapshots globally, use the corresponding EODatabase method.

__See
Also:__  [- snapshotForSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyskehjzgk3dboruw63ttnbuxattbnvstu), [- localSnapshotForSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwgylmknxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyskehjzgk3dboruw63ttnbuxattbnvstu), [- recordToManySnapshots:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrkg6tlbnz4vg3tbobzwq33uom5a)

---

### recordSnapshots:

`- (void)recordSnapshots:(NSDictionary
*)snapshots`

Records the objects in _snapshots_,
a dictionary of snapshots. The _snapshots_ argument's
keys are GlobalIDs and its values are the corresponding snapshots
represented as NSDictionaries. This method only records snapshots
locally (in the transaction scope). If you want to record snapshots
globally, use the corresponding EODatabase method.

__See
Also:__  [- recordSnapshot:forGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrjw4ylqonug65b2mzxxer3mn5rgc3cjiq5a), [- localSnapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwgylmknxgc4dtnbxxirtpojdwy33cmfwesrb2), [- forgetSnapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forjw4ylqonug65cgn5zeo3dpmjqwyskehi), [- snapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponxgc4dtnbxxirtpojdwy33cmfwesrb2)

---

### recordToManySnapshots:

`- (void)recordToManySnapshots:(NSDictionary
*)snapshots`

Records the objects in _snapshots_. _snapshots_ should
be an NSDictionary of NSDictionaries, in which the top-level dictionary
has as its key the globaID of the enterprise object for which to-many
relationships are being recorded. The key's value is a dictionary
whose keys are the names of the Enterprise Object's to-many relationships.
Each of these keys in turn has as its value an array of globalIDs
that identify the objects at the destination of the relationship.

This
method only records snapshots locally (in the transaction scope).
If you want to record snapshots globally, use the corresponding
EODatabase method.

__See Also:__  [- recordSnapshot:forSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrjw4ylqonug65b2mzxxeu3povzggzkhnrxweylmjfcdu4tfnrqxi2lpnzzwq2lqjzqw2zj2), [- snapshotForSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyskehjzgk3dboruw63ttnbuxattbnvstu), [- localSnapshotForSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwgylmknxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyskehjzgk3dboruw63ttnbuxattbnvstu)

---

### recordUpdateForObject:changes:

`- (void)recordUpdateForObject:(id)object
changes:(NSDictionary *)changes`

Overrides the inherited implementation to communicate
to the receiver that _changes_ from
another EOCooperatingObjectStore (through the EOObjectStoreCoordinator)
need to be made to an _object_ in the
receiver. For example, an insert of an object in a relationship
property might require changing a foreign key property in an object
owned by another cooperating store. This method can be invoked any time
after [prepareForSaveWithCoordinator:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpobzgk4dbojsum33sknqxmzkxnf2gqq3pn5zgi2lomf2g64r2mvsgs5djnztug33oorsxq5b2) and
before [ownsGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpobsxeztpojwug2dbnztwk4y).

---

### refaultObject:withGlobalID:editingContext:

`- (void)refaultObject:(id)anObject
withGlobalID:(EOGlobalID *)globalID
editingContext:(EOEditingContext
*)anEditingContext`

Overrides the inherited implementation to refault
the enterprise object identified by _globalID_ in _anEditingContext_.
Newly-inserted objects should not be refaulted, since they can't
be refetched from the external store. If you attempt to do this,
an exception will be raised. Don't refault to-many relationship
arrays, just recreate them.

This method should be used with
caution since refaulting an object doesn't remove the object snapshot from
the undo stack, after which the object snapshot may not refer to
the proper object.

---

### registerChannel:

`- (void)registerChannel:(EODatabaseChannel
*)channel`

Registers _channel_,
which means that it adds it to the pool of available channels used
to service fetch and fault requests. Registered channels are retained
by the receiver. You use this method if you need to perform more
than one fetch simultaneously.

__See Also:__  [- availableChannel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmf3gc2lmmfrgyzkdnbqw43tfnq), [- registeredChannels](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswo2ltorsxezleinugc3tomvwhg), [- unregisterChannel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpovxhezlhnfzxizlsinugc3tomvwdu)

---

### registeredChannels

`- (NSArray *)registeredChannels`

Returns all of the EODatabaseChannels that have
been registered for use with the receiver.

__See
Also:__  [- registerChannel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswo2ltorsxeq3imfxg4zlmhi), [- availableChannel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmf3gc2lmmfrgyzkdnbqw43tfnq), [- unregisterChannel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpovxhezlhnfzxizlsinugc3tomvwdu)

---

### registerLockedObjectWithGlobalID:

`- (void)registerLockedObjectWithGlobalID:(EOGlobalID
*)globalID`

Registers as a locked object the enterprise
object identified by _globalID_. This
method is used internally to keep track of objects corresponding
to rows that are locked in the database.

__See
Also:__  [- forgetAllLocks](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forawy3cmn5rww4y), [- isObjectLockedWithGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnfzu6ytkmvrxitdpmnvwkzcxnf2gqr3mn5rgc3cjiq5a), [- forgetLocksForObjectsWithGlobalIDs:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forgg6y3londg64spmjvgky3uonlws5dii5wg6ytbnreui4z2), [- lockObjectWithGlobalID:editingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwg22pmjvgky3uk5uxi2chnrxweylmjfcduzlenf2gs3thinxw45dfpb2du), - __lockObject:__ (EOEditingContext)

---

### rollbackChanges

`- (void)rollbackChanges`

Overrides the inherited implementation to instruct
the adaptor to roll back the transaction. Rolls back any changed
snapshots, and releases all locks.

__See Also:__  [- ownsGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpobsxeztpojwug2dbnztwk4y), [- commitChanges](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmnxw23ljorbwqylom5sxg)

---

### saveChangesInEditingContext:

`- (void)saveChangesInEditingContext:(EOEditingContext
*)context`

Overrides the inherited implementation to save
the changes made in _context_. This
message is sent by an EOEditingContext to its EOObjectStore to commit
changes. Normally an editing context doesn't send this message
to an EODatabaseContext, but to an EOObjectStoreCoordinator. Raises
an exception if an error occurs; the error message indicates the
nature of the problem.

---

### setDelegate:

`- (void)setDelegate:(id)delegate`

Sets the receiver's delegate to _delegate_,
and propagates the delegate to all of the receiver's EODatabaseChannels.
EODatabaseChannels share the delegate of their EODatabaseContext.

__See
Also:__  [- delegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmrswyzlhmf2gk)

---

### setUpdateStrategy:

`- (void)setUpdateStrategy:(EOUpdateStrategy)strategy`

Sets the update strategy used by the EODatabaseContext
to _strategy_. See ["Updating And Locking Strategies"](EODatabaseContext-3.md#apple-inbuuq2hjjauo) for
information on the update strategies:

- `EOUpdateWithOptimisticLocking`
- `EOUpdateWithPessimisticLocking`
- `EOUpdateWithNoLocking`

Raises an NSInvalidArgumentException if
the receiver has any transactions in progress or if you try to set _strategy_ to `EOUpdateWithPessimisticLocking` and
the receiver's EODatabase already has snapshots.

__See
Also:__  [- updateStrategy](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpovygiylumvjxi4tborswo6i)

---

### snapshotForGlobalID:

`- (NSDictionary *)snapshotForGlobalID:(EOGlobalID
*)globalID`

Equivalent to invoking [snapshotForGlobalID:after:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponxgc4dtnbxxirtpojdwy33cmfwesrb2mfthizlshi) with [EODistantPastTimeInterval](EODatabase-3.md#apple-iraukq2jjjdeq) as the time interval,
this method returns the snapshot associated with _globalID_.

__See
Also:__  [- recordSnapshot:forGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrjw4ylqonug65b2mzxxer3mn5rgc3cjiq5a), [- localSnapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwgylmknxgc4dtnbxxirtpojdwy33cmfwesrb2), [- forgetSnapshotForGlobalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmzxxez3forjw4ylqonug65cgn5zeo3dpmjqwyskehi), [- recordSnapshots:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrjw4ylqonug65dthi)

---

### snapshotForGlobalID:after:

`- (NSDictionary *)snapshotForGlobalID:(EOGlobalID
*)globalId
after:(NSTimeInterval)timestamp`

Returns the snapshot associated with _globalID_.
Returns `nil` if there
isn't a snapshot for the globalID or if the corresponding timestamp
is less than _timestamp_. Searches
first locally (in the transaction scope) and then in the EODatabase.

---

### snapshotForSourceGlobalID:relationshipName:

`- (NSArray *)snapshotForSourceGlobalID:(EOGlobalID
*)globalID
relationshipName:(NSString *)name`

Equivalent to invoking [snapshotForSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyskehjzgk3dboruw63ttnbuxattbnvstu) with [EODistantPastTimeInterval](EODatabase-3.md#apple-iraukq2jjjdeq) as the time
interval, this method returns the to-many snapshot for _globalId_ and _name_.

__See
Also:__  [- recordSnapshot:forSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrjw4ylqonug65b2mzxxeu3povzggzkhnrxweylmjfcdu4tfnrqxi2lpnzzwq2lqjzqw2zj2), [- localSnapshotForSourceGlobalID:relationshipName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwgylmknxgc4dtnbxxirtpojjw65lsmnsuo3dpmjqwyskehjzgk3dboruw63ttnbuxattbnvstu), [- recordToManySnapshots:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswg33smrkg6tlbnz4vg3tbobzwq33uom5a)

---

### snapshotForSourceGlobalID:relationshipName:after:

`- (NSArray *)snapshotForSourceGlobalID:(EOGlobalID
*)globalId
relationshipName:(NSString *)name
after:(NSTimeInterval)timestamp`

Returns the to-many snapshot for _globalId_ and _name_.
A to-many snapshot is an array of globalIDs. These globalIDs identify
the objects at the destination of the to-many relationship named _name_,
which is a property of the object identified by _globalID._ Returns `nil` if
there isn't a to-many snapshot for _globalId_ or
if the timestamp is less than _timestamp_.
Searches first locally (in the transaction scope) and then in the
EODatabase.

---

### unlock

`- (void)unlock`

Used internally to release the lock that protects
access to the receiver in a multi-threaded environment.

__See
Also:__  [- lock](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpnrxwg2y)

---

### unregisterChannel:

`- (void)unregisterChannel:(EODatabaseChannel
*)channel`

Unregisters the EODatabaseChannel _channel_,
which means that it removes it from the pool of available channels
used for database communication (for example, to service fetch and
fault requests).

__See Also:__  [- registerChannel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswo2ltorsxeq3imfxg4zlmhi), [- registeredChannels](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpojswo2ltorsxezleinugc3tomvwhg), [- availableChannel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bpmf3gc2lmmfrgyzkdnbqw43tfnq)

---

### updateStrategy

`- (EOUpdateStrategy)updateStrategy`

Returns the update strategy used by the receiver,
one of:

- `EOUpdateWithOptimisticLocking`
- `EOUpdateWithPessimisticLocking`
- `EOUpdateWithNoLocking`

The
default strategy is `EOUpdateWithOptimisticLocking`.

__See
Also:__  [- setUpdateStrategy:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug33oorsxq5bponsxivlqmrqxizktorzgc5dfm54tu)

---

### valuesForKeys:object:

`- (NSDictionary *)valuesForKeys:(NSArray
*)keys
object:(id)object`

Overrides the inherited implementation to return
values for the specified _keys_ from
the snapshot of _object_. The returned
values are used primarily by another EODatabaseContext to extract
foreign key properties for objects owned by the receiver.

---

## Notifications

---

### EODatabaseChannelNeededNotification

This notification is broadcast whenever
an EODatabaseContext is asked to perform an object store operation
and it doesn't have an available EODatabaseChannel. Subscribers
can create a new channel and add it to the EODatabaseContext at
this time.

|  |  |
| --- | --- |
| __Notification Object__ | The EODatabaseContext. |
| __userInfo Dictionary__ | None. |

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
