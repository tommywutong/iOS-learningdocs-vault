---
title: CustomGet unresolved alias
apple_id: DTS10000044
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-13'
source_url: https://developer.apple.com/library/archive/samplecode/CustomGet_unresolved_alias/Introduction/Intro.html
archived_at: '2026-07-18T03:05:33.561043Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](CustomGet%20unresolved%20alias.c.md)

# CustomGet unresolved alias

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-03-13 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon System 7.0 |

This sample demonstrates how to let the user choose an alias file from an "open" dialog. The basic idea is to intercept the pseudo- item 'sfHookOpenAlias' in a CustomGetFile hook function and transform it into 'getOpen'. This causes the dialog to behave as if the user had clicked the open button. Also, we intercept the item number of a check box we have added to the dialog item template in order to allow the user to choose whether to resolve aliases. Finally, when CustomGetFile returns, we call Alert to let the user know what happened. Requirements: System 7.0 Keywords: Standard File, CustomGetFile, choosing aliases

[Next](CustomGet%20unresolved%20alias.c.md)

