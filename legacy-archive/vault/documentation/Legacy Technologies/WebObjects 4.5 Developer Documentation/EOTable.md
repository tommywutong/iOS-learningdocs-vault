---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOTable.html
archived_at: '2026-07-15T08:11:45.011326Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOTable

> **__Inherits
> from:__**
> : javax.swing.JScrollPane :
> javax.swing.JComponent :
> java.awt.Container :
> java.awt.Component :
> Object

> **__Implements:__**
> : NSDisposable

> **__Package:__**
> : com.apple.client.eointerface

---

## Class Description

---

The EOTable class is used to represent tables
of data. An EOTable object uses a JTable to do its work. As a subclass
of JScrollPane, an EOTable wraps its JTable in a scroll view and
adds the JTable's JTableHeader to the EOTable's column header.
If you want to configure or message an EOTable's JTable, you can
access the it with the method [jTable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dff5vfiylcnrsq).

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.yellow.eointerface package. |

## Interfaces Implemented

---

> NSDisposable: `dispose`

## Instance Methods

---

### debuggingHint

`public String debuggingHint()`

Returns the receiver's debugging
hint.

---

### jTable

`public javax.swing.JTable jTable()`

Returns the receiver's JTable.

---

### setDebuggingHint

`public void setDebuggingHint(String  hint)`

Sets the receiver's debugging
hint to  _hint._

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
