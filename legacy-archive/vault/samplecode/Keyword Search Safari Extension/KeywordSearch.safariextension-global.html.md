---
title: Keyword Search Safari Extension
apple_id: DTS40012648
resource_type: Sample Code
platform: Safari|macOS
topic: General
technology: null
published: '2012-06-10'
source_url: https://developer.apple.com/library/archive/samplecode/KeywordSearchSafariExtension/Listings/KeywordSearch_safariextension_global_html.html
archived_at: '2026-07-18T03:13:23.447996Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Keyword Search Safari Extension](Keyword%20Search%20Safari%20Extension.md)


[Next](Document%20Revision%20History.md)[Previous](ReadMe.txt.md)

# KeywordSearch.safariextension/global.html

```
<!--
    File: global.html
Abstract: Global Page HTML file.
 Version: 1.0

Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
Inc. ("Apple") in consideration of your agreement to the following
terms, and your use, installation, modification or redistribution of
this Apple software constitutes acceptance of these terms.  If you do
not agree with these terms, please do not use, install, modify or
redistribute this Apple software.

In consideration of your agreement to abide by the following terms, and
subject to these terms, Apple grants you a personal, non-exclusive
license, under Apple's copyrights in this original Apple software (the
"Apple Software"), to use, reproduce, modify and redistribute the Apple
Software, with or without modifications, in source and/or binary forms;
provided that if you redistribute the Apple Software in its entirety and
without modifications, you must retain this notice and the following
text and disclaimers in all such redistributions of the Apple Software.
Neither the name, trademarks, service marks or logos of Apple Inc. may
be used to endorse or promote products derived from the Apple Software
without specific prior written permission from Apple.  Except as
expressly stated in this notice, no other rights or licenses, express or
implied, are granted by Apple herein, including but not limited to any
patent rights that may be infringed by your derivative works or by other
works in which the Apple Software may be incorporated.

The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

Copyright (C) 2012 Apple Inc. All Rights Reserved.

-->

<!DOCTYPE html>
<script>
var keywordSearches = [
    { "keyword": "b", "query": "https://bugs.webkit.org/buglist.cgi?quicksearch={searchTerm}" },
    { "keyword": "t", "query": "http://trac.webkit.org/search?q={searchTerm}" },
    { "keyword": "d", "query": "https://developer.apple.com/search/index.php?q={searchTerm}" }
];

// By registering the listener at the SafariApplication level, ensure that the beforeSearchHandler
// will be invoked before a search is done in any tab in any window.
safari.application.addEventListener("beforeSearch", beforeSearchHandler, true);

function beforeSearchHandler(event)
{
    for (var i = 0; i < keywordSearches.length; ++i) {
        if (event.query.indexOf(keywordSearches[i].keyword + " ") != 0)
            continue;

        // Prevent the the default action for this event, which is to execute the search.
        event.preventDefault();

        // In the tab where the search was going to be executed, which is the target of the event,
        // navigate to the desired site and do the search there.
        event.target.url = keywordSearches[i].query.replace("{searchTerm}", escape(event.query.substring(keywordSearches[i].keyword.length + 1)));
        return;
    }
}
</script>
```

[Next](Document%20Revision%20History.md)[Previous](ReadMe.txt.md)

