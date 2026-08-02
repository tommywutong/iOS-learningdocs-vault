---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EODatabaseContext.html
archived_at: '2026-07-15T08:13:41.448316Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EODatabaseContext

> __Inherits from:__ EOCooperatingObjectStore
>
> __Implements:__
> NSDisposable
> NSLocking
> NSDisposable
> NSLocking
>
> __Package:__ com.webobjects.eoaccess

---

## Class Description

---

An EODatabaseContext object is an EOObjectStore (EOControl) for accessing relational databases, creating and saving objects based on EOEntity definitions in an EOModel.

An EODatabaseContext represents a single connection to a database server, and it determines the updating and locking strategy used by its EODatabaseChannel objects. An EODatabaseContext has a corresponding EODatabase object. If the server supports multiple concurrent transactions, the EODatabase object may have several database contexts. If the server and adaptor support it, a database context may in turn have several database channels, which handle access to the data on the server.

For a more information on EODatabaseContext, see the sections:

- ["EODatabaseContext's Interaction with Other Classes" (page 165)](EODatabaseContext.Concepts.md#apple-ijduurkcijbuq)
- ["Creating and Using an EODatabaseContext" (page 167)](EODatabaseContext.Concepts.md#apple-ijduuqsci5dem)
- ["Fetching and Saving Objects" (page 168)](EODatabaseContext.Concepts.md#apple-ijduuqseijeuk)
- ["Using a Custom Query" (page 169)](EODatabaseContext.Concepts.md#apple-ijduurcjijeuo)
- ["Faulting" (page 169)](EODatabaseContext.Concepts.md#apple-ijduurcjjfdus)
- ["Delegate Methods" (page 170)](EODatabaseContext.Concepts.md#apple-ijduuq2kinbuk)
- ["Snapshots" (page 171)](EODatabaseContext.Concepts.md#apple-ijduurcdjjaum)
- ["Updating And Locking Strategies" (page 172)](EODatabaseContext.Concepts.md#apple-inbuuq2hjjauo)

## Constants

---

EODatabaseContext defines the following constants:

|  |  |  |
| --- | --- | --- |
| __Constant__ | __Type__ | __Description__ |
| UpdateWithOptimisticLocking | `int` | Identifies the locking strategy as optimistic. |
| UpdateWithPessimisticLocking | `int` | Identifies the locking strategy as pessimistic |
| UpdateWithNoLocking | `int` | Identifies the locking strategy as no locking |
| CustomQueryExpressionHintKey | `String` | A key in an EOFetchSpecification's hint dictionary |
| StoredProcedureNameHintKey | `String` | A key in an EOFetchSpecification's hint dictionary |
| DatabaseContextKey | `String` | A key in an `GenericAdaptorException`'s userInfo dictionary |
| DatabaseOperationsKey | `String` | A key in an `GenericAdaptorException`'s userInfo dictionary |
| FailedDatabaseOperationKey | `String` | A key in an `GenericAdaptorException`'s userInfo dictionary |
| DatabaseChannelNeededNotification | `String` | Description forthcoming. |

In addition, EODatabaseContext defines a constant for the name of the notification it posts. For more information on the notification, see ["Notifications" (page 163)](#apple-irauoscdjfees).

## Method Types

---

> Constructors[EODatabaseContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5cu6rdborqweyltmvbw63tumv4hi)Fetching objects[objectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5xwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33o)[objectsForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5xwe2tfmn2hgrtpojjw65lsmnsuo3dpmjqwyske)[arrayFaultWithSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5qxe4tbpfdgc5lmorlws5diknxxk4tdmvdwy33cmfwesra)[faultForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tgc5lmordg64shnrxweylmjfca)[faultForRawRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tgc5lmordg64ssmf3ve33x)[batchFetchRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5rgc5ddnbdgk5ddnbjgk3dboruw63ttnbuxa)[missingObjectGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wws43tnfxgot3cnjswg5chnrxweylmjfchg)Enabling shared object loading[setSharedObjectLoadingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdborqweyltmvbw63tumv4hil3tmv2fg2dbojswit3cnjswg5cmn5qwi2lom5cw4ylcnrswi)[isSharedObjectLoadingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdborqweyltmvbw63tumv4hil3jonjwqylsmvse6ytkmvrxitdpmfsgs3thivxgcytmmvsa)Accessing the adaptor context[adaptorContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5qwiylqorxxeq3pnz2gk6du)Managing the database connection[forceConnectionWithModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdborqweyltmvbw63tumv4hil3gn5zggzkdn5xg4zldoruw63sxnf2gqtlpmrswy)[handleDroppedConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5ugc3tenrsui4tpobygkzcdn5xg4zldoruw63q)Accessing the database object[database](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5sgc5dbmjqxgzi)Accessing the coordinator[coordinator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5rw633smruw4ylun5za)Managing channels[availableChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5qxmyljnrqwe3dfinugc3tomvwa)[registerChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgkz3jon2gk4sdnbqw43tfnq)[registeredChannels](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgkz3jon2gk4tfmrbwqylonzswy4y)[unregisterChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf52w44tfm5uxg5dfojbwqylonzswy)[hasBusyChannels](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5ugc42covzxsq3imfxg4zlmom)Accessing the delegate[setDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zwk5cemvwgkz3borsq)[delegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5sgk3dfm5qxizi)[setDefaultDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdborqweyltmvbw63tumv4hil3tmv2eizlgmf2wy5cemvwgkz3borsq)[defaultDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdborqweyltmvbw63tumv4hil3emvtgc5lmorcgk3dfm5qxizi)Committing or discarding changes[saveChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zwc5tfinugc3thmvzus3sfmruxi2lom5bw63tumv4hi)[invalidateAllObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5uw45tbnruwiylumvawy3cpmjvgky3uom)[invalidateObjectsWithGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5uw45tbnruwiylumvhwe2tfmn2hgv3jorueo3dpmjqwyskeom)[rollbackChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zg63dmmjqwg22dnbqw4z3fom)[commitChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5rw63lnnf2eg2dbnztwk4y)[prepareForSaveWithCoordinator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5yhezlqmfzgkrtpojjwc5tfk5uxi2cdn5xxezdjnzqxi33s)[recordUpdateForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojsfk4demf2gkrtpojhwe2tfmn2a)[recordChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojseg2dbnztwk42jnzcwi2lunfxgoq3pnz2gk6du)[refaultObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgkztbovwhit3cnjswg5a)Determining if the EODatabaseContext is responsible for a particular operation[ownsObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5xxo3ttj5rguzldoq)[ownsGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5ygk4tgn5zg2q3imfxgozlt)[handlesFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5ugc3tenrsxgrtforrwqu3qmvrwsztjmnqxi2lpny)Recording snapshots[recordSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojsfg3tbobzwq33uizxxer3mn5rgc3cjiq)[recordSnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojsfg3tbobzwq33uom)[recordSnapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojsfg3tbobzwq33uizxxeu3povzggzkhnrxweylmjfca)[recordToManySnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojsfi32nmfxhsu3omfyhg2dporzq)Forgetting snapshots[forgetSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2fg3tbobzwq33uizxxer3mn5rgc3cjiq)[forgetSnapshotsForGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2fg3tbobzwq33uondg64shnrxweylmjfchg)[editingContextDidForgetObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5swi2lunfxgoq3pnz2gk6duiruwirtpojtwk5cpmjvgky3uk5uxi2chnrxweylmjfca)Accessing snapshots[localSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3bnrjw4ylqonug65cgn5zeo3dpmjqwyske)[localSnapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3bnrjw4ylqonug65cgn5zfg33vojrwkr3mn5rgc3cjiq)[snapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zw4ylqonug65cgn5zeo3dpmjqwyske)[snapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zw4ylqonug65cgn5zfg33vojrwkr3mn5rgc3cjiq)Initializing objects[initializeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5uw42lunfqwy2l2mvhwe2tfmn2a)Obtaining an EODatabaseContext[registeredDatabaseContextForModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdborqweyltmvbw63tumv4hil3smvtws43umvzgkzcemf2gcytbonsug33oorsxq5cgn5ze233emvwa)Locking objects[setUpdateStrategy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zwk5cvobsgc5dfkn2heylumvtxs)[updateStrategy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf52xazdborsvg5dsmf2gkz3z)[registerLockedObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgkz3jon2gk4smn5rwwzlej5rguzldorlws5dii5wg6ytbnreui)[isObjectLockedWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5uxgt3cnjswg5cmn5rwwzlek5uxi2chnrxweylmjfca)[isObjectLockedWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5uxgt3cnjswg5cmn5rwwzlek5uxi2chnrxweylmjfca)[forgetAllLocks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2ec3dmjrxwg23t)[forgetLocksForObjectsWithGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2ey33dnnzum33sj5rguzldorzvo2lunbdwy33cmfwesrdt)[lockObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3lj5rguzldorlws5dii5wg6ytbnreui)Returning information about objects[valuesForKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf53gc3dvmvzum33sjnsxs4y)Setting the context class[contextClassToRegister](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdborqweyltmvbw63tumv4hil3dn5xhizlyorbwyyltonkg6utfm5uxg5dfoi)[setContextClassToRegister](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdborqweyltmvbw63tumv4hil3tmv2eg33oorsxq5cdnrqxg42un5jgkz3jon2gk4q)Thread safety[lock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3l)[unlock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf52w43dpmnvq)

## Constructors

---

### EODatabaseContext

`public EODatabaseContext(EODatabase aDatabase)`

Creates and returns a new EODatabaseContext. Typically, you don't need to programmatically create database contexts. Rather, they are created automatically by the control layer. See ["Creating and Using an EODatabaseContext"](EODatabaseContext.Concepts.md#apple-ijduuqsci5dem) for more information.

_aDatabase_ is assigned to the new database as the EODatabase object with which the new context works. The new database context creates an EOAdaptorContext with which to communicate with the database server. Throws an exception if the underlying adaptor context can't create a corresponding adaptor channel.

__See Also:__ [database](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5sgc5dbmjqxgzi)

---

## Static Methods

---

### contextClassToRegister

`public static Class contextClassToRegister()`

Returns the class that is registered with an EOObjectStoreCoordinator when the coordinator broadcasts an `CooperatingObjectStoreNeeded` notification. By default this is EODatabaseContext, but you can use [setContextClassToRegister](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdborqweyltmvbw63tumv4hil3tmv2eg33oorsxq5cdnrqxg42un5jgkz3jon2gk4q) to specify your own subclass of EODatabaseContext.

When an EOObjectStoreCoordinator sends an `CooperatingObjectStoreNeeded` notification for an EOEntity in the default model group, if __contextClassToRegister__ is non-null (and it should be-it makes no sense to set __contextClassToRegister__ to `null`), an instance of the that class is created, the EOModel for the EOEntity is registered, and the context class is registered with the requesting EOObjectStoreCoordinator.

---

### defaultDelegate

`public static Object defaultDelegate()`

Returns the default delegate-the object assigned as delegate to new EODatabaseContext instances.

---

### forceConnectionWithModel

`public static EODatabaseContext forceConnectionWithModel( EOModel aModel, NSDictionary overrides, com.webobjects.eocontrol.EOEditingContext anEditingContext)`

Forces the stack of objects in the EOAccess layer to be instantiated, if necessary, and then makes a connection to the database. If there is an existing connection for _amodel_, it is first closed and then reconnected. The new connection dictionary is effectively made up of the model's connection dictionary, overlaid with _overrides_. All compatible models in the model's group also are associated with the new connection (so they share the same adaptor). Returns the EODatabaseContext associated with the model for _anEditingContext_.

---

### isSharedObjectLoadingEnabled

`public static boolean isSharedObjectLoadingEnabled()`

Returns `true` if database contexts automatically load enterprise objects into the default shared editing context when they load models; `false` otherwise. The objects loaded into the shared editing context are those identified by entities' shared fetch specifications.

__See Also:__ sharedObjectFetchSpecificationNames (EOEntity)

---

### registeredDatabaseContextForModel

`public static EODatabaseContext registeredDatabaseContextForModel( EOModel aModel, com.webobjects.eocontrol.EOEditingContext anEditingContext)`

Finds the EOObjectStoreCoordinator (EOControl) for _anEditingContext_ and checks to see if it already contains an EODatabaseContext cooperating store for _aModel_. If it does, it returns that EODatabaseContext. Otherwise it instantiates a new EODatabaseContext, adds it to the EOObjectStoreCoordinator, and returns the EODatabaseContext.

`public static EODatabaseContext registeredDatabaseContextForModel( EOModel aModel, com.webobjects.eocontrol.EOObjectStoreCoordinator objectStoreCoord)`

Description forthcoming.

---

### setContextClassToRegister

`public static void setContextClassToRegister(Class contextClass)`

Sets to _contextClass_ the "contextClassToRegister." For more discussion of this topic, see the method description for [contextClassToRegister](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdborqweyltmvbw63tumv4hil3dn5xhizlyorbwyyltonkg6utfm5uxg5dfoi).

---

### setDefaultDelegate

`public static void setDefaultDelegate(Object defaultDelegate)`

Sets the default delegate to _defaultDelegate_-the object assigned as delegate to new instances of EODatabaseContext.

---

### setSharedObjectLoadingEnabled

`public static void setSharedObjectLoadingEnabled(boolean flag)`

Sets according to _flag_ whether database contexts automatically load enterprise objects into the default shared editing context when they load models. The default is `true` (the database automatically loads shared objects). The objects loaded into the shared editing context are those identified by entities' shared fetch specifications.

__See Also:__ sharedObjectFetchSpecificationNames (EOEntity)

---

## Instance Methods

---

### adaptorContext

`public EOAdaptorContext adaptorContext()`

Returns the EOAdaptorContext used by the EODatabaseContext for communication with the database server.

---

### arrayFaultWithSourceGlobalID

`public NSArray arrayFaultWithSourceGlobalID( com.webobjects.eocontrol.EOGlobalID globalID, String name, com.webobjects.eocontrol.EOEditingContext anEditingContext)`

Overrides the inherited implementation to create a to-many fault for _anEditingContext_. _name_ must correspond to an EORelationship in the EOEntity for the specified _globalID_.

__See Also:__ [faultForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tgc5lmordg64shnrxweylmjfca)

---

### availableChannel

`public EODatabaseChannel availableChannel()`

Returns an EODatabaseChannel that's registered with the receiver and that isn't busy. If the method can't find a channel that meets these criteria, it posts an [DatabaseChannelNeededNotification](#apple-irauorcgirdem) in the hopes that someone will provide a new channel. After posting the notification, the receiver checks its list of channels again. If there are still no available channels, the receiver creates an EODatabaseChannel itself. However, if the list is not empty and there are no available channels, the method returns `null`.

__See Also:__ [registerChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgkz3jon2gk4sdnbqw43tfnq), [registeredChannels](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgkz3jon2gk4tfmrbwqylonzswy4y), [unregisterChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf52w44tfm5uxg5dfojbwqylonzswy)

---

### batchFetchRelationship

`public void batchFetchRelationship( EORelationship relationship, NSArray objects, com.webobjects.eocontrol.EOEditingContext anEditingContext)`

Clear all the faults for the _relationship_ of _anEditingContext_'s _objects_ and performs a single, efficient, fetch (at most two fetches, if the relationship is many-to-many). This method provides a way to fetch the same relationship for multiple objects. For example, given an array of Employee objects, this method can fetch all of their departments with one round trip to the server, rather than asking the server for each of the employee's departments individually.

---

### commitChanges

`public void commitChanges()`

Overrides the inherited implementation to instruct the adaptor to commit the transaction. If the commit is successful, any primary and foreign key changes are written back to the saved objects, database locks are released, and an `CooperatingObjectStoreNeeded` (defined in EOControl's EOObjectStore) is posted describing the committed changes. Raises an exception if the adaptor is unable to commit the transaction; the error message indicates the nature of the problem. You should never need to invoke this method directly.

__See Also:__ [ownsGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5ygk4tgn5zg2q3imfxgozlt), [rollbackChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zg63dmmjqwg22dnbqw4z3fom)

---

### coordinator

`public com.webobjects.eocontrol.EOObjectStoreCoordinator coordinator()`

Returns the receiver's EOObjectStoreCoordinator (EOControl) or `null` if there is none.This method is only valid during a save operation.

---

### database

`public EODatabase database()`

Returns the receiver's EODatabase.

__See Also:__ [EODatabaseContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5cu6rdborqweyltmvbw63tumv4hi)

---

### delegate

`public Object delegate()`

Returns the receiver's delegate.

__See Also:__ [setDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zwk5cemvwgkz3borsq)

---

### dispose

`public void dispose()`

Conformance to NSDisposable.

---

### editingContextDidForgetObjectWithGlobalID

`public void editingContextDidForgetObjectWithGlobalID( com.webobjects.eocontrol.EOEditingContext context, com.webobjects.eocontrol.EOGlobalID gid)`

Overrides the inherited implementation. Invoked when context is no longer using the object corresponding to _gid_. EODatabaseContext's implementation destroys related data (such as snapshots) if no other objects are using it. Don't invoke this method; it is invoked automatically by the Framework.

__See Also:__ decrementSnapshotCountForGlobalID (EODatabase), incrementSnapshotCountForGlobalID (EODatabase)

---

### faultForGlobalID

`public com.webobjects.eocontrol.EOEnterpriseObject faultForGlobalID( com.webobjects.eocontrol.EOGlobalID globalID, com.webobjects.eocontrol.EOEditingContext anEditingContext)`

Overrides the inherited implementationto create a to-one fault for the object identified by _globalID_ and register it in _anEditingContext._

__See Also:__ [arrayFaultWithSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5qxe4tbpfdgc5lmorlws5diknxxk4tdmvdwy33cmfwesra)

---

### faultForRawRow

`public com.webobjects.eocontrol.EOEnterpriseObject faultForRawRow( NSDictionary row, String entityName, com.webobjects.eocontrol.EOEditingContext editingContext)`

Returns a fault for a raw row. _row_ is the raw data, in the form of an NSDictionary. _entityName_ is the name of the appropriate entity for the EO you want to create (as a fault). _editingContext_ is the EOEditingContext in which to create the fault.

---

### forgetAllLocks

`public void forgetAllLocks()`

Clears all of the receiver's locks. Doesn't cause the locks to be forgotten in the server, only in the receiver. This method is useful when something has happened to cause the server to forget the locks and the receiver needs to be synced up. This method is invoked whenever a transaction is committed or rolled back.

__See Also:__ [registerLockedObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgkz3jon2gk4smn5rwwzlej5rguzldorlws5dii5wg6ytbnreui), [isObjectLockedWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5uxgt3cnjswg5cmn5rwwzlek5uxi2chnrxweylmjfca), [isObjectLockedWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5uxgt3cnjswg5cmn5rwwzlek5uxi2chnrxweylmjfca), [forgetLocksForObjectsWithGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2ey33dnnzum33sj5rguzldorzvo2lunbdwy33cmfwesrdt), [lockObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3lj5rguzldorlws5dii5wg6ytbnreui), __lockObject__ (EOEditingContext)

---

### forgetLocksForObjectsWithGlobalIDs

`public void forgetLocksForObjectsWithGlobalIDs(NSArray globalIDs)`

Clears the locks made for the enterprise objects identified by each of the EOGlobalIDs in _globalIDs_. Doesn't cause the locks to be forgotten in the server, only in the receiver.

__See Also:__ [registerLockedObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgkz3jon2gk4smn5rwwzlej5rguzldorlws5dii5wg6ytbnreui), [isObjectLockedWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5uxgt3cnjswg5cmn5rwwzlek5uxi2chnrxweylmjfca), [isObjectLockedWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5uxgt3cnjswg5cmn5rwwzlek5uxi2chnrxweylmjfca), [forgetAllLocks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2ec3dmjrxwg23t), [lockObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3lj5rguzldorlws5dii5wg6ytbnreui), __lockObject__ (EOEditingContext)

---

### forgetSnapshotForGlobalID

`public void forgetSnapshotForGlobalID(com.webobjects.eocontrol.EOGlobalID globalID)`

Deletes the snapshot made for the enterprise object identified by _globalID_.

__See Also:__ [recordSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojsfg3tbobzwq33uizxxer3mn5rgc3cjiq), [localSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3bnrjw4ylqonug65cgn5zeo3dpmjqwyske), [recordSnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojsfg3tbobzwq33uom), [snapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zw4ylqonug65cgn5zeo3dpmjqwyske), [forgetSnapshotsForGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2fg3tbobzwq33uondg64shnrxweylmjfchg)

---

### forgetSnapshotsForGlobalIDs

`public void forgetSnapshotsForGlobalIDs(NSArray globalIDs)`

Deletes the snapshots made for the enterprise objects identified by _globalIDs_, an array of EOGlobalID objects.

__See Also:__ [recordSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojsfg3tbobzwq33uizxxer3mn5rgc3cjiq), [localSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3bnrjw4ylqonug65cgn5zeo3dpmjqwyske), [recordSnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojsfg3tbobzwq33uom), [snapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zw4ylqonug65cgn5zeo3dpmjqwyske)

---

### handleDroppedConnection

`public void handleDroppedConnection()`

Cleans up after a database connection is dropped by releasing the receiver's adaptor context and database channels, and then creating a new adaptor context. Don't invoke this method; it's invoked automatically by the Framework.

---

### handlesFetchSpecification

`public boolean handlesFetchSpecification(com.webobjects.eocontrol.EOFetchSpecification fetchSpec)`

Overrides the inherited implementation to return `true` if the receiver is responsible for fetching the objects described by the entity name in _fetchSpec_.

__See Also:__ [ownsObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5xxo3ttj5rguzldoq), [ownsGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5ygk4tgn5zg2q3imfxgozlt)

---

### hasBusyChannels

`public boolean hasBusyChannels()`

Returns `true` if the receiver's EOAdaptorContext has channels that have outstanding operations (that is, have a fetch in progress), `false` otherwise.

---

### initializeObject

`public void initializeObject( com.webobjects.eocontrol.EOEnterpriseObject object, com.webobjects.eocontrol.EOGlobalID globalID, com.webobjects.eocontrol.EOEditingContext anEditingContext)`

Overrides the inherited implementation initialize _object_ for _anEditingContext_ by filling it with properties based on row data fetched from the adaptor. The snapshot for _globalID_ is looked up and those attributes in the snapshot that are marked as class properties in the EOEntity are assigned to _object_. For relationship class properties, faults are constructed and assigned to the object.

---

### invalidateAllObjects

`public void invalidateAllObjects()`

Overrides the inherited implementation to discard all snapshots in the receiver's EODatabase, forget all locks, and post an `InvalidatedAllObjectsInStoreNotification`, as well as an `ObjectsChangedInStoreNotification` with the invalidated global IDs in the __userInfo__ dictionary. Both of these notifications are defined in EOObjectStore (EOControl). This method works by invoking [invalidateObjectsWithGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5uw45tbnruwiylumvhwe2tfmn2hgv3jorueo3dpmjqwyskeom) for all of the snapshots in the receiver's EODatabase.

---

### invalidateObjectsWithGlobalIDs

`public void invalidateObjectsWithGlobalIDs(NSArray globalIDs)`

Overrides the inherited implementation to discard the snapshots for the objects identified by the EOGlobalIDs in _globalIDs_ and broadcasts an `ObjectsChangedInStoreNotification` (defined in EOObjectStore), which causes the EOEditingContext containing objects fetched from the receiver to refault those objects. The result is that these objects will be refetched from the database the next time they're accessed.

---

### isObjectLockedWithGlobalID

`public boolean isObjectLockedWithGlobalID(com.webobjects.eocontrol.EOGlobalID globalID)`

Returns `true` if the enterprise object identified by _globalID_ is locked, `false` otherwise.

__See Also:__ [registerLockedObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgkz3jon2gk4smn5rwwzlej5rguzldorlws5dii5wg6ytbnreui), [forgetAllLocks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2ec3dmjrxwg23t), [isObjectLockedWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5uxgt3cnjswg5cmn5rwwzlek5uxi2chnrxweylmjfca), [forgetLocksForObjectsWithGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2ey33dnnzum33sj5rguzldorzvo2lunbdwy33cmfwesrdt), [lockObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3lj5rguzldorlws5dii5wg6ytbnreui), __lockObject__ (EOEditingContext)

---

### isObjectLockedWithGlobalID

`public boolean isObjectLockedWithGlobalID( com.webobjects.eocontrol.EOGlobalID globalID, com.webobjects.eocontrol.EOEditingContext anEditingContext)`

Overrides the EOObjectStore method __isObjectLockedWithGlobalID:editingContext:__ to return `true` if the database row corresponding to _globalID_ has been locked in an open transaction held by the receiver.

__See Also:__ [registerLockedObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgkz3jon2gk4smn5rwwzlej5rguzldorlws5dii5wg6ytbnreui), [isObjectLockedWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5uxgt3cnjswg5cmn5rwwzlek5uxi2chnrxweylmjfca), [forgetAllLocks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2ec3dmjrxwg23t), [forgetLocksForObjectsWithGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2ey33dnnzum33sj5rguzldorzvo2lunbdwy33cmfwesrdt), [lockObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3lj5rguzldorlws5dii5wg6ytbnreui), __lockObject__ (EOEditingContext)

---

### localSnapshotForGlobalID

`public NSDictionary localSnapshotForGlobalID(com.webobjects.eocontrol.EOGlobalID globalID)`

Returns the snapshot for the object identified by _globalID_, if there is one; else returns `null`. Only searches locally (in the transaction scope), not in the EODatabase.

__See Also:__ [recordSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojsfg3tbobzwq33uizxxer3mn5rgc3cjiq), [forgetSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2fg3tbobzwq33uizxxer3mn5rgc3cjiq), [recordSnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojsfg3tbobzwq33uom), [snapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zw4ylqonug65cgn5zeo3dpmjqwyske)

---

### localSnapshotForSourceGlobalID

`public NSArray localSnapshotForSourceGlobalID( com.webobjects.eocontrol.EOGlobalID globalID, String name)`

Returns an array that is the snapshot for the objects at the destination of the to-many relationship named _name_, which is a property of the object identified by _globalID_. The returned array contains the globalIDs of the destination objects. If there is no snapshot, returns `null`. Only searches locally (in the transaction scope), not in the EODatabase.

__See Also:__ [recordSnapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojsfg3tbobzwq33uizxxeu3povzggzkhnrxweylmjfca), [snapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zw4ylqonug65cgn5zfg33vojrwkr3mn5rgc3cjiq)

---

### lock

`public void lock()`

Used internally to protect access to the receiver in a multi-threaded environment. Do not confuse this with any methods which work with the database locking mechanism.

__See Also:__ [unlock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf52w43dpmnvq)

---

### lockObjectWithGlobalID

`public void lockObjectWithGlobalID( com.webobjects.eocontrol.EOGlobalID globalID, com.webobjects.eocontrol.EOEditingContext anEditingContext)`

Overrides the inherited implementation to attempt to lock the database row corresponding to _globalID_ in the underlying database server, on behalf of _anEditingContext_. If a transaction is not already open at the time of the lock request, the transaction is begun and is held open until either __commitChanges__ or __invalidateAllObjects__ is invoked. At that point all locks are released. Throws an exception if unable to obtain the lock.

__See Also:__ [registerLockedObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgkz3jon2gk4smn5rwwzlej5rguzldorlws5dii5wg6ytbnreui), [isObjectLockedWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5uxgt3cnjswg5cmn5rwwzlek5uxi2chnrxweylmjfca), [forgetAllLocks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2ec3dmjrxwg23t), [forgetLocksForObjectsWithGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2ey33dnnzum33sj5rguzldorzvo2lunbdwy33cmfwesrdt), __lockObject__ (EOEditingContext)

---

### missingObjectGlobalIDs

`public NSArray missingObjectGlobalIDs()`

Returns the globalIDs of any "missing" enterprise objects, or an empty array if no missing objects are known to the receiver. An object is "missing" when a fault fires and the corresponding row for the fault isn't found in the database.

To be notified when a missing object is discovered, implement the delegate method databaseContextFailedToFetchObject.

If an application tries to save a missing object, an exception is raised.

---

### objectsForSourceGlobalID

`public NSArray objectsForSourceGlobalID( com.webobjects.eocontrol.EOGlobalID globalID, String name, com.webobjects.eocontrol.EOEditingContext anEditingContext)`

Overrides the inherited implementation to service a to-many fault. The snapshot for the source object identified by _globalID_ is located and the EORelationship named _name_ is used to construct a qualifier from that snapshot. This qualifier is then used to fetch the requested objects into _anEditingContext_ using the method [objectsWithFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5xwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33o).

---

### objectsWithFetchSpecification

`public NSArray objectsWithFetchSpecification( com.webobjects.eocontrol.EOFetchSpecification fetchSpecification, com.webobjects.eocontrol.EOEditingContext anEditingContext)`

Overrides the inherited implementation to fetch objects from an external store into _anEditingContext_. The receiver obtains an available EODatabaseChannel and issues a fetch with _fetchSpecification_. If one of these objects is already present in memory, by default this method doesn't overwrite its values with the new values from the database (you can change this behavior; see the __setRefreshesRefetchedObjects__ method in the EOFetchSpecification class specification).

You can fine-tune the fetching behavior by adding hints to _fetchSpecification_'s __hints__ dictionary. For this purpose, EODatabaseContext defines the following keys:

|  |  |
| --- | --- |
| __Constant__ | __Corresponding value in the hints dictionary__ |
| `CustomQueryExpressionHintKey` | A String specifying raw SQL with which to perform the fetch. There is no way to pass down parameters with this hint. |
| `StoredProcedureNameHintKey` | A String specifying a name for a stored procedure in the model that should be used rather than building the SQL statement. The stored procedure must query the exact same attributes in the same order as EOF would query if generating the SELECT expression dynamically. If this key is supplied, other aspects of the EOFetchSpecification such as __isDeep__, __qualifier__, and __sortOrderings__ are ignored (in that sense, this key is more of a directive than a hint). There is no way to pass down parameters with this hint. |

The class description contains additional information on using these hints. See ["Using a Custom Query."](EODatabaseContext.Concepts.md#apple-ijduurcjijeuo)

You can also use this method to implement "on-demand" locking by using a _fetchSpecification_ that includes locking. For more discussion of this subject, see "Updating And Locking Strategies" in the class description.

Raises an exception if an error occurs; the error message indicates the nature of the problem.

__See Also:__ __objectsWithFetchSpecification__ (EOEditingContext)

---

### __ownsGlobalID__

`public boolean ownsGlobalID(com.webobjects.eocontrol.EOGlobalID globalID)`

Overrides the inherited implementation to return `true` if the receiver is responsible for fetching and saving the object identified by _globalID_, `false` otherwise. The receiver is determined to be responsible if _globalID_ is a subclass of EOKeyGlobalID and _globalID_ has an entity from one of the receiver's EODatabase's EOModels.

__See Also:__ [handlesFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5ugc3tenrsxgrtforrwqu3qmvrwsztjmnqxi2lpny), [ownsObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5xxo3ttj5rguzldoq)

---

### ownsObject

`public boolean ownsObject(com.webobjects.eocontrol.EOEnterpriseObject object)`

Overrides the inherited implementation to return `true` if the receiver is responsible for fetching and saving _object_, `false` otherwise. The receiver is determined to be responsible if the entity corresponding to _object_ is in one of the receiver's EODatabase's EOModels.

__See Also:__ [ownsGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5ygk4tgn5zg2q3imfxgozlt), [handlesFetchSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5ugc3tenrsxgrtforrwqu3qmvrwsztjmnqxi2lpny)

---

### performChanges

`public void performChanges()`

Overrides the inherited implementation to construct EOAdaptorOperations from the EODatabaseOperations produced during [recordChangesInEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojseg2dbnztwk42jnzcwi2lunfxgoq3pnz2gk6du) and [recordUpdateForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojsfk4demf2gkrtpojhwe2tfmn2a). Invokes the delegate method databaseContextWillOrderAdaptorOperations to give the delegate an opportunity to construct alternative EOAdaptorOperations from the EODatabaseOperations. Then invokes the delegate method databaseContextWillPerformAdaptorOperations to let the delegate substitute its own array of EOAdaptorOperations. Gives the EOAdaptorOperations to an available EOAdaptorChannel for execution. If the save succeeds, updates the snapshots in the receiver to reflect the new state of the server. You should never need to invoke this method directly.

This method raises an exception if the adaptor is unable to perform the operations. The exception's userInfo dictionary contains these keys:

|  |  |
| --- | --- |
| __Key (String Constant)__ | __Value__ |
| `DatabaseContextKey` | The EODatabaseContext object that was trying to save to its underlying repository when the exception was raised. |
| `DatabaseOperationsKey` | The list of database operations the EODatabaseContext was trying to perform when the failure occurred. |
| `FailedDatabaseOperationKey` | The database operation the EODatabaseContext failed to perform. |

The userInfo dictionary may also contain some of the keys listed in the method description for the EOAdaptorChannel method __performAdaptorOperation:__. For more information, see the EOAdaptorChannel class specification.

__See Also:__ [commitChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5rw63lnnf2eg2dbnztwk4y), [rollbackChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zg63dmmjqwg22dnbqw4z3fom)

---

### prepareForSaveWithCoordinator

`public void prepareForSaveWithCoordinator( com.webobjects.eocontrol.EOObjectStoreCoordinator coordinator, com.webobjects.eocontrol.EOEditingContext anEditingContext)`

Overrides the inherited implementation to do whatever is necessary to prepare to save changes. If needed, generates primary keys for any new objects in _anEditingContext_ that are owned by the receiver. This method is invoked before the object graph is analyzed and foreign key assignments are performed. You should never need to invoke this method directly.

---

### recordChangesInEditingContext

`public void recordChangesInEditingContext()`

Overrides the inherited implementation to construct a list of EODatabaseOperations for all changes to objects in the EOEditingContext that are owned by the receiver. Forwards any relationship changes discovered but not owned by the receiver to the EOObjectStoreCoordinator. This method is typically invoked in the course of an EOObjectStoreCoordinator saving changes through its __saveChangesInEditingContext__ method. It's invoked after [prepareForSaveWithCoordinator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5yhezlqmfzgkrtpojjwc5tfk5uxi2cdn5xxezdjnzqxi33s) and before [ownsGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5ygk4tgn5zg2q3imfxgozlt). You should never need to invoke this method directly.

---

### recordSnapshotForGlobalID

`public void recordSnapshotForGlobalID( NSDictionary aSnapshot, com.webobjects.eocontrol.EOGlobalID aGlobalID)`

Records _aSnapshot_ under _globalID_. This method only records snapshots locally (in the transaction scope). If you want to record snapshots globally, use the corresponding EODatabase method.

__See Also:__ [forgetSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2fg3tbobzwq33uizxxer3mn5rgc3cjiq), [localSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3bnrjw4ylqonug65cgn5zeo3dpmjqwyske), [recordSnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojsfg3tbobzwq33uom), [snapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zw4ylqonug65cgn5zeo3dpmjqwyske)

---

### recordSnapshotForSourceGlobalID

`public void recordSnapshotForSourceGlobalID( NSArray globalIDs, com.webobjects.eocontrol.EOGlobalID globalID, String name)`

For the object identified by _globalID_, records an NSArray of _globalIDs_ for the to-many relationship named _name_. These _globalIDs_ identify the objects at the destination of the relationship. This method only records snapshots locally (in the transaction scope). If you want to record snapshots globally, use the corresponding EODatabase method.

__See Also:__ [snapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zw4ylqonug65cgn5zfg33vojrwkr3mn5rgc3cjiq), [localSnapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3bnrjw4ylqonug65cgn5zfg33vojrwkr3mn5rgc3cjiq), [recordToManySnapshots](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojsfi32nmfxhsu3omfyhg2dporzq)

---

### recordSnapshots

`public void recordSnapshots(NSDictionary snapshots)`

Records the objects in _snapshots_, a dictionary of snapshots. The _snapshots_ argument's keys are GlobalIDs and its values are the corresponding snapshots represented as NSDictionaries. This method only records snapshots locally (in the transaction scope). If you want to record snapshots globally, use the corresponding EODatabase method.

__See Also:__ [recordSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojsfg3tbobzwq33uizxxer3mn5rgc3cjiq), [localSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3bnrjw4ylqonug65cgn5zeo3dpmjqwyske), [forgetSnapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2fg3tbobzwq33uizxxer3mn5rgc3cjiq), [snapshotForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zw4ylqonug65cgn5zeo3dpmjqwyske)

---

### recordToManySnapshots

`public void recordToManySnapshots(NSDictionary snapshots)`

Records the objects in _snapshots_. _snapshots_ should be an NSDictionary of NSDictionaries, in which the top-level dictionary has as its key the globaID of the enterprise object for which to-many relationships are being recorded. The key's value is a dictionary whose keys are the names of the Enterprise Object's to-many relationships. Each of these keys in turn has as its value an array of globalIDs that identify the objects at the destination of the relationship.

This method only records snapshots locally (in the transaction scope). If you want to record snapshots globally, use the corresponding EODatabase method.

__See Also:__ [recordSnapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgky3pojsfg3tbobzwq33uizxxeu3povzggzkhnrxweylmjfca), [snapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zw4ylqonug65cgn5zfg33vojrwkr3mn5rgc3cjiq), [localSnapshotForSourceGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3bnrjw4ylqonug65cgn5zfg33vojrwkr3mn5rgc3cjiq)

---

### recordUpdateForObject

`public void recordUpdateForObject( com.webobjects.eocontrol.EOEnterpriseObject object, NSDictionary changes)`

Overrides the inherited implementation to communicate to the receiver that _changes_ from another EOCooperatingObjectStore (through the EOObjectStoreCoordinator) need to be made to an _object_ in the receiver. For example, an insert of an object in a relationship property might require changing a foreign key property in an object owned by another cooperating store. This method can be invoked any time after [prepareForSaveWithCoordinator](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5yhezlqmfzgkrtpojjwc5tfk5uxi2cdn5xxezdjnzqxi33s) and before [ownsGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5ygk4tgn5zg2q3imfxgozlt).

---

### refaultObject

`public void refaultObject( com.webobjects.eocontrol.EOEnterpriseObject object, com.webobjects.eocontrol.EOGlobalID globalID, com.webobjects.eocontrol.EOEditingContext anEditingContext)`

Overrides the inherited implementation to refault the enterprise object identified by _globalID_ in _anEditingContext_. Newly-inserted objects should not be refaulted, since they can't be refetched from the external store. If you attempt to do this, an exception will be raised. Don't refault to-many relationship arrays, just recreate them.

This method should be used with caution since refaulting an object doesn't remove the object snapshot from the undo stack, after which the object snapshot may not refer to the proper object.

---

### registerChannel

`public void registerChannel(EODatabaseChannel channel)`

Registers _channel_, which means that it adds it to the pool of available channels used to service fetch and fault requests. You use this method if you need to perform more than one fetch simultaneously.

__See Also:__ [availableChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5qxmyljnrqwe3dfinugc3tomvwa), [registeredChannels](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgkz3jon2gk4tfmrbwqylonzswy4y), [unregisterChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf52w44tfm5uxg5dfojbwqylonzswy)

---

### registeredChannels

`public NSArray registeredChannels()`

Returns all of the EODatabaseChannels that have been registered for use with the receiver.

__See Also:__ [registerChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgkz3jon2gk4sdnbqw43tfnq), [availableChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5qxmyljnrqwe3dfinugc3tomvwa), [unregisterChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf52w44tfm5uxg5dfojbwqylonzswy)

---

### registerLockedObjectWithGlobalID

`public void registerLockedObjectWithGlobalID(com.webobjects.eocontrol.EOGlobalID globalID)`

Registers as a locked object the enterprise object identified by _globalID_. This method is used internally to keep track of objects corresponding to rows that are locked in the database.

__See Also:__ [forgetAllLocks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2ec3dmjrxwg23t), [isObjectLockedWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5uxgt3cnjswg5cmn5rwwzlek5uxi2chnrxweylmjfca), [forgetLocksForObjectsWithGlobalIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5tg64thmv2ey33dnnzum33sj5rguzldorzvo2lunbdwy33cmfwesrdt), [lockObjectWithGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3lj5rguzldorlws5dii5wg6ytbnreui), __lockObject__ (EOEditingContext)

---

### rollbackChanges

`public void rollbackChanges()`

Overrides the inherited implementation to instruct the adaptor to roll back the transaction. Rolls back any changed snapshots, and releases all locks.

__See Also:__ [ownsGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5ygk4tgn5zg2q3imfxgozlt), [commitChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5rw63lnnf2eg2dbnztwk4y)

---

### saveChangesInEditingContext

`public void saveChangesInEditingContext(com.webobjects.eocontrol.EOEditingContext context)`

Overrides the inherited implementation to save the changes made in _context_. This message is sent by an EOEditingContext to its EOObjectStore to commit changes. Normally an editing context doesn't send this message to an EODatabaseContext, but to an EOObjectStoreCoordinator. Raises an exception if an error occurs; the error message indicates the nature of the problem.

---

### setDelegate

`public void setDelegate(Object delegate)`

Sets the receiver's delegate to _delegate_, and propagates the delegate to all of the receiver's EODatabaseChannels. EODatabaseChannels share the delegate of their EODatabaseContext.

__See Also:__ [delegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5sgk3dfm5qxizi)

---

### setUpdateStrategy

`public void setUpdateStrategy(int strategy)`

Sets the update strategy used by the EODatabaseContext to _strategy_. See ["Updating And Locking Strategies" (page 172)](EODatabaseContext.Concepts.md#apple-inbuuq2hjjauo) for information on the update strategies:

- `UpdateWithOptimisticLocking`
- `UpdateWithPessimisticLocking`
- `UpdateWithNoLocking`

Throws an exception if the receiver has any transactions in progress or if you try to set _strategy_ to `UpdateWithPessimisticLocking` and the receiver's EODatabase already has snapshots.

__See Also:__ [updateStrategy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf52xazdborsvg5dsmf2gkz3z)

---

### snapshotForGlobalID

`public NSDictionary snapshotForGlobalID( com.webobjects.eocontrol.EOGlobalID globalID, long timestamp)`

`public NSDictionary snapshotForGlobalID(com.webobjects.eocontrol.EOGlobalID globalID)`

Returns the snapshot associated with _globalID_. Returns null if there isn't a snapshot for the globalID or if the corresponding timestamp is less than _timestamp_. Searches first locally (in the transaction scope) and then in the EODatabase.

---

### snapshotForSourceGlobalID

`public NSArray snapshotForSourceGlobalID( com.webobjects.eocontrol.EOGlobalID globalId, String name, long timestamp)`

`public NSArray snapshotForSourceGlobalID( com.webobjects.eocontrol.EOGlobalID globalId, String name)`

Returns the to-many snapshot for _globalId_ and _name_. A to-many snapshot is an array of globalIDs. These globalIDs identify the objects at the destination of the to-many relationship named _name_, which is a property of the object identified by _globalID._ Returns `null` if there isn't a to-many snapshot for _globalId_ or if the timestamp is less than _timestamp_. Searches first locally (in the transaction scope) and then in the EODatabase.

---

### unlock

`public void unlock()`

Used internally to release the lock that protects access to the receiver in a multi-threaded environment.

__See Also:__ [lock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5wg6y3l)

---

### unregisterChannel

`public void unregisterChannel(EODatabaseChannel channel)`

Unregisters the EODatabaseChannel _channel_, which means that it removes it from the pool of available channels used for database communication (for example, to service fetch and fault requests).

__See Also:__ [registerChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgkz3jon2gk4sdnbqw43tfnq), [registeredChannels](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zgkz3jon2gk4tfmrbwqylonzswy4y), [availableChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5qxmyljnrqwe3dfinugc3tomvwa)

---

### updateStrategy

`public int updateStrategy()`

Returns the update strategy used by the receiver, one of:

- `UpdateWithOptimisticLocking`
- `UpdateWithPessimisticLocking`
- `UpdateWithNoLocking`

The default strategy is `UpdateWithOptimisticLocking`.

__See Also:__ [setUpdateStrategy](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirqxiylcmfzwkq3pnz2gk6duf5zwk5cvobsgc5dfkn2heylumvtxs)

---

### valuesForKeys

`public NSDictionary valuesForKeys( NSArray keys, com.webobjects.eocontrol.EOEnterpriseObject object)`

Overrides the inherited implementation to return values for the specified _keys_ from the snapshot of _object_. The returned values are used primarily by another EODatabaseContext to extract foreign key properties for objects owned by the receiver.

---

## Notifications

---

### DatabaseChannelNeededNotification

This notification is broadcast whenever an EODatabaseContext is asked to perform an object store operation and it doesn't have an available EODatabaseChannel. Subscribers can create a new channel and add it to the EODatabaseContext at this time.

|  |  |
| --- | --- |
| __Notification Object__ | The EODatabaseContext. |
| __userInfo Dictionary__ | None. |

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
