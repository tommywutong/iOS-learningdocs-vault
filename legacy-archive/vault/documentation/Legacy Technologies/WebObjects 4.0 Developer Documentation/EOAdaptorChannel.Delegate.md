---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOAdaptorChannelDelegate.html
archived_at: '2026-07-18T01:28:14.364539Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOStoredProcedure.md)
[!](EOAdaptorContext.Delegate.md)

---

# EOAdaptorChannel.Delegate

EOAdaptorChannel delegate objects

__Inherits From:__
com.apple.yellow.eoaccess

EOAdaptorChannel sends messages to its delegate for nearly every operation that would affect data in the database server. The delegate can use these methods to preempt these operations, modify their results, or simply track activity.

---

## Instance Methods

---

### adaptorChannelDidChangeResultSet

public abstract void `adaptorChannelDidChangeResultSet`(java.lang.Object _channel_)

Invoked from [`fetchRow`](../Classes/EOAdaptorChannel.md#apple-gyztsni) when a select operation resulted in multiple result sets. This method tells the delegate that the next invocation of [`fetchRow`](../Classes/EOAdaptorChannel.md#apple-gyztsni) will fetch from the next result set. This method is invoked when [`fetchRow`](../Classes/EOAdaptorChannel.md#apple-gyztsni) returns `null` andthere are still result sets left to fetch. The delegate can invoke [`setAttributesToFetch`](../Classes/EOAdaptorChannel.md#apple-geydsny) to prepare for fetching the new rows.

---

### adaptorChannel:didEvaluateExpression

public abstract void `adaptorChannelDidEvaluateExpression`(java.lang.Object _channel_,
EOSQLExpression _expression_)

Invoked from [`evaluateExpression`](../Classes/EOAdaptorChannel.md#apple-geydaoi) to tell the delegate that a query language expression has been evaluated by the database server.

---

### adaptorChannelDidExecuteStoredProcedure

public abstract void `adaptorChannelDidExecuteStoredProcedure`(java.lang.Object _channel_,
EOStoredProcedure _procedure_,
NSDictionary _values_)

Invoked from [`executeStoredProcedure`](../Classes/EOAdaptorChannel.md#apple-gyztona) after _procedure_ is executed successfully.

---

### adaptorChannelDidFetchRow

public abstract void `adaptorChannelDidFetchRow`(java.lang.Object _channel_, NSMutableDictionary _row_)

Invoked from [`fetchRow`](../Classes/EOAdaptorChannel.md#apple-gyztsni) after a row is fetched successfully. This method is not invoked if an exception occurs during the fetch or if the same returns `null` because there are no more rows in the current result set. The delegate may modify _row_, which will be returned from [`fetchRow`](../Classes/EOAdaptorChannel.md#apple-gyztsni).

---

### adaptorChannelDidFinishFetching

public abstract void `adaptorChannelDidFinishFetching`(java.lang.Object _channel_)

Invoked from [`fetchRow`](../Classes/EOAdaptorChannel.md#apple-gyztsni) to tell the delegate that fetching is finished for the current select operation. This method is invoked when a fetch ends in [`fetchRow`](../Classes/EOAdaptorChannel.md#apple-gyztsni) because there are no more result sets.

---

### adaptorChannelDidPerformOperations

public abstract java.lang.Throwable `adaptorChannelDidPerformOperations`(
java.lang.Object _channel_,
NSArray _operations_,
java.lang.Throwable _exception_)

Invoked from [`performAdaptorOperations`](../Classes/EOAdaptorChannel.md#apple-geydomi). _exception_ is `null` if no exception was raised while _operations_ were performed. Otherwise, _exception_ is the raised exception. The delegate can return the same or a different exception, which is re-raised by [`performAdaptorOperations`](../Classes/EOAdaptorChannel.md#apple-geydomi), or it can return `null` to prevent the adaptor channel from raising an exception.

---

### adaptorChannelDidSelectAttributes

public abstract void `adaptorChannelDidSelectAttributes`(java.lang.Object _channel_,
NSArray _attributes_,
com.apple.yellow.eocontrol.EOFetchSpecification _fetchSpecification_,
boolean _flag_,
EOEntity _entity_)

Invoked from [`selectAttributes:fetchSpecification`](../Classes/EOAdaptorChannel.md#apple-geydsma) to tell the delegate that rows have been selected in the database server.

---

### adaptorChannelShouldConstructStoredProcedureReturnValues

public abstract NSDictionary `adaptorChannelShouldConstructStoredProcedureReturnValues`(java.lang.Object _channel_)

Invoked from [`returnValuesForLastStoredProcedureInvocation`](../Classes/EOAdaptorChannel.md#apple-geydqnq) to tell the delegate that _channel_ is constructing return values for the last stored procedure evaluated. If the delegate returns a value other than `null`, that value will be returned immediately from [`returnValuesForLastStoredProcedureInvocation`](../Classes/EOAdaptorChannel.md#apple-geydqnq).

---

### adaptorChannelShouldEvaluateExpression

public abstract boolean `adaptorChannelShouldEvaluateExpression`(java.lang.Object _channel_,
EOSQLExpression _expression_)

Invoked from [`evaluateExpression`](../Classes/EOAdaptorChannel.md#apple-geydaoi) to tell the delegate that _channel_ is sending an expression to the database server. The delegate returns true to permit the adaptor channel to send _expression_ to the server. If the delegate returns false, the adaptor channel does not send the expression and returns immediately. When the delegate returns false, the adaptor channel expects that the implementor of the delegate has done the work that [`evaluateExpression`](../Classes/EOAdaptorChannel.md#apple-geydaoi) would have done. The delegate can create a new EOSQLExpression and send the expression itself before returning false.

---

### adaptorChannelShouldExecuteStoredProcedure

public abstract NSDictionary `adaptorChannelShouldExecuteStoredProcedure`(java.lang.Object _channel_,
EOStoredProcedure _procedure_,
NSDictionary _values_)

Invoked from [`executeStoredProcedure`](../Classes/EOAdaptorChannel.md#apple-gyztona) to tell the delegate that _channel_ is executing a stored procedure. If the delegate returns a value other than `null`, that value is used as the arguments to the stored procedure instead of _values_.

---

### adaptorChannel:shouldReturnValuesForStoredProcedure

public abstract NSDictionary `adaptorChannelShouldReturnValuesForStoredProcedure`(java.lang.Object _channel_, NSDictionary _returnValues_)

Invoked from [`returnValuesForLastStoredProcedureInvocation`](../Classes/EOAdaptorChannel.md#apple-geydqnq) to tell the delegate that _channel_ is returning values for a stored procedure. If the delegate returns a value other than `null`, that value is returned from [`returnValuesForLastStoredProcedureInvocation`](../Classes/EOAdaptorChannel.md#apple-geydqnq) instead of _returnValues_.

---

### adaptorChannelShouldSelectAttributes

public abstract boolean `adaptorChannelShouldSelectAttributes`(java.lang.Object _channel_,
NSArray _attributes_,
com.apple.yellow.eocontrol.EOFetchSpecification _fetchSpecification_,
boolean _flag_,
EOEntity _entity_)

Invoked from [`selectAttributes:fetchSpecification`](../Classes/EOAdaptorChannel.md#apple-geydsma) to ask the delegate whether a select operation should be performed. The delegate should not modify _fetchSpecification_. Instead, if the delegate wants to perform a different select it should invoke [`selectAttributes:fetchSpecification`](../Classes/EOAdaptorChannel.md#apple-geydsma) itself with a new fetch specification, and return false (indicating that the adaptor channel should not perform the select itself).

---

### adaptorChannelWillFetchRow

public abstract void `adaptorChannelWillFetchRow`(java.lang.Object _channel_)

Invoked from [`fetchRow`](../Classes/EOAdaptorChannel.md#apple-gyztsni) to tell the delegate that a single row will be fetched. The delegate can determine the attributes used by the fetch by sending [`attributesToFetch`](../Classes/EOAdaptorChannel.md#apple-gq3dmmq) to _channel_, and can change the set of attributes to fetch by sending [`setAttributesToFetch`](../Classes/EOAdaptorChannel.md#apple-geydsny) to _channel_. The adaptor channel performs the actual fetch.

---

### adaptorChannelWillPerformOperations

public abstract NSArray `adaptorChannelWillPerformOperations`(java.lang.Object _channel_,
NSArray _operations_)

Invoked from [`performAdaptorOperations`](../Classes/EOAdaptorChannel.md#apple-geydomi) to tell the delegate that _channel_ is performing the EOAdaptorOperations in _operations_. The delegate may return _operations_ or a different NSArray for the adaptor channel to perform. If the delegate returns `null`, the adaptor channel does not perform the operations and returns from the method immediately.

---

[!](EOStoredProcedure.md)
[!](EOAdaptorContext.Delegate.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
