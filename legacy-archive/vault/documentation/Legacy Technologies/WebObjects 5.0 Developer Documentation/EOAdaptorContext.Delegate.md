---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Protocols/EOAdaptorContextDelegate.html
archived_at: '2026-07-15T08:13:41.972830Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

# EOAdaptorContext.Delegate

> __(informal interface)__

> **__Package:__**
> : com.webobjects.eoaccess

---

## Interface Description

---

EOAdaptorContext sends messages to its delegate for any transaction begin, commit, or rollback. The delegate can use these methods to preempt these operations, modify their results, or simply track activity.

## Instance Methods

---

### adaptorContextDidBegin

`public abstract void adaptorContextDidBegin(Object context)`

Invoked from beginTransaction to tell the delegate that a transaction has begun.

---

### adaptorContextDidCommit

`public abstract void adaptorContextDidCommit(Object context)`

Invoked from commitTransaction to tell the delegate that a transaction has been committed.

---

### adaptorContextDidRollback

`public abstract void adaptorContextDidRollback(Object context)`

Invoked from rollbackTransaction to tell the delegate that a transaction has been rolled back.

---

### adaptorContextShouldBegin

`public abstract boolean adaptorContextShouldBegin(Object context)`

Invoked from beginTransaction to tell the delegate that _context_ is beginning a transaction. If this method returns `false`, the adaptor context does not begin a transaction. Return `true` to allow the adaptor context to begin a transaction.

---

### adaptorContextShouldCommit

`public abstract boolean adaptorContextShouldCommit(Object context)`

Invoked from commitTransaction to tell the delegate that _context_ is committing a transaction. If this method returns `false`, the adaptor context does not commit the transaction. Return `true` to allow the adaptor context to commit.

Note that if you implement this delegate method to return `false`, your delegate must perform the database COMMIT itself; the rest of the Enterprise Objects Framework assumes that the commit has taken place. adaptorContextShouldCommit doesn't specify whether or not the commit should take place; it only specifies whether or not the adaptor context should do it for you.

---

### adaptorContextShouldConnect

`public abstract boolean adaptorContextShouldConnect(Object context)`

Invoked before the adaptor attempts to connect. The delegate can return `false` if it wants to override the connect, `true` if it wants the adaptor to attempt to connect in the usual way. The delegate should throw an exception if it fails to connect.

---

### adaptorContextShouldRollback

`public abstract boolean adaptorContextShouldRollback(Object context)`

Invoked from rollbackTransaction to tell the delegate that _context_ is rolling back a transaction. If this method returns `false`, the adaptor context does not roll back the transaction. Return `true` to allow the adaptor context to roll back.

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
