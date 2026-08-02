---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/More/EOAdaptorContext.html
archived_at: '2026-07-15T08:11:33.911733Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md)

# EOAdaptorContext

## Controlling Transactions

EOAdaptorContext defines a simple set of methods for explicitly
controlling transactions: [beginTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3cmvtws3suojqw443bmn2gs33o), [commitTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dn5ww22lukrzgc3ttmfrxi2lpny),
and [rollbackTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3sn5wgyytbmnvvi4tbnzzwcy3unfxw4).
Each of these messages confirms the requested action with the adaptor
context's delegate, then performs the action if possible.

There's also a set of methods for notifying an adaptor context
that a transaction has been started, committed, or rolled back without
using the __beginTransaction__, __commitTransaction__,
or __rollbackTransaction__ methods. For example,
if you invoke a stored procedure in the server that begins a transaction,
you need to notify the adaptor context that a transaction has been
started. Use the following methods to keep an adaptor context synchronized
with the state of the database server: [transactionDidBegin](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3uojqw443bmn2gs33oiruwiqtfm5uw4), [transactionDidCommit](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3uojqw443bmn2gs33oiruwiq3pnvwws5a),
and [transactionDidRollback](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3uojqw443bmn2gs33oiruwiutpnrwgeyldnm).
These methods post notifications.

## The Adaptor Context's Delegate and Notifications

You can assign a delegate to an adaptor context. The delegate
responds to certain messages on behalf of the context. An EOAdaptorContext
sends these messages directly to its delegate. The transaction-controlling
methods- [beginTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3cmvtws3suojqw443bmn2gs33o), [commitTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dn5ww22lukrzgc3ttmfrxi2lpny),
and [rollbackTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3sn5wgyytbmnvvi4tbnzzwcy3unfxw4)-notify
the adaptor context's delegate before and after a transaction
operation is performed. Some delegate methods, such as [adaptorContextShouldBegin:](EOAdaptorContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbw63tumv4hiicemvwgkz3borss6ylemfyhi33sinxw45dfpb2fg2dpovwgiqtfm5uw4oq),
let the delegate determine whether the context should perform an
operation. Others, such as [adaptorContextDidBegin:](EOAdaptorContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbw63tumv4hiicemvwgkz3borss6ylemfyhi33sinxw45dfpb2ei2leijswo2lohi),
are simply notifications that an operation has occurred. The delegate
has an opportunity to respond by implementing the delegate methods.
If the delegate wants to intervene, it implements [adaptorContextShouldBegin:](EOAdaptorContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbw63tumv4hiicemvwgkz3borss6ylemfyhi33sinxw45dfpb2fg2dpovwgiqtfm5uw4oq).
If it simply wants notification when a transaction has begun, it
implements [adaptorContextDidBegin:](EOAdaptorContext%20Delegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbw63tumv4hiicemvwgkz3borss6ylemfyhi33sinxw45dfpb2ei2leijswo2lohi).

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

- [+ setDebugEnabledDefault:](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuczdbob2g64sdn5xhizlyoqxxgzluirswe5lhivxgcytmmvseizlgmf2wy5b2)
- [- transactionDidBegin](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3uojqw443bmn2gs33oiruwiqtfm5uw4)
- [- transactionDidCommit](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3uojqw443bmn2gs33oiruwiq3pnvwws5a)
- [- transactionDidRollback](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3uojqw443bmn2gs33oiruwiutpnrwgeyldnm)
- [- hasOpenTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3imfzu64dfnzkheyloonqwg5djn5xa)

If you override any of the above methods, your implementations
should incorporate the superclass's implementation through a message
to __super__.

Other methods require database-specific implementations that
can be provided only by a concrete adaptor context subclass. A subclass
must override the following methods in terms of the persistent storage
system to which it interacts:

- [- beginTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3cmvtws3suojqw443bmn2gs33o)
- [- commitTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dn5ww22lukrzgc3ttmfrxi2lpny)
- [- createAdaptorChannel](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dojswc5dfifsgc4dun5zeg2dbnzxgk3a)
- [- rollbackTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3sn5wgyytbmnvvi4tbnzzwcy3unfxw4)

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md)
