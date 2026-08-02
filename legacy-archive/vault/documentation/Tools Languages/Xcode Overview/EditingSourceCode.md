---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/EditingSourceCode.html
archived_at: '2026-07-27T06:57:07.949546Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](SearchandReplace.md)[Previous](AddingandOpeningFiles.md)

## Editing Source Code

### Fix Errors as You Type

As you type into the source editor, Xcode scans your text. When you make a syntax error, Xcode marks it with a red underline or a caret. Click the error, and Xcode displays a message describing the issue.

（原归档配图获取待重试：`FixItError_2x.png`）

Often, Fix-it offers to repair your error automatically. Select a suggested correction, and press Return to accept it. In the screenshot, Fix-it suggests inserting the “`@`” character before the text string. For more information, see Catching Mistakes with Fix-it.

### Speed Up Typing with Code Completion

When you begin typing the name of a symbol, Xcode offers inline suggestions for completing the name. Click an item in the suggestion list to select it, or use the Up Arrow and Down Arrow keys to change the selected suggestion. Press Return to accept the suggestion.

（原归档配图获取待重试：`CodeCompletion_2x.png`）

When a method or function contains parameters or arguments, code completion includes a placeholder for each. To move from one placeholder to another, choose Navigate > Jump to Next Placeholder (or Navigate > Jump to Previous Placeholder). Alternatively, Tab navigates to the next placeholder and Shift-Tab navigates to the previous one.

For more detail, see Entering Text with Code Completion.

### Match Pairs of Braces, Parentheses, and Brackets Automatically

Xcode helps you balance delimiters automatically. For example:

- Position the pointer over the focus ribbon on the left edge of the source editor. Xcode highlights the scope at that location, as shown in the previous screenshot.
- Type an opening brace. Xcode automatically inserts a closing brace after you enter a line break.
- Type a closing brace or other delimiter. Xcode briefly highlights its counterpart.
- Use the Right Arrow key to move the insertion point past a closing delimiter. Xcode briefly highlights its counterpart.
- Choose Editor > Structure > Balance Delimiter. Xcode selects the text surrounding the insertion point, including the nearest set of enclosing delimiters.
- Double-click any delimiter. Xcode selects the text enclosed by the delimiter and its counterpart.

For more detail, see Matching Pairs of Braces, Parentheses, and Brackets.

### Drop Code Snippets into Your Files

Use code snippets to enter source text with minimum effort. You can drag a code snippet directly from the Code Snippet library into a source file. To access Code Snippets, click the Code Snippet button (（原归档配图未能恢复：`XC_O_library_code_templates_button_2x.png`）) in the utilities area of the workspace window. The library provides useful standard snippets, such as the switch statement snippet shown in the screenshot. To add your own code snippets to the library, create your own snippets, and add shortcuts, see [Xcode Help](https://help.apple.com/xcode).

（原归档配图获取待重试：`Snippet_2x.png`）

### Use Gestures and Keyboard Shortcuts

Gestures and keyboard shortcuts can simplify and enhance your use of the source editor. Besides the common Multi-Touch gestures in OS X, these gestures are particularly applicable within the source editor:

- A two-finger click opens a contextual menu for the editor (as does Control-click or Left-click with the mouse).
- A two-finger swipe up or down scrolls vertically, and left or right scrolls horizontally.
- A two-finger swipe left or right navigates through any files opened in an editor. Swiping left shows the previous file, and swiping right shows the next file.

Keyboard sequences serve as shortcuts for many common menu commands in Xcode. For example, Shift-Command-O invokes the Open Quickly command from the File menu, and Shift-Command-J invokes the Jump to Definition command from the Navigate menu. Other keyboard shortcuts assist with editing operations. For example, Control-K deletes every character from the insertion point to the end of the line.

Keyboard shortcuts are established through key bindings, which you can view and modify by choosing Xcode > Preferences and selecting Key Bindings.

[Opening and Adding Files](AddingandOpeningFiles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmzvfvjvomi)

[Search and Replace](SearchandReplace.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmzwfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](SearchandReplace.md)[Previous](AddingandOpeningFiles.md)
