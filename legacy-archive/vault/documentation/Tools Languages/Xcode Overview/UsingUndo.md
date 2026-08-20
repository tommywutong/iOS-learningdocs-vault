---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/UsingUndo.html
archived_at: '2026-07-27T06:57:08.195827Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](UsingSourceCodeControl.md)[Previous](UsingFileSaving.md)

## Using Undo

To back out changes to a file incrementally, choose Edit > Undo _change_. The Undo command is contextualized by your last operation. For example, the command appears as Undo Typing if you make an edit to an implementation file; the command changes to Undo Add Button if you add a button object to a storyboard.

With the Undo command, you can back out every change to a file since the start of your editing session. An editing session begins when you open a project and ends when you close the project. Xcode lets you undo _all_ the edits in that session, even those already saved to disk. (Note, however, that the Revert Document command clears the Undo history, and you cannot undo a revert operation.)

After you’ve chosen the Undo command, you can choose Edit > Redo to reverse the last undo operation.

[Using File Saving](UsingFileSaving.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnrvfvjvomi)

[Using Source Code Control](UsingSourceCodeControl.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnrxfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](UsingSourceCodeControl.md)[Previous](UsingFileSaving.md)
