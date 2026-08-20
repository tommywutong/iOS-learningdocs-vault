---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/SybaseChannelDelegate.html
archived_at: '2026-07-18T01:28:50.647852Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](SybaseSQLExpression-2.md)
[!](SybaseContextDelegate.md)

---

# SybaseChannelDelegate

__Adopted By:__
SybaseChannel delegate objects

__Declared in:__
SybaseEOAdaptor/SybaseChannel.h

# Protocol Description

SybaseChannel's delegate methods used for processing compute rows and stored procedures give you access to the three types of non-regular rows supported by Sybase: compute rows, return parameters (from a stored procedure), and status from a stored procedure. Because the access layer can only handle regular table rows, the Sybase adaptor channel normally skips non-regular rows. However, you can use the delegate methods to intercept non-regular rows before they are skipped. These delegate methods are [`sybaseChannel:willFetchAttributes:forRowOfType:withComputeRowId:`](#apple-giydmny)and[`sybaseChannel:willReturnRow:ofType:withComputeRowId:`](#apple-giytamy). The method [`sybaseChannel:willFetchAttributes:forRowOfType:withComputeRowId:`](#apple-giydmny) is invoked when a row is fetched, while [`sybaseChannel:willReturnRow:ofType:withComputeRowId:`](#apple-giytamy) is invoked when a row is about to be returned. Based on the type of the row, the delegate can specify the appropriate behavior. This enables you to use data in one of the three non-regular row types and either extract the data from them or use the method __describeResults__  to return an array of attributes that describe the properties available in the current result set. Using __describeResults__  is appropriate if you're not concerned with format-for example, if you're just writing raw data to a report.

__Note:__
The regular rows in the results from a stored procedure must map to the attributes in the
corresponding entity, and must be in alphabetical order.

The SybaseChannel adaptor defines the following constants against which you can compare the returned row type:

- SybaseRegularRow
- SybaseComputeRow
- SybaseReturnParameterRow
- SybaseReturnStatusRow

---

## Instance Methods

---

### sybaseChannel:willFetchAttributes:forRowOfType:withComputeRowId:

- (NSArray \*)__sybaseChannel:__ (SybaseChannel \*)_channel___willFetchAttributes:__ (NSArray \*)_attributes___forRowOfType:__ (SybaseRowType)_rowType___withComputeRowId:__ (int)_computeRowId_

Invoked whenever a row is fetched. The delegate can return `nil`, which causes the row to be skipped, or can return a substitute set of attributes that is appropriate for the type of row being fetched. Delegates can have the channel fabricate a set of attributes for the current non-regular row by calling `describeResults`. See the protocol introduction for a list of defined constants for _rowType_.

For example, the following implementation checks the row type; if it's a regular row, it simply returns the attributes. If it's not a regular row type, __describeResults__  is used to return an array of attributes that describe the properties available in the current result set. Note that __describeResults__  always describes the current row type.

> ```
> - (NSArray *)sybaseChannel:(SybaseChannel *)channel
> willFetchAttributes:(NSArray *)attributes
> forRowOfType:(SybaseRowType)rowType
> withComputeRowId:(int)computeRowId
> {
> if (rowType == SybaseRegularRow)
> return attributes;
>
> attributes = [(EOAdaptorChannel *) channel describeResults];
> return attributes;
> }
> ```

---

### sybaseChannel:willReturnRow:ofType:withComputeRowId:

- (BOOL)__sybaseChannel:__ (SybaseChannel \*)_channel_
__willReturnRow:__ (NSDictionary \*)_row_
__ofType:__ (SybaseRowType)_rowType_
__withComputeRowId:__ (int)_computeRowId_

Invoked once a row has been read from the database and packaged into the dictionary. Delegates can return YES to cause the row to be returned from `fetchAttributes:WithZone:`, or they can return NO to cause the row to be skipped. See the protocol introduction for a list of defined constants for `rowType`.

For example, the following implementation checks each row type and uses __NSLog()__  to output a message describing the row's type. In this example all rows are returned, but you could use this template to selectively return or not return rows based on type.

> ```
> - (BOOL)sybaseChannel:(SybaseChannel *)channel
> willReturnRow:(NSDictionary *)row ofType:(SybaseRowType)rowType
> withComputeRowId:(int)computeRowId
> {
> switch (rowType) {
>     case SybaseRegularRow:
>         break;
>     case SybaseComputeRow:
>         NSLog(@"Returning compute row");
>         break;
>     case SybaseReturnParameterRow:
>         NSLog(@"Returning return parameter row");
>         break;
>     case SybaseReturnStatusRow:
>         NSLog(@"Returning return status row");
>         break;
> }
> return YES;
> }
> ```

****

---

[!](SybaseSQLExpression-2.md)
[!](SybaseContextDelegate.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
