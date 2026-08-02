---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/More/EOAdaptorContext_more.html
archived_at: '2026-07-18T01:28:11.239315Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOAdaptorContext.md)
[!](EOAdaptorOperation.md)

---

# EOAdaptorContext

EOAdaptorContext is an abstract class that provides its concrete subclasses with a structure for handling database transactions. It's associated with EOAdaptor and EOAdaptorChannel, which, together with EOAdaptorContext, form the _adaptor level_ of Enterprise Objects Framework's access layer. See the EOAdaptor class specification for more information about accessing, creating, and using adaptor level objects.

A concrete subclass of EOAdaptorContext provides database-specific method implementations and represents a single transaction scope (logical user) on the database server to which its EOAdaptor object is connected. You never interact with instances of the EOAdaptorContext class, rather your Enterprise Objects Framework applications use instances of concrete subclasses that are written to work with a specific database or other persistent storage system. To create an instance of a concrete EOAdaptorContext subclass, you send a [`createAdaptorContext`](../EOAdaptor.md#apple-gqydmoa) message to an instance of the corresponding EOAdaptor subclass. You rarely create adaptor contexts yourself. They are generally created automatically by other framework objects.

If a database server supports multiple concurrent transaction sessions, an adaptor context's EOAdaptor can have several contexts. When you use multiple EOAdaptorContexts for a single EOAdaptor, you can have several database server transactions in progress simultaneously. You should be aware of the issues involved in concurrent access if you do this.

An EOAdaptorContext has an EOAdaptorChannel, which handles actual access to the data on the server. If the database server supports it, a context can have multiple channels. See your adaptor context's documentation to find out if your adaptor supports multiple channels. An EOAdaptorContext by default has no EOAdaptorChannels; to create a new channel send your EOAdaptorContext a [`createAdaptorChannel`](../EOAdaptorContext.md#apple-gm4tamq) message.

---

## Controlling Transactions

EOAdaptorContext defines a simple set of methods for explicitly controlling transactions: [`beginTransaction`](../EOAdaptorContext.md#apple-gu2to), [`commitTransaction`](../EOAdaptorContext.md#apple-gu3tk), and [`rollbackTransaction`](../EOAdaptorContext.md#apple-gm4tkna). Each of these messages confirms the requested action with the adaptor context's delegate, then performs the action if possible.

There's also a set of methods for notifying an adaptor context that a transaction has been started, committed, or rolled back without using the `beginTransaction`, `commitTransaction`, or `rollbackTransaction` methods. For example, if you invoke a stored procedure in the server that begins a transaction, you need to notify the adaptor context that a transaction has been started. Use the following methods to keep an adaptor context synchronized with the state of the database server: [`transactionDidBegin`](../EOAdaptorContext.md#apple-gyzdq), [`transactionDidCommit`](../EOAdaptorContext.md#apple-gyztc), and [`transactionDidRollback`](../EOAdaptorContext.md#apple-gyzti). These methods post notifications.

---

## The Adaptor Context's Delegate and Notifications

You can assign a delegate to an adaptor context. The delegate responds to certain messages on behalf of the context. An EOAdaptorContext sends these messages directly to its delegate. The transaction-controlling methods-[`beginTransaction`](../EOAdaptorContext.md#apple-gu2to), [`commitTransaction`](../EOAdaptorContext.md#apple-gu3tk), and [`rollbackTransaction`](../EOAdaptorContext.md#apple-gm4tkna)-notify the adaptor context's delegate before and after a transaction operation is performed. Some delegate methods, such as [`adaptorContextShouldBegin`](../../Protocols/EOAdaptorContextDelegate.md#apple-gy3di), let the delegate determine whether the context should perform an operation. Others, such as [`adaptorContextDidBegin`](../../Protocols/EOAdaptorContextDelegate.md#apple-gqydsmi), are simply notifications that an operation has occurred. The delegate has an opportunity to respond by implementing the delegate methods. If the delegate wants to intervene, it implements `adaptorContextShouldBegin:`. If it simply wants notification when a transaction has begun, it implements `adaptorContextDidBegin:`.

EOAdaptorContext also posts notifications to the application's default notification center. Any object may register to receive one or more of the notifications posted by an adaptor context by sending the message `addObserver` to the default notification center (an instance of the NSNotificationCenter class). For more information on notifications, see the NSNotificationCenter class specification in the _Foundation Framework Reference_.

---

## Creating an EOAdaptorContext Subclass

EOAdaptorContext provides many default method implementations that are sufficient for concrete subclasses. The following methods establish structure and conventions that other Enterprise Objects Framework classes depend on and should be overridden with caution:

- [transactionDidBegin](EOAdaptorContext.md#apple-gyzdq)
- [transactionDidCommit](EOAdaptorContext.md#apple-gyztc)
- [transactionDidRollback](EOAdaptorContext.md#apple-gyzti)
- [transactionNestingLevel](EOAdaptorContext.md#apple-gyzto)

If you override any of the above methods, your implementations should incorporate the superclass's implementation through a message to `super`.

Other methods require database-specific implementations that can be provided only by a concrete adaptor context subclass. A subclass must override the following methods in terms of the persistent storage system to which it interacts:

- [beginTransaction](EOAdaptorContext.md#apple-gu2to)
- [canNestTransactions](EOAdaptorContext.md#apple-gu3do)
- [commitTransaction](EOAdaptorContext.md#apple-gu3tk)
- [createAdaptorChannel](EOAdaptorContext.md#apple-gm4tamq)
- [rollbackTransaction](EOAdaptorContext.md#apple-gm4tkna)

  ****

---

[!](EOAdaptorContext.md)
[!](EOAdaptorOperation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
