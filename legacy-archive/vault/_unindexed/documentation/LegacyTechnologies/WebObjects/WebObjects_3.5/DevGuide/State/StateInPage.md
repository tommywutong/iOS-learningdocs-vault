---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/StateInPage.html
archived_at: '2026-07-15T07:52:21.815492Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](StateInServer.md)

### State in the Page

To store state in the page, you must do two things:

- Specify page session store as the application's state storage mechanism.
- Include a WOStateStorage element inside of a form on each page.

You specify the page session store this way:

```
    // Application.java
    public Application() {
        super();
        this.setSessionStore(SessionStore.pageSessionStore());
    }

    // Application.wos.
    - init {
        [super init];
        [self setSessionStore:[WOSessionStore pageSessionStore]];
        return self;
    }
```


Next, you must add a form to each page of the application and place a WOStateStorage object within the form. You do this in WebObjects Builder by adding a Custom WebObject to the form and then using the Inspector panel to specify that the type of element is "WOStateStorage".)
The WOStateStorage element maps to an HTML input element of type "hidden." The "hidden" input type contains text that is not displayed in the user's browser. For example, using state in the page, the HTML source for the Guess page of the SessionStores example would look something like this:

```
    <FORM METHOD=Post ACTION=someAction>
        Can you guess my favorite digit?<BR>
        <SELECT NAME="guesses">
            <OPTION>1
            <OPTION>2
            ...
            <OPTION>9
        </SELECT>
        <INPUT TYPE="hidden" NAME="hiddenState" VALUE="previousGuesses">
        <INPUT TYPE="submit" VALUE="Guess">
    </FORM>
```


When WebObjects generates a response page containing a WOSessionStore element, it packages the session state by archiving the session object-and consequently, all the component objects that it contains-using classes and methods defined in the Foundation framework. The session and components are archived into an NSData object. (In Java, NSData is called next.util.ImmutableBytes.) The NSData object is then asked for its ASCII representation, which is written into the HTML page as hidden fields. (See the class specification for NSArchiver in the _Foundation Framework Reference_ for more information on archiving.)
WebObjects writes as many hidden fields as are necessary to contain the state data.WOStateStorage's size attribute specifies the maximum size of each of these hidden fields (500 bytes in the example above). The size attribute is provided because browsers differ in the amount of text that they allow within a single hidden field. Most browsers have no problem with the default value for __size__ (1000 bytes).
When the user submits the HTML page to the server, the process is reversed. The application's page session store restores the session state by recombining the ASCII data it finds in the hidden fields into the original ASCII archive, converting the ASCII archive to its binary, NSData, representation, and then unarchiving the session object and its contents from the NSData object.
There are some limitations inherent in storing state in the page:

- __Forms are required.__ Because state is stored in an input element-which according to the HTML specification must exist within a form element-you must structure your application around forms. If you want session state to be available at any point in the application, each page of the application must have a form, and that form must contain a WOStateStorage element.

If a page has multiple forms, you must include the page state data in each form. If a form lacking this data is submitted, the application will no longer have the state information it needs.

- __Backtracking.__ Because each page carries a record of the state existing at the time of its creation, backtracking can make the page state and the actual state disagree. If, for example, the user make five guesses in the SessionStores example, backtracks two pages, and submits another guess, the application will claim that four guesses were made, when the actual number is six.
- __Frames.__ Storing state in the page is a problem if the "pages" in question are frames. Your state can quickly get out of sync. For example, suppose you have a mail application with two frames. One of the frames shows a list of messages with one message selected, and the other frame shows the text of the selected message. If you delete the message in the top frame, the state of the bottom frame isn't updated (unless you implement your own solution).
- __Archiving.__ Because WOStateStorage works by archiving the objects to be stored, only objects that can be archived using the Foundation framework's archiving mechanism can be stored. That is, the objects must conform to the NSCoding protocol (or the next.util.Coding interface in Java). For scripted objects, you don't need to worry about this. WebScript provides a default archiving implementation that will archive data stored in the object's instance variables. For compiled objects (whether Java or Objective-C), on the other hand, you have to implement the archiving methods yourself, as described in ["Storing State for Custom Objects"](StateForCustomObjects.md#apple-guzdqoa).

[!Table of Contents](StateTOC.md) [!Next Section](StateInCookies.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
