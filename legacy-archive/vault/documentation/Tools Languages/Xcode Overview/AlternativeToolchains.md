---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/AlternativeToolchains.html
archived_at: '2026-07-27T06:57:07.932700Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](AddingandOpeningFiles.md)[Previous](WorkingonRelatedProjects.md)

## Using Alternative Toolchains

Xcode supports using alternative toolchains instead of the default tools, such as toolchains downloaded from [Swift.org](https://swift.org/), for indexing, building, and debugging your projects.

> [!IMPORTANT]
>
> If you use an alternative toolchain, you might encounter regressions because the alternative tools won’t have been fully qualified by Apple for official release.

### Installing Alternative Toolchains

Alternative toolchains for Xcode are installed into either the top level library (/Library/Developer/Toolchains) or into a user library (~/Library/Developer/ Toolchains). Installing a toolchain into a user library makes it available only to that user, where installation into the top level library makes it available for all users who share accounts on that computer. For information on using alternative toolchains with Xcode Server, see [Create Bots to Perform Integrations](../../IDEs/Xcode%20Server%20and%20Continuous%20Integration%20Guide/ConfigureBots.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezteojsfvbuqojnknlte) in _[Xcode Server and Continuous Integration Guide](../../IDEs/Xcode%20Server%20and%20Continuous%20Integration%20Guide/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezteojs)_.

### Viewing and Managing Installed Toolchains

Alternative toolchains appear in the Toolchains pane of Components preferences. The Toolchains pane is only available when alternative toolchains are installed. Figure 12-1 shows the pane with one alternative toolchain.

__Figure 12-1__Components preferences Toolchains pane
（原归档配图未能恢复：`XC_O_toolchain_prefs_2x.png`）

In the Toolchains pane, you can:

- View installed alternative toolchains
- Switch between toolchains
- Verify the code signature of a toolchain
- Reveal the location of a toolchain in the Finder
- Delete an installed toolchain

### Viewing and Switching Toolchains

Each item in the Toolchains pane shows the name, version, origin, and size of the toolchain. For example, in Figure 12-1 the alternative toolchain is a development snapshot from Swift Open Source, and is 618 MB.

Xcode indicates that an alternative toolchain is selected by:

- Adding the alternative toolchain indicator (（原归档配图获取待重试：`XC_O_icon_toolchain_2x.png`）) to the activity view in the Workspace toolbar as shown in Figure 12-2
- Adding the name of the alternative toolchain to the About window
- Adding the name of the alternative toolchain to the Welcome window

__Figure 12-2__Alternative toolchain indicator
（原归档配图未能恢复：`XC_O_Toolbar_toolchain_button_2x.png`）

Clicking the alternative toolchain indicator opens the Toolchains pane of Components preferences.

Use the Toolchains pane of Components preferences to switch between installed alternative toolchains. For information on how to do this, see Switching Toolchains in Components Preferences Help.

### Verifying, Revealing, and Deleting Alternative Toolchains

Control-click on an installed toolchain to reveal the contextual menu seen in Figure 12-3. Alternatively, move the pointer over an item in the Toolchains pane and click on the Action button (（原归档配图未能恢复：`XC_O_icon_gear_2x.png`）) that appears.

Use the menu's commands to verify the toolchain's associated Code Signature, reveal the location of the toolchain in the file system, or delete the toolchain.

__Figure 12-3__Toolchain preferences contextual menu
（原归档配图未能恢复：`XC_O_toolchain_gear_shortcut_menu_2x.png`）

### Building, Running, and Debugging Apps with Alternative Toolchains

Xcode uses the selected toolchain to build, run, and debug your app. For example, you can use the development snapshots from [Swift.org](https://swift.org/) to build and run your app on OS X, on devices, or on simulators for iOS, tvOS, and watchOS.

> [!IMPORTANT]
>
> Executing playgrounds requires using the default Xcode toolchain.
>
> Apps uploaded to iTunes Connect must be built using the default toolchain.

[Working on Related Projects](WorkingonRelatedProjects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmztfvjvomi)

[Opening and Adding Files](AddingandOpeningFiles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmzvfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](AddingandOpeningFiles.md)[Previous](WorkingonRelatedProjects.md)
