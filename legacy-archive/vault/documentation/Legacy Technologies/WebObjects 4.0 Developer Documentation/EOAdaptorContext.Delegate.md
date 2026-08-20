---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOAdaptorContextDelegate.html
archived_at: '2026-07-18T01:28:14.452042Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOAdaptorChannel.Delegate.md)
[!](EOAdaptor.Delegate.md)

---

# EOAdaptorContext.Delegate

EOAdaptorContext delegate objects

__Inherits From:__
com.apple.yellow.eoaccess

EOAdaptorContext sends messages to its delegate for any transaction begin, commit, or rollback. The delegate can use these methods to preempt these operations, modify their results, or simply track activity.

---

## Instance Methods

---

### adaptorContextDidBegin

public abstract void `adaptorContextDidBegin`(java.lang.Object _context_)

Invoked from [`beginTransaction`](../Classes/EOAdaptorContext.md#apple-gu2to) to tell the delegate that a transaction has begun.

---

### adaptorContextDidCommit

public abstract void `adaptorContextDidCommit`(java.lang.Object _context_)

Invoked from [`commitTransaction`](../Classes/EOAdaptorContext.md#apple-gu3tk) to tell the delegate that a transaction has been committed.

---

### adaptorContextDidRollback

public abstract void `adaptorContextDidRollback`(java.lang.Object _context_)

Invoked from [`rollbackTransaction`](../Classes/EOAdaptorContext.md#apple-gm4tkna) to tell the delegate that a transaction has been rolled back.

---

### adaptorContextShouldBegin

public abstract boolean `adaptorContextShouldBegin`(java.lang.Object _context_)

Invoked from `[beginTransaction](../Classes/EOAdaptorContext.md#apple-gu2to)` to tell the delegate that _context_ is beginning a transaction. If this method returns false, the adaptor context does not begin a transaction. Return true to allow the adaptor context to begin a transaction.

---

### adaptorContextShouldCommit

public abstract boolean `adaptorContextShouldCommit`(java.lang.Object _context_)

Invoked from [`commitTransaction`](../Classes/EOAdaptorContext.md#apple-gu3tk) to tell the delegate that _context_ is committing a transaction. If this method returns false, the adaptor context does not commit the transaction. Return true to allow the adaptor context to commit.

Note that if you implement this delegate method to return false, your delegate must perform the database COMMIT itself; the rest of the Enterprise Objects Framework assumes that the commit has taken place. [`adaptorContextShouldCommit`](#apple-gy3do) doesn't specify whether or not the commit should take place; it only specifies whether or not the adaptor context should do it for you.

---

### adaptorContextShouldConnect

public abstract boolean `adaptorContextShouldConnect`(java.lang.Object _context_)

Invoked before the adaptor attempts to connect. The delegate can return false if it wants to override the connect, true if it wants the adaptor to attempt to connect in the usual way. The delegate should throw an exception if it fails to connect.

---

### adaptorContextShouldRollback

public abstract boolean `adaptorContextShouldRollback`(java.lang.Object _context_)

Invoked from [`rollbackTransaction`](../Classes/EOAdaptorContext.md#apple-gm4tkna) to tell the delegate that _context_ is rolling back a transaction. If this method returns false, the adaptor context does not roll back the transaction. Return true to allow the adaptor context to roll back.

---

[!](EOAdaptorChannel.Delegate.md)
[!](EOAdaptor.Delegate.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
