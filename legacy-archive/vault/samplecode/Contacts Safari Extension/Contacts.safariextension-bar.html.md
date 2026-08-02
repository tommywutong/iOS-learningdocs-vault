---
title: Contacts Safari Extension
apple_id: DTS40010123
resource_type: Sample Code
platform: Safari|macOS
topic: User Experience
technology: null
published: '2010-06-08'
source_url: https://developer.apple.com/library/archive/samplecode/ContactsSafariExtension/Listings/Contacts_safariextension_bar_html.html
archived_at: '2026-07-18T03:04:15.127779Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Contacts Safari Extension](Contacts%20Safari%20Extension.md)


[Next](Contacts.safariextension-global.html.md)[Previous](Contacts%20Safari%20Extension.md)

# Contacts.safariextension/bar.html

```
<!--
    File: bar.html
Abstract: Bar page HTML file.
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
<html>
<head>
    <script>
    // Function that is called from the global page to update the contacts select.
    function updateContacts()
    {
        // Get the global page's window, so we can access functions and data.
        var globalPageWindow = safari.extension.globalPage.contentWindow;

        // Get the global contacts array.
        var contacts = globalPageWindow.contacts;

        // Make sure the contacts array is defined, if it isn't then the global page
        // might not be loaded yet. The global page will call us when it does load.
        if (!contacts)
            return;

        // Get the select element that will be updated to show the contacts.
        // If the contacts element dosen't exist yet, then we were called by the
        // global page too early. We will be called again during the load event.
        var contactsSelect = document.getElementById("existing-contacts");
        if (!contactsSelect)
            return;

        // Remove all the existing options.
        contactsSelect.innerHTML = "";

        // Iterate over the contacts and make options for them.
        for (var i = 0; i < contacts.length; ++i) {
            var contact = contacts[i];

            // Make a new option to append to the select.
            var option = document.createElement("option");
            option.textContent = contact.name;
            option.value = contact.email;

            // Append the option to the select.
            contactsSelect.appendChild(option);
        }

        // Reset the selected option so nothing is selected.
        contactsSelect.selectedIndex = -1;
    }

    // Function that is called when a contact is selected from the select element.
    function emailContact(contactsSelect)
    {
        // Get the selected option.
        var selectedOption = contactsSelect.options[contactsSelect.selectedIndex];
        if (!selectedOption)
            return;

        // The value of the option is the email address to use.
        var emailAddress = selectedOption.value;

        // Tell the page to active tab to the email address. This will not change the page
        // the tab is showing, since it is not "http", but it will cause the URL to open in Mail.
        safari.self.browserWindow.activeTab.url = "mailto:" + emailAddress;

        // Reset the selected option so nothing is selected.
        contactsSelect.selectedIndex = -1;
    }

    // Function that is called when the Add Contact button is clicked.
    function createContact()
    {
        // Get the name element, make sure it isn't empty.
        var nameElement = document.getElementById("name");
        if (!nameElement.value)
            return;

        // Get the email element, make sure it isn't empty.
        var emailElement = document.getElementById("email");
        if (!emailElement.value)
            return;

        // Get the global page's window, so we can access functions and data.
        var globalPageWindow = safari.extension.globalPage.contentWindow;

        // Call the addContact function in the global page. This will cause
        // the contact to be added and all the bars will be updated.
        globalPageWindow.addContact(nameElement.value, emailElement.value);

        // Reset the name and email elements.
        nameElement.value = "";
        emailElement.value = "";
    }
    </script>
    <style>
    body {
        padding: 2px 7px;   
    }

    #existing-contacts {
        min-width: 125px;
    }

    #new-contact {
        margin-left: 2em;
    }

    #new-contact label {
        margin-right: 0.5em;
    }

    #new-contact input {
        width: 150px;
    }
    </style>
</head>
<body onload="updateContacts()">
    <label>Contacts: <select id="existing-contacts" onchange="emailContact(this)"></select></label>
    <span id="new-contact">
        <label>New Name: <input id="name"></label>
        <label>Email: <input id="email"></label>
        <button onclick="createContact()">Add Contact</button>
    </span>
</body>
</html>
```

[Next](Contacts.safariextension-global.html.md)[Previous](Contacts%20Safari%20Extension.md)

