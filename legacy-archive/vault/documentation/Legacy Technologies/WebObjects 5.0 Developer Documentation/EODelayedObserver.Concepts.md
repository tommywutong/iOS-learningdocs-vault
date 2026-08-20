---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/Concepts/EODelayedObserverConcepts.html
archived_at: '2026-07-15T08:13:43.623372Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Classes/Art/up.gif)](../../EOControlTOC.md) 

# EODelayedObserver.Concepts

## Creating a Subclass of EODelayedObserver

EODelayedObserver implements the basic objectWillChange method to simply enqueue the receiver on an EODelayedObserverQueue. Regardless of how many of these messages the receiver gets during the run loop, it receives a single subjectChanged message from the queue-at the end of the run loop. In this method the delayed observer can check for changes and take whatever action is necessary. Subclasses should record objects they're interested in and examine them in __subjectChanged__. An EOAssociation.(EOInterface) for example, examines each of the EODisplayGroups (EOInterface) it's bound to in order to find out what has changed. Another kind of subclass might record each changed object for later examination by overriding __objectWillChange__, but it must be sure to invoke __super__'s implementation when doing so.

The rest of EODelayedObserver's methods have meaningful, if static, default implementations. EODelayedObserverQueue sends change notifications according to the priority of each enqueued observer. EODelayedObserver's implementation of the priority method returns ObserverPriorityThird. Your subclass can override it to return a higher or lower priority, or to have a settable priority. The other method a subclass might override is observerQueue, which returns a default EODelayedObserverQueue normally shared by all EODelayedObservers. Because sharing a single queue keeps all EODelayedObserver's synchronized according to their priority, you should rarely override this method, doing so only if your subclass is involved in a completely independent system.

A final method, discardPendingNotification, need never be overridden by subclasses, but must be invoked when a delayed observer is done observing changes. This prevents observers from being sent change notifications after they've been finalized.

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Classes/Art/up.gif)](../../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
