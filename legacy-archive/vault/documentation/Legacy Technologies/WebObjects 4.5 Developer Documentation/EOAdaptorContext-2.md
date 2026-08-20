---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Classes/More/EOAdaptorContext.html
archived_at: '2026-07-15T08:11:32.110567Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md)

# EOAdaptorContext

## Controlling Transactions

EOAdaptorContext defines a simple set of methods for explicitly
controlling transactions: [beginTransaction](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmjswo2lokrzgc3ttmfrxi2lpny), [commitTransaction](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmnxw23ljorkheyloonqwg5djn5xa),
and [rollbackTransaction](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpojxwy3dcmfrwwvdsmfxhgyldoruw63q).
Each of these messages confirms the requested action with the adaptor
context's delegate, then performs the action if possible.

There's also a set of methods for notifying an adaptor context
that a transaction has been started, committed, or rolled back without
using the __beginTransaction__, __commitTransaction__,
or __rollbackTransaction__ methods. For example,
if you invoke a stored procedure in the server that begins a transaction,
you need to notify the adaptor context that a transaction has been
started. Use the following methods to keep an adaptor context synchronized
with the state of the database server: [transactionDidBegin](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bporzgc3ttmfrxi2lpnzcgszccmvtws3q), [transactionDidCommit](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bporzgc3ttmfrxi2lpnzcgszcdn5ww22lu),
and [transactionDidRollback](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bporzgc3ttmfrxi2lpnzcgszcsn5wgyytbmnvq).
These methods post notifications.

## The Adaptor Context's Delegate and Notifications

You can assign a delegate to an adaptor context. The delegate
responds to certain messages on behalf of the context. An EOAdaptorContext
sends these messages directly to its delegate. The transaction-controlling
methods- [beginTransaction](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmjswo2lokrzgc3ttmfrxi2lpny), [commitTransaction](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmnxw23ljorkheyloonqwg5djn5xa),
and [rollbackTransaction](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpojxwy3dcmfrwwvdsmfxhgyldoruw63q)-notify
the adaptor context's delegate before and after a transaction
operation is performed. Some delegate methods, such as [adaptorContextShouldBegin](EOAdaptorContext.Delegate.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpifsgc4dun5zeg33oorsxq5boirswyzlhmf2gkl3bmrqxa5dpojbw63tumv4hiu3in52wyzccmvtws3q),
let the delegate determine whether the context should perform an
operation. Others, such as [adaptorContextDidBegin](EOAdaptorContext.Delegate.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpifsgc4dun5zeg33oorsxq5boirswyzlhmf2gkl3bmrqxa5dpojbw63tumv4hirdjmrbgkz3jny),
are simply notifications that an operation has occurred. The delegate
has an opportunity to respond by implementing the delegate methods.
If the delegate wants to intervene, it implements [adaptorContextShouldBegin](EOAdaptorContext.Delegate.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpifsgc4dun5zeg33oorsxq5boirswyzlhmf2gkl3bmrqxa5dpojbw63tumv4hiu3in52wyzccmvtws3q).
If it simply wants notification when a transaction has begun, it
implements [adaptorContextDidBegin](EOAdaptorContext.Delegate.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpifsgc4dun5zeg33oorsxq5boirswyzlhmf2gkl3bmrqxa5dpojbw63tumv4hirdjmrbgkz3jny).

EOAdaptorContext also posts notifications to the application's
default notification center. Any object may register to receive
one or more of the notifications posted by an adaptor context by
registering as an observer with the default notification center
(an instance of the NSNotificationCenter class). For more information
on notifications, see the NSNotificationCenter class specification
in the _Foundation Framework Reference_.

## Creating an EOAdaptorContext Subclass

EOAdaptorContext provides many default method implementations
that are sufficient for concrete subclasses. The following methods
establish structure and conventions that other Enterprise Objects Framework
classes depend on and should be overridden with caution:

- [setDebugEnabledDefault](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sinxw45dfpb2c643forcgkytvm5cw4ylcnrswirdfmzqxk3du)
- [transactionDidBegin](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bporzgc3ttmfrxi2lpnzcgszccmvtws3q)
- [transactionDidCommit](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bporzgc3ttmfrxi2lpnzcgszcdn5ww22lu)
- [transactionDidRollback](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bporzgc3ttmfrxi2lpnzcgszcsn5wgyytbmnvq)
- [hasOpenTransaction](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpnbqxgt3qmvxfi4tbnzzwcy3unfxw4)

If you override any of the above methods, your implementations
should incorporate the superclass's implementation through a message
to __super__.

Other methods require database-specific implementations that
can be provided only by a concrete adaptor context subclass. A subclass
must override the following methods in terms of the persistent storage
system to which it interacts:

- [beginTransaction](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmjswo2lokrzgc3ttmfrxi2lpny)
- [commitTransaction](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmnxw23ljorkheyloonqwg5djn5xa)
- [createAdaptorChannel](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmnzgkylumvawiylqorxxeq3imfxg4zlm)
- [rollbackTransaction](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpojxwy3dcmfrwwvdsmfxhgyldoruw63q)

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md)
