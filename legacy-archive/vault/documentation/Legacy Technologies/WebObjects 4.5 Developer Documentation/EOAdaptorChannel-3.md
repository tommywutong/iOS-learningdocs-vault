---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOAdaptorChannel.html
archived_at: '2026-07-15T08:11:33.351033Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOAdaptorChannel

> __Inherits
> from:__  NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  EOAccess/EOAdaptorChannel.h

---

## Class Description

---

EOAdaptorChannel is an abstract class that provides its concrete
subclasses with a structure for performing database operations.
It's associated with EOAdaptor and EOAdaptorContext, which, together
with EOAdaptorChannel, form the __adaptor level__ of
Enterprise Objects Framework's access layer. See the [EOAdaptor](EOAdaptor-3.md#apple-ivhuczdbob2g64q) class specification for
more information about accessing, creating, and using adaptor level
objects.

A concrete subclass of EOAdaptorChannel provides database-specific
method implementations and represents an independent communication
channel to the database server to which its EOAdaptor object is
connected. You never interact with instances of the EOAdaptorChannel
class, rather your Enterprise Objects Framework applications use
instances of concrete subclasses that are written to interact with
a specific database or other persistent storage system.

You use an adaptor channel to manipulate rows (records) by
selecting, fetching, inserting, deleting, and updating them. An
adaptor channel also gives you access to some of the metadata on
the server, such as what stored procedures exist, what tables exist,
and what their basic attributes and relationships are.

All of an adaptor channel's operations take place within
the context of transactions controlled or tracked by its EOAdaptorContext.
An adaptor context may manage several channels (though not all can),
but a channel is associated with only one context.

## Notifying the Adaptor Channel's Delegate

You can assign a delegate to an adaptor channel. The EOAdaptorChannel
sends certain messages directly to the delegate, and the delegate
responds to these messages on the channel's behalf. Many of the
adaptor channel methods notify the channel's delegate before and
after an operation is performed. Some delegate methods, such as [adaptorChannel:shouldEvaluateExpression:](EOAdaptorChannel%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbwqylonzswyicemvwgkz3borss6ylemfyhi33sinugc3tomvwdu43in52wyzcfozqwy5lborsuk6dqojsxg43jn5xdu),
let the delegate determine whether the channel should perform an
operation. Others, such as [adaptorChannel:didEvaluateExpression:](EOAdaptorChannel%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbwqylonzswyicemvwgkz3borss6ylemfyhi33sinugc3tomvwduzdjmrcxmylmovqxizkfpbyhezltonuw63r2),
are simply notifications that an operation has occurred. The delegate
has an opportunity to respond by implementing the delegate methods.
If the delegate wants to intervene, it implements [adaptorChannel:shouldEvaluateExpression:](EOAdaptorChannel%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbwqylonzswyicemvwgkz3borss6ylemfyhi33sinugc3tomvwdu43in52wyzcfozqwy5lborsuk6dqojsxg43jn5xdu).
If it simply wants notification when a transaction has begun, it
implements [adaptorChannel:didEvaluateExpression:](EOAdaptorChannel%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbwqylonzswyicemvwgkz3borss6ylemfyhi33sinugc3tomvwduzdjmrcxmylmovqxizkfpbyhezltonuw63r2).

The principal attributes of the EOAdaptorChannel class are:

- Adaptor context
- Delegate

To create an instance of a concrete EOAdaptorChannel subclass,
you send a [createAdaptorChannel](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dojswc5dfifsgc4dun5zeg2dbnzxgk3a) message to an
instance of the corresponding EOAdaptorContext subclass. You rarely
create adaptor channels yourself. They are generally created automatically
by other framework objects.

The following table lists EOAdaptorChannel's more commonly-used
methods:

|  |  |
| --- | --- |
| __Method__ | __Description__ |
| [openChannel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3pobsw4q3imfxg4zlm) | Opens the channel so it can perform database operations. |
| [closeChannel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3dnrxxgzkdnbqw43tfnq) | Close the channel. |
| [selectAttributes:fetchSpecification:lock:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmvwgky3uif2hi4tjmj2xizlthjtgk5ddnbjxazldnftgsy3boruw63r2nrxwg2z2mvxhi2lupe5a) | Selects rows matching the specified qualifier. |
| [fetchRowWithZone:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi) | Fetches a row resulting from the last __selectAttributes:fetchSpecification:lock:entity:__, __executeStoredProcedure:withValues:__, or __evaluateExpression:__. |
| [insertRow:forEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jnzzwk4tukjxxootgn5zek3tunf2hsoq) | Inserts the specified row. |
| [updateValues:inRowsDescribedByQualifier:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3vobsgc5dfkzqwy5lfom5gs3ssn53xgrdfonrxe2lcmvsee6krovqwy2lgnfsxeotfnz2gs5dzhi) | Updates the row described by the specified qualifier. |
| [deleteRowDescribedByQualifier:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvwgk5dfkjxxordfonrxe2lcmvsee6krovqwy2lgnfsxeotfnz2gs5dzhi) | Deletes the row described by the specified qualifier. |
| [executeStoredProcedure:withValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fpbswg5lumvjxi33smvsfa4tpmnswi5lsmu5ho2lunblgc3dvmvztu) | Performs the specified stored procedure. |
| [evaluateExpression:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fozqwy5lborsuk6dqojsxg43jn5xdu) | Sends the specified expression to the database. |

|  |  |
| --- | --- |
| __Method__ | __Description__ |
| [- openChannel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3pobsw4q3imfxg4zlm) | Opens the channel so it can perform database operations. |
| [- closeChannel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3dnrxxgzkdnbqw43tfnq) | Close the channel. |
| [- selectAttributes:fetchSpecification:lock:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmvwgky3uif2hi4tjmj2xizlthjtgk5ddnbjxazldnftgsy3boruw63r2nrxwg2z2mvxhi2lupe5a) | Selects rows matching the specified qualifier. |
| [- fetchRowWithZone:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi) | Fetches a row resulting from the last __selectAttributes:fetchSpecification:lock:entity:__, __executeStoredProcedure:withValues:__, or __evaluateExpression:__. |
| [- insertRow:forEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jnzzwk4tukjxxootgn5zek3tunf2hsoq) | Inserts the specified row. |
| [- updateValues:inRowDescribedByQualifier:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3vobsgc5dfkzqwy5lfom5gs3ssn53uizltmnzgsytfmrbhsulvmfwgsztjmvzduzlooruxi6j2) | Updates the row described by the specified qualifier. |
| [- deleteRowDescribedByQualifier:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvwgk5dfkjxxordfonrxe2lcmvsee6krovqwy2lgnfsxeotfnz2gs5dzhi) | Deletes the row described by the specified qualifier. |
| [- executeStoredProcedure:withValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fpbswg5lumvjxi33smvsfa4tpmnswi5lsmu5ho2lunblgc3dvmvztu) | Performs the specified stored procedure. |
| [- evaluateExpression:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fozqwy5lborsuk6dqojsxg43jn5xdu) | Sends the specified expression to the database. |
| [- performAdaptorOperation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qmvzgm33snvawiylqorxxet3qmvzgc5djn5xdu) | Performs an adaptor operation by invoking the EOAdaptorChannel method appropriate for performing the specified operation. |

For more information on subclassing EOAdaptorChannel, see ["Creating an EOAdaptorChannel Subclass"](EOAdaptorChannel-4.md#apple-ijaucq2hivdeo).

## Constants

---

EOAccess defines several NSString constants in EOAdaptorChannel.h for
use as keys and values in an exception's userInfo dictionary (see [performAdaptorOperations:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qmvzgm33snvawiylqorxxet3qmvzgc5djn5xhgoq)).

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| EOAdaptorOperationsKey | A userInfo dictionary key. |
| EOFailedAdaptorOperationKey | A userInfo dictionary key. |
| EOAdaptorFailureKey | A userInfo dictionary key. |
| EOAdaptorOptimisticLockingFailure | A userInfo dictionary value. |

## Method Types

---

> **Accessing the adaptor
> context**
> : [- adaptorContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3bmrqxa5dpojbw63tumv4hi)
>
> **Opening and closing a
> channel**
> : [- openChannel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3pobsw4q3imfxg4zlm)
> : [- closeChannel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3dnrxxgzkdnbqw43tfnq)
> : [- isOpen](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jonhxazlo)
>
> **Creating an EOAdaptorChannel**
> : [- initWithAdaptorContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jnzuxiv3jorueczdbob2g64sdn5xhizlyoq5a)
>
> **Modifying rows**
> : [- insertRow:forEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jnzzwk4tukjxxootgn5zek3tunf2hsoq)
> : [- updateValues:inRowDescribedByQualifier:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3vobsgc5dfkzqwy5lfom5gs3ssn53uizltmnzgsytfmrbhsulvmfwgsztjmvzduzlooruxi6j2)
> : [- updateValues:inRowsDescribedByQualifier:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3vobsgc5dfkzqwy5lfom5gs3ssn53xgrdfonrxe2lcmvsee6krovqwy2lgnfsxeotfnz2gs5dzhi)
> : [- deleteRowDescribedByQualifier:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvwgk5dfkjxxordfonrxe2lcmvsee6krovqwy2lgnfsxeotfnz2gs5dzhi)
> : [- deleteRowsDescribedByQualifier:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvwgk5dfkjxxo42emvzwg4tjmjswiqtzkf2wc3djmzuwk4r2mvxhi2lupe5a)
> : [- lockRowComparingAttributes:entity:qualifier:snapshot:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3mn5rwwutpo5bw63lqmfzgs3thif2hi4tjmj2xizlthjsw45djor4tu4lvmfwgsztjmvzdu43omfyhg2dpoq5a)
>
> **Fetching rows**
> : [- selectAttributes:fetchSpecification:lock:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmvwgky3uif2hi4tjmj2xizlthjtgk5ddnbjxazldnftgsy3boruw63r2nrxwg2z2mvxhi2lupe5a)
> : [- describeResults](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvzwg4tjmjsvezltovwhi4y)
> : [- setAttributesToFetch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmv2ec5duojuwe5lumvzvi32gmv2gg2b2)
> : [- attributesToFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3bor2he2lcov2gk42un5dgk5ddna)
> : [- fetchRowWithZone:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi)
> : [- dictionaryWithObjects:forAttributes:zone:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3enfrxi2lpnzqxe6kxnf2gqt3cnjswg5dthjtg64sbor2he2lcov2gk4z2pjxw4zj2)
> : [- cancelFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3dmfxggzlmizsxiy3i)
> : [- isFetchInProgress](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jondgk5ddnbew4udsn5txezltom)
>
> **Invoking stored procedures**
> : [- executeStoredProcedure:withValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fpbswg5lumvjxi33smvsfa4tpmnswi5lsmu5ho2lunblgc3dvmvztu)
> : [- returnValuesForLastStoredProcedureInvocation](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3smv2hk4tokzqwy5lfondg64smmfzxiu3un5zgkzcqojxwgzleovzgksloozxwgylunfxw4)
>
> **Assigning primary keys**
> : [- primaryKeyForNewRowWithEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qojuw2ylspffwk6kgn5ze4zlxkjxxov3joruek3tunf2hsoq)
>
> **Sending SQL to the server**
> : [- evaluateExpression:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fozqwy5lborsuk6dqojsxg43jn5xdu)
>
> **Batch processing operations**
> : [- performAdaptorOperation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qmvzgm33snvawiylqorxxet3qmvzgc5djn5xdu)
> : [- performAdaptorOperations:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qmvzgm33snvawiylqorxxet3qmvzgc5djn5xhgoq)
>
> **Accessing schema information**
> : [- describeTableNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvzwg4tjmjsviylcnrsu4ylnmvzq)
> : [- describeStoredProcedureNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvzwg4tjmjsvg5dpojswiudsn5rwkzdvojsu4ylnmvzq)
> : [- addStoredProceduresNamed:toModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3bmrsfg5dpojswiudsn5rwkzdvojsxgttbnvswiotun5gw6zdfnq5a)
> : [- describeModelWithTableNames:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvzwg4tjmjsu233emvwfo2lunbkgcytmmvhgc3lfom5a)
>
> **Debugging**
> : [- setDebugEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmv2eizlcovtuk3tbmjwgkzb2)
> : [- isDebugEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3joncgkytvm5cw4ylcnrswi)
>
> **Accessing the delegate**
> : [- delegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvwgkz3borsq)
> : [- setDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmv2eizlmmvtwc5dfhi)

## Instance Methods

---

### adaptorContext

`- (EOAdaptorContext *)adaptorContext`

Returns the receiver's EOAdaptorContext. A
subclass of EOAdaptorChannel doesn't need to override this method.

__See
Also:__  [- initWithAdaptorContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jnzuxiv3jorueczdbob2g64sdn5xhizlyoq5a)

---

### addStoredProceduresNamed:toModel:

`- (void)addStoredProceduresNamed:(NSArray
*)storedProcedureNames
toModel:(EOModel *)model`

Overridden by subclasses to create EOStoredProcedure
objects for the stored procedures named in _storedProcedureNames_ and
then to add them to _model_. This method
is used in conjunction with [describeStoredProcedureNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvzwg4tjmjsvg5dpojswiudsn5rwkzdvojsu4ylnmvzq) to build
a default model in EOModeler. Raises an exception if an error occurs.

---

### attributesToFetch

`- (NSArray *)attributesToFetch`

Implemented by subclasses to return the set
of attributes to retrieve when [fetchRowWithZone:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi) is
next invoked. An adaptor channel subclass should override this method
without invoking EOAdaptorChannel's implementation.

---

### cancelFetch

`- (void)cancelFetch`

Implemented by subclasses to clear all result
sets established by the last [selectAttributes:fetchSpecification:lock:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmvwgky3uif2hi4tjmj2xizlthjtgk5ddnbjxazldnftgsy3boruw63r2nrxwg2z2mvxhi2lupe5a), [executeStoredProcedure:withValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fpbswg5lumvjxi33smvsfa4tpmnswi5lsmu5ho2lunblgc3dvmvztu),
or [evaluateExpression:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fozqwy5lborsuk6dqojsxg43jn5xdu) message
and terminate the current fetch, so that __isFetchInProgress__ returns NO.

An
adaptor channel subclass should override this method without invoking
EOAdaptorChannel's implementation.

---

### closeChannel

`- (void)closeChannel`

Implemented by subclasses to close the EOAdaptorChannel
so that it can't perform operations with the server. Any fetch
in progress is canceled. If the receiver is the last open channel
in an adaptor context and if the channel's adaptor context has
outstanding transactions, closing the channel has server-dependent
results: some database servers roll back all outstanding transactions
but others do nothing. Regardless of whether outstanding transactions
are rolled back, this method has the side effect of closing the
receiver's adaptor context's connection with the database if
the receiver is its adaptor context's last open channel.

An
adaptor channel subclass should override this method without invoking
EOAdaptorChannel's implementation.

__See
Also:__  [- cancelFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3dmfxggzlmizsxiy3i), [- hasOpenTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3imfzu64dfnzkheyloonqwg5djn5xa) (EOAdaptorContext)

---

### delegate

`- (id)delegate`

Returns the receiver's delegate, or nil if
the receiver doesn't have a delegate. A subclass of EOAdaptorChannel
doesn't need to override this method.

---

### deleteRowDescribedByQualifier:entity:

`- (void)deleteRowDescribedByQualifier:(EOQualifier
*)qualifier
entity:(EOEntity *)entity`

Deletes the row described by _qualifier_ from
the database table corresponding to _entity_.
Invokes [deleteRowsDescribedByQualifier:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvwgk5dfkjxxo42emvzwg4tjmjswiqtzkf2wc3djmzuwk4r2mvxhi2lupe5a) and raises an
exception unless exactly one row is deleted. A subclass of EOAdaptorChannel
doesn't need to override this method.

---

### deleteRowsDescribedByQualifier:entity:

`- (unsigned int)deleteRowsDescribedByQualifier:(EOQualifier
*)qualifier
entity:(EOEntity *)entity`

Implemented by subclasses to delete the rows
described by _qualifier_ from the database
table corresponding to _entity_. Returns
the number of rows deleted. Raises an exception on failure. Some possible
reasons for failure are:

- The adaptor channel isn't
  open.
- The adaptor channel is in an invalid state (for example, it's
  fetching).
- An error occurs in the database server.

An
adaptor channel subclass should override this method without invoking
EOAdaptorChannel's implementation.

__See
Also:__  [- deleteRowDescribedByQualifier:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvwgk5dfkjxxordfonrxe2lcmvsee6krovqwy2lgnfsxeotfnz2gs5dzhi), [- isOpen](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jonhxazlo), [- isFetchInProgress](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jondgk5ddnbew4udsn5txezltom),
[- hasOpenTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3imfzu64dfnzkheyloonqwg5djn5xa) (EOAdaptorContext)

---

### describeModelWithTableNames:

`- (EOModel *)describeModelWithTableNames:(NSArray
*)tableNames`

Overridden by subclasses to create and return
a default model containing entities for the tables specified in
tableNames. Assigns the adaptor name and connection dictionary to
the new model. This method is typically used in conjunction with __describeTableNames__ and [describeStoredProcedureNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvzwg4tjmjsvg5dpojswiudsn5rwkzdvojsu4ylnmvzq).

EOAdaptorChannel's
implementation does nothing. An adaptor channel subclass should
override this method to create a default model from the database's
metadata.

---

### describeResults

`- (NSArray *)describeResults`

Implemented by subclasses to return an array
of EOAttributes describing the properties available in the current
result set, as determined by [selectAttributes:fetchSpecification:lock:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmvwgky3uif2hi4tjmj2xizlthjtgk5ddnbjxazldnftgsy3boruw63r2nrxwg2z2mvxhi2lupe5a), [executeStoredProcedure:withValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fpbswg5lumvjxi33smvsfa4tpmnswi5lsmu5ho2lunblgc3dvmvztu),
or a statement evaluated by __evaluateExpression:__.
Only invoke this method if a fetch is in progress as determined
by [isFetchInProgress](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jondgk5ddnbew4udsn5txezltom).

An
adaptor channel subclass should override this method without invoking
EOAdaptorChannel's implementation.

---

### describeStoredProcedureNames

`- (NSArray *)describeStoredProcedureNames`

Overridden by subclasses to read and return
an array of stored procedure names from the database. This method
is used in conjunction with [addStoredProceduresNamed:toModel:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3bmrsfg5dpojswiudsn5rwkzdvojsxgttbnvswiotun5gw6zdfnq5a) to
build a default model in EOModeler. Raises an exception if an error
occurs.

---

### describeTableNames

`- (NSArray *)describeTableNames`

Overridden by subclasses to read and return
an array of table names from the database. This method in conjunction
with [describeModelWithTableNames:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvzwg4tjmjsu233emvwfo2lunbkgcytmmvhgc3lfom5a) is used
to build a default model.

EOAdaptorChannel's implementation
simply returns nil. An adaptor channel subclass should override
this method to construct an array of table names from database metadata.

---

### dictionaryWithObjects:forAttributes:zone:

`- (NSMutableDictionary *)dictionaryWithObjects:(id
*)objects
forAttributes:(NSArray *)attributes
zone:(NSZone *)zone`

Used by EOAdaptorChannel subclasses to create
dictionaries that can be returned from [fetchRowWithZone:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi).
You don't ordinarily invoke this method unless you are writing
your own concrete adaptor. If you are writing a concrete adaptor,
use of this method is optional but strongly recommended because
it enables performance optimizations. The objects in _objects_ are
the values for the row that correspond to the EOAttribute objects
in _attributes_. The dictionary representation
of the row is created from _zone_.

A
subclass of EOAdaptorChannel shouldn't override this method.

---

### evaluateExpression:

`- (void)evaluateExpression:(EOSQLExpression
*)expression`

Implemented by subclasses to send _expression_ to
the database server for evaluation, beginning a transaction first
and committing it after evaluation if a transaction isn't already
in progress. Raises an exception if an error occurs. An EOAdaptorChannel
uses this method to send SQL expressions to the database.

If
expression results in a select operation being performed, you can
fetch the results as you would if you had sent a [selectAttributes:fetchSpecification:lock:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmvwgky3uif2hi4tjmj2xizlthjtgk5ddnbjxazldnftgsy3boruw63r2nrxwg2z2mvxhi2lupe5a).
You must use the method [setAttributesToFetch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmv2ec5duojuwe5lumvzvi32gmv2gg2b2) before
you begin fetching. Also, if _expression_ evaluates
to multiple result sets, you must invoke __setAttributesToFetch:__ before
you begin fetching each subsequent set.

__evaluateExpression:__ invokes
the delegate methods [adaptorChannel:shouldEvaluateExpression:](EOAdaptorChannel%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbwqylonzswyicemvwgkz3borss6ylemfyhi33sinugc3tomvwdu43in52wyzcfozqwy5lborsuk6dqojsxg43jn5xdu) and [adaptorChannel:didEvaluateExpression:](EOAdaptorChannel%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbwqylonzswyicemvwgkz3borss6ylemfyhi33sinugc3tomvwduzdjmrcxmylmovqxizkfpbyhezltonuw63r2).

An
adaptor channel subclass should override this method without invoking
EOAdaptorChannel's implementation. Note, however, that the upper
layers of the Framework never invoke [evaluateExpression:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fozqwy5lborsuk6dqojsxg43jn5xdu) directly.
Thus, adaptors for data stores that don't naturally support an
expression language (for example, flat file adaptors) don't need
to implement this method to work with the Framework.

__See
Also:__  [- fetchRowWithZone:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi)

---

### executeStoredProcedure:withValues:

`- (void)executeStoredProcedure:(EOStoredProcedure
*)storedProcedure
withValues:(NSDictionary *)values`

Implemented by subclasses to execute storedProcedure.
Any arguments to the stored procedure are in _values_,
a dictionary whose keys are the argument names. Use [fetchRowWithZone:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi) to
get result rows and [returnValuesForLastStoredProcedureInvocation](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3smv2hk4tokzqwy5lfondg64smmfzxiu3un5zgkzcqojxwgzleovzgksloozxwgylunfxw4) to
get return arguments and result status, if any. Raises an exception
if an error occurs.

An adaptor channel subclass should override
this method without invoking EOAdaptorChannel's implementation.
Note, however, that the upper layers of the Framework never invoke [executeStoredProcedure:withValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fpbswg5lumvjxi33smvsfa4tpmnswi5lsmu5ho2lunblgc3dvmvztu) directly.
Thus, adaptors for data stores that don't support stored procedures
(for example, flat file adaptors) don't need to implement this
method to work with the Framework

---

### fetchRowWithZone:

`- (NSMutableDictionary *)fetchRowWithZone:(NSZone
*)zone`

Implemented by subclasses to fetch the next
row from the result set of the last [selectAttributes:fetchSpecification:lock:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmvwgky3uif2hi4tjmj2xizlthjtgk5ddnbjxazldnftgsy3boruw63r2nrxwg2z2mvxhi2lupe5a), [executeStoredProcedure:withValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fpbswg5lumvjxi33smvsfa4tpmnswi5lsmu5ho2lunblgc3dvmvztu),
or [evaluateExpression:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fozqwy5lborsuk6dqojsxg43jn5xdu) message
sent to the receiver. Returns values for the receiver's [attributesToFetch](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3bor2he2lcov2gk42un5dgk5ddna) in
a dictionary whose keys are the attribute names. When there are
no more rows in the current result set, this method returns nil,
and invokes the delegate method [adaptorChannelDidChangeResultSet:](EOAdaptorChannel%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbwqylonzswyicemvwgkz3borss6ylemfyhi33sinugc3tomvwei2leinugc3thmvjgk43vnr2fgzluhi) if
there are more results sets. When there are no more rows or result
sets, this method returns nil, ends the fetch, and invokes [adaptorChannelDidFinishFetching:](EOAdaptorChannel%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbwqylonzswyicemvwgkz3borss6ylemfyhi33sinugc3tomvwei2leizuw42ltnbdgk5ddnbuw4zz2). [isFetchInProgress](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jondgk5ddnbew4udsn5txezltom) returns YES until
the fetch is canceled or until this method exhausts all result sets
and returns nil. This method also invoke the delegate methods [adaptorChannelWillFetchRow:](EOAdaptorChannel%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbwqylonzswyicemvwgkz3borss6ylemfyhi33sinugc3tomvwfo2lmnrdgk5ddnbjg65z2) and [adaptorChannel:didFetchRow:](EOAdaptorChannel%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbwqylonzswyicemvwgkz3borss6ylemfyhi33sinugc3tomvwduzdjmrdgk5ddnbjg65z2).Raises an
exception if an error occurs.

An adaptor channel subclass should
override this method without invoking EOAdaptorChannel's implementation.

__See
Also:__  [- setAttributesToFetch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmv2ec5duojuwe5lumvzvi32gmv2gg2b2)

---

### initWithAdaptorContext:

`- initWithAdaptorContext:(EOAdaptorContext
*)adaptorContext`

The designated initializer for the EOAdaptorChannel
class, this method is overridden by subclasses to initialize a newly
allocated EOAdaptorChannel subclass and retain _adaptorContext_.
Returns __self__.

You never invoke this
method directly unless you are implementing a concrete adaptor context.
It is invoked automatically from [createAdaptorChannel](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dojswc5dfifsgc4dun5zeg2dbnzxgk3a)-the EOAdaptorContext
method you use to create a new adaptor channel.

A subclass
of EOAdaptorChannel doesn't need to override this method, but
may override it to perform additional initialization. A subclass
that does override this method must incorporate the superclass's version
through a message to __super__.

__See
Also:__  [- adaptorContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3bmrqxa5dpojbw63tumv4hi)

---

### insertRow:forEntity:

`- (void)insertRow:(NSDictionary
*)row
forEntity:(EOEntity *)entity`

Implemented by subclasses to insert the values
of _row_ into the table in the database
that corresponds to _entity_. _row_ is
a dictionary whose keys are attribute names and whose values are
the values to insert. Raises an exception on failure. Some possible
reasons for failure are:

- The user logged in to
  the database doesn't have permission to insert a new row.
- The adaptor channel is in an invalid state (for example, fetching).
- The row fails to satisfy a constraint defined in the database
  server.

An adaptor channel subclass should
override this method without invoking EOAdaptorChannel's implementation.

---

### isDebugEnabled

`- (BOOL)isDebugEnabled`

Returns YES if the adaptor channel logs evaluated
SQL and other useful information to the console (or to the standard
error stream), NO if not. A subclass of EOAdaptorChannel doesn't
need to override this method.

__See Also:__  [- setDebugEnabled:](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3tmv2eizlcovtuk3tbmjwgkzb2) (EOAdaptorContext)

---

### isFetchInProgress

`- (BOOL)isFetchInProgress`

Implemented by subclasses to return YES if the
receiver is fetching, NO otherwise. An adaptor channel is fetching
if:

- It's been sent a successful [selectAttributes:fetchSpecification:lock:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmvwgky3uif2hi4tjmj2xizlthjtgk5ddnbjxazldnftgsy3boruw63r2nrxwg2z2mvxhi2lupe5a) message.
- A stored procedure that returns rows has been successfully
  executed using [executeStoredProcedure:withValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fpbswg5lumvjxi33smvsfa4tpmnswi5lsmu5ho2lunblgc3dvmvztu).
- An expression sent through __evaluateExpression:__ resulted
  in a select operation being performed.

An
adaptor channel stops fetching when there are no more records to
fetch or when it's sent a __cancelFetch__ message.

An
adaptor channel subclass should override this method without invoking
EOAdaptorChannel's implementation.

__See
Also:__  [- fetchRowWithZone:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi)

---

### isOpen

`- (BOOL)isOpen`

Implemented by subclasses to return YES if the
channel has been opened with __openChannel__, NO if
not. An adaptor channel subclass should override this method without
invoking EOAdaptorChannel's implementation.

__See
Also:__  [- closeChannel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3dnrxxgzkdnbqw43tfnq)

---

### lockRowComparingAttributes:entity:qualifier:snapshot:

`- (void)lockRowComparingAttributes:(NSArray
*)attributes
entity:(EOEntity *)entity
qualifier:(EOQualifier *)qualifier
snapshot:(NSDictionary *)snapshot`

Attempts to lock a row in the database by selecting
it with locking on. The lock operation succeeds if a select statement
generated with _qualifier_ retrieves
exactly one row and the values in the row match the values in _snapshot_,
a dictionary whose keys are attribute names and whose values are
the values that were last fetched from the database.

__lockRowComparingAttributes:entity:qualifier:snapshot:__ invokes [selectAttributes:fetchSpecification:lock:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmvwgky3uif2hi4tjmj2xizlthjtgk5ddnbjxazldnftgsy3boruw63r2nrxwg2z2mvxhi2lupe5a) with _attributes_ as
the attributes to select, a fetch specification built from _qualifier_,
locking on, and _entity_ as the entity.
If the select returns no rows or more than one row, the method raises an EOGeneralAdaptorException.
It also raises an EOGeneralAdaptorException if the values in the
returned row don't match the corresponding values in _snapshot_.

The
Framework uses this method whenever it needs to lock a row. When
the Framework invokes it, _qualifier_ specifies
the primary key of the row to be locked and attributes used for
locking to be compared in the database server. If any of the values
specified in _qualifier_ are different
from the values in the database row, the select operation will not
retrieve or lock the row. When this happens, the row to be locked
has been updated in the database since it was last retrieved, and
it isn't safe to update it.

Some attributes (such
as BLOB types) can't be compared in the database. _attributes_ should
specify any such attributes. (If the row doesn't contain any such
attributes, _attributes_ can be nil.)
If _qualifier_ generates a select statement
that returns and locks a single row, this method performs an in-memory comparison
between the value in the retrieved row and the value in _snapshot_ for
each attribute in _attributes_. Therefore, _snapshot_ must
contain an entry for each attribute in _attributes_.
In addition, it must contain an entry for the row's primary key.

A
subclass of EOAdaptorChannel doesn't need to override this method.

---

### openChannel

`- (void)openChannel`

Implemented by subclasses to put the channel
and both its context and adaptor into a state where they are ready
to perform database operations. Raises an exception if an error
occurs. An adaptor channel subclass should override this method
without invoking EOAdaptorChannel's implementation.

__See
Also:__  [- isOpen](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jonhxazlo), [- closeChannel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3dnrxxgzkdnbqw43tfnq)

---

### performAdaptorOperation:

`- (void)performAdaptorOperation:(EOAdaptorOperation
*)adaptorOperation`

Performs _adaptorOperation_ by
invoking the adaptor channel method appropriate for performing the specified
operation. For example, if the adaptor operator for _adaptorOperation_ is EOAdaptorInsertOperator,
this method invokes [insertRow:forEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jnzzwk4tukjxxootgn5zek3tunf2hsoq) using
information in _adaptorOperation_ to
supply the arguments. Raises an exception if an error occurs.

A
subclass of EOAdaptorChannel doesn't need to override this method.

__See
Also:__  [- performAdaptorOperations:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qmvzgm33snvawiylqorxxet3qmvzgc5djn5xhgoq)

---

### performAdaptorOperations:

`- (void)performAdaptorOperations:(NSArray
*)adaptorOperations`

Performs adaptor operations by invoking [performAdaptorOperation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qmvzgm33snvawiylqorxxet3qmvzgc5djn5xdu) with each
EOAdaptorOperation object in the array _adaptorOperations_.
An adaptor channel subclass may be able to override this method to
take advantage of database-specific batch processing capabilities.
Invokes the delegate methods [adaptorChannel:willPerformOperations:](EOAdaptorChannel%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbwqylonzswyicemvwgkz3borss6ylemfyhi33sinugc3tomvwdu53jnrwfazlsmzxxe3kpobsxeylunfxw44z2) and [adaptorChannel:didPerformOperations:exception:](EOAdaptorChannel%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbwqylonzswyicemvwgkz3borss6ylemfyhi33sinugc3tomvwduzdjmrigk4tgn5zg2t3qmvzgc5djn5xhgotfpbrwk4dunfxw4oq).

This
method raises an exception if an error occurs. The exception's
userInfo dictionary contains these keys:

|  |  |
| --- | --- |
| __Constant__ | __The corresponding value in the exception's userInfo dictionary__ |
| `EOAdaptorOperationsKey` | An array of the EOAdaptorOperations being executed. |
| [EOFailedAdaptorOperationKey](#apple-ijaucrcgivdes) | The particular EOAdaptorOperation that failed. |
| `EOAdaptorFailureKey` | If present, offers additional information on the type of error that occurred. Currently, the only possible value for this key is `EOAdaptorOptimisticLockingFailure`, which indicates that an update or lock operation failed because the row found in the database did not match the snapshot taken when the row was last fetched into the application. |

A subclass of EOAdaptorChannel doesn't need to override
the __performAdaptorOperations:__ method.

---

### primaryKeyForNewRowWithEntity:

`- (NSDictionary *)primaryKeyForNewRowWithEntity:(EOEntity
*)entity`

Overridden by subclasses to return a primary
key for a new row in the database table that corresponds to _entity_.
The primary key returned from this method is a dictionary whose
keys are the primary key attribute names. For example, suppose you've
got a table MOVIE with primary key MOVIE_ID, and the corresponding
Movie entity's primary key attribute is __movieID__.
In this scenario, the dictionary returned from [primaryKeyForNewRowWithEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qojuw2ylspffwk6kgn5ze4zlxkjxxov3joruek3tunf2hsoq) has
one entry whose key is __movieID__ and whose
value is the unique value to assign. If the primary key is compound
(made up of more than one attribute), the dictionary should contain
an entry for each primary key attribute. Note, however, that the
Enterprise Objects Frameworks adaptors don't handle compound primary
keys; they return nil from [primaryKeyForNewRowWithEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qojuw2ylspffwk6kgn5ze4zlxkjxxov3joruek3tunf2hsoq) if
the primary key is compound.

If information in _entity_ specifies
an adaptor-specific means to assign a new primary key (for example, a
sequence name or stored procedure), then this method returns a new
primary key. Otherwise, if the key is a simple integer, the method
tries to fetch a new primary key from the database using an adaptor-specific
scheme. Otherwise, the method returns nil.

EOAdaptorChannel's
implementation simply returns nil. See your adaptor channel's
documentation for information on how it generates primary keys.

A
subclass of EOAdaptorChannel must override this method. For example,
to return a value generated by a sequence, you'd create the proper
SQL statement (using EOSQLExpression's [expressionForString:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5sxq4dsmvzxg2lpnzdg64storzgs3thhi) method)
and evaluate it (using the [evaluateExpression:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fozqwy5lborsuk6dqojsxg43jn5xdu) method).

---

### returnValuesForLastStoredProcedureInvocation

`- (NSDictionary *)returnValuesForLastStoredProcedureInvocation`

Implemented by subclasses to return stored procedure
parameter and return values. Used in conjunction with [executeStoredProcedure:withValues:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fpbswg5lumvjxi33smvsfa4tpmnswi5lsmu5ho2lunblgc3dvmvztu).
The dictionary returned by this method has entries whose keys are
stored procedure parameter names and whose values are the parameter
values. The dictionary also contains a special entry for the stored
procedures return value with the key "returnValue". Returns
an empty dictionary for stored procedures that have void return
types. Returns nil if the stored procedure has results to fetch.
In this case, you must use [fetchRowWithZone:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi) until
there are no more results to fetch before the return value will
be available.

An adaptor channel subclass should override this
method without invoking EOAdaptorChannel's implementation.

---

### selectAttributes:fetchSpecification:lock:entity:

`- (void)selectAttributes:(NSArray
*)attributes
fetchSpecification:(EOFetchSpecification
*)fetchSpecification
lock:(BOOL)flag
entity:(EOEntity *)entity`

Implemented by subclasses to select attributes
in rows matching the qualifier in _fetchSpecification_ and
set the receiver's attributes to fetch. The selected rows compose
one or more result sets, each row of which will be returned by subsequent [fetchRowWithZone:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi) messages
according to fetchSpecification's sort orderings. If flag is YES,
the rows are locked if possible so that no other user can modify
them (the lock specification in _fetchSpecification_ is
ignored). Raises an exception if an error occurs. Some possible
reasons for failure are:

- The adaptor channel is
  in an invalid state (for example, fetching).
- The database failed to lock the specified rows.

An
adaptor channel subclass should override this method without invoking
EOAdaptorChannel's implementation.

__See
Also:__  [- setAttributesToFetch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmv2ec5duojuwe5lumvzvi32gmv2gg2b2)

---

### setAttributesToFetch:

`- (EOAdaptorContext *)adaptorContext`

Implemented by subclasses to specify the set
of attributes used to describe fetch data from a corresponding select. _attributes_ is
an array of the attributes to fetch. This method is invoked after [evaluateExpression:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fozqwy5lborsuk6dqojsxg43jn5xdu) but
before the first call to [fetchRowWithZone:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi).
This method raises an exception if invoked when there is no fetch
in progress.

An adaptor channel subclass should override this
method without invoking EOAdaptorChannel's implementation.

__See
Also:__  [- selectAttributes:fetchSpecification:lock:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmvwgky3uif2hi4tjmj2xizlthjtgk5ddnbjxazldnftgsy3boruw63r2nrxwg2z2mvxhi2lupe5a)

---

### setDebugEnabled:

`- (void)setDebugEnabled:(BOOL)flag`

Enables debugging in the receiver and all its
channels. If _flag_ is YES, enables
debugging; otherwise, disables debugging. When debugging is enabled,
the adaptor channel logs evaluated SQL and other useful debugging
information to the console (or to the standard error stream). The
information provided may vary from adaptor to adaptor and may change
from release to release.

A subclass of EOAdaptorChannel doesn't
need to override this method. A subclass that does override it must
incorporate the superclass's version through a message to __super__.

__See
Also:__  [- setDebugEnabled:](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3tmv2eizlcovtuk3tbmjwgkzb2) (EOAdaptorContext)

---

### setDelegate:

`- (void)setDelegate:(id)delegate`

Sets the receiver's delegate to _delegate_,
or removes its delegate if _delegate_ is nil.The
receiver does not retain its delegate. A subclass of EOAdaptorChannel
doesn't need to override this method. A subclass that does override
it must incorporate the superclass's version through a message
to __super__.

---

### updateValues:inRowDescribedByQualifier:entity:

`- (void)updateValues:(NSDictionary
*)values
inRowDescribedByQualifier:(EOQualifier
*)qualifier
entity:(EOEntity *)entity`

Updates the row described by _qualifier_.
Invokes [updateValues:inRowsDescribedByQualifier:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3vobsgc5dfkzqwy5lfom5gs3ssn53xgrdfonrxe2lcmvsee6krovqwy2lgnfsxeotfnz2gs5dzhi) and
raises an exception unless exactly one row is updated.

A subclass
of EOAdaptorChannel doesn't need to override this method.

---

### updateValues:inRowsDescribedByQualifier:entity:

`- (unsigned int)updateValues:(NSDictionary
*)values
inRowsDescribedByQualifier:(EOQualifier
*)qualifier
entity:(EOEntity *)entity`

Implemented by subclasses to update the rows
described by qualifier with the values in _values_. _values_ is
a dictionary whose keys are attribute names and whose values are
the new values for those attributes (the dictionary need only contain
entries for the attributes being changed). Returns the number of updated
rows. Raises an exception if an error occurs. Some possible reasons
for failure are:

- The user logged in to the database
  doesn't have permission to update.
- The adaptor channel is in an invalid state (for example, fetching).
- The new values fail to satisfy a constraint defined in the
  database server.

An adaptor channel subclass
should override this method without invoking EOAdaptorChannel's implementation.

__See
Also:__  [- updateValues:inRowDescribedByQualifier:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3vobsgc5dfkzqwy5lfom5gs3ssn53uizltmnzgsytfmrbhsulvmfwgsztjmvzduzlooruxi6j2)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
