---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/SybaseChannelDelegate.html
archived_at: '2026-07-18T01:28:50.173114Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](SybaseSQLExpression.md)
[!](SybaseContext.Delegate.md)

---

# SybaseChannel.Delegate

SybaseChannel delegate objects

__Inherits From:__
com.apple.yellow.sybaseeoadaptor

SybaseChannel's delegate methods used for processing compute rows and stored procedures give you access to the three types of non-regular rows supported by Sybase: compute rows, return parameters (from a stored procedure), and status from a stored procedure. Because the access layer can only handle regular table rows, the Sybase adaptor channel normally skips non-regular rows. However, you can use the delegate methods to intercept non-regular rows before they are skipped. These delegate methods are [`sybaseChannelWillFetchAttributes`](#apple-giydmny)and[`sybaseChannelWillReturnRow`](#apple-giytamy). The method [`sybaseChannelWillFetchAttributes`](#apple-giydmny) is invoked when a row is fetched, while [`sybaseChannelWillReturnRow`](#apple-giytamy) is invoked when a row is about to be returned. Based on the type of the row, the delegate can specify the appropriate behavior. This enables you to use data in one of the three non-regular row types and either extract the data from them or use the method __describeResults__  to return an array of attributes that describe the properties available in the current result set. Using __describeResults__  is appropriate if you're not concerned with format-for example, if you're just writing raw data to a report.

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

### sybaseChannelWillFetchAttributes

public abstract NSArray `sybaseChannelWillFetchAttributes`(SybaseChannel _channel_,
NSArray _attributes_,
int _rowType_,
int _computeRowId_)

Invoked whenever a row is fetched. The delegate can return __null__, which causes the row to be skipped, or can return a substitute set of attributes that is appropriate for the type of row being fetched. Delegates can have the channel fabricate a set of attributes for the current non-regular row by calling __describeResults__. See the interface introduction for a list of defined constants for _rowType_.

---

### sybaseChannelWillReturnRow

public abstract boolean `sybaseChannelWillReturnRow`(SybaseChannel _channel_,
NSDictionary _row_,
int _rowType_,
int _computeRowId_)

Invoked once a row has been read from the database and packaged into the dictionary. Delegates can return __true__ to cause the row to be returned from __fetchAttributes__, or they can return __false__ to cause the row to be skipped. See the interface introduction for a list of defined constants for _rowType_.

****

---

[!](SybaseSQLExpression.md)
[!](SybaseContext.Delegate.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
