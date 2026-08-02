---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/More/EODelayedObserver.html
archived_at: '2026-07-15T08:11:38.050764Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)

# EODelayedObserver

## Creating a Subclass of EODelayedObserver

EODelayedObserver implements the basic [objectWillChange](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5xwe2tfmn2fo2lmnrbwqylom5sq) method
to simply enqueue the receiver on an EODelayedObserverQueue. Regardless
of how many of these messages the receiver gets during the run loop,
it receives a single [subjectChanged](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5zxkytkmvrxiq3imfxgozle) message from the queue-at
the end of the run loop. In this method the delayed observer can
check for changes and take whatever action is necessary. Subclasses should
record objects they're interested in and examine them in `subjectChanged`.
An EOAssociation.(EOInterface) for example, examines each of the
EODisplayGroups (EOInterface) it's bound to in order to find out
what has changed. Another kind of subclass might record each changed object
for later examination by overriding `objectWillChange`,
but it must be sure to invoke `super`'s implementation
when doing so.

The rest of EODelayedObserver's methods have meaningful,
if static, default implementations. EODelayedObserverQueue sends
change notifications according to the priority of each enqueued observer.
EODelayedObserver's implementation of the [priority](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5yhe2lpojuxi6i) method returns [ObserverPriorityThird](EODelayedObserver.md#apple-incuoq2difeem). Your subclass
can override it to return a higher or lower priority, or to have
a settable priority. The other method a subclass might override
is [observerQueue](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5xwe43foj3gk4srovsxkzi), which returns a default EODelayedObserverQueue
normally shared by all EODelayedObservers. Because sharing a single queue
keeps all EODelayedObserver's synchronized according to their
priority, you should rarely override this method, doing so only
if your subclass is involved in a completely independent system.

A final method, [discardPendingNotification](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5sgs43dmfzgiudfnzsgs3thjzxxi2lgnfrwc5djn5xa),
need never be overridden by subclasses, but must be invoked when
a delayed observer is done observing changes. This prevents observers
from being sent change notifications after they've been finalized.

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)
