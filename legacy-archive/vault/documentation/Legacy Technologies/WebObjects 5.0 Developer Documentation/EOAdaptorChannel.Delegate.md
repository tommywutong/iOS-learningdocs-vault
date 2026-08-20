---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Protocols/EOAdaptorChannelDelegate.html
archived_at: '2026-07-15T08:13:41.943682Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

# EOAdaptorChannel.Delegate

> __(informal interface)__

> **__Package:__**
> : com.webobjects.eoaccess

---

## Interface Description

---

EOAdaptorChannel sends messages to its delegate for nearly every operation that would affect data in the database server. The delegate can use these methods to preempt these operations, modify their results, or simply track activity.

## Instance Methods

---

### adaptorChannelDidChangeResultSet

`public abstract void adaptorChannelDidChangeResultSet(Object channel)`

Invoked from fetchRow when a select operation resulted in multiple result sets. This method tells the delegate that the next invocation of fetchRow will fetch from the next result set. This method is invoked when fetchRow returns `null` andthere are still result sets left to fetch. The delegate can invoke setAttributesToFetch to prepare for fetching the new rows.

---

### adaptorChannelDidEvaluateExpression

`public abstract void adaptorChannelDidEvaluateExpression( Object channel, EOSQLExpression expression)`

Invoked from evaluateExpression to tell the delegate that a query language expression has been evaluated by the database server.

---

### adaptorChannelDidExecuteStoredProcedure

`public abstract void adaptorChannelDidExecuteStoredProcedure( Object channel, EOStoredProcedure procedure, NSDictionary values)`

Invoked from executeStoredProcedure after _procedure_ is executed successfully.

---

### adaptorChannelDidFetchRow

`public abstract void adaptorChannelDidFetchRow( Object channel, NSMutableDictionary row)`

Invoked from fetchRow after a row is fetched successfully. This method is not invoked if an exception occurs during the fetch or if the same returns `null` because there are no more rows in the current result set. The delegate may modify _row_, which will be returned from fetchRow.

---

### adaptorChannelDidFinishFetching

`public abstract void adaptorChannelDidFinishFetching(Object channel)`

Invoked from fetchRow to tell the delegate that fetching is finished for the current select operation. This method is invoked when a fetch ends in fetchRow because there are no more result sets.

---

### adaptorChannelDidPerformOperations

`public abstract Throwable adaptorChannelDidPerformOperations( Object channel, NSArray operations, Throwable exception)`

Invoked from performAdaptorOperations. _exception_ is `null` if no exception was raised while _operations_ were performed. Otherwise, _exception_ is the raised exception. The delegate can return the same or a different exception, which is re-raised by performAdaptorOperations, or it can return `null` to prevent the adaptor channel from raising an exception.

---

### adaptorChannelDidSelectAttributes

`public abstract void adaptorChannelDidSelectAttributes( Object channel, NSArray attributes, com.webobjects.eocontrol.EOFetchSpecification fetchSpecification, boolean flag, EOEntity entity)`

Invoked from selectAttributes to tell the delegate that rows have been selected in the database server.

---

### adaptorChannelShouldConstructStoredProcedureReturnValues

`public abstract NSDictionary adaptorChannelShouldConstructStoredProcedureReturnValues(Object channel)`

Invoked from returnValuesForLastStoredProcedureInvocation to tell the delegate that _channel_ is constructing return values for the last stored procedure evaluated. If the delegate returns a value other than `null`, that value will be returned immediately from returnValuesForLastStoredProcedureInvocation.

---

### adaptorChannelShouldEvaluateExpression

`public abstract boolean adaptorChannelShouldEvaluateExpression( Object channel, EOSQLExpression expression)`

Invoked from evaluateExpression to tell the delegate that _channel_ is sending an expression to the database server. The delegate returns `true` to permit the adaptor channel to send _expression_ to the server. If the delegate returns `false`, the adaptor channel does not send the expression and returns immediately. When the delegate returns `false`, the adaptor channel expects that the implementor of the delegate has done the work that evaluateExpression would have done. The delegate can create a new EOSQLExpression and send the expression itself before returning `false`.

---

### adaptorChannelShouldExecuteStoredProcedure

`public abstract NSDictionary adaptorChannelShouldExecuteStoredProcedure( Object channel, EOStoredProcedure procedure, NSDictionary values)`

Invoked from executeStoredProcedure to tell the delegate that _channel_ is executing a stored procedure. If the delegate returns a value other than `null`, that value is used as the arguments to the stored procedure instead of _values_.

---

### adaptorChannelShouldReturnValuesForStoredProcedure

`public abstract NSDictionary adaptorChannelShouldReturnValuesForStoredProcedure( Object channel, NSDictionary returnValues)`

Invoked from returnValuesForLastStoredProcedureInvocation to tell the delegate that _channel_ is returning values for a stored procedure. If the delegate returns a value other than `null`, that value is returned from returnValuesForLastStoredProcedureInvocation instead of _returnValues_.

---

### adaptorChannelShouldSelectAttributes

`public abstract boolean adaptorChannelShouldSelectAttributes( Object channel, NSArray attributes, com.webobjects.eocontrol.EOFetchSpecification fetchSpecification, boolean flag, EOEntity entity)`

Invoked from selectAttributes to ask the delegate whether a select operation should be performed. The delegate should not modify fetchSpecification. Instead, if the delegate wants to perform a different select it should invoke selectAttributes itself with a new fetch specification, and return `false` (indicating that the adaptor channel should not perform the select itself).

---

### adaptorChannelWillFetchRow

`public abstract void adaptorChannelWillFetchRow(Object channel)`

Invoked from fetchRow to tell the delegate that a single row will be fetched. The delegate can determine the attributes used by the fetch by sending attributesToFetch to _channel_, and can change the set of attributes to fetch by sending setAttributesToFetch to _channel_. The adaptor channel performs the actual fetch.

---

### adaptorChannelWillPerformOperations

`public abstract NSArray adaptorChannelWillPerformOperations( Object channel, NSArray operations)`

Invoked from performAdaptorOperations to tell the delegate that _channel_ is performing the EOAdaptorOperations in _operations_. The delegate may return _operations_ or a different NSArray for the adaptor channel to perform. If the delegate returns `null`, the adaptor channel does not perform the operations and returns from the method immediately.

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
