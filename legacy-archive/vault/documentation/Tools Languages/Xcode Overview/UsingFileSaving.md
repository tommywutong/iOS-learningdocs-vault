---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/UsingFileSaving.html
archived_at: '2026-07-27T06:57:08.190327Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](UsingUndo.md)[Previous](RecordingUITests.md)

## Using File Saving

Xcode automatically saves changes to source, project, and workspace files as you work. This feature requires no configuration, because Xcode continuously tracks your changes and saves them in memory. Xcode then writes these changes to disk whenever you:

- Build and run your app
- Commit files to a source code repository
- Close the project
- Quit Xcode

You can also manually save changes to disk by choosing File > Save.

Xcode lets you revert files and entire projects to a previous state; you can also discard those changes. You use source control management to keep track of changes at a fine-grained level.

### Reverting to the Last Saved Version of a File

To discard all changes you’ve made to a file since it was last saved to disk, choose File > Revert to Saved. The Revert to Saved command operates only on the file that has the editing focus. Give editing focus to a file either by clicking its editor pane or by selecting it in the project navigator. For example, you experiment with a new user interface layout and then decide to revert to the previous layout. Or you need to undo some code changes because they introduced a problem.

The Revert to Saved command always returns the contents of the file to the last saved version on disk. If you prefer to back out changes one change at a time, use the Undo command in the Edit menu.

[Recording UI Tests](RecordingUITests.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnzvfvjvomi)

[Using Undo](UsingUndo.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnrwfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](UsingUndo.md)[Previous](RecordingUITests.md)
