---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.2e.html
archived_at: '2026-07-15T08:14:52.743456Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.2d.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.2f.md)

#   Pessimistic Locking in Oracle

##  Synopsis

Describes how pessimistic locking works in Oracle.

##  Discussion

Oracle supports row-level pessimistic locking. By default EOF uses Oracle's
SELECT FOR UPDATE
without the
NO WAIT
clause. This can be changed by calling OracleSQLExpression's
setUseNoWaitLocks
class method.

The standard
SELECT FOR UPDATE
lock will cause all the
UPDATE
or
SELECT FOR UPDATE
statements from other database connections to block until a commit, rollback, or a deadlock exception occurs. A deadlock exception occurs when one user has row A locked and is trying to lock row B, while another user has row B locked and is trying to lock row A. In this case, Oracle disables one of the users locks while letting the other user lock both rows.

When using the
SELECT FOR UPDATE NO WAIT
locks, Oracle will cause an exception whenever a locked row is selected. This can be useful if you don't want to block a user for an indefinite amount of time.

Also note that a
SELECT
statement without the
FOR UPDATE
clause will always work. This can be somewhat dangerous. For example, suppose user A fetches an object without locking it. User B fetches the object with locking and saves it. User A then modifies the object and again saves it, overwriting what user B has done. The only way this can be avoided is to use a consistent locking strategy.

##  See Also

- 

  [Pessimistic Locking in Oracle](#apple-giztqnbs)
- 

  [Choosing an Approach for Locking](Choosing%20an%20Approach%20for%20Locking.md#apple-ge2tmmjy)

##  Questions

- 

  What is locking?
- 

  How does pessimistic locking work with Oracle?

##  Keywords

- 

  Lock
- 

  Pessimistic
- 

  Oracle

##  Revision History

22 July, 1998. Paul Haddad. First Draft.

```

```

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.2d.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.2f.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
