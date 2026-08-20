---
title: Form Programming Topics
apple_id: 10000021i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2002-11-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Form/Tasks/ManagingFormEntries.html
archived_at: '2026-07-15T07:15:54.472129Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Form Programming Topics](Introduction%20to%20Forms.md)


[Next](Document%20Revision%20History.md)[Previous](Setting%20a%20Form%E2%80%99s%20Appearance.md)

# Managing Form Entries

NSForm has several methods for manipulating its entries. These methods dynamically add and remove entries:

- To add an entry, use `addEntry:` and `insertEntry:atIndex:`.
- To remove an entry, use `removeEntryAtIndex:`.

These methods find and select a particular entry:

- To get the index of the entry with a specified tag, use `indexOfCellWithTag:`.
- To get the index of the entry that contains the insertion point, use `indexOfSelectedItem`.
- To get the entry at a specified index, use `cellAtIndex:`
- To select all the text in a specified entry, `selectTextAtIndex:`.

[Next](Document%20Revision%20History.md)[Previous](Setting%20a%20Form%E2%80%99s%20Appearance.md)

