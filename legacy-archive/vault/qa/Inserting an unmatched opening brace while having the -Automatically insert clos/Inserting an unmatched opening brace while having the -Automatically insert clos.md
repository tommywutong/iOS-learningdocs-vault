---
title: Inserting an unmatched opening brace while having the "Automatically insert
  closing '}'" feature enabled.
apple_id: DTS40009345
resource_type: QA
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2009-10-27'
source_url: https://developer.apple.com/library/archive/qa/qa1671/_index.html
archived_at: '2026-07-18T02:33:36.206965Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1671

# Inserting an unmatched opening brace while having the "Automatically insert closing '}'" feature enabled.

## Q:  I have Xcode's "Automatically insert closing '}'" feature enabled, but sometimes I want to insert an unmatched opening brace. How can I do this?

A: Xcode supports arbitrary shell scripting that you can use to insert text into the editor view. In this case, you can create a new shell script that echoes the opening brace, replacing the current selection, and then create a key binding for that script.

To create a new shell script, start by opening the User Scripts window.

__Figure 1__  Opening the User Scripts window:

!

Then add a new shell script using the "+" button in the bottom left corner.

__Figure 2__  Adding a script:

!

Initially the new script will not have a name or key binding, and the script contents will be as shown in Figure 3

__Figure 3__  New script:

!!

Give the script a name and bind it to a key combination of your choice, such as "Command-Control-[". Then complete the shell script and set the Input, Output, and other options as shown in Figure 4

__Figure 4__  The completed script:

!!

After you close the User Scripts window you can use the new key binding to insert an opening { that won't be matched by a closing brace.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-10-27 | New document that describes an Xcode shell script that inserts unmatched opening braces with the "Automatically insert closing '}'" feature enabled. |

