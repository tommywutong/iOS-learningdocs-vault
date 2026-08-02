---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/GuestBookPlus/GuestBookPlus1.html
archived_at: '2026-07-15T07:53:39.756688Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBookPlusTOC.md) [!Previous Section](GuestBookPlusTOC.md)

# Duplicating Your Project

Before proceeding, you'll create a new project by copying the old one and renaming it. This way, you can make changes and still retain your previous version.

- In WebObjects Builder, close the component window.
- In Project Builder, close GuestBook's project window.

If there are any unsaved files, you are prompted to save them.

- In your machine's file system, navigate to the directory where your project is located (the WebObjects directory under your server's document root).
!- Duplicate the GuestBook folder.

On Windows NT, you can do this by selecting the folder, choosing Edit!Copy, then Edit!Paste.

- Open the new folder (Copy of GuestBook) and double-click the project file __PB.project__.

Project Builder opens a new browser window for this project. (Alternatively, you could have opened the project from within Project Builder by choosing Project!Open, then navigating to the project folder and selecting __PB.project__.)

- Click ! from the toolbar to bring up the Project Build panel.
- Click ! in the Project Build panel.

This command deletes all the files that were generated when you built the project previously.

- Click ! to open the Project Inspector.
- Choose Project Attributes from the pop-up list at the top of the window.
- In the Name field, enter GuestBookPlus and press Enter.
- Respond Yes to the prompt that asks if you want to rename the folder.

You now have a new project called GuestBookPlus.

[!Table of Contents](GuestBookPlusTOC.md) [!Next Section](GuestBookPlus2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
