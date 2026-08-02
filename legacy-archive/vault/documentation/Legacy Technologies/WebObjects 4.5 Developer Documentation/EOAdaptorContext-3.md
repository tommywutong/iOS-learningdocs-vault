---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOAdaptorContext.html
archived_at: '2026-07-15T08:11:33.381804Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOAdaptorContext

> __Inherits
> from:__  NSObject

> __Declared in:__  EOAccess/EOAdaptorContext.h

---

## Class Description

---

EOAdaptorContext is an abstract class that provides its concrete
subclasses with a structure for handling database transactions.
It's associated with EOAdaptor and EOAdaptorChannel, which, together
with EOAdaptorContext, form the _adaptor level_ of
Enterprise Objects Framework's access layer. See the EOAdaptor
class specification for more information about accessing, creating,
and using adaptor level objects.

A concrete subclass of EOAdaptorContext provides database-specific
method implementations and represents a single transaction scope
(logical user) on the database server to which its EOAdaptor object is
connected. You never interact with instances of the EOAdaptorContext
class, rather your Enterprise Objects Framework applications use
instances of concrete subclasses that are written to work with a specific
database or other persistent storage system.

If a database server supports multiple concurrent transaction
sessions, an adaptor context's EOAdaptor can have several contexts.
When you use multiple EOAdaptorContexts for a single EOAdaptor,
you can have several database server transactions in progress simultaneously.
You should be aware of the issues involved in concurrent access
if you do this.

|  |
| --- |
| EOAdaptorContext isn't declared to be abstract, but conceptually it is abstract. Never create instances of the EOAdaptorContext class. |

An EOAdaptorContext has an EOAdaptorChannel, which handles
actual access to the data on the server. If the database server
supports it, a context can have multiple channels. See your adaptor context's
documentation to find out if your adaptor supports multiple channels.
An EOAdaptorContext by default has no EOAdaptorChannels; to create
a new channel send your EOAdaptorContext a [createAdaptorChannel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dojswc5dfifsgc4dun5zeg2dbnzxgk3a) message.

The EOAdaptorContext class has the following principal attributes:

- Array of adaptor channels
- Delegate
- Adaptor

To create an instance of a concrete EOAdaptorContext subclass,
you send a [createAdaptorContext](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwg4tfmf2gkqlemfyhi33sinxw45dfpb2a) message to an
instance of the corresponding EOAdaptor subclass. You rarely create
adaptor contexts yourself. They are generally created automatically
by other framework objects.

You typically don't interact with EOAdaptorContext API directly;
rather, a concrete adaptor context subclass inherits from EOAdaptorContext
and overrides many of its methods, which are invoked automatically
by the Enterprise Objects Framework. If you're not creating a
concrete adaptor context subclass, there aren't very many methods
you need to use, and you'll rarely invoke them directly. The following
table lists the most commonly-used EOAdaptorContext methods:

|  |  |
| --- | --- |
| __Method__ | __Description__ |
| [- beginTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3cmvtws3suojqw443bmn2gs33o) | Begins a transaction in the database server. |
| [- commitTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dn5ww22lukrzgc3ttmfrxi2lpny) | Commits the last transaction begun. |
| [- rollbackTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3sn5wgyytbmnvvi4tbnzzwcy3unfxw4) | Rolls back the last transaction begun. |
| [- setDebugEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3tmv2eizlcovtuk3tbmjwgkzb2) | Enables debugging in all the adaptor context's channels. |

## Method Types

---

> **Creating an EOAdaptorContext**
> : [- initWithAdaptor:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3jnzuxiv3jorueczdbob2g64r2)
>
> **Accessing the adaptor**
> : [- adaptor](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3bmrqxa5dpoi)
>
> **Creating adaptor channels**
> : [- createAdaptorChannel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dojswc5dfifsgc4dun5zeg2dbnzxgk3a)
> : [- channels](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dnbqw43tfnrzq)
>
> **Accessing and managing
> connection status**
> : [- hasOpenChannels](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3imfzu64dfnzbwqylonzswy4y)
> : [- hasBusyChannels](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3imfzue5ltpfbwqylonzswy4y)
> : [- handleDroppedConnection](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3imfxgi3dfirzg64dqmvseg33onzswg5djn5xa)
>
> **Controlling transactions**
> : [- beginTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3cmvtws3suojqw443bmn2gs33o)
> : [- commitTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dn5ww22lukrzgc3ttmfrxi2lpny)
> : [- rollbackTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3sn5wgyytbmnvvi4tbnzzwcy3unfxw4)
> : [- transactionDidBegin](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3uojqw443bmn2gs33oiruwiqtfm5uw4)
> : [- transactionDidCommit](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3uojqw443bmn2gs33oiruwiq3pnvwws5a)
> : [- transactionDidRollback](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3uojqw443bmn2gs33oiruwiutpnrwgeyldnm)
> : [- hasOpenTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3imfzu64dfnzkheyloonqwg5djn5xa)
>
> **Debugging**
> : [+ setDebugEnabledDefault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64sdn5xhizlyoqxxgzluirswe5lhivxgcytmmvseizlgmf2wy5b2)
> : [+ debugEnabledDefault](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64sdn5xhizlyoqxwizlcovtuk3tbmjwgkzcemvtgc5lmoq)
> : [- setDebugEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3tmv2eizlcovtuk3tbmjwgkzb2)
> : [- isDebugEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3joncgkytvm5cw4ylcnrswi)
>
> **Accessing the delegate**
> : [- delegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3emvwgkz3borsq)
> : [- setDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3tmv2eizlmmvtwc5dfhi)
> : [+ defaultDelegate](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64sdn5xhizlyoqxwizlgmf2wy5cemvwgkz3borsq)
> : [+ setDefaultDelegate:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64sdn5xhizlyoqxxgzluirswmylvnr2eizlmmvtwc5dfhi)

## Class Methods

---

### debugEnabledDefault

`+ (BOOL)debugEnabledDefault`

Returns YES if new adaptor context instances
have debugging enabled by default, NO otherwise. By default, adaptor
contexts have debugging enabled if the user default EOAdaptorDebugEnabled
is YES. (For more information on user defaults, see the NSUserDefaults
class specification in the _Foundation Framework Reference_.)
You can override the user default using the class method [setDebugEnabledDefault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64sdn5xhizlyoqxxgzluirswe5lhivxgcytmmvseizlgmf2wy5b2), or you can
set debugging behavior for a specific instance with the instance method [setDebugEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3tmv2eizlcovtuk3tbmjwgkzb2).

---

### defaultDelegate

`+ (id)defaultDelegate`

Returns the default delegate-the object that
is assigned as delegate to new adaptor context instances (and their
channels).

---

### setDebugEnabledDefault:

`+ (void)setDebugEnabledDefault:(BOOL)flag`

Sets default debugging behavior for new instances
of EOAdaptorContext. If _flag_ is YES,
debugging is enabled for new instances. If _flag_ is NO,
debugging is disabled. Use the instance method [setDebugEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3tmv2eizlcovtuk3tbmjwgkzb2) to
enable debugging for a specific adaptor context.

__See
Also:__  [- isDebugEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3joncgkytvm5cw4ylcnrswi)

---

### setDefaultDelegate:

`+ (void)setDefaultDelegate:(id)defaultDelegate`

Sets the default delegate-the object assigned
as delegate to all newly created EOAdaptorContext instances (and
their EOAdaptorChannels). By default there is no default delegate.

---

## Instance Methods

---

### adaptor

`- (EOAdaptor *)adaptor`

Returns the receiver's EOAdaptor.

__See
Also:__  [- initWithAdaptor:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3jnzuxiv3jorueczdbob2g64r2)

---

### beginTransaction

`- (void)beginTransaction`

Implemented by subclasses to attempt to begin
a new transaction. A successful invocation of __beginTransaction__ must
be paired with an invocation of either __commitTransaction__ or __rollbackTransaction__ to
end the transaction.

The Enterprise Objects Framework automatically
wraps database operations in transactions, so you don't have to
begin and end transactions explicitly. In fact, letting the framework
manage transactions is sometimes more efficient. You typically use __beginTransaction__ only
to execute more than one database operation in the same transaction
scope.

This method invokes the delegate method [adaptorContextShouldBegin:](EOAdaptorContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbw63tumv4hiicemvwgkz3borss6ylemfyhi33sinxw45dfpb2fg2dpovwgiqtfm5uw4oq) before
beginning the transaction. If the transaction is begun successfully,
the method sends self a [transactionDidBegin](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3uojqw443bmn2gs33oiruwiqtfm5uw4) message
and invokes the delegate method [adaptorContextDidBegin:](EOAdaptorContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbw63tumv4hiicemvwgkz3borss6ylemfyhi33sinxw45dfpb2ei2leijswo2lohi). Raises an
exception if the attempt is unsuccessful. Some possible reasons
for failure are:

- A connection to the database
  hasn't been established.
- A transaction is already in progress.
- A fetch is in progress.
- The delegate refuses__.__
- The database server fails to begin a transaction.

An
adaptor context subclass should override this method without invoking
EOAdaptorContext's implementation.

__See
Also:__  [- hasOpenTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3imfzu64dfnzkheyloonqwg5djn5xa)

---

### channels

`- (NSArray *)channels`

Returns an array of channels created by the
receiver.

__See Also:__  [- createAdaptorChannel](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dojswc5dfifsgc4dun5zeg2dbnzxgk3a)

---

### commitTransaction

`- (void)commitTransaction`

Implemented by subclasses to attempt to commit
the last transaction begun. Invokes the delegate method [adaptorContextShouldCommit:](EOAdaptorContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbw63tumv4hiicemvwgkz3borss6ylemfyhi33sinxw45dfpb2fg2dpovwgiq3pnvwws5b2) before
committing the transaction. If the transaction is committed successfully,
the method sends self a [transactionDidCommit](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3uojqw443bmn2gs33oiruwiq3pnvwws5a) message
and invokes the delegate method [adaptorContextDidCommit:](EOAdaptorContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbw63tumv4hiicemvwgkz3borss6ylemfyhi33sinxw45dfpb2ei2leinxw23ljoq5a). Raises an
exception if the attempt is unsuccessful. Some possible reasons
for failure are:

- A transaction is not in progress.
- Fetches are in progress.
- The delegate refuses.
- The database server fails to commit.

An
adaptor context subclass should override this method without invoking
EOAdaptorContext's implementation.

__See
Also:__  [- beginTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3cmvtws3suojqw443bmn2gs33o), [- rollbackTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3sn5wgyytbmnvvi4tbnzzwcy3unfxw4), [- hasBusyChannels](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3imfzue5ltpfbwqylonzswy4y)

---

### createAdaptorChannel

`- (EOAdaptorChannel *)createAdaptorChannel`

Implemented by subclasses to create and return
a new AdaptorChannel, or nil if a new channel cannot be created. Initializes
the new channel by sending it [initWithAdaptorContext:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jnzuxiv3jorueczdbob2g64sdn5xhizlyoq5a)self.
The newly created channel retains its context. A newly created adaptor
context has no channels. Specific adaptors have different limits
on the maximum number of channels a context can have, and __createAdaptorChannel__ fails
if a newly created channel would exceed the limits.

__See
Also:__  [- channels](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dnbqw43tfnrzq)

---

### delegate

`- delegate`

Returns the receiver's delegate, or nil if
the receiver doesn't have a delegate.

---

### handleDroppedConnection

`- (void)handleDroppedConnection`

Implemented
by subclasses to clean up after the receiver's adaptor lost its
connection to its database server. Invoked from EOAdaptor's [handleDroppedConnection](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwqylomrwgkrdsn5yhazleinxw43tfmn2gs33o), this method
cleans up the state of its adaptor channels and of itself so the
receiver and its channels can be safely disposed of without any errors.

You
should never invoke this method; it is invoked automatically by
the Framework. Subclasses must implement this method, without invoking
super, if the adaptor supports automatic database reconnection.

---

### hasBusyChannels

`- (BOOL)hasBusyChannels`

Returns YES if any of the receiver's channels
have outstanding operations (that is, have a fetch in progress), NO otherwise.

__See
Also:__  [- isFetchInProgress](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jondgk5ddnbew4udsn5txezltom) (EOAdaptorChannel)

---

### hasOpenChannels

`- (BOOL)hasOpenChannels`

Returns YES if any of the receiver's channels
are open, NO otherwise.

__See Also:__  [- openChannel](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3pobsw4q3imfxg4zlm) (EOAdaptorChannel), [- isOpen](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jonhxazlo) (EOAdaptorChannel)

---

### hasOpenTransaction

`- (BOOL)hasOpenTransaction`

Returns `YES` if
a transaction is open (begun but not yet committed or rolled back), `NO` otherwise.

---

### initWithAdaptor:

`- initWithAdaptor:(EOAdaptor
*)adaptor`

The designated initializer for the EOAdaptorContext
class, this method is overridden by subclasses to initialize a newly
allocated EOAdaptorContext subclass and retain _adaptor_.
Returns __self__.

You never invoke this
method directly. You must use the EOAdaptor method [createAdaptorContext](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwg4tfmf2gkqlemfyhi33sinxw45dfpb2a) to create a
new adaptor context.

__See Also:__  [- adaptor](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3bmrqxa5dpoi)

---

### isDebugEnabled

`- (BOOL)isDebugEnabled`

Returns YES if debugging is enabled in the receiver, NO otherwise.

__See
Also:__  [+ debugEnabledDefault](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64sdn5xhizlyoqxwizlcovtuk3tbmjwgkzcemvtgc5lmoq), [+ setDebugEnabledDefault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64sdn5xhizlyoqxxgzluirswe5lhivxgcytmmvseizlgmf2wy5b2)

---

### rollbackTransaction

`- (void)rollbackTransaction`

Implemented by subclasses to attempt to roll
back the last transaction begun. Invokes the delegate method [adaptorContextShouldRollback:](EOAdaptorContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbw63tumv4hiicemvwgkz3borss6ylemfyhi33sinxw45dfpb2fg2dpovwgiutpnrwgeyldnm5a) before
rolling back the transaction. If the transaction is begun successfully,
the method sends self a [transactionDidRollback](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3uojqw443bmn2gs33oiruwiutpnrwgeyldnm) message
and invokes the delegate method [adaptorContextDidRollback:](EOAdaptorContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbw63tumv4hiicemvwgkz3borss6ylemfyhi33sinxw45dfpb2ei2lekjxwy3dcmfrwwoq). Raises an
exception if the attempt is unsuccessful. Some possible reasons
for failure are:

- A transaction is not in progress.
- Fetches are in progress.
- The delegate refuses.
- The database server fails to rollback.

An
adaptor context subclass should override this method without invoking
EOAdaptorContext's implementation.

__See
Also:__  [- beginTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3cmvtws3suojqw443bmn2gs33o), [- commitTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dn5ww22lukrzgc3ttmfrxi2lpny)

---

### setDebugEnabled:

`- (void)setDebugEnabled:(BOOL)flag`

Enables debugging in the receiver and all its
channels. If _flag_ is YES, enables
debugging; otherwise, disables debugging.

__See
Also:__  [- setDebugEnabled:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmv2eizlcovtuk3tbmjwgkzb2) (EOAdaptorChannel), [- isDebugEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3joncgkytvm5cw4ylcnrswi), [+ setDebugEnabledDefault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64sdn5xhizlyoqxxgzluirswe5lhivxgcytmmvseizlgmf2wy5b2), [- channels](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dnbqw43tfnrzq)

---

### setDelegate:

`- (void)setDelegate:delegate`

Sets the receiver's delegate and the delegate
of all the receiver's channels to _delegate_,
or removes their delegates if _delegate_ is nil.
The receiver does not retain delegate.

__See
Also:__  [- channels](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dnbqw43tfnrzq)

---

### transactionDidBegin

`- (void)transactionDidBegin`

Informs the adaptor context that a transaction
has begun in the database server, so the receiver can update its
state to reflect this fact and send an [EOAdaptorContextBeginTransactionNotification](#apple-ijeucq2ki5deo).
This method is invoked from [beginTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3cmvtws3suojqw443bmn2gs33o) after a transaction
has successfully been started. It is also invoked when the Enterprise
Objects Framework implicitly begins a transaction.

You don't
need to invoke this method unless you are implementing a concrete
adaptor. Your concrete adaptor should invoke this method from within
your adaptor context's implementation of [beginTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3cmvtws3suojqw443bmn2gs33o) method
and anywhere else it begins a transaction-either implicitly or
explicitly. For example, an adaptor channel's implementation of [evaluateExpression:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fozqwy5lborsuk6dqojsxg43jn5xdu) should
check to see if a transaction is in progress. If no transaction
is in progress, it can start one explicitly by invoking [beginTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3cmvtws3suojqw443bmn2gs33o).
Alternatively, it can start an implicit transaction by invoking [transactionDidBegin](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3uojqw443bmn2gs33oiruwiqtfm5uw4).

A
subclass of EOAdaptorContext doesn't need to override this method.
A subclass that does override it must incorporate the superclass's
version through a message to __super__.

---

### transactionDidCommit

`- (void)transactionDidCommit`

Informs the adaptor context that a transaction
has committed in the database server, so the receiver can update
its state to reflect this fact and send an [EOAdaptorContextCommitTransactionNotification](#apple-ijeucrckjbfee).
This method is invoked from [commitTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dn5ww22lukrzgc3ttmfrxi2lpny) after
a transaction has successfully committed.

You don't need
to invoke this method unless you are implementing a concrete adaptor.
Your concrete adaptor should invoke this method from within your
adaptor context's implementation of [commitTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dn5ww22lukrzgc3ttmfrxi2lpny) method
and anywhere else it commits a transaction-either implicitly or
explicitly.

A subclass of EOAdaptorContext doesn't
need to override this method. A subclass that does override it must
incorporate the superclass's version through a message to __super__.

---

### transactionDidRollback

`- (void)transactionDidRollback`

Informs the receiver that a transaction has
rolled back in the database server, so the adaptor context can update
its state to reflect this fact and send an [EOAdaptorContextRollbackTransactionNotification](#apple-ijeucrkjiveeg).
This method is invoked from [rollbackTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3sn5wgyytbmnvvi4tbnzzwcy3unfxw4) after
a transaction has successfully been rolled back.

You don't
need to invoke this method unless you are implementing a concrete
adaptor. Your concrete adaptor should invoke this method from within
your adaptor context's implementation of [rollbackTransaction](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3sn5wgyytbmnvvi4tbnzzwcy3unfxw4) method
and anywhere else it rolls back a transaction-either implicitly
or explicitly.

A subclass of EOAdaptorContext doesn't
need to override this method. A subclass that does override it must
incorporate the superclass's version through a message to __super__.

---

## Notifications

---

### EOAdaptorContextBeginTransactionNotification

Sent from [transactionDidBegin](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3uojqw443bmn2gs33oiruwiqtfm5uw4) to
tell observers that a transaction has begun. The notification contains:

|  |  |
| --- | --- |
| Notification Object | The notifying EOAdaptorContext object |
| Userinfo | None |

### EOAdaptorContextCommitTransactionNotification

Sent from [transactionDidCommit](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3uojqw443bmn2gs33oiruwiq3pnvwws5a) to
tell observers that a transaction has been committed. The notification
contains:

|  |  |
| --- | --- |
| Notification Object | The notifying EOAdaptorContext object |
| Userinfo | None |

### EOAdaptorContextRollbackTransactionNotification

Sent from [transactionDidRollback](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3uojqw443bmn2gs33oiruwiutpnrwgeyldnm) to tell observers
that a transaction has been rolled back. The notification contains:

|  |  |
| --- | --- |
| Notification Object | The notifying EOAdaptorContext object |
| Userinfo | None |

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
