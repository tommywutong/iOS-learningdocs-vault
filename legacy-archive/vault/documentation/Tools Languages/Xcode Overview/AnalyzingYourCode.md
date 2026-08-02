---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/AnalyzingYourCode.html
archived_at: '2026-07-27T06:57:07.971707Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](CustomizingtheEditor.md)[Previous](WorkingwithSymbols.md)

## Analyzing Your Code

### Examining the Structure of Your Code with Code Folding

You can more easily focus your attention on a particular method or function in source code by hiding the other parts of the source code. Choose Editor > Code Folding > Fold Methods & Functions. Navigate to the method you want to unfold and double-click the Ellipsis button to unfold the method. The screenshot shows the `configureConnectedGameControllers` method unfolded.

（原归档配图未能恢复：`CodeFolding_2x.png`）

Move the pointer into the focus ribbon on the left edge of the editor to display a scope—such as the `for` statement in the screenshot—in a focus box. Additional scopes are indicated by degrees of shading in the code.

For more detail, see Folding and Unfolding Source Code.

### Performing Static Code Analysis

Use the static analyzer to find bugs in your code before you even run your app. The static analyzer tries out thousands of possible code paths in a few seconds, reporting potential bugs that might have remained hidden or bugs that might be nearly impossible to replicate. This process also identifies areas in your code that don’t follow recommended API usage, such as Foundation, UIKit, and AppKit idioms.

To perform static code analysis, choose Product > Analyze. The Xcode static analyzer parses the project source code and identifies these types of problems:

- Logic flaws, such as accessing uninitialized variables and dereferencing null pointers
- Memory management flaws, such as leaking allocated memory
- Dead store (unused variable) flaws
- API usage flaws that result from not following the policies required by the frameworks and libraries the project is using

The static analyzer reports problems in the issue navigator, available by clicking the Issue Navigator button ![image: ../art/XC_O_navigator_issue_button_2x.png](attachments/Art/XC_O_navigator_issue_button_2x.png) in the project navigator bar. Select an analyzer message in the issue navigator to display the associated code in the source editor. Click the corresponding message in the source editor. Use the pop-up menu in the analysis results bar above the source code editor to study the flow path of the flaw. Then edit the code to fix the flaw.

For more detail, see Performing Static Code Analysis in _Xcode Help_.

[Working with Symbols](WorkingwithSymbols.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmzxfvjvomi)

[Customizing the Editor](CustomizingtheEditor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmzzfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](CustomizingtheEditor.md)[Previous](WorkingwithSymbols.md)
