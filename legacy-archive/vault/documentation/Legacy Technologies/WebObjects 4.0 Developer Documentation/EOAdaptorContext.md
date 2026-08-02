---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOAdaptorContext.html
archived_at: '2026-07-18T01:28:08.798153Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](SubclassingEOAdaptorChnnl.md)
[!](EOAdaptorContext-2.md)

---

# EOAdaptorContext

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.webobjects

---

## Class Description

EOAdaptorContext is an abstract class that defines transaction handling in Enterprise Objects Framework applications. You typically don't interact with EOAdaptorContext API directly; rather, a concrete adaptor context subclass inherits from EOAdaptorContext and overrides many of its methods, which are invoked automatically by the Enterprise Objects Framework. If you're not creating a concrete adaptor context subclass, there aren't very many methods you need to use, and you'll rarely invoke them directly.

The EOAdaptorContext class has the following principal attributes:

- Array of adaptor channels
- Delegate
- Adaptor

Other framework classes create EOAdaptorContext objects automatically. This is typically done with EOAdaptor's [createAdaptorContext](EOAdaptor.md#apple-gqydmoa) method, which creates an adaptor context and assigns its adaptor.

The following table lists the most commonly-used EOAdaptorContext methods:

| [beginTransaction](#apple-gu2to) | Begins a transaction in the database server. |
| [commitTransaction](#apple-gu3tk) | Commits the last transaction begun. |
| [rollbackTransaction](#apple-gm4tkna) | Rolls back the last transaction begun. |
| [setDebugEnabled](#apple-gyzda) | Enables debugging in all the adaptor context's channels. |

```
```

For more information, see ["EOAdaptorContext"](EOAdaptorContext-2.md).

---

## Method Types

**Constructors**

**[EOAdaptorContext](#apple-ha2domq)**

**Accessing the adaptor**

**[adaptor](#apple-gm2danq)**

**Creating adaptor channels**

**[createAdaptorChannel](#apple-gm4tamq)

**[channels](#apple-gu3tc)****

**Checking connection status**

**[hasOpenChannels](#apple-gu4tq)

**[hasBusyChannels](#apple-gu4ti)****

**Controlling transactions**

**[beginTransaction](#apple-gu2to)

**[commitTransaction](#apple-gu3tk)

**[rollbackTransaction](#apple-gm4tkna)

**[transactionDidBegin](#apple-gyzdq)

**[transactionDidCommit](#apple-gyztc)

**[transactionDidRollback](#apple-gyzti)

**[canNestTransactions](#apple-gu3do)

**[transactionNestingLevel](#apple-gyzto)****************

**Debugging**

**[setDebugEnabledDefault](#apple-gu2dq)

**[debugEnabledDefault](#apple-gu2dk)

**[setDebugEnabled](#apple-gyzda)

**[isDebugEnabled](#apple-gyydo)********

**Accessing the delegate**

**[delegate](#apple-gmydomq)

**[setDelegate](#apple-gyzdi)****

---

## Constructors

---

### EOAdaptorContext

public `EOAdaptorContext`()

public `EOAdaptorContext`(EOAdaptor _anAdaptor_)

Returns a new EOAdaptorContext. You never invoke either of the constructors directly. You must use the Adaptor method [`createAdaptorContext`](EOAdaptor.md#apple-gqydmoa) to create a new adaptor context.

__See also:__
[`adaptor`](#apple-gm2danq)

#

---

### debugEnabledDefault

public static boolean `debugEnabledDefaul`t()

Returns `true` if new adaptor context instances have debugging enabled by default, `false` otherwise. By default, adaptor contexts have debugging enabled if the user default EOAdaptorDebugEnabled is `true`. (For more information on user defaults, see the NSUserDefaults class specification in the _Foundation Framework Reference_.) You can override the user default using the class method `[setDebugEnabledDefault](#apple-gu2dq)`, or you can set debugging behavior for a specific instance with the instance method [`setDebugEnabled`](#apple-gyzda).

---

### setDebugEnabledDefault

public static void `setDebugEnabledDefault`(boolean _flag_)

Sets default debugging behavior for new instances of EOAdaptorContext. If _flag_ is `true`, debugging is enabled for new instances. If _flag_ is `false`, debugging is disabled. Use the instance method `[setDebugEnabled](#apple-gyzda)` to enable debugging for a specific adaptor context.

__See also:__
[`debugEnabledDefault`](#apple-gu2dk), [`isDebugEnabled`](#apple-gyydo)

---

## Instance Methods

---

### adaptor

public EOAdaptor `adaptor`()

Returns the receiver's EOAdaptor.

---

### beginTransaction

public abstract void `beginTransaction`()

Implemented by subclasses to attempt to begin a new transaction, nested within the current one if nested transactions are supported. Each successful invocation of `beginTransaction` must be paired with an invocation of either `commitTransaction` or `rollbackTransaction` to end the transaction.

The Enterprise Objects Framework automatically wraps database operations in transactions, so you don't have to begin and end transactions explicitly. In fact, letting the framework manage transactions is sometimes more efficient. You typically use `beginTransaction` only to execute more than one database operation in the same transaction scope.

This method invokes the delegate method [`adaptorContextShouldBegin`](../Protocols/EOAdaptorContextDelegate.md#apple-gy3di) before beginning the transaction. If the transaction is begun successfully, the method sends `this` a `[transactionDidBegin](#apple-gyzdq)` message and invokes the delegate method `[adaptorContextDidBegin](../Protocols/EOAdaptorContextDelegate.md#apple-gqydsmi)`. Throws an exception if the attempt is unsuccessful. Some possible reasons for failure are:

- A connection to the database hasn't been established.
- Nested transactions aren't supported, and a transaction is already in progress.
- A fetch is in progress.
- The delegate refuses`.`
- The database server fails to begin a transaction.

An adaptor context subclass should override this method without invoking EOAdaptorContext's implementation.

__See also:__
[`canNestTransactions`](#apple-gu3do), [`transactionNestingLevel`](#apple-gyzto)

---

### canNestTransactions

public abstract boolean `canNestTransaction`s()

Implemented by subclasses to return `true` if the database server and the adaptor context can nest transactions, `false` otherwise. An adaptor context subclass should override this method without invoking EOAdaptorContext's implementation.

__See also:__
[`transactionNestingLevel`](#apple-gyzto)

---

### channels

public NSArray `channels`()

Returns an array of channels created by the receiver.

__See also:__
[`createAdaptorChannel`](#apple-gm4tamq)

---

### commitTransaction

public abstract void `commitTransaction`()

Implemented by subclasses to attempt to commit the last transaction begun. Invokes the delegate method [`adaptorContextShouldCommit`](../Protocols/EOAdaptorContextDelegate.md#apple-gy3do) before committing the transaction. If the transaction is committed successfully, the method sends `this` a `[transactionDidCommit](#apple-gyztc)` message and invokes the delegate method `[adaptorContextDidCommit](../Protocols/EOAdaptorContextDelegate.md#apple-gy2tq)`. Throws an exception if the attempt is unsuccessful. Some possible reasons for failure are:

- A transaction is not in progress.
- Fetches are in progress.
- The delegate refuses.
- The database server fails to commit.

An adaptor context subclass should override this method without invoking EOAdaptorContext's implementation.

__See also:__
[`beginTransaction`](#apple-gu2to), [`rollbackTransaction`](#apple-gm4tkna), [`hasBusyChannels`](#apple-gu4ti)

---

### createAdaptorChannel

public abstract EOAdaptorChannel `createAdaptorChannel`()

Implemented by subclasses to create and return a new AdaptorChannel, or `null` if a new channel cannot be created. Sets the new channel's [`adaptorContext`](EOAdaptorChannel.md#apple-gq3dqni) to `this`. A newly created adaptor context has no channels. Specific adaptors have different limits on the maximum number of channels a context can have, and [`createAdaptorChannel`](#apple-gm4tamq) fails if a newly created channel would exceed the limits.

__See also:__
[`channels`](#apple-gu3tc)

---

### delegate

public java.lang.Object `delegate`()

Returns the receiver's delegate, or `null` if the receiver doesn't have a delegate.

__See also:__
[`setDelegate`](#apple-gyzdi)

---

### hasBusyChannels

public boolean `hasBusyChannels`()

Returns `true` if any of the receiver's channels have outstanding operations (that is, have a fetch in progress), `false` otherwise.

__See also:__
[`isFetchInProgress`](EOAdaptorChannel.md#apple-geydimq) (EOAdaptorChannel)

---

### hasOpenChannels

public boolean `hasOpenChannels`()

Returns `true` if any of the receiver's channels are open, `false` otherwise.

__See also:__
[`openChannel`](EOAdaptorChannel.md#apple-geydmmq) (EOAdaptorChannel), [`isOpen`](EOAdaptorChannel.md#apple-geydkmi) (EOAdaptorChannel)

---

### isDebugEnabled

public boolean `isDebugEnabled`()

Returns `true` if debugging is enabled in the receiver, `false` otherwise.

__See also:__
[`setDebugEnabled`](#apple-gyzda), [`debugEnabledDefault`](#apple-gu2dk), [`setDebugEnabledDefault`](#apple-gu2dq)

---

### rollbackTransaction

public abstract void `rollbackTransaction`()

Implemented by subclasses to attempt to roll back the last transaction begun. Invokes the delegate method [`adaptorContextShouldRollback`](../Protocols/EOAdaptorContextDelegate.md#apple-gy3ta) before rolling back the transaction. If the transaction is begun successfully, the method sends `this` a `[transactionDidRollback](#apple-gyzti)` message and invokes the delegate method `[adaptorContextDidRollback](../Protocols/EOAdaptorContextDelegate.md#apple-gy3dc)`. Throws an exception if the attempt is unsuccessful. Some possible reasons for failure are:

- A transaction is not in progress.
- Fetches are in progress.
- The delegate refuses.
- The database server fails to rollback.

An adaptor context subclass should override this method without invoking EOAdaptorContext's implementation.

__See also:__
[`beginTransaction`](#apple-gu2to), [`commitTransaction`](#apple-gu3tk)

---

### setDebugEnabled

public void `setDebugEnabled`(boolean _flag_)

Enables debugging in the receiver and all its channels. If _flag_ is `true`, enables debugging; otherwise, disables debugging.

__See also:__
[`setDebugEnabled`](EOAdaptorChannel.md#apple-geytamq) (EOAdaptorChannel), [`isDebugEnabled`](#apple-gyydo), [`setDebugEnabledDefault`](#apple-gu2dq), [`channels`](#apple-gu3tc)

---

### setDelegate

public void `setDelegate`(java.lang.Object _delegate_)

Sets the receiver's delegate and the delegate of all the receiver's channels to _delegate_, or removes their delegates if _delegate_ is `null`.

__See also:__
[`delegate`](#apple-gmydomq), [`channels`](#apple-gu3tc)

---

### transactionDidBegin

public void `transactionDidBegin`()

Informs the adaptor context that a transaction has begun in the database server, so the receiver can update its state to reflect this fact and send an EOAdaptorContextBeginTransactionNotification. This method is invoked from [`beginTransaction`](#apple-gu2to) after a transaction has successfully been started. It is also invoked when the Enterprise Objects Framework implicitly begins a transaction.

You don't need to invoke this method unless you are implementing a concrete adaptor. Your concrete adaptor should invoke this method from within your adaptor context's implementation of `[beginTransaction](#apple-gu2to)` method and anywhere else it begins a transaction-either implicitly or explicitly. For example, an adaptor channel's implementation of `[evaluateExpression](EOAdaptorChannel.md#apple-geydaoi)` should check to see if a transaction is in progress. If no transaction is in progress, it can start one explicitly by invoking [`beginTransaction`](#apple-gu2to). Alternatively, it can start an implicit transaction by invoking [`transactionDidBegin`](#apple-gyzdq).

A subclass of EOAdaptorContext doesn't need to override this method. A subclass that does override it must incorporate the superclass's version through a message to `super`.

__See also:__
[`transactionDidCommit`](#apple-gyztc), [`transactionDidRollback`](#apple-gyzti)

---

### transactionDidCommit

public void `transactionDidCommit`()

Informs the adaptor context that a transaction has committed in the database server, so the receiver can update its state to reflect this fact and send an EOAdaptorContextCommitTransactionNotification. This method is invoked from [`commitTransaction`](#apple-gu3tk) after a transaction has successfully committed.

You don't need to invoke this method unless you are implementing a concrete adaptor. Your concrete adaptor should invoke this method from within your adaptor context's implementation of `[commitTransaction](#apple-gu3tk)` method and anywhere else it commits a transaction-either implicitly or explicitly.

A subclass of EOAdaptorContext doesn't need to override this method. A subclass that does override it must incorporate the superclass's version through a message to `super`.

__See also:__
[`transactionDidBegin`](#apple-gyzdq), [`transactionDidRollback`](#apple-gyzti)

---

### transactionDidRollback

public void `transactionDidRollback`()

Informs the receiver that a transaction has rolled back in the database server, so the adaptor context can update its state to reflect this fact and send an EOAdaptorContextRollbackTransactionNotification. This method is invoked from [`rollbackTransaction`](#apple-gm4tkna) after a transaction has successfully been rolled back.

You don't need to invoke this method unless you are implementing a concrete adaptor. Your concrete adaptor should invoke this method from within your adaptor context's implementation of `[rollbackTransaction](#apple-gm4tkna)` method and anywhere else it rolls back a transaction-either implicitly or explicitly.

A subclass of EOAdaptorContext doesn't need to override this method. A subclass that does override it must incorporate the superclass's version through a message to `super`.

__See also:__
[`transactionDidBegin`](#apple-gyzdq), [`transactionDidCommit`](#apple-gyztc)

---

### transactionNestingLevel

public int `transactionNestingLevel`()

Returns the number of transactions in progress. If the database server and the adaptor support nested transactions, this number may be greater than 1.

__See also:__
[`canNestTransactions`](#apple-gu3do)

---

# Notifications

---

### AdaptorContextBeginTransactionNotification

public static final java.lang.String `AdaptorContextBeginTransactionNotification`

Sent from [`transactionDidBegin`](#apple-gyzdq) to tell observers that a transaction has begun.

---

### AdaptorContextCommitTransactionNotification

public static final java.lang.String `AdaptorContextCommitTransactionNotification`

Sent from [`transactionDidCommit`](#apple-gyztc) to tell observers that a transaction has been committed.

---

### AdaptorContextRollbackTransactionNotification

public static final java.lang.String `AdaptorContextRollbackTransactionNotification`

Sent from [`transactionDidRollback`](#apple-gyzti) to tell observers that a transaction has been rolled back.

---

[!](SubclassingEOAdaptorChnnl.md)
[!](EOAdaptorContext-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
