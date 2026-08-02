---
title: Contacts Safari Extension
apple_id: DTS40010123
resource_type: Sample Code
platform: Safari|macOS
topic: User Experience
technology: null
published: '2010-06-08'
source_url: https://developer.apple.com/library/archive/samplecode/ContactsSafariExtension/Listings/Contacts_safariextension_global_html.html
archived_at: '2026-07-18T03:04:15.292545Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Contacts Safari Extension](Contacts%20Safari%20Extension.md)


[Next](Read%20Me.txt.md)[Previous](Contacts.safariextension-bar.html.md)

# Contacts.safariextension/global.html

```
<!--
    File: global.html
Abstract: Global page HTML file.
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

Copyright (C) 2010 Apple Inc. All Rights Reserved.

-->
<!DOCTYPE HTML>
<script>
// This is data we want to share. Initialize it from settings,
// making an empty array if it doesn't exist yet.
var contacts = safari.extension.settings.contacts || [];

// Function that is called from the bars to add contacts.
function addContact(name, email)
{
    // Push a new contact onto the contacts array.
    contacts.push({name: name, email: email});

    // Store the contacts in settings so it will persist between launches.
    safari.extension.settings.contacts = contacts;

    // Tell all the bars to update.
    _updateBars();
}

// Function to update all the bars when changes are made. It is prefixed
// with an underscore to communicate that it is private. Since JavaScript
// does not have private functions, this is a good practice.
function _updateBars()
{
    var bars = safari.extension.bars;
    for (var i = 0; i < bars.length; ++i) {
        if (bars[i].identifier !== "contacts")
            continue;

        var barWindow = bars[i].contentWindow;
        if (typeof barWindow.updateContacts === "function")
            barWindow.updateContacts();
    }
}

// Update the bars here in case we get loaded after a bar, and the bar wouldn't have had
// access to the contacts array yet.
_updateBars();
</script>
```

[Next](Read%20Me.txt.md)[Previous](Contacts.safariextension-bar.html.md)

