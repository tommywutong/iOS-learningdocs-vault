---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Protocols/EOAdaptorContextDelegate.html
archived_at: '2026-07-15T08:11:35.959049Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EOAdaptorContext Delegate

> __(informal protocol)__

> __Declared in:__  EOAccess/EOAdaptorContext.h

## Protocol Description

---

EOAdaptorContext sends messages to its delegate for any transaction
begin, commit, or rollback. The delegate can use these methods to
preempt these operations, modify their results, or simply track activity.

## Instance Methods

---

### adaptorContextDidBegin:

`- (void)adaptorContextDidBegin:context`

Invoked from [beginTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3cmvtws3suojqw443bmn2gs33o) to tell the delegate
that a transaction has begun.

---

### adaptorContextDidCommit:

`- (void)adaptorContextDidCommit:context`

Invoked from [commitTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dn5ww22lukrzgc3ttmfrxi2lpny) to
tell the delegate that a transaction has been committed.

---

### adaptorContextDidRollback:

`- (void)adaptorContextDidRollback:context`

Invoked from [rollbackTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3sn5wgyytbmnvvi4tbnzzwcy3unfxw4) to
tell the delegate that a transaction has been rolled back.

---

### adaptorContextShouldBegin:

`- (BOOL)adaptorContextShouldBegin:context`

Invoked from [beginTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3cmvtws3suojqw443bmn2gs33o) to tell the delegate
that _context_ is beginning a transaction.
If this method returns NO, the adaptor context does not begin a
transaction. Return YES to allow the adaptor context to begin a
transaction.

---

### adaptorContextShouldCommit:

`- (BOOL)adaptorContextShouldCommit:context`

Invoked from [commitTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3dn5ww22lukrzgc3ttmfrxi2lpny) to
tell the delegate that _context_ is
committing a transaction. If this method returns NO, the adaptor
context does not commit the transaction. Return YES to allow the adaptor
context to commit.

Note that if you implement this delegate method to return NO,
your delegate must perform the database COMMIT itself; the rest
of the Enterprise Objects Framework assumes that the commit has
taken place. [adaptorContextShouldCommit:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2bmrqxa5dpojbw63tumv4hiicemvwgkz3borss6ylemfyhi33sinxw45dfpb2fg2dpovwgiq3pnvwws5b2) doesn't
specify whether or not the commit should take place; it only specifies
whether or not the adaptor context should do it for you.

---

### adaptorContextShouldConnect:

`- (BOOL)adaptorContextShouldConnect:context`

Invoked before the adaptor attempts to connect.
The delegate can return NO if it wants to override the connect, YES if
it wants the adaptor to attempt to connect in the usual way. The
delegate should raise an exception if it fails to connect.

---

### adaptorContextShouldRollback:

`- (BOOL)adaptorContextShouldRollback:context`

Invoked from [rollbackTransaction](EOAdaptorContext-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbw63tumv4hil3sn5wgyytbmnvvi4tbnzzwcy3unfxw4) to
tell the delegate that _context_ is
rolling back a transaction. If this method returns NO, the adaptor
context does not roll back the transaction. Return YES to allow
the adaptor context to roll back.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
