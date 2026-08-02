---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EOAdaptorChannelDelegate.html
archived_at: '2026-07-18T01:28:23.740793Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](NSString%20Additions.md)
[!](EOAdaptorContextDelegate.md)

---

# EOAdaptorChannelDelegate

__Adopted By:__
EOAdaptorChannel delegate objects

__Declared in:__
EOAccess/EOAdaptorChannel.h

# Protocol Description

EOAdaptorChannel sends messages to its delegate for nearly every operation that would affect data in the database server. The delegate can use these methods to preempt these operations, modify their results, or simply track activity.

---

## Instance Methods

---

### adaptorChannelDidChangeResultSet:

- (void)`adaptorChannelDidChangeResultSet:`(id)_channel_

Invoked from [`fetchRowWithZone:`](../Classes/EOAdaptorChannel.md#apple-gyztsni) when a select operation resulted in multiple result sets. This method tells the delegate that the next invocation of [`fetchRowWithZone:`](../Classes/EOAdaptorChannel.md#apple-gyztsni) will fetch from the next result set. This method is invoked when [`fetchRowWithZone:`](../Classes/EOAdaptorChannel.md#apple-gyztsni) returns `nil` andthere are still result sets left to fetch. The delegate can invoke [`setAttributesToFetch:`](../Classes/EOAdaptorChannel.md#apple-geydsny) to prepare for fetching the new rows.

---

### adaptorChannel:didEvaluateExpression:

- (void)`adaptorChannel:`(id)_channel_`didEvaluateExpression:`(EOSQLExpression \*)_expression_

Invoked from [`evaluateExpression:`](../Classes/EOAdaptorChannel.md#apple-geydaoi) to tell the delegate that a query language expression has been evaluated by the database server.

---

### adaptorChannel:didExecuteStoredProcedure:withValues:

- (void)`adaptorChannel:`(id)_channel_`didExecuteStoredProcedure:`(EOStoredProcedure \*)_procedure_`withValues:`(NSDictionary \*)_values_

Invoked from [`executeStoredProcedure:withValues:`](../Classes/EOAdaptorChannel.md#apple-gyztona) after _procedure_ is executed successfully.

---

### adaptorChannel:didFetchRow:

- (void)`adaptorChannel:`(id)_channel_ `didFetchRow:`(NSMutableDictionary \*)_row_

Invoked from [`fetchRowWithZone:`](../Classes/EOAdaptorChannel.md#apple-gyztsni) after a row is fetched successfully. This method is not invoked if an exception occurs during the fetch or if the same returns `nil` because there are no more rows in the current result set. The delegate may modify _row_, which will be returned from [`fetchRowWithZone:`](../Classes/EOAdaptorChannel.md#apple-gyztsni).

---

### adaptorChannelDidFinishFetching:

- (void)`adaptorChannelDidFinishFetching:`(id)_channel_

Invoked from [`fetchRowWithZone:`](../Classes/EOAdaptorChannel.md#apple-gyztsni) to tell the delegate that fetching is finished for the current select operation. This method is invoked when a fetch ends in [`fetchRowWithZone:`](../Classes/EOAdaptorChannel.md#apple-gyztsni) because there are no more result sets.

---

### adaptorChannel:didPerformOperations:exception:

- (NSException \*)`adaptorChannel:`(id)_channel_`didPerformOperations:`(NSArray \*)_operations_`exception:`(NSException \*)_exception_

Invoked from [`performAdaptorOperations:`](../Classes/EOAdaptorChannel.md#apple-geydomi). _exception_ is `nil` if no exception was raised while _operations_ were performed. Otherwise, _exception_ is the raised exception. The delegate can return the same or a different exception, which is re-raised by [`performAdaptorOperations:`](../Classes/EOAdaptorChannel.md#apple-geydomi), or it can return `nil` to prevent the adaptor channel from raising an exception.

---

### adaptorChannel:didSelectAttributes:fetchSpecification:lock:entity:

- (void)`adaptorChannel:`(id)_channel_`didSelectAttributes:`(NSArray \*)_attributes_`fetchSpecification:`(EOFetchSpecification \*)_fetchSpecification_`lock:`(BOOL)_flag_`entity:`(EOEntity \*)_entity_

Invoked from [`selectAttributes:fetchSpecification:lock:entity:`](../Classes/EOAdaptorChannel.md#apple-geydsma) to tell the delegate that rows have been selected in the database server.

---

### adaptorChannelShouldConstructStoredProcedureReturnValues:

- (NSDictionary \*)`adaptorChannelShouldConstructStoredProcedureReturnValues:`(id)_channel_

Invoked from [`returnValuesForLastStoredProcedureInvocation`](../Classes/EOAdaptorChannel.md#apple-geydqnq) to tell the delegate that _channel_ is constructing return values for the last stored procedure evaluated. If the delegate returns a value other than `nil`, that value will be returned immediately from [`returnValuesForLastStoredProcedureInvocation`](../Classes/EOAdaptorChannel.md#apple-geydqnq).

---

### adaptorChannel:shouldEvaluateExpression:

- (BOOL)`adaptorChannel:`(id)_channel_`shouldEvaluateExpression:`(EOSQLExpression \*)_expression_

Invoked from [`evaluateExpression:`](../Classes/EOAdaptorChannel.md#apple-geydaoi) to tell the delegate that _channel_ is sending an expression to the database server. The delegate returns YES to permit the adaptor channel to send _expression_ to the server. If the delegate returns NO, the adaptor channel does not send the expression and returns immediately. When the delegate returns NO, the adaptor channel expects that the implementor of the delegate has done the work that [`evaluateExpression:`](../Classes/EOAdaptorChannel.md#apple-geydaoi) would have done. The delegate can create a new EOSQLExpression and send the expression itself before returning NO.

---

### adaptorChannel:shouldExecuteStoredProcedure:withValues:

- (NSDictionary \*)`adaptorChannel:`(id)_channel_`shouldExecuteStoredProcedure:`(EOStoredProcedure \*)_procedure_`withValues:`(NSDictionary \*)_values_

Invoked from [`executeStoredProcedure:withValues:`](../Classes/EOAdaptorChannel.md#apple-gyztona) to tell the delegate that _channel_ is executing a stored procedure. If the delegate returns a value other than `nil`, that value is used as the arguments to the stored procedure instead of _values_.

---

### adaptorChannel:shouldReturnValuesForStoredProcedure:

- (NSDictionary \*)`adaptorChannel:`(id)_channel_`shouldReturnValuesForStoredProcedure:`(NSDictionary \*)_returnValues_

Invoked from [`returnValuesForLastStoredProcedureInvocation`](../Classes/EOAdaptorChannel.md#apple-geydqnq) to tell the delegate that _channel_ is returning values for a stored procedure. If the delegate returns a value other than `nil`, that value is returned from [`returnValuesForLastStoredProcedureInvocation`](../Classes/EOAdaptorChannel.md#apple-geydqnq) instead of _returnValues_.

---

### adaptorChannel:shouldSelectAttributes:fetchSpecification:lock:entity:

- (BOOL)`adaptorChannel:`(id)_channel_`shouldSelectAttributes:`(NSArray \*)_attributes_`fetchSpecification:`(EOFetchSpecification \*)_fetchSpecification_`lock:`(BOOL)_flag_`entity:`(EOEntity \*)_entity_

Invoked from [`selectAttributes:fetchSpecification:lock:entity:`](../Classes/EOAdaptorChannel.md#apple-geydsma) to ask the delegate whether a select operation should be performed. The delegate should not modify _fetchSpecification_. Instead, if the delegate wants to perform a different select it should invoke [`selectAttributes:fetchSpecification:lock:entity:`](../Classes/EOAdaptorChannel.md#apple-geydsma) itself with a new fetch specification, and return NO (indicating that the adaptor channel should not perform the select itself).

---

### adaptorChannelWillFetchRow:

- (void)`adaptorChannelWillFetchRow:`(id)_channel_

Invoked from [`fetchRowWithZone:`](../Classes/EOAdaptorChannel.md#apple-gyztsni) to tell the delegate that a single row will be fetched. The delegate can determine the attributes used by the fetch by sending [`attributesToFetch`](../Classes/EOAdaptorChannel.md#apple-gq3dmmq) to _channel_, and can change the set of attributes to fetch by sending [`setAttributesToFetch:`](../Classes/EOAdaptorChannel.md#apple-geydsny) to _channel_. The adaptor channel performs the actual fetch.

---

### adaptorChannel:willPerformOperations:

- (NSArray \*)`adaptorChannel:`(id)_channel_ `willPerformOperations:`(NSArray \*)_operations_

Invoked from [`performAdaptorOperations:`](../Classes/EOAdaptorChannel.md#apple-geydomi) to tell the delegate that _channel_ is performing the EOAdaptorOperations in _operations_. The delegate may return _operations_ or a different NSArray for the adaptor channel to perform. If the delegate returns `nil`, the adaptor channel does not perform the operations and returns from the method immediately.

---

[!](NSString%20Additions.md)
[!](EOAdaptorContextDelegate.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
