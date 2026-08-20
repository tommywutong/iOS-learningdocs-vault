---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/ManagingSchemes.html
archived_at: '2026-07-27T06:57:08.110094Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](UsingtheDebugger.md)[Previous](RunningonaDevice.md)

## Managing Schemes

To edit a scheme, choose Edit Scheme from the Scheme menu. The left column of the scheme configuration dialog lists the actions that the scheme can perform. You can modify settings for each action. In the screenshot, the Run action is modified to simulate the location of Mexico City when Xcode launches the app.

（原归档配图获取待重试：`scheme_options_2x.png`）

You can edit a scheme so that it performs such actions as:

- Building multiple targets
- Executing scripts before or after any action
- Sending emails before or after any action
- Running with memory management diagnostics
- Producing either a debug or release build for any action.

A convenient way to create a new scheme is to click the Duplicate Scheme button. This button uses the active scheme as a template for you to rename, edit, and save.

If you create schemes, you can manage them by clicking the Manage Schemes button in the scheme configuration dialog or by choosing Manage Schemes from the Scheme menu as shown in the screenshot below. You can rename or reorganize how schemes appear in the Scheme menu. You can also specify whether a scheme should be displayed in the menu, where a scheme is stored in the project or workspace, and whether a scheme should be shared, such as with team members accessing a project from a source code repository. You can click the Autocreate Schemes Now button to make Xcode create schemes for any targets that don’t have them.

（原归档配图获取待重试：`SchemeHelp_2x.png`）

Get step-by-step instructions for creating, editing, and managing schemes by pressing Control-click anywhere in the scheme configuration dialog, or see [Xcode Help](https://help.apple.com/xcode).

[Running on a Device](RunningonaDevice.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnjvfvjvomi)

[Using the Debugger](UsingtheDebugger.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnjxfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](UsingtheDebugger.md)[Previous](RunningonaDevice.md)
