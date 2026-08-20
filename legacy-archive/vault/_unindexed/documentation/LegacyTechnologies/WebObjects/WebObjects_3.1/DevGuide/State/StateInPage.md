---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/StateInPage.html
archived_at: '2026-07-15T07:47:53.515918Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](StateInServer.md)

# State in the Page

The HTML specification defines an input element of type "hidden" that's commonly used to pass state information back and forth between the client and server. The hidden field simply contains text that is not displayed in the user's browser. For example using state in the page, the HTML source for the Guess page of the SessionStores example would look something like this:

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

The hidden field carries the record of the user's previous guesses back and forth between the client and server for the duration of the game.

Through its page session store and WOStateStorage dynamic element, WebObjects makes it simple to use the page state storage mechanism, as you'll soon see. However, there are some limitations inherent in storing state in the page, as we can deduce from the code excerpt above:

- Since state is stored in an input element---which according to the HTML specification must exist within a form element---you must structure your application around forms. If you want session state to be available at any point in the application, each page of the application must have a form, and that form must contain a hidden field (or in the case of WebObjects, a WOStateStorage element, as discussed later).
- Each page carries a record of the state existing at the time of its creation, so backtracking can make the page state and the actual state disagree. For example, if the user make five guesses in the SessionStores example, backtracks two pages, and submits another guess, the application will claim that four guesses were made when the actual number is six.
- Storing state in the page is a problem if the "pages" in question are frames. Your state can quickly get out of sync. For example, suppose you have a mail application with two frames. One of the frames shows a list of messages with one message selected, and the other frame shows the text of the selected message. If you delete the message in the top frame, the state of the bottom frame isn't updated (unless you implement your own solution).
- If a page has multiple forms, you must include the page state data in each form. If a form lacking this data is submitted, the application will no longer have the state information it needs.

A WebObjects application can store state in the page by establishing the page session store as the application's state storage mechanism and by structuring its pages so that they each contain an HTML form and a WOStateStorage element.

You generally set the session storage type in the __init__ method of the application script (__Application.wos__):

```
- init {
    [super init];
    [self setSessionStore:[WOSessionStore pageSessionStore]];
    return self;
}
```

Next, you must add a form to each page of the application and place a WOStateStorage object within the form. For example, the HTML template of a page might look like this:

```
<WEBOBJECT NAME="FORM">
      <WEBOBJECT NAME = "STATE"></WEBOBJECT>
      <WEBOBJECT NAME = "NAME_FIELD"></WEBOBJECT><BR>
      <WEBOBJECT NAME = "SUBMIT_BUTTON"></WEBOBJECT><BR>
</WEBOBJECT>
```

The declarations file declares that the State element is a WOStateStorage dynamic element:

```
    STATE: WOStateStorage{ size = 500 };
```

(With WebObjects Builder, you embed a WOStateStorage element in a page by dragging a Custom element from the Palettes panel into the component window and then using the Inspector panel to specify that the type of the element is "WOStateStorage".)

When you run the application, WebObjects stores session state in the HTML page at the location specified by the WOStateStorage element. What happens is this: When WebObjects generates a page to return to the user, it packages the session state by archiving the session object---and consequently, all the component objects that it contains---into an NSData object. The NSData object is then asked for its ASCII representation, which is written into the HTML page as hidden fields.

WOStateStorage's __size__ attributes specifies the maximum size of each of these hidden fields (500 bytes in the example above). WebObjects writes as many hidden fields as necessary to accommodate the state data. The __size__ attribute is provided since browsers differ in the amount of text that they allow within a single hidden field. Most browsers have no problem with the default value of 1000 bytes.

When the user submits the HTML page to the server, the process is reversed. The application's page session store restores the session state by recombining the ASCII data it finds in the hidden fields into the original ASCII archive, converting the ASCII archive to its binary, NSData, representation, and then unarchiving the session object and its contents from the NSData object. (See the class specification for NSArchiver in the _Foundation Framework Reference_ for more information on archiving.)

One consequence of storing state in the page is that only objects that know how to archive themselves can be stored. For scripted objects, WebObjects provides a default archiving implementation that will archive data stored in the object's instance variables. For compiled objects, on the other hand, you have to implement the archiving methods yourself, as described in "[Storing State for Custom Objects](StateForCustomObjects.md)".

[!Table of Contents](ManagingState.book.md)
[!Next Section](StateInCookies.md)
