---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/DisplayingHistory.html
archived_at: '2026-07-15T07:14:50.763266Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Making%20Policy%20Decisions.md)[Previous](Paging%20Back%20and%20Forward.md)

# Managing History

[WebHistory](https://developer.apple.com/documentation/webkit/webhistory) and [WebHistoryItem](https://developer.apple.com/documentation/webkit/webhistoryitem) objects are used to maintain a history of all the pages a user visits. `WebHistoryItem` encapsulates all the information about a page that has been visited, and `WebHistory` maintains an ordered collection of these history items. `WebHistory` doesn’t just maintain a linear list. It also keeps track of the days on which a user visits pages. Therefore, you can group and present history items to users by day. For example, you can use submenus to group history items by the last three visited days.

`WebHistory` objects are not automatically created by WebKit. You enable the history feature by creating a `WebHistory` object and assigning it to your `WebView` object.

You can create [WebHistory](https://developer.apple.com/documentation/webkit/webhistory) objects in one of two ways. You can assign each `WebView` object its own `WebHistory` object, or you can create one `WebHistory` object that is shared by all `WebView` objects in your application as in:

```
 // Create a shared WebHistory object
    WebHistory *myHistory = [[WebHistory alloc] init];
    [WebHistory setOptionalSharedHistory:myHistory];
```


Like back-forward lists, history items are automatically added to the WebHistory object as the user navigates the web. If an item with the same URL already exists in the list, then it is replaced with the newer item even if the previous item was visited on a different day. Consequently, if the user revisits a URL it is always moved to the top of the list. Otherwise, items are not removed from the history list unless your application explicitly removes them.

For example, you could implement a clear history action by sending [removeAllItems](https://developer.apple.com/documentation/webkit/webhistory/1521404-removeallitems) to your WebHistory object as in:

```objc
// Removes all the history items
- (IBAction)clearHistory:(id)sender
{
    [[WebHistory optionalSharedHistory] removeAllItems];
}
```

After removing all the items, the [removeAllItems](https://developer.apple.com/documentation/webkit/webhistory/1521404-removeallitems) method posts a `WebHistoryAllItemsRemovedNotification` notification. The [addItems:](https://developer.apple.com/documentation/webkit/webhistory/1521407-additems) and [removeItems:](https://developer.apple.com/documentation/webkit/webhistory/1521409-removeitems) methods post similar notifications. You typically observe these notifications to update your display of history items as follows:

```
 // Observe WebHistory notifications
    nc = [NSNotificationCenter defaultCenter];
    [nc addObserver:self selector:@selector(historyDidRemoveAllItems:)
               name:WebHistoryAllItemsRemovedNotification object:myHistory];
    [nc addObserver:self selector:@selector(historyDidAddItems:)
               name:WebHistoryItemsAddedNotification object:myHistory];
    [nc addObserver:self selector:@selector(historyDidRemoveItems:)
               name:WebHistoryItemsRemovedNotification object:myHistory];
```

The `userInfo` attribute of these notifications is an array containing the added or removed items. For example, you might implement the `historyDidAddItems:` method to add a corresponding menu item to your History menu for each new history item in the `userInfo` array.

Once the user has the ability to select a history item to load, you need to implement an action to perform the load. You send [loadRequest:](https://developer.apple.com/documentation/webkit/webframe/1494250-load) to the main frame of the appropriate WebView object, passing the selected WebHistoryItem’s URL string as the argument. The following example assumes `historyItem` is the selected WebHistoryItem object:

```objc
- (void)goToHistoryItem:(id)historyItem
{
    // Load the history item in the main frame
    [[webView mainFrame] loadRequest:[NSURLRequest requestWithURL:[NSURL URLWithString:[historyItem URLString]]]];
}
```


Unlike WebBackForwardList objects, WebHistory objects can be persistent—that is, they can be loaded from and saved to a writable URL. You send [loadFromURL:error:](https://developer.apple.com/documentation/webkit/webhistory/1521402-load) to a WebHistory object to load history items from a readable URL, and you send [saveToURL:error:](https://developer.apple.com/documentation/webkit/webhistory/1521400-savetourl) to a WebHistory object to save history items to a writable URL.

[Next](Making%20Policy%20Decisions.md)[Previous](Paging%20Back%20and%20Forward.md)

