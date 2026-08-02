---
title: AppleScript Studio Programming Guide
apple_id: TP30000889
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2011-01-07'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/StudioBuildingApps/chapter10/studio_write_code.html
archived_at: '2026-07-15T05:20:37.673705Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Studio Programming Guide](Introduction%20to%20AppleScript%20Studio%20Programming%20Guide.md)


[Next](Mail%20Search%20Tutorial-%20Build%20and%20Test%20the%20Application.md)[Previous](Mail%20Search%20Tutorial-%20Connect%20the%20Interface.md)

# Mail Search Tutorial: Write the Code

In this chapter you’ll write the scripts and handlers for Mail Search, an AppleScript Studio application that searches for specified text in messages in the Mac OS X Mail application. You’ll also build and test the completed application. To do this, you’ll perform the steps described in the following sections:

1. [Define Global Variables and Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkcineumrsjijfa).
2. [Write Event Handlers for the Interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkukbmferkgge2tm).
3. [Write Scripts and Additional Handlers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkukbmferkgge2to).

This chapter assumes you have completed previous Mail Search tutorial chapters.

The Mail Search tutorial chapters in this document contain listings for most of the handlers and script objects the application uses, and you can find a complete listing in [Chapter 10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkukbmferkggeydc). However, both for convenience and completeness, it is recommended that you obtain script statements by copying them from the Mail Search sample application distributed with AppleScript Studio.

Look for the file `Mail Search.applescript` in the Mail Search project folder. See [AppleScript Studio Sample Applications](About%20AppleScript%20Studio.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2dslkdjjbeuqsgifaq) for information on where to find the sample applications.

You should also read the section [Switching Between AppleScript Studio and Script Editor](Programming%20With%20AppleScript%20Studio.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tclkciffeorskjfea) before beginning this tutorial.

In [Plan the Code](Mail%20Search%20Tutorial-%20Design%20the%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tilkcineuossbjjbq), you identified a handful of global variables and properties Mail Search makes available to all its scripts and handlers. The one global variable is a global list to keep track of instances of the controller script. Each controller script handles search operations for one search window. You define this global variable as shown in Listing 9-1 and place it at the top of the script file `Mail Search.applescript`.

__Listing 9-1__  Global list variable to store instances of controller script

```
(*==== Globals ====*)

global controllers
```

Mail Search uses two global properties, a counter to keep track of the number of open windows and a boolean to keep track of whether the status panel nib file has been opened. You define these properties as shown in Listing 9-2 and place them at the top of the script file `Mail Search.applescript`, below the global variable you just defined.

__Listing 9-2__  Properties used in Mail Search

```
(*==== Properties ====*)

property windowCount: 0
property statusPanelNibLoaded: false
```


In [Plan the Code](Mail%20Search%20Tutorial-%20Design%20the%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tilkcineuossbjjbq), you identified event handlers for objects in Mail Search’s interface that must respond to user actions or changes in application state (pending or completed). For example, the search window has three handlers: `became main`, called when the window becomes active; `will open`, called as the window is about to open, and `will close`, called when the window is about to close. The find button has one handler, `clicked`, called when a user clicks the button.

In [Connect the Interface](Mail%20Search%20Tutorial-%20Connect%20the%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tmlkukbmferkgge2tk), you hooked up objects in the interface to the required handlers. As part of that step, Interface Builder inserted event handler declarations in the file `Mail Search.applescript`. In this section, you’ll write script statements for those handlers.

When planning the code, you also specified additional scripts and handlers to carry out operations such as searching, displaying results, and displaying status. You’ll write those scripts and handlers in [Write Scripts and Additional Handlers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkukbmferkgge2to). The handlers you’ll write in this section don’t do much except call other handlers, so you won’t be able to build and run the application until you’ve completed both sections (though you can compile `Mail Search.applescript` to check syntax).

While this approach may be suitable for simple applications—or for a tutorial, where the end result is already known—it’s not recommended for complex, real-world applications. For those applications, you will most likely work incrementally, adding parts of the interface, connecting them to event handlers, and testing individual scripts and handlers as you create them.

As a workaround to allow you to continue to build the application, you can add empty versions of the handlers you haven’t implemented yet to the script file. And as always, you can put `display dialog` statements in the stubbed out handlers to show when they are called.

Position each of the event handlers described here at the beginning of the script file `Mail Search.applescript`, just after the global variables and properties defined earlier.

Before working on this section, be sure you’ve read the section [Obtaining the Code for the Mail Search Tutorial](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkukbmferkggiytq).

You previously connected a `will finish launching` handler for the application object. That handler is called after the application’s user interface has been unarchived from its nib files and just before the application enters its main event loop. In that handler, Mail Search can do any additional initialization it requires before a user performs any actions.

The only initialization Mail Search requires is to set the global `controllers` variable to an empty list, as shown in Listing 9-3.

__Listing 9-3__  The `will finish launching` handler for the application object

```
on will finish launching theObject
    set controllers to {}
end will finish launching
```


You previously connected three handlers for the application.search window: `will open`, `became main`, and `will close`.

The `will open` handler is called after a window has been created from a nib file and before the window opens. At this point, Mail Search can do any additional initialization for the window. The handler is shown in Listing 9-4.

__Listing 9-4__  `will open` handler for search window

```
on will open theObject
    set theController to makeController(theObject)
    if theController is not equal to null then
        addController(theController)
        tell theController to initialize()
    end if
end will open
```

The `will open` handler performs these operations:

1. It calls `makeController` to create a controller for the window. The controller is a script that responds to user actions in the window.
2. If `makeController` successfully returns a controller, the `will open` handler adds the controller to the global list of controllers, then tells the controller to initialize itself.

The `became main` handler is called when a window becomes the current window. It’s similar to what you might be familiar with as an activate event—an event a window receives when it needs to present itself as the active window. The handler is shown in Listing 9-5.

__Listing 9-5__  The `became main` handler for the search window

```
on became main theObject
    set theController to controllerForWindow(theObject)
    if theController is not equal to null then
        tell theController to loadMailboxes()
    end if
end became main
```

The `became main` handler performs these operations:

1. It calls `controllerForWindow` to get the controller for the window. The controller should have been created during a previous call to `will open`.
2. If `controllerForWindow` successfully returns a controller, the `became main` handler calls the controller’s `loadMailboxes` handler (shown in [Listing 9-12](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkcineuqqkii5cq)) to search the Mail application for all available mailboxes and display them in the Mailboxes outline view.

The `will close` handler is called before a window closes. At this point, Mail Search can do any cleanup for the window. The only cleanup Mail Search requires is to remove window’s controller from the global list of controllers, as shown in Listing 9-6.

__Listing 9-6__  The `will close` handler for the search window

```
on will close theObject
    removeController(theObject)
end will close
```


You previously connected an `action` handler for the search text field object. That handler is called when a user presses the Return key. The handler is shown in Listing 9-7.

__Listing 9-7__  The `action` handler for the search text field

```
on action theObject
    set theController to controllerForWindow(window of theObject)
    if theController is not equal to null then
        tell theController to find()
    end if
end action
```

The `action` handler performs these operations:

1. It calls `controllerForWindow` to get the controller for the window.
2. If `controllerForWindow` successfully returns a controller, the `action` handler calls the controller’s `find` handler (shown in [Listing 9-16](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkcineukssgjfba)) to search for the specified text in messages in the selected mailboxes (and display any matching messages in the Messages table view).

You previously connected a `clicked` handler for the find button object. That handler is called when a user clicks the find button. The handler is shown in Listing 9-8.

__Listing 9-8__  The `clicked` handler for the find button

```
on clicked theObject
    set theController to controllerForWindow(window of theObject)
    if theController is not equal to null then
        tell theController to find()
    end if
end clicked
```

The `clicked` handler is virtually identical to the `action` handler described in [Text Field Handler](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkcineukrshizaq):

1. It calls `controllerForWindow` to get the controller for the window.
2. If `controllerForWindow` successfully returns a controller, the `clicked` handler calls the controller’s `find` handler (shown in [Listing 9-16](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkcineukssgjfba)) to search for the specified text in messages in the selected mailboxes (and display any matching messages in the Messages table view).

You previously connected a `double clicked` handler for the Messages table view object. That handler is called when a user double-clicks a selected message in the table. The handler is shown in Listing 9-9.

__Listing 9-9__  The `double clicked` handler for the search results table view

```
on double clicked theObject
    set theController to controllerForWindow(window of theObject)
    if theController is not equal to null then
        tell theController to openMessages()
    end if
end double clicked
```

The `double clicked` handler performs these operations:

1. It calls `controllerForWindow` to get the controller for the window.
2. If `controllerForWindow` successfully returns a controller, the `double clicked` handler calls the controller’s `openMessages` handler (shown in [Listing 9-18](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkcineusr2ejfbq)) to open the selected message (or messages) in a separate window.

In [Plan the Code](Mail%20Search%20Tutorial-%20Design%20the%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tilkcineuossbjjbq), you identified handlers for objects in Mail Search’s interface that must respond to user actions or changes in application state (pending or completed). In [Connect the Interface](Mail%20Search%20Tutorial-%20Connect%20the%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tmlkukbmferkgge2tk), you hooked up objects in the interface to the required handlers. Then you wrote the event handlers, in [Write Event Handlers for the Interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkukbmferkgge2tm).

When planning the code, you also specified additional scripts and handlers to carry out operations such as searching, displaying results, and displaying status. In this section, you’ll write those scripts and handlers. As mentioned previously, you won’t be able to build and run the application until you’ve completed this section, though you can compile `Mail Search.applescript` to check syntax.

Before working on this section, be sure you’ve read the section [Obtaining the Code for the Mail Search Tutorial](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkukbmferkggiytq).

Mail Search defines a controller script to perform tasks associated with the search window, including finding and displaying mailboxes, and finding and displaying messages that match the current search criteria. You specified the properties and handlers for this script in [The Controller Script](Mail%20Search%20Tutorial-%20Design%20the%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tilkukbmferkggiydg). In this section, you’ll look at the actual script and the handlers it contains. The controller script is defined in the `makeController` handler. All of the controller’s properties and handlers shown here are defined in that handler, which is listed in full in [Chapter 10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkukbmferkggeydc).

The controller script is defined in the `makeController` handler, which is described in [Write Handlers for Working With Controllers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkcineuersiirfa). The script defines and initializes properties for several things it needs to keep track of:

- `theWindow:` a reference to its window
- `theStatusPanel:` a reference to a status panel
- `foundMessages:` a list of found messages
- `mailboxesLoaded:` a boolean for whether it has created a list of available mailboxes

Listing 9-10 shows the definitions for these properties.

__Listing 9-10__  Properties of the controller script

```
        property theWindow : forWindow
        property theStatusPanel : null
        property foundMessages : {}
        property mailboxesLoaded : false
```

The value for the `theWindow` property, `forWindow`, is passed to the `makeController` handler.

The controller script initialization handler sets up columns in the data handlers that provide data for the mailboxes and messages views in the search window. This handler is shown in Listing 9-11.

__Listing 9-11__  The controller script’s `initialize` handler

```
        on initialize()
            -- Add a column to the mailboxes data source
            tell scroll view "mailboxes" of split view 1 of theWindow
                make new data column at the end of the data columns of data source ¬
                    of outline view "mailboxes" with properties {name:"mailboxes"}
            end tell

            -- Add the columns to the messages data source
            tell scroll view "messages" of split view 1 of theWindow
                make new data column at the end of the data columns of data source ¬
                    of table view "messages" with properties {name:"from"}
                make new data column at the end of the data columns of data source ¬
                    of table view "messages" with properties {name:"subject"}
                make new data column at the end of the data columns of data source ¬
                    of table view "messages" with properties {name:"mailbox"}
            end tell

            set windowCount to windowCount + 1
        end initialize
```

The `initialize` handler performs the following steps:

1. It adds a mailboxes column with the name “mailboxes” to the data source of the Mailboxes outline view. The data source supplies the outline view with the data to display (account and mailbox names).
2. Similarly, it adds columns for “from”, “subject”, and “mailbox” to the data source of the Messages table view. The data source supplies the table view with the data to display (from names, subject lines, and mailbox names).

This section describes the handlers in the controller script Mail Search uses to find and display mailboxes in the search window. The jumping off point for displaying mailboxes is the `loadMailboxes` handler, shown in Listing 9-12. It is called from the `became main` handler, shown in [Listing 9-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkcineusrkeijba), to ensure that whenever a window is activated it displays the available mailboxes. The `loadMailboxes` handler is responsible for loading all available mailboxes from all available accounts, if they have not already been loaded, and for showing the status dialog while loading.

The logic for the process of loading mailboxes is as follows:

1. `loadMailboxes` kicks off the process by calling `addMailBoxes`.
2. Mailboxes can reside in any account, so for each account, `addMailBoxes` calls `addAccount`.
3. For each mailbox the account contains, `addAccount` calls `addMailbox`.
4. `addAccount` adds the mailbox to the outline view of mailboxes available to search.

__Listing 9-12__  The controller script’s `loadMailboxes` handler

```
        on loadMailboxes()
            if not mailboxesLoaded then
                -- Open the status panel
                set theStatusPanel to makeStatusPanel(theWindow)
                tell theStatusPanel to openPanel("Looking for Mailboxes...")

                -- Add the mailboxes
                addMailboxes()

                -- Close the status panel
                tell theStatusPanel to closePanel()

                set mailboxesLoaded to true
            end if
        end loadMailboxes
```

The `loadMailboxes` handler performs the following steps:

1. If the mailboxes have already been loaded, it does nothing. Otherwise it performs the following steps.
2. It calls the `makeStatusPanel` handler to create a status dialog script object, and stores a reference to it in the `theStatusPanel` property. The `makeStatusPanel` handler is described in [Write Handlers for Working With the Status Dialog](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkukbmferkggiytk).
3. It calls the `openPanel` handler of the status dialog script object to start displaying the dialog, with the message “Looking for Mailboxes...” The `openPanel` handler is described in [The Status Dialog Script](Mail%20Search%20Tutorial-%20Design%20the%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tilkukbmferkggiydi).
4. It calls the controller handler `addMailboxes` to get all available mailboxes in all available accounts.
5. On completion of the previous step, it closes the status dialog.
6. It sets the controller property `mailboxesLoaded` to `true` (so it won’t load the mailboxes if they’ve already been loaded).

The `addMailboxes` handler is shown in Listing 9-13. It is called from the `loadMailboxes` handler, shown in Listing 9-12. The `addMailboxes` handler is responsible for iterating over all available accounts to obtain their mailboxes.

__Listing 9-13__  The controller script’s `addMailboxes` handler

```
        on addMailboxes()
            tell application "Mail"
                set accountIndex to 0
                repeat with a in (get accounts)
                    try
                        set accountIndex to accountIndex + 1
                        my addAccount(a, accountIndex, account name of a)
                    end try
                end repeat
            end tell
        end addMailboxes
```

The `addMailboxes` handler performs the following steps:

1. It targets the Mail application.
2. It gets a list of all accounts from the application.
3. It uses a repeat statement to iterate over the accounts.
4. For each account, it calls the controller handler `addAccount` (shown in Listing 9-14), passing among other things the name of the account.

   Within the `tell application "Mail"` statement block, the `addMailboxes` handler uses the term `my addAccount` to specify that it is calling another handler in the controller script.

The `addAccount` handler (shown in Listing 9-14) is called from the `addMailboxes` handler (shown in Listing 9-13). The `addAccount` handler is responsible for getting all available mailboxes in the passed account and adding them to the data source for the mailboxes view in the search window.

__Listing 9-14__  The controller script’s `addAccounts` handler

```
        on addAccount(a, accountIndex, accountName)
            -- Add a new item
            set accountItem to make new data item at the end of the data items ¬
                of data source of outline view "mailboxes" ¬
                of scroll view "mailboxes" of split view 1 of theWindow
            set name of data cell 1 of accountItem to "mailboxes"
            set contents of data cell 1 of accountItem to accountName
            set associated object of accountItem to accountIndex

            -- Add the mail boxes
            tell application "Mail"
                set mailboxIndex to 0
                repeat with m in (get mailboxes of a)
                    try
                        set mailboxIndex to mailboxIndex + 1
                        my addMailbox(accountItem, accountName, mailboxIndex, ¬
                            mailbox name of m)
                    end try
                end repeat
            end tell
        end addAccount
```

The `addAccount` handler performs the following steps:

1. It adds an account item to the data source for the mailboxes view in the search window. It also sets various information for the item, including its name (the name of the account).
2. It targets the Mail application.
3. It gets a list of all mailboxes in the account from the application.
4. It uses a repeat statement to iterate over the mailboxes.
5. For each mailbox, it calls the controller handler `addMailbox` (shown in Listing 9-15), passing among other things the name of the mailbox, to add the mailbox to the data source for the mailboxes view in the search window.

The `addMailbox` handler is called from the `addAccount` handler, shown in Listing 9-14, to add a single mailbox to the data source for the mailboxes view in the search window. The `addMailbox` handler is shown in Listing 9-15.

__Listing 9-15__  The controller script’s `addMailbox` handler

```
        on addMailbox(accountItem, accountName, mailboxIndex, mailboxName)
            -- Add a new item
            set mailboxItem to make new data item at the end of the data items ¬
                of accountItem
            set name of data cell 1 of mailboxItem to "mailboxes"
            set contents of data cell 1 of mailboxItem to mailboxName
            set associated object of mailboxItem to mailboxIndex
        end addMailbox
```

The `addMailboxes` handler performs the following step:

1. It adds a mailbox item to the data source for the mailboxes view in the search window. It also sets various information for the item, including its name (the name of the mailbox).

This section describes the handlers in the controller script Mail Search uses to find and display messages in the search window. Only messages in the specified mailboxes that contain the specified text in the specified part of the message are displayed.

The jumping off point for finding messages is the `find` handler. It is called from the `clicked` handler for the find button, shown in [Listing 9-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkcineukr2eijdq) and the `action` handler for the search text field, shown in [Listing 9-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkcineuir2hjfca). The `find` handler is responsible for gathering the search criteria, searching the selected mailboxes for matching messages, and displaying any such messages that are found. It also displays various status messages during the search. The `find` handler is shown in Listing 9-16

__Listing 9-16__  The controller script’s `find` handler

```
        on find()
            -- Get what and where to find
            set whatToFind to contents of text field "what" of theWindow
            set whereToFind to title of current menu item of popup button "where" ¬
                of theWindow

            -- Make sure that we have something to find
            if (count of whatToFind) is greater than 0 then
                -- Clear any previously found messages
                clearMessages()

                -- Setup a status panel
                set theStatusPanel to makeStatusPanel(theWindow)
                tell theStatusPanel to ¬
                    openPanel("Determining the number of messages...")

                try
                    -- Determine the mailboxes to search
                    set mailboxesToSearch to selectedMailboxes()

                    -- Determine the total number of messages to search
                    set totalCount of theStatusPanel to ¬
                        countMessages(mailboxesToSearch)

                    -- Adjust the status panel
                    tell theStatusPanel to adjustPanel()

                    -- Find the messages
                    set foundMessages to findMessages(mailboxesToSearch, ¬
                        whereToFind, whatToFind)

                    -- Change the status panel
                    tell theStatusPanel to changePanel("Adding found messages...")

                    -- Add the found messages to the result table
                    addMessages(foundMessages)

                    -- Close the status panel
                    tell theStatusPanel to closePanel()
                on error errorText
                    tell theStatusPanel to closePanel()
                    display alert "AppleScript Error" as critical ¬
                        attached to theWindow message errorText
                end try
            else
                display alert "Missing Value" as critical attached to theWindow ¬
                    message "You need to enter a value to search for."
            end if
        end find
```

The `find` handler performs the following steps:

1. It gets the search criteria: the contents of the search text field (the “what” field) and the title of the location pop-up (the “where” menu).
2. If there is no search text, it displays an error message “Missing Value”. Otherwise it performs the following steps.
3. It calls the controller handler `clearMessages` to clear any previous found messages in the Messages table view.
4. It calls the `makeStatusPanel` handler to create a status dialog script object, and stores a reference to it in the `theStatusPanel` property. The `makeStatusPanel` handler is described in [Write Handlers for Working With the Status Dialog](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkukbmferkggiytk).
5. It calls the `openPanel` handler of the status dialog script object to start displaying the panel, with the message “Determining the number of messages...” The `openPanel` handler is described in [The Status Dialog Script](Mail%20Search%20Tutorial-%20Design%20the%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tilkukbmferkggiydi).
6. It sets up an error handler (a `try…on error…end try` statement) around the statements that search for and display messages. If an error occurs, the `on error` clause closes the status dialog and displays an error message. Within the handler, it performs these steps:

   1. It calls the controller handler `selectedMailboxes` to get the selected mailboxes.
   2. It calls the controller handler `countMessages` to set the total count property of the status dialog to the total number of messages to search.
   3. It calls the `adjustPanel` handler of the status dialog script object to display the number of the messages to be searched. The `adjustPanel` handler is described in [The Status Dialog Script](Mail%20Search%20Tutorial-%20Design%20the%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tilkukbmferkggiydi).
   4. It calls the controller handler `findMessages` (shown in Listing 9-17), passing the mailboxes to search, the search location, and the text to find.
   5. It calls the `changePanel` handler of the status dialog script object to display the message “Adding found messages...” The `changePanel` handler is described in [The Status Dialog Script](Mail%20Search%20Tutorial-%20Design%20the%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tilkukbmferkggiydi).
   6. It calls the controller handler `addMessages`, to display the found messages in the search window’s message view.
   7. It closes the status dialog.

The `findMessages` handler is shown in Listing 9-17. It is called from the `find` handler, shown in Listing 9-16. The `findMessages` handler is responsible for iterating over the specified mailboxes and finding any messages that contain the specified text in the specified location (From, To, or Contents of the message).

__Listing 9-17__  The controller script’s `findMessages` handler

```
on findMessages(mailboxesToSearch, whereToFind, whatToFind)
    -- Initialize the result
    set messagesFound to {}

    tell application "Mail"
        -- Search through each of the mail boxes
        repeat with b in (get mailboxesToSearch)
            try
                -- Search through each of the messages of the mail box
                repeat with m in (get messages of b)
                    try
                        if whereToFind is equal to "Subject" then
                            if whatToFind is in the subject of m then
                                copy m to end of messagesFound
                            end if
                        else if whereToFind is equal to "From" then
                            if whatToFind is in sender of m then
                                copy m to end of messagesFound
                            end if
                        else if whereToFind is equal to "To" then
                            set foundRecipient to false

                            -- Recipients
                            repeat with r in (get recipients of m)
                                if whatToFind is in address of r or whatToFind ¬
                                        is in display name of r then
                                    set foundRecipient to true
                                end if
                            end repeat

                            -- To Recipients
                            if not foundRecipient then
                                repeat with r in (get to recipients of m)
                                    if whatToFind is in address of r or whatToFind ¬
                                            is in display name of r then
                                        set foundRecipient to true
                                    end if
                                end repeat
                            end if

                            -- cc Recipients
                            if not foundRicipient then
                                repeat with r in (get cc recipients of m)
                                    if whatToFind is in address of r or whatToFind ¬
                                            is in display name of r then
                                        set foundRecipient to true
                                    end if
                                end repeat
                            end if

                            -- bcc Recipients
                            if not foundRicipient then
                                repeat with r in (get bcc recipients of m)
                                    if whatToFind is in address of r or whatToFind ¬
                                            is in display name of r then
                                        set foundRecipient to true
                                    end if
                                end repeat
                            end if

                            if foundRecipient then
                                copy m to end of messagesFound
                            end if
                        else if whereToFind is equal to "Contents" then
                            if whatToFind is in the content of m then
                                copy m to end of messagesFound
                            end if
                        end if

                        -- Update the status panel
                        tell theStatusPanel to incrementPanel()
                    end try
                end repeat
            end try
        end repeat
    end tell

    -- Return the result
    return messagesFound
end findMessages
```

The `findMessages` handler is similar in many ways to the `find` handler. It performs the following steps:

1. It gets the location criteria: the title of the current choice of the search location pop-up (the “where” menu).
2. It targets the Mail application.
3. It sets up a Repeat loop for each selected mailbox. The repeat loop contains a `try…end try` error handler so that if any error occurs, the script doesn’t halt. Any error is displayed by the error handler in the calling routine (`find`).
4. It sets up a Repeat loop for each message in the mailbox. This repeat loop also contains an error handler.
5. Within the inner repeat loop it does the following:

   1. It calls on the Mail application to search for the specified text in the specified location.
   2. If a message contains the specified text, it adds it to a list of found messages.
   3. At the end of the loop, it calls the `incrementPanel` handler of the status dialog script object to increment the count of the messages to be searched. The `incrementPanel` handler is described in [Write Handlers for Working With Message Windows](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkcineugrcfinca).
6. It returns the list of found messages. The list may be empty.

The `find` handler (shown in [Listing 9-16](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkcineukssgjfba)) also calls the following handlers. These handlers, which perform simple operations, aren’t shown in individual listings, but you can examine them in [Chapter 10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkukbmferkggeydc) or in the Mail Search sample application.

- `clearMessages`: Tells the data source of the Messages table view of the controller script object’s search window to delete every row, thus clearing the messages.
- `countMessages`: Communicates with the Mail application to count the messages in each mailbox in the passed list of mailboxes. Returns the total count.
- `addMessages`: Turns off updating in the Message table view. For each message in the passed list of messages, calls `addMessage`. Turns updating back on, so that the Messages table view displays the added messages.
- `addMessage`: (Not called directly by the `find` handler, but called by `addMessages`.) For the passed message, adds a row to the data source for the Messages table view, then adds a cell for each column in the row, so that the row displays the From, Subject, and Mailbox information for the message.
- `selectedMailboxes`: Gets the currently selected mailboxes from the Mailboxes outline view. If any accounts are selected, calls the `mailboxesForIndex` handler to get all corresponding mailboxes (both from accounts and from individual selected mailboxes) from the Mail application. If only mailboxes are selected, gets the mailboxes itself from the Mail Application. Returns the list of selected mailboxes (which may be empty).
- `mailboxesForIndex`: (Not called directly by the `find` handler, but called by `selectedMailboxes`.) Communicates with the Mail application to obtain the actual mailboxes corresponding to the currently selected mailboxes. Returns the list of selected mailboxes (which may be empty).

Because the Mail application’s scripting support doesn’t currently allow you to open a message in a separate window, Mail Search gets the message text and displays it in its own window. This section describes the controller handlers Mail Search uses to do this.

The jumping off point for displaying messages is the `openMessages` handler. It is called from the `double clicked` handler for the Messages view in the Search window (the handler is shown in [Listing 9-9](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkcineumsscijaq)). The Messages view currently supports only selection of single messages, so the `openMessages` handler merely calls the `openMessageWindow` handler to open the selected message. You could, however, modify the Messages table view in Interface Builder to allow multiple selection (see the Attributes pane in the Info window), then modify `openMessages` to iterate over the current selections, calling `openMessageWindow` for each selection.

The `openMessageWindow` handler is shown in Listing 9-18

__Listing 9-18__  The controller script’s `openMessageWindow` handler

```
on openMessageWindow()
    set clickedRow to clicked row of table view "messages" ¬
        of scroll view "messages" of split view 1 of theWindow
    if clickedRow is greater than or equal to 0 then
        set theAccount to ""
        set theMailbox to ""
        set theSubject to ""
        set theDateReceived to ""
        set theContents to ""
        set theSender to ""
        set theRecipients to ""
        set theCCRecipients to ""
        set theReplyTo to ""

        tell application "Mail"
            set theMessage to Abstract object clickedRow of foundMessages

            set theAccount to account name of account of container of theMessage
            set theMailbox to mailbox name of container of theMessage
            set theSubject to subject of theMessage
            -- set theDateReceived to date received of theMessage
            set theContents to content of theMessage
            set theSender to sender of theMessage
            set theRecipients to address of every recipient of theMessage
            set theCCRecipients to address of every cc recipient of theMessage
            set theReplyTo to reply to of theMessage
        end tell

        set messageWindow to makeMessageWindow()
        tell messageWindow
            set messageContents to "Account: " & theAccount & return
            set messageContents to messageContents & "Mailbox: " & theMailbox & return
            if length of theSender > 0 then
                set messageContents to messageContents & "From: " & theSender & return
            end if
            if length of theDateReceived as string > 0 then
                set messageContents to messageContents & "Date: " ¬
                    & (theDateReceived as string) & return
            end if
            if length of theRecipients > 0 then
                set messageContents to messageContents & "To: " ¬
                    & theRecipients & return
            end if
            if length of theCCRecipients > 0 then
                set messageContents to messageContents & "Cc: " ¬
                    & theCCRecipients & return
            end if
            if length of theSubject > 0 then
                set messageContents to messageContents & "Subject: " ¬
                    & theSubject & return
            end if
            if length of theReplyTo > 0 then
                set messageContents to messageContents & "Reply-To: " ¬
                    & theReplyTo & return & return
            end if
            set messageContents to messageContents & theContents
            set contents of text view "message" of scroll view "message" ¬
                to messageContents
            set title to theSubject
            set visible to true
        end tell
    end if
end openMessageWindow
```

The `openMessageWindow` handler performs the following steps:

1. It gets the row number for the currently selected message from the Messages table view.
2. If there is no currently selected row (the row number is less than zero), it does nothing. Otherwise it performs the following steps.
3. It initializes some local variables to store message information, such as the account, mailbox, subject, and so on.
4. It calls on the Mail application to obtain an object representing the message at the selected row. The term `Abstract object` is a Cocoa scripting term specifying an object that is the parent for all script objects that have no other parent class.
5. Continuing to use the Mail application, it sets local variables to message information from the message object returned in the previous step.
6. It calls the `makeMessageWindow` handler to create a new message window for displaying the message. The `makeMessageWindow` handler is described in [Write Handlers for Working With Message Windows](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkcineugrcfinca).
7. It sets another local variable to the message contents of the found message by concatenating the message information previously stored in local variables, then sets the text contents of the new message window.
8. It sets the title of the new window to the subject of the found message.
9. It sets the visible property of the new window to display it to the user.

Mail Search needs several handlers for working with controllers. These handlers are not part of the controller script itself. They aren’t shown in individual listings, but you can examine them in [Chapter 10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkukbmferkggeydc) or in the Mail Search sample application.

- `makeController`: This handler contains the entire controller script. You’ve examined most of the handlers in this script in previous sections. The `makeController` handler is called by the `will open` handler, shown in [Listing 9-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkcineugr2hjbdq), to create a controller script object for a search window. Since the script is the only content of the `makeController` handler, calling the handler effectively returns the script object as a return result.
- `addController`: This handler is also called by the `will open` handler, shown in [Listing 9-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkcineugr2hjbdq). It simply adds a controller to the global list of controllers.
- `removeController`: This handler is also called by the `will close` handler, shown in [Listing 9-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkcineumscjindq). It simply removes a controller from the global list of controllers by calling the utility handler `deleteItemInList`.
- `controllerForWindow`: This handler is called whenever a handler needs to obtain the controller for the current window. It returns the controller for the passed window from the global list of controllers.

Mail Search only needs one handler to work with the status dialog script, the `makeStatusPanel` handler, which creates the status dialog script object. This handler is shown in full in [Chapter 10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkukbmferkggeydc). The handlers and properties it contains are described in [The Status Dialog Script](Mail%20Search%20Tutorial-%20Design%20the%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tilkukbmferkggiydi). Since the script is the only content of the `makeStatusPanel` handler, calling the handler effectively returns the script object as a return result.

Mail Search only needs one handler to work with the message window, the `makeMessageWindow` handler. This handler, shown in Listing 9-19, is called from the `openMessageWindow` handler (shown in Listing 9-18.

__Listing 9-19__  The `makeMessageWindow` handler

```
on makeMessageWindow()
    load nib "Message"
    set windowCount to windowCount + 1
    set windowName to "message " & windowCount
    set name of window "message" to windowName
    return window windowName
end makeMessageWindow
```

The `makeMessageWindow` performs the following steps:

1. It loads an instance of the Message window from the Message nib.
2. It increments Mail Search’s global window count property.
3. It constructs a name for the window.
4. It returns the window name.

Mail Search needs one utility handler, `deleteItemInList`, to remove an item from a list. This handler is called by `removeController`, which in turn is called by the window’s `will close` handler to remove a controller before the window closes. AppleScript doesn’t currently support deleting items from lists directly, so scripters rely on a utility handler such as `deleteItemInList`, shown in Listing 9-20.

__Listing 9-20__  Utility function to delete an item from a list

```
on deleteItemInList(x, theList)
    (* To Be Provided *)
end deleteItemInList
```

[Next](Mail%20Search%20Tutorial-%20Build%20and%20Test%20the%20Application.md)[Previous](Mail%20Search%20Tutorial-%20Connect%20the%20Interface.md)

