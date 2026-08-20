---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/Concepts/EOAdaptorContext.html
archived_at: '2026-07-15T08:13:38.588367Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Classes/Art/up.gif)](../../EOAccessTOC.md)

# EOAdaptorContext.Concepts

## Controlling Transactions

EOAdaptorContext defines a simple set of methods for explicitly controlling transactions: beginTransaction, commitTransaction, and rollbackTransaction. Each of these messages confirms the requested action with the adaptor context's delegate, then performs the action if possible.

There's also a set of methods for notifying an adaptor context that a transaction has been started, committed, or rolled back without using the __beginTransaction__, __commitTransaction__, or __rollbackTransaction__ methods. For example, if you invoke a stored procedure in the server that begins a transaction, you need to notify the adaptor context that a transaction has been started. Use the following methods to keep an adaptor context synchronized with the state of the database server: transactionDidBegin, transactionDidCommit, and transactionDidRollback. These methods post notifications.

## The Adaptor Context's Delegate and Notifications

You can assign a delegate to an adaptor context. The delegate responds to certain messages on behalf of the context. An EOAdaptorContext sends these messages directly to its delegate. The transaction-controlling methods-beginTransaction, commitTransaction, and rollbackTransaction-notify the adaptor context's delegate before and after a transaction operation is performed. Some delegate methods, such as adaptorContextShouldBegin, let the delegate determine whether the context should perform an operation. Others, such as adaptorContextDidBegin, are simply notifications that an operation has occurred. The delegate has an opportunity to respond by implementing the delegate methods. If the delegate wants to intervene, it implements adaptorContextShouldBegin. If it simply wants notification when a transaction has begun, it implements adaptorContextDidBegin.

EOAdaptorContext also posts notifications to the application's default notification center. Any object may register to receive one or more of the notifications posted by an adaptor context by registering as an observer with the default notification center (an instance of the NSNotificationCenter class). For more information on notifications, see the NSNotificationCenter class specification in the _Foundation Framework Reference_.

## Creating an EOAdaptorContext Subclass

EOAdaptorContext provides many default method implementations that are sufficient for concrete subclasses. The following methods establish structure and conventions that other Enterprise Objects Framework classes depend on and should be overridden with caution:

- transactionDidBegin
- transactionDidCommit
- transactionDidRollback
- hasOpenTransaction

If you override any of the above methods, your implementations should incorporate the superclass's implementation through a message to __super__.

Other methods require database-specific implementations that can be provided only by a concrete adaptor context subclass. A subclass must override the following methods in terms of the persistent storage system to which it interacts:

- beginTransaction
- commitTransaction
- createAdaptorChannel
- rollbackTransaction

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Classes/Art/up.gif)](../../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
