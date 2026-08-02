---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.2f.html
archived_at: '2026-07-15T08:14:52.800064Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.2e.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.30.md)

#   Pessimistic Locking in Sybase

##  Synopsis

Describes how pessimistic locking works in Sybase.

##  Discussion

All Sybase versions prior to version 11.9 use page-level locking. Unlike a row-level lock, a page-level lock not only locks the row you selected, but also locks all other rows in the same page. Page sizes can be changed, but doing so may affect overall database performance.

EOF uses the
HOLDLOCK
clause when performing a select to enable Sybase's pessimistic locking. Suppose two users lock a record with the
HOLDLOCK
clause. If user A tries to update the record before user B, user A blocks until user B either saves his changes or reverts his changes. If user B attempts to save his changes, an exception is raised and his update fails, whereupon user A's update succeeds.

Suppose user A locks a record, but user B does not. If user B attempts to update that record, he blocks until user A saves his changes or reverts his changes. At this point, user B's update continues, and no exception is raised.

##  See Also

- 

  [Pessimistic Locking](Pessimistic%20Locking.md#apple-ge2dgmrw)
- 

  [Choosing an Approach for Locking](Choosing%20an%20Approach%20for%20Locking.md#apple-ge2tmmjy)

##  Questions

- 

  What is locking?
- 

  How does pessimistic locking work with Sybase?

##  Keywords

- 

  Lock
- 

  Pessimistic
- 

  Sybase

##  Revision History

22 July, 1998. Paul Haddad. First Draft.

```

```

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.2e.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.30.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
