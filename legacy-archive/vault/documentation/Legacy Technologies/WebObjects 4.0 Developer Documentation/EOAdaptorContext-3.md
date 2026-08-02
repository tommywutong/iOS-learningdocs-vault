---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOAdaptorContext.html
archived_at: '2026-07-18T01:28:15.573547Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](SubclassingEOAdaptorChnnl-2.md)
[!](More%20about%20EOAdaptorContext.md)

---

# EOAdaptorContext

__Inherits From:__
NSObject

__Declared in:__
EOAccess/EOAdaptorContext.h

---

## Class Description

EOAdaptorContext is an abstract class that defines transaction handling in Enterprise Objects Framework applications. You typically don't interact with EOAdaptorContext API directly; rather, a concrete adaptor context subclass inherits from EOAdaptorContext and overrides many of its methods, which are invoked automatically by the Enterprise Objects Framework. If you're not creating a concrete adaptor context subclass, there aren't very many methods you need to use, and you'll rarely invoke them directly.

The EOAdaptorContext class has the following principal attributes:

- Array of adaptor channels
- Delegate
- Adaptor

Other framework classes create EOAdaptorContext objects automatically. This is typically done with EOAdaptor's [- createAdaptorContext](EOAdaptor-2.md#apple-gqydmoa) method, which creates an adaptor context and assigns its adaptor.

The following table lists the most commonly-used EOAdaptorContext methods:

| [- beginTransaction](#apple-gu2to) | Begins a transaction in the database server. |
| [- commitTransaction](#apple-gu3tk) | Commits the last transaction begun. |
| [- rollbackTransaction](#apple-gm4tkna) | Rolls back the last transaction begun. |
| [- setDebugEnabled:](#apple-gyzda) | Enables debugging in all the adaptor context's channels. |

```
```

For more information, see ["More about EOAdaptorContext"](More%20about%20EOAdaptorContext.md).

---

## Method Types

**Creating an EOAdaptorContext**

**[- initWithAdaptor:](#apple-g42dmoi)**

**Accessing the adaptor**

**[- adaptor](#apple-gm2danq)**

**Creating adaptor channels**

**[- createAdaptorChannel](#apple-gm4tamq)

**[- channels](#apple-gu3tc)****

**Checking connection status**

**[- hasOpenChannels](#apple-gu4tq)

**[- hasBusyChannels](#apple-gu4ti)****

**Controlling transactions**

**[- beginTransaction](#apple-gu2to)

**[- commitTransaction](#apple-gu3tk)

**[- rollbackTransaction](#apple-gm4tkna)

**[- transactionDidBegin](#apple-gyzdq)

**[- transactionDidCommit](#apple-gyztc)

**[- transactionDidRollback](#apple-gyzti)

**[- canNestTransactions](#apple-gu3do)

**[- transactionNestingLevel](#apple-gyzto)****************

**Debugging**

**[+ setDebugEnabledDefault:](#apple-gu2dq)

**[+ debugEnabledDefault](#apple-gu2dk)

**[- setDebugEnabled:](#apple-gyzda)

**[- isDebugEnabled](#apple-gyydo)********

**Accessing the delegate**

**[- delegate](#apple-gmydomq)

**[- setDelegate:](#apple-gyzdi)****

---

## Class Methods

---

### debugEnabledDefault

+ (BOOL)__debugEnabledDefault__

Returns YES if new adaptor context instances have debugging enabled by default, NO otherwise. By default, adaptor contexts have debugging enabled if the user default EOAdaptorDebugEnabled is YES. (For more information on user defaults, see the NSUserDefaults class specification in the _Foundation Framework Reference_.) You can override the user default using the class method `[setDebugEnabledDefault:](#apple-gu2dq)`, or you can set debugging behavior for a specific instance with the instance method [`setDebugEnabled:`](#apple-gyzda).

---

### setDebugEnabledDefault:

+ (void)__setDebugEnabledDefault:__ (BOOL)_flag_

Sets default debugging behavior for new instances of EOAdaptorContext. If _flag_ is YES, debugging is enabled for new instances. If _flag_ is NO, debugging is disabled. Use the instance method `[setDebugEnabled:](#apple-gyzda)` to enable debugging for a specific adaptor context.

__See also:__
[+ `debugEnabledDefault`](#apple-gu2dk), [- `isDebugEnabled`](#apple-gyydo)

---

## Instance Methods

---

### adaptor

- (EOAdaptor \*)__adaptor__

Returns the receiver's EOAdaptor.

__See also:__
[- `initWithAdaptor:`](#apple-g42dmoi)

---

### beginTransaction

- (void)__beginTransaction__

Implemented by subclasses to attempt to begin a new transaction, nested within the current one if nested transactions are supported. Each successful invocation of `beginTransaction` must be paired with an invocation of either `commitTransaction` or `rollbackTransaction` to end the transaction.

The Enterprise Objects Framework automatically wraps database operations in transactions, so you don't have to begin and end transactions explicitly. In fact, letting the framework manage transactions is sometimes more efficient. You typically use `beginTransaction` only to execute more than one database operation in the same transaction scope.

This method invokes the delegate method [`adaptorContextShouldBegin:`](../Protocols/EOAdaptorContextDelegate.md#apple-gy3di) before beginning the transaction. If the transaction is begun successfully, sends `self` a `[transactionDidBegin](#apple-gyzdq)` message and invokes the delegate method `[adaptorContextDidBegin:](../Protocols/EOAdaptorContextDelegate.md#apple-gqydsmi)`. Raises if the attempt is unsuccessful. Some possible reasons for failure are:

- A connection to the database hasn't been established.
- Nested transactions aren't supported, and a transaction is already in progress.
- A fetch is in progress.
- The delegate refuses`.`
- The database server fails to begin a transaction.

An adaptor context subclass should override this method without invoking EOAdaptorContext's implementation.

__See also:__
[- `commitTransaction`](#apple-gu3tk), [- `rollbackTransaction`](#apple-gm4tkna), [- `canNestTransactions`](#apple-gu3do),
[- `transactionNestingLevel`](#apple-gyzto)

---

### canNestTransactions

- (BOOL)__canNestTransactions__

Implemented by subclasses to return YES if the database server and the adaptor context can nest transactions, NO otherwise. An adaptor context subclass should override this method without invoking EOAdaptorContext's implementation.

__See also:__
[- `transactionNestingLevel`](#apple-gyzto)

---

### channels

- (NSArray \*)__channels__

Returns an array of channels created by this context.

__See also:__
[`createAdaptorChannel`](#apple-gm4tamq)

---

### commitTransaction

- (void)__commitTransaction__

Implemented by subclasses to attempt to commit the last transaction begun. Invokes the delegate method [`adaptorContextShouldCommit:`](../Protocols/EOAdaptorContextDelegate.md#apple-gy3do) before committing the transaction. If the transaction is committed successfully, sends `self` a `[transactionDidCommit](#apple-gyztc)` message and invokes the delegate method `[adaptorContextDidCommit:](../Protocols/EOAdaptorContextDelegate.md#apple-gy2tq)`. Raises if the attempt is unsuccessful. Some possible reasons for failure are:

- A transaction is not in progress.
- Fetches are in progress.
- The delegate refuses.
- The database server fails to commit.

An adaptor context subclass should override this method without invoking EOAdaptorContext's implementation.

__See also:__
[- `beginTransaction`](#apple-gu2to), [- `createAdaptorChannel`](#apple-gm4tamq), [- `transactionDidCommit`](#apple-gyztc), [- `hasBusyChannels`](#apple-gu4ti)

---

### createAdaptorChannel

- (EOAdaptorChannel \*)__createAdaptorChannel__

Implemented by subclasses to create and return a new AdaptorChannel, or `nil` if a new channel cannot be created. Initializes the new channel by sending it `[initWithAdaptorContext:](EOAdaptorChannel.md#apple-ge2dknzs)self`. The newly created channel retains its context. A newly created adaptor context has no channels. Specific adaptors have different limits on the maximum number of channels a context can have, and [`createAdaptorChannel`](#apple-gm4tamq) fails if a newly created channel would exceed the limits.

__See also:__
[- `channels`](#apple-gu3tc)

---

### delegate

- __delegate__

Returns the receiver's delegate, or `nil` if the receiver doesn't have a delegate.

__See also:__
[- `setDelegate:`](#apple-gyzdi)

---

### hasBusyChannels

- (BOOL)__hasBusyChannels__

Returns YES if any of the receiver's channels have outstanding operations (that is, have a fetch in progress), NO otherwise.

__See also:__
[- `isFetchInProgress`](EOAdaptorChannel.md#apple-geydimq) (EOAdaptorChannel)

---

### hasOpenChannels

- (BOOL)__hasOpenChannels__

Returns YES if any of the receiver's channels are open, NO otherwise.

__See also:__
[- `openChannel`](EOAdaptorChannel.md#apple-geydmmq) (EOAdaptorChannel), [- `isOpen`](EOAdaptorChannel.md#apple-geydkmi) (EOAdaptorChannel)

---

### initWithAdaptor:

- __initWithAdaptor:__ (EOAdaptor \*)_adaptor_

The designated initializer for the EOAdaptorContext class, this method is overridden by subclasses to initialize a newly allocated EOAdaptorContext subclass and retain _adaptor_. Returns `self`.

You never invoke this method directly. You must use the EOAdaptor method `[createAdaptorContext](EOAdaptor.md#apple-gqydmoa)` to create a new adaptor context.

__See also:__
[- `adaptor`](#apple-gm2danq)

---

### isDebugEnabled

- (BOOL)__isDebugEnabled__

Returns YES if debugging is enabled in the receiver, NO otherwise.

__See also:__
[- `setDebugEnabled:`](#apple-gyzda), [+ `debugEnabledDefault`](#apple-gu2dk), [+ `setDebugEnabledDefault:`](#apple-gu2dq)

---

### rollbackTransaction

- (void)__rollbackTransaction__

Implemented by subclasses to attempt to roll back the last transaction begun. Invokes the delegate method [`adaptorContextShouldRollback:`](../Protocols/EOAdaptorContextDelegate.md#apple-gy3ta) before rolling back the transaction. If the transaction is begun successfully, sends `self` a `[transactionDidRollback](#apple-gyzti)` message and invokes the delegate method `[adaptorContextDidRollback:](../Protocols/EOAdaptorContextDelegate.md#apple-gy3dc)`. Raises if the attempt is unsuccessful. Some possible reasons for failure are:

- A transaction is not in progress.
- Fetches are in progress.
- The delegate refuses.
- The database server fails to rollback.

An adaptor context subclass should override this method without invoking EOAdaptorContext's implementation.

__See also:__
[- `beginTransaction`](#apple-gu2to), [- `commitTransaction`](#apple-gu3tk)

---

### setDebugEnabled:

- (void)__setDebugEnabled:__ (BOOL)_flag_

Enables debugging in the receiver and all its channels. If _flag_ is YES, enables debugging; otherwise, disables debugging.

__See also:__
[- `setDebugEnabled:`](EOAdaptorChannel.md#apple-geytamq) (EOAdaptorChannel), [- `isDebugEnabled`](#apple-gyydo), [+ `setDebugEnabledDefault:`](#apple-gu2dq),
[- `channels`](#apple-gu3tc)

---

### setDelegate:

- (void)__setDelegate:__ _delegate_

Sets the receiver's delegate and the delegate of all the receiver's channels to _delegate_, or removes their delegates if _delegate_ is `nil`. The receiver does not retain _delegate_.

__See also:__
[- `delegate`](#apple-gmydomq), [- `channels`](#apple-gu3tc)

---

### transactionDidBegin

- (void)__transactionDidBegin__

Informs the adaptor context that a transaction has begun in the database server, so the receiver can update its state to reflect this fact and send an EOAdaptorContextBeginTransactionNotification. This method is invoked from [`beginTransaction`](#apple-gu2to) after a transaction has successfully been started. It is also invoked when the Enterprise Objects Framework implicitly begins a transaction.

You don't need to invoke this method unless you are implementing a concrete adaptor. Your concrete adaptor should invoke this method from within your adaptor context's implementation of `[beginTransaction](#apple-gu2to)` method and anywhere else it begins a transaction-either implicitly or explicitly. For example, an adaptor channel's implementation of `[evaluateExpression:](EOAdaptorChannel.md#apple-geydaoi)` should check to see if a transaction is in progress. If no transaction is in progress, it can start one explicitly by invoking [`beginTransaction`](#apple-gu2to). Alternatively, it can start an implicit transaction by invoking [`transactionDidBegin`](#apple-gyzdq).

A subclass of EOAdaptorContext doesn't need to override this method. A subclass that does override it must incorporate the superclass's version through a message to `super`.

__See also:__
[- `transactionDidCommit`](#apple-gyztc), [- `transactionDidRollback`](#apple-gyzti)

---

### transactionDidCommit

- (void)__transactionDidCommit__

Informs the adaptor context that a transaction has committed in the database server, so the receiver can update its state to reflect this fact and send an EOAdaptorContextCommitTransactionNotification. This method is invoked from [`commitTransaction`](#apple-gu3tk) after a transaction has successfully committed.

You don't need to invoke this method unless you are implementing a concrete adaptor. Your concrete adaptor should invoke this method from within your adaptor context's implementation of `[commitTransaction](#apple-gu3tk)` method and anywhere else it commits a transaction-either implicitly or explicitly.

A subclass of EOAdaptorContext doesn't need to override this method. A subclass that does override it must incorporate the superclass's version through a message to `super`.

__See also:__
[- `transactionDidBegin`](#apple-gyzdq), [- `transactionDidRollback`](#apple-gyzti)

---

### transactionDidRollback

- (void)__transactionDidRollback__

Informs the receiver that a transaction has rolled back in the database server, so the adaptor context can update its state to reflect this fact and send an EOAdaptorContextRollbackTransactionNotification. This method is invoked from [`rollbackTransaction`](#apple-gm4tkna) after a transaction has successfully been rolled back.

You don't need to invoke this method unless you are implementing a concrete adaptor. Your concrete adaptor should invoke this method from within your adaptor context's implementation of `[rollbackTransaction](#apple-gm4tkna)` method and anywhere else it rolls back a transaction-either implicitly or explicitly.

A subclass of EOAdaptorContext doesn't need to override this method. A subclass that does override it must incorporate the superclass's version through a message to `super`.

__See also:__
[- `transactionDidBegin`](#apple-gyzdq), [- `transactionDidCommit`](#apple-gyztc)

---

### transactionNestingLevel

- (unsigned)__transactionNestingLevel__

Returns the number of transactions in progress. If the database server and the adaptor support nested transactions, this number may be greater than 1.

__See also:__
[- `canNestTransactions`](#apple-gu3do)

---

# Notifications

---

### EOAdaptorContextBeginTransactionNotification

Sent from [`transactionDidBegin`](#apple-gyzdq) to tell observers that a transaction has begun. The notification contains:

| __Notification Object__ | The notifying EOAdaptorContext object |
| __Userinfo__ | None |

```
```


---

### EOAdaptorContextCommitTransactionNotification

Sent from [`transactionDidCommit`](#apple-gyztc) to tell observers that a transaction has been committed. The notification contains:

| __Notification Object__ | The notifying EOAdaptorContext object |
| __Userinfo__ | None |

```
```


---

### EOAdaptorContextRollbackTransactionNotification

Sent from [`transactionDidRollback`](#apple-gyzti) to tell observers that a transaction has been rolled back. The notification contains:

| __Notification Object__ | The notifying EOAdaptorContext object |
| __Userinfo__ | None |

```
```

---

[!](SubclassingEOAdaptorChnnl-2.md)
[!](More%20about%20EOAdaptorContext.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
