---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EOAdaptorContext.html
archived_at: '2026-07-15T08:13:41.255722Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOAdaptorContext

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.eoaccess

---

## Class Description

---

EOAdaptorContext is an abstract class that provides its concrete subclasses with a structure for handling database transactions. It's associated with EOAdaptor and EOAdaptorChannel, which, together with EOAdaptorContext, form the _adaptor level_ of Enterprise Objects Framework's access layer. See the EOAdaptor class specification for more information about accessing, creating, and using adaptor level objects.

A concrete subclass of EOAdaptorContext provides database-specific method implementations and represents a single transaction scope (logical user) on the database server to which its EOAdaptor object is connected. You never interact with instances of the EOAdaptorContext class, rather your Enterprise Objects Framework applications use instances of concrete subclasses that are written to work with a specific database or other persistent storage system.

If a database server supports multiple concurrent transaction sessions, an adaptor context's EOAdaptor can have several contexts. When you use multiple EOAdaptorContexts for a single EOAdaptor, you can have several database server transactions in progress simultaneously. You should be aware of the issues involved in concurrent access if you do this.

|  |
| --- |
| __Note:__ EOAdaptorContext is abstract. Never create instances of the EOAdaptorContext class. |

An EOAdaptorContext has an EOAdaptorChannel, which handles actual access to the data on the server. If the database server supports it, a context can have multiple channels. See your adaptor context's documentation to find out if your adaptor supports multiple channels. An EOAdaptorContext by default has no EOAdaptorChannels; to create a new channel send your EOAdaptorContext a [createAdaptorChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmnzgkylumvawiylqorxxeq3imfxg4zlm) message.

The EOAdaptorContext class has the following principal attributes:

- Array of adaptor channels
- Delegate
- Adaptor

To create an instance of a concrete EOAdaptorContext subclass, you send a createAdaptorContext message to an instance of the corresponding EOAdaptor subclass. You rarely create adaptor contexts yourself. They are generally created automatically by other framework objects.

You typically don't interact with EOAdaptorContext API directly; rather, a concrete adaptor context subclass inherits from EOAdaptorContext and overrides many of its methods, which are invoked automatically by the Enterprise Objects Framework. If you're not creating a concrete adaptor context subclass, there aren't very many methods you need to use, and you'll rarely invoke them directly. The following table lists the most commonly-used EOAdaptorContext methods:

|  |  |
| --- | --- |
| __Method__ | __Description__ |
| [beginTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmjswo2lokrzgc3ttmfrxi2lpny) | Begins a transaction in the database server. |
| [commitTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmnxw23ljorkheyloonqwg5djn5xa) | Commits the last transaction begun. |
| [rollbackTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpojxwy3dcmfrwwvdsmfxhgyldoruw63q) | Rolls back the last transaction begun. |

## Method Types

---

> **Constructors**
> : [EOAdaptorContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpivhuczdbob2g64sdn5xhizlyoq)
>
> **Accessing the adaptor**
> : [adaptor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmfsgc4dun5za)
>
> **Creating adaptor channels**
> : [createAdaptorChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmnzgkylumvawiylqorxxeq3imfxg4zlm): [channels](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmnugc3tomvwhg)
>
> **Accessing and managing connection status**
> : [hasOpenChannels](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpnbqxgt3qmvxeg2dbnzxgk3dt): [hasBusyChannels](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpnbqxgqtvon4ug2dbnzxgk3dt): [handleDroppedConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpnbqw4zdmmvche33qobswiq3pnzxgky3unfxw4)
>
> **Controlling transactions**
> : [beginTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmjswo2lokrzgc3ttmfrxi2lpny): [commitTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmnxw23ljorkheyloonqwg5djn5xa): [rollbackTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpojxwy3dcmfrwwvdsmfxhgyldoruw63q): [transactionDidBegin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bporzgc3ttmfrxi2lpnzcgszccmvtws3q): [transactionDidCommit](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bporzgc3ttmfrxi2lpnzcgszcdn5ww22lu): [transactionDidRollback](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bporzgc3ttmfrxi2lpnzcgszcsn5wgyytbmnvq): [hasOpenTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpnbqxgt3qmvxfi4tbnzzwcy3unfxw4)
>
> **Accessing the delegate**
> : [delegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmrswyzlhmf2gk): [setDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bponsxirdfnrswoylumu): [defaultDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sinxw45dfpb2c6zdfmzqxk3duirswyzlhmf2gk): [setDefaultDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sinxw45dfpb2c643forcgkztbovwhirdfnrswoylumu)

## Constructors

---

### EOAdaptorContext

`public EOAdaptorContext(EOAdaptor anAdaptor)`

Returns a new EOAdaptorContext. You never invoke this constructor directly. You must use the Adaptor method createAdaptorContext to create a new adaptor context.

__See Also:__ [adaptor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmfsgc4dun5za)

---

## Static Methods

---

### defaultDelegate

`public static Object defaultDelegate()`

Returns the default delegate-the object that is assigned as delegate to new adaptor context instances (and their channels).

---

### setDefaultDelegate

`public static void setDefaultDelegate(Object anObject)`

Sets the default delegate-the object assigned as delegate to all newly created EOAdaptorContext instances (and their EOAdaptorChannels). By default there is no default delegate.

---

## Instance Methods

---

### adaptor

`public EOAdaptor adaptor()`

Returns the receiver's EOAdaptor.

__See Also:__ [EOAdaptorContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpivhuczdbob2g64sdn5xhizlyoq) constructor

---

### beginTransaction

`public abstract void beginTransaction()`

Implemented by subclasses to attempt to begin a new transaction. A successful invocation of __beginTransaction__ must be paired with an invocation of either __commitTransaction__ or __rollbackTransaction__ to end the transaction.

The Enterprise Objects Framework automatically wraps database operations in transactions, so you don't have to begin and end transactions explicitly. In fact, letting the framework manage transactions is sometimes more efficient. You typically use __beginTransaction__ only to execute more than one database operation in the same transaction scope.

This method invokes the delegate method adaptorContextShouldBegin before beginning the transaction. If the transaction is begun successfully, the method sends `this` a [transactionDidBegin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bporzgc3ttmfrxi2lpnzcgszccmvtws3q) message and invokes the delegate method adaptorContextDidBegin. Throws an exception if the attempt is unsuccessful. Some possible reasons for failure are:

- A connection to the database hasn't been established.
- A transaction is already in progress.
- A fetch is in progress.
- The delegate refuses__.__
- The database server fails to begin a transaction.

An adaptor context subclass should override this method without invoking EOAdaptorContext's implementation.

__See Also:__ [hasOpenTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpnbqxgt3qmvxfi4tbnzzwcy3unfxw4)

---

### __canNestTransactions__

`public boolean canNestTransactions()`

Description forthcoming.

---

### channels

`public NSArray channels()`

Returns an array of channels created by the receiver.

__See Also:__ [createAdaptorChannel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmnzgkylumvawiylqorxxeq3imfxg4zlm)

---

### commitTransaction

`public abstract void commitTransaction()`

Implemented by subclasses to attempt to commit the last transaction begun. Invokes the delegate method adaptorContextShouldCommit before committing the transaction. If the transaction is committed successfully, the method sends `this` a [transactionDidCommit](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bporzgc3ttmfrxi2lpnzcgszcdn5ww22lu) message and invokes the delegate method adaptorContextDidCommit. Throws an exception if the attempt is unsuccessful. Some possible reasons for failure are:

- A transaction is not in progress.
- Fetches are in progress.
- The delegate refuses.
- The database server fails to commit.

An adaptor context subclass should override this method without invoking EOAdaptorContext's implementation.

__See Also:__ [beginTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmjswo2lokrzgc3ttmfrxi2lpny), [rollbackTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpojxwy3dcmfrwwvdsmfxhgyldoruw63q), [hasBusyChannels](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpnbqxgqtvon4ug2dbnzxgk3dt)

---

### createAdaptorChannel

`public abstract EOAdaptorChannel createAdaptorChannel()`

Implemented by subclasses to create and return a new AdaptorChannel, or `null` if a new channel cannot be created. Sets the new channel's adaptorContext to this. A newly created adaptor context has no channels. Specific adaptors have different limits on the maximum number of channels a context can have, and __createAdaptorChannel__ fails if a newly created channel would exceed the limits.

__See Also:__ [channels](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmnugc3tomvwhg)

---

### delegate

`public Object delegate()`

Returns the receiver's delegate, or `null` if the receiver doesn't have a delegate.

---

### handleDroppedConnection

`public abstract void handleDroppedConnection()`

Implemented by subclasses to clean up after the receiver's adaptor lost its connection to its database server. Invoked from EOAdaptor's handleDroppedConnection, this method cleans up the state of its adaptor channels and of itself so the receiver and its channels can be safely disposed of without any errors.

You should never invoke this method; it is invoked automatically by the Framework. Subclasses must implement this method, without invoking super, if the adaptor supports automatic database reconnection.

---

### hasBusyChannels

`public boolean hasBusyChannels()`

Returns `true` if any of the receiver's channels have outstanding operations (that is, have a fetch in progress), `false` otherwise.

__See Also:__ isFetchInProgress (EOAdaptorChannel)

---

### hasOpenChannels

`public boolean hasOpenChannels()`

Returns `true` if any of the receiver's channels are open, `false` otherwise.

__See Also:__ openChannel (EOAdaptorChannel), isOpen (EOAdaptorChannel)

---

### hasOpenTransaction

`public boolean hasOpenTransaction()`

Returns `true` if a transaction is open (begun but not yet committed or rolled back), `false` otherwise.

---

### rollbackTransaction

`public abstract void rollbackTransaction()`

Implemented by subclasses to attempt to roll back the last transaction begun. Invokes the delegate method adaptorContextShouldRollback before rolling back the transaction. If the transaction is begun successfully, the method sends `this` a [transactionDidRollback](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bporzgc3ttmfrxi2lpnzcgszcsn5wgyytbmnvq) message and invokes the delegate method adaptorContextDidRollback. Throws an exception if the attempt is unsuccessful. Some possible reasons for failure are:

- A transaction is not in progress.
- Fetches are in progress.
- The delegate refuses.
- The database server fails to rollback.

An adaptor context subclass should override this method without invoking EOAdaptorContext's implementation.

__See Also:__ [beginTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmjswo2lokrzgc3ttmfrxi2lpny), [commitTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmnxw23ljorkheyloonqwg5djn5xa)

---

### setDelegate

`public void setDelegate(Object delegate)`

Sets the receiver's delegate and the delegate of all the receiver's channels to _delegate_, or removes their delegates if _delegate_ is `null`.

__See Also:__ [channels](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmnugc3tomvwhg)

---

### transactionDidBegin

`public void transactionDidBegin()`

Informs the adaptor context that a transaction has begun in the database server, so the receiver can update its state to reflect this fact and send an [AdaptorContextBeginTransactionNotification](#apple-ijeucq2ki5deo). This method is invoked from [beginTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmjswo2lokrzgc3ttmfrxi2lpny) after a transaction has successfully been started. It is also invoked when the Enterprise Objects Framework implicitly begins a transaction.

You don't need to invoke this method unless you are implementing a concrete adaptor. Your concrete adaptor should invoke this method from within your adaptor context's implementation of [beginTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmjswo2lokrzgc3ttmfrxi2lpny) method and anywhere else it begins a transaction-either implicitly or explicitly. For example, an adaptor channel's implementation of evaluateExpression should check to see if a transaction is in progress. If no transaction is in progress, it can start one explicitly by invoking [beginTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmjswo2lokrzgc3ttmfrxi2lpny). Alternatively, it can start an implicit transaction by invoking [transactionDidBegin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bporzgc3ttmfrxi2lpnzcgszccmvtws3q).

A subclass of EOAdaptorContext doesn't need to override this method. A subclass that does override it must incorporate the superclass's version through a message to __super__.

---

### transactionDidCommit

`public void transactionDidCommit()`

Informs the adaptor context that a transaction has committed in the database server, so the receiver can update its state to reflect this fact and send an [AdaptorContextCommitTransactionNotification](#apple-ijeucrckjbfee). This method is invoked from [commitTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmnxw23ljorkheyloonqwg5djn5xa) after a transaction has successfully committed.

You don't need to invoke this method unless you are implementing a concrete adaptor. Your concrete adaptor should invoke this method from within your adaptor context's implementation of [commitTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmnxw23ljorkheyloonqwg5djn5xa) method and anywhere else it commits a transaction-either implicitly or explicitly.

A subclass of EOAdaptorContext doesn't need to override this method. A subclass that does override it must incorporate the superclass's version through a message to __super__.

---

### transactionDidRollback

`public void transactionDidRollback()`

Informs the receiver that a transaction has rolled back in the database server, so the adaptor context can update its state to reflect this fact and send an [AdaptorContextRollbackTransactionNotification](#apple-ijeucrkjiveeg). This method is invoked from [rollbackTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpojxwy3dcmfrwwvdsmfxhgyldoruw63q) after a transaction has successfully been rolled back.

You don't need to invoke this method unless you are implementing a concrete adaptor. Your concrete adaptor should invoke this method from within your adaptor context's implementation of [rollbackTransaction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpojxwy3dcmfrwwvdsmfxhgyldoruw63q) method and anywhere else it rolls back a transaction-either implicitly or explicitly.

A subclass of EOAdaptorContext doesn't need to override this method. A subclass that does override it must incorporate the superclass's version through a message to __super__..

---

### __transactionNestingLevel__

`public int transactionNestingLevel()`

Description forthcoming.

---

## Notifications

---

### AdaptorContextBeginTransactionNotification

`public static final String AdaptorContextBeginTransactionNotification`

Sent from [transactionDidBegin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bporzgc3ttmfrxi2lpnzcgszccmvtws3q) to tell observers that a transaction has begun. The notification contains:

|  |  |
| --- | --- |
| Notification Object | The notifying EOAdaptorContext object |
| Userinfo | None |

### AdaptorContextCommitTransactionNotification

`public static final String AdaptorContextCommitTransactionNotification`

Sent from [transactionDidCommit](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bporzgc3ttmfrxi2lpnzcgszcdn5ww22lu) to tell observers that a transaction has been committed. The notification contains:

|  |  |
| --- | --- |
| Notification Object | The notifying EOAdaptorContext object |
| Userinfo | None |

### AdaptorContextRollbackTransactionNotification

`public static final String AdaptorContextRollbackTransactionNotification`

Sent from [transactionDidRollback](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bporzgc3ttmfrxi2lpnzcgszcsn5wgyytbmnvq) to tell observers that a transaction has been rolled back. The notification contains:

|  |  |
| --- | --- |
| Notification Object | The notifying EOAdaptorContext object |
| Userinfo | None |

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
