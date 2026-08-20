---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/PessimisticLockingOra.html
archived_at: '2026-07-15T08:01:21.777452Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Pessimistic Locking in Oracle

##  Synopsis

Describes how pessimistic locking works in Oracle.

##  Discussion

Oracle supports row-level pessimistic locking. By default EOF uses Oracle's _SELECT FOR UPDATE_
without the _NO WAIT_
clause. This can be changed by calling OracleSQLExpression's _setUseNoWaitLocks_
class method.

The standard _SELECT FOR UPDATE_
lock will cause all the _UPDATE_
or _SELECT FOR UPDATE_
statements from other database connections to block until a commit, rollback, or a deadlock exception occurs. A deadlock exception occurs when one user has row A locked and is trying to lock row B, while another user has row B locked and is trying to lock row A. In this case, Oracle disables one of the users locks while letting the other user lock both rows.

When using the _SELECT FOR UPDATE NO WAIT_
locks, Oracle will cause an exception whenever a locked row is selected. This can be useful if you don't want to block a user for an indefinite amount of time.

Also note that a _SELECT_
statement without the _FOR UPDATE_
clause will always work. This can be somewhat dangerous. For example, suppose user A fetches an object without locking it. User B fetches the object with locking and saves it. User A then modifies the object and again saves it, overwriting what user B has done. The only way this can be avoided is to use a consistent locking strategy.

##  See Also

· Pessimistic Locking

· Choosing an Approach for Locking

##  Questions

· What is locking?

· How does pessimistic locking work with Oracle?

##  Keywords

· Pessimistic Locking

· Oracle

##  Revision History

22 July, 1998. Paul Haddad. First Draft.

```

```


Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
