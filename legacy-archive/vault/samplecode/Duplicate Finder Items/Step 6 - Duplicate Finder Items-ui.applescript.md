---
title: Duplicate Finder Items
apple_id: DTS10003717
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: null
published: '2005-06-06'
source_url: https://developer.apple.com/library/archive/samplecode/DuplicateFinderItems/Listings/Step_6___Duplicate_Finder_Items_ui_applescript.html
archived_at: '2026-07-18T03:07:24.433117Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Duplicate Finder Items](Duplicate%20Finder%20Items.md)


[Next](Document%20Revision%20History.md)[Previous](Step%206%20-%20Duplicate%20Finder%20Items-main.applescript.md)

# Step 6 - Duplicate Finder Items/ui.applescript

```
(*

File: ui.applescript

Abstract: User Interface Implementation for Duplicate Finder Items Automator action

Version: 1.0

Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
Computer, Inc. ("Apple") in consideration of your agreement to the
following terms, and your use, installation, modification or
redistribution of this Apple software constitutes acceptance of these
terms.  If you do not agree with these terms, please do not use,
install, modify or redistribute this Apple software.

In consideration of your agreement to abide by the following terms, and
subject to these terms, Apple grants you a personal, non-exclusive
license, under Apple's copyrights in this original Apple software (the
"Apple Software"), to use, reproduce, modify and redistribute the Apple
Software, with or without modifications, in source and/or binary forms;
provided that if you redistribute the Apple Software in its entirety and
without modifications, you must retain this notice and the following
text and disclaimers in all such redistributions of the Apple Software. 
Neither the name, trademarks, service marks or logos of Apple Computer,
Inc. may be used to endorse or promote products derived from the Apple
Software without specific prior written permission from Apple.  Except
as expressly stated in this notice, no other rights or licenses, express
or implied, are granted by Apple herein, including but not limited to
any patent rights that may be infringed by your derivative works or by
other works in which the Apple Software may be incorporated.

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

Copyright © 2005 Apple Computer, Inc., All Rights Reserved

*)

property contentview_reference : missing value

on awake from nib theObject
    set the contentview_reference to theObject
end awake from nib

on opened theObject
    update_example()
end opened

on clicked theObject
    update_example()
end clicked

on parameters updated theObject parameters theParameters
    set (the state of button "return duplicate items" of contentview_reference) to |returnDuplicateItems| of theParameters as integer
    update_example()
end parameters updated

on update_example()
    tell the contentview_reference
        if the state of button "return duplicate items" is 1 then
            set the display_example to my localized_string("Return duplicate items") as Unicode text
        else
            set the display_example to my localized_string("Return original items") as Unicode text
        end if
        set the content of text field "example" to (display_example)
    end tell
end update_example

on localized_string(key_string)
    return localized string key_string in bundle with identifier "com.yourcompany.Automator.Duplicate_Finder_Items"
end localized_string
```

[Next](Document%20Revision%20History.md)[Previous](Step%206%20-%20Duplicate%20Finder%20Items-main.applescript.md)

