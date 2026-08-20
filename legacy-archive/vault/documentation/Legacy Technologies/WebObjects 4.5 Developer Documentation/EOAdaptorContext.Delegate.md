---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Protocols/EOAdaptorContextDelegate.html
archived_at: '2026-07-15T08:11:33.190631Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EOAdaptorContext.Delegate

> __(informal interface)__

> __Package:__
> com.apple.yellow.eoaccess

## Interface Description

---

EOAdaptorContext sends messages to its delegate for any transaction
begin, commit, or rollback. The delegate can use these methods to
preempt these operations, modify their results, or simply track activity.

## Instance Methods

---

### adaptorContextDidBegin

`public abstract void adaptorContextDidBegin(Object context)`

Invoked from [beginTransaction](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmjswo2lokrzgc3ttmfrxi2lpny) to tell the delegate
that a transaction has begun.

---

### adaptorContextDidCommit

`public abstract void adaptorContextDidCommit(Object context)`

Invoked from [commitTransaction](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmnxw23ljorkheyloonqwg5djn5xa) to
tell the delegate that a transaction has been committed.

---

### adaptorContextDidRollback

`public abstract void adaptorContextDidRollback(Object context)`

Invoked from [rollbackTransaction](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpojxwy3dcmfrwwvdsmfxhgyldoruw63q) to
tell the delegate that a transaction has been rolled back.

---

### adaptorContextShouldBegin

`public abstract boolean adaptorContextShouldBegin(Object context)`

Invoked from [beginTransaction](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmjswo2lokrzgc3ttmfrxi2lpny) to tell the delegate
that _context_ is beginning a transaction.
If this method returns false, the adaptor context does not begin
a transaction. Return true to allow the adaptor context to begin
a transaction.

---

### adaptorContextShouldCommit

`public abstract boolean adaptorContextShouldCommit(Object context)`

Invoked from [commitTransaction](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpmnxw23ljorkheyloonqwg5djn5xa) to
tell the delegate that _context_ is
committing a transaction. If this method returns false, the adaptor
context does not commit the transaction. Return true to allow the adaptor
context to commit.

Note that if you implement this delegate method to return false,
your delegate must perform the database COMMIT itself; the rest
of the Enterprise Objects Framework assumes that the commit has taken
place. [adaptorContextShouldCommit](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpifsgc4dun5zeg33oorsxq5boirswyzlhmf2gkl3bmrqxa5dpojbw63tumv4hiu3in52wyzcdn5ww22lu) doesn't
specify whether or not the commit should take place; it only specifies
whether or not the adaptor context should do it for you.

---

### adaptorContextShouldConnect

`public abstract boolean adaptorContextShouldConnect(Object context)`

Invoked before the adaptor attempts to connect.
The delegate can return false if it wants to override the connect, true if
it wants the adaptor to attempt to connect in the usual way. The
delegate should throw an exception if it fails to connect.

---

### adaptorContextShouldRollback

`public abstract boolean adaptorContextShouldRollback(Object context)`

Invoked from [rollbackTransaction](EOAdaptorContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg33oorsxq5bpojxwy3dcmfrwwvdsmfxhgyldoruw63q) to
tell the delegate that _context_ is
rolling back a transaction. If this method returns false, the adaptor
context does not roll back the transaction. Return true to allow
the adaptor context to roll back.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
