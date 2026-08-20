---
title: AutomatorHandsOn
apple_id: DTS10004384
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: Automator
published: '2007-06-12'
source_url: https://developer.apple.com/library/archive/samplecode/AutomatorHandsOn/Listings/Put_Contents_in_User_Library_Automator_Find_Images_by_Keyword_action_Contents_Resources_main_command.html
archived_at: '2026-07-18T03:01:37.090027Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AutomatorHandsOn](AutomatorHandsOn.md)


[Next](Select%20Images%20%28completed%29-PhotoBrowserItem.h.md)[Previous](Find%20Images%20by%20Keyword-main.command.md)

# Put Contents in User Library/Automator/Find Images by Keyword.action/Contents/Resources/main.command

```sh
#!/usr/bin/env sh

# main.command
# Find Images by Keyword

#  Created by Otto on 6/6/07.
#  Copyright 2007 Apple, Inc. All rights reserved.

while read fldrPath; do
    mdfind -onlyin "$fldrPath" "(kMDItemContentType == 'public.jpeg' || kMDItemContentType == 'public.tiff' || kMDItemContentType == 'public.png') && kMDItemKeywords == '${keywordString}'"
    echo
done
```

[Next](Select%20Images%20%28completed%29-PhotoBrowserItem.h.md)[Previous](Find%20Images%20by%20Keyword-main.command.md)

