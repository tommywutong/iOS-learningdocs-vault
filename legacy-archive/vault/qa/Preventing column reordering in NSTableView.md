---
title: Preventing column reordering in NSTableView
apple_id: DTS10004187
resource_type: QA
platform: macOS
topic: User Experience
technology: AppKit
published: '2007-01-24'
source_url: https://developer.apple.com/library/archive/qa/qa1503/_index.html
archived_at: '2026-07-18T02:31:39.693951Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1503

# Preventing column reordering in NSTableView

## Q:  How do I prevent a particular column from being reordered or moved in my `NSTableView`?

A: How do I prevent a particular column from being reordered or moved in my `NSTableView`?

You can prevent the moving of a column by implementing the `NSTableView` delegate method `tableView:mouseDownInHeaderOfTableColumn:` and responding to `NSTableViewColumnDidMoveNotification`. The method `tableView:mouseDownInHeaderOfTableColumn:` will prevent the first column from being dragged, and `tableViewColumnDidMove:` can be written to restore the original order of the columns if the user attempts to move any column to the left of column 0.

For example, assume the first `NSTableColumn` (column 0) identifier is set to "`FirstName`".

__Listing 1__  Block the `NSTableView` from dragging the first column using the `NSTableView` delegate method.

```objc
-(void)tableView: (NSTableView*)inTableView mouseDownInHeaderOfTableColumn:(NSTableColumn*)tableColumn {     if ([[tableColumn identifier] isEqualToString:@"FirstName"])     {         [inTableView setAllowsColumnReordering:NO];     }     else     {         [inTableView setAllowsColumnReordering:YES];     } }
```

In your `awakeFromNib` or `init` method use the following:

`[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(tableViewColumnDidMove:) name:NSTableViewColumnDidMoveNotification object:nil];`

__Listing 2__  Reorder the columns after a drag reorder by responding to `NSTableViewColumnDidMoveNotification`.

```objc
- (void)tableViewColumnDidMove:(NSNotification*)aNotification {     NSDictionary* userInfo = [aNotification userInfo];      // if the user tries to move the first column out, move it back     if ([[userInfo objectForKey:@"NSOldColumn"] intValue] == 0)     {          // temporarily stop listening to column moves to prevent recursion          [[NSNotificationCenter defaultCenter] removeObserver:self                 name:NSTableViewColumnDidMoveNotification object:nil];           // move the column          [tableView moveColumn:[[userInfo objectForKey:@"NSNewColumn"] intValue] toColumn:0];           // listen again for column moves          [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(tableViewColumnDidMove:)                 name:NSTableViewColumnDidMoveNotification object:nil];     }     // if the user tries to move a column in front of the first column, move it back      else if ([[userInfo objectForKey:@"NSNewColumn"] intValue] == 0)     {          // temporarily stop listening to column moves to prevent recursion          [[NSNotificationCenter defaultCenter] removeObserver:self                 name:NSTableViewColumnDidMoveNotification object:nil];            // move the column          [tableView moveColumn:0 toColumn:[[userInfo objectForKey:@"NSOldColumn"] intValue]];           // listen again for column moves          [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(tableViewColumnDidMove:)                 name:NSTableViewColumnDidMoveNotification object:nil];     } }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-01-24 | New document that demonstrates how to prevent column reordering of certain columns in NSTableView. |

