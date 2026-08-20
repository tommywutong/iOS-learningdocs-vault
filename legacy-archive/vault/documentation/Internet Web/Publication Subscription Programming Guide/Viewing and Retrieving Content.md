---
title: Publication Subscription Programming Guide
apple_id: TP40004945
resource_type: Guide
platform: macOS
topic: null
technology: PublicationSubscription
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/InternetWeb/Conceptual/PubSub/viewingcontent/viewingcontent.html
archived_at: '2026-07-15T07:43:37.547233Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Publication Subscription Programming Guide](Introduction.md)


[Next](Glossary.md)[Previous](Subscribing%20to%20a%20Feed.md)

# Viewing and Retrieving Content

After you obtain a feed object, you need to be able to retrieve the information from within it. Sometimes this information contains not only text, but also files in enclosures or extension XML. The following chapter describes what information is available in an entry and how to access it.

Most feeds contains one or more entries. To retrieve the entries from a feed object, use either the `entries` property (for an array of entry objects) or the `entryEnumeratorSortedBy:` method (for an enumerator of entry objects).

An entry object contains all the information specific to an entry, such as its title, its URL, its authors, its content, and, if necessary, its enclosures. Most of this information is a simple string or URL. However, three of components are a little more complicated.

In some feed standards, the author contains not only a name but also contains an email address and a homepage (see [Feed Formats](Understanding%20Feeds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsnbvfvbuqmznknltc)). The author information in Publication Subscription is stored in an author object. An author object represents a name, an email address, a homepage and a link to an `ABPerson` object.

The content of an entry is also more complex than a simple string. It often comes in one of two different forms: either plain text, or HTML formatted text. In Publication Subscription the content and the summary of an entry are stored as content objects. A content object contains methods for retrieving the content either as a plain text string or an HTML string. The content is returned in the specified format based on which accessor method is used.

An enclosure is a way to attach a file to an entry. If an entry contains enclosures, they will be linked to the entry object. For more information about enclosures, read [Downloading Enclosures](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsnbvfvbuqnrnknltc).

To print out the title and content of every entry in a feed, the code would look like Listing 4-1.

__Listing 4-1__  Accessing every entry in a feed

```
// Retrieve the entries as an unsorted enumerator
NSEnumerator *entries = [feed entryEnumeratorSortedBy: nil];
PSEntry *entry;

// Go through each entry and print out the title, authors, and content
while (entry = [entries nextObject]) {
    NSLog(@"Entry Title:%@", entry.title);
    NSLog(@"Entry Authors:%@", entry.authorsForDisplay);
    NSLog(@"Entry Content:%@", entry.content.plainTextString);
}
```

Since it follows an observer design pattern, Publication Subscription can also notify your application when any changes occur to a feed. Register with the notification center to be alerted when any change occurs (`PSFeedEntriesChangedNotification`). When your callback method is invoked, the changed entries are stored as a key-value pair in the user information dictionary of the notification.

Some entries may contain links to files as enclosures. Publication Subscription provides features that make it easy to download the files within the enclosure. Each enclosure is stored as a enclosure object in its associated entry object. Because there may be more than one enclosure in an entry, the entry object property `enclosures` returns an array of enclosure objects. In most cases, this array only contains one object. Each of these objects contains information about the enclosure’s size, URL and MIME type.

By default, enclosures are not automatically downloaded. You can change this setting on a per-feed basis so that any enclosure from a subscribed feed is downloaded with the entry. Listing 4-2 shows how to make a feed download its enclosures automatically.

__Listing 4-2__  Downloading enclosures automatically

```
PSFeedSettings *settings = feed.settings;
settings.downloadsEnclosures = YES;
feed.settings = settings;
```

If you want to download the file in the enclosures individually, send `download:` to the appropriate enclosure object. The `download:` method is asynchronous, so it rarely returns an error. Instead, check on the status of the download with the `downloadState` property. There are six possible states:

- `PSEnclosureDownloadDidFail`
- `PSEnclosureDownloadDidFinish`
- `PSEnclosureDownloadIsIdle`
- `PSEnclosureDownloadIsQueued`
- `PSEnclosureDownloadIsActive`
- `PSEnclosureDownloadWasDeleted`

If the download failed, see what caused the failure by using the `downloadError` method. If the download is still active, you can check on its progress by using the `downloadProgress` method. Assuming the download finishes, the location of the downloaded file is available with the `downloadedPath` property.

Although the download status can be checked in a synchronous manner, it is recommended that you register for the notification `PSEnclosureDownloadStateDidChangeNotification` instead. When your callback method is invoked, you can determine the status of the download. Listing 4-3 shows how to start downloading the file in the enclosure and register for the appropriate notification. Listing 4-4 shows a callback method for the notification.

__Listing 4-3__  Downloading an enclosure

```

// Get the enclosures from the current entry, and retrieve the first one
NSArray *enclosureArray = entry.enclosures;
enclosure = [enclosureArray objectAtIndex: 0];
NSError *error;

// Download the enclosure
if (![enclosure download:&error]) {
    NSLog(@"Enclosure download failed: %@", error)
} else {

    // Register for any changes to the download's state
    [[NSNotificationCenter defaultCenter]
            addObserver:self
            selector:@selector(downloadStateChanged:)
            name: PSEnclosureDownloadStateDidChangeNotification
            object: enclosure];
}
```


__Listing 4-4__  Receiving download state changes through notifications

```objc

- (void) downloadStateChanged: (NSNotification *) sender {

    // See what state change cause the notification to be sent
    switch (enclosure.downloadState) {

        // If the download failed, log why and stop receiving notifications
        case PSEnclosureDownloadStateDidFail:
            NSLog(@"Enclosure download failed: %@", enclosure.downloadError);
            [[NSNotificationCenter defaultCenter]
                removeObserver: self
                name: PSEnclosureDownloadStateDidChangeNotification
                object: enclosure];
            break;

        // If the download succeeded, log the location of the file and stop
        // receiving notifications
        case PSEnclosureDownloadStateDidFinish:
            NSLog(@"Location of downloaded file is: %@", enclosure.downloadedPath);
            [[NSNotificationCenter defaultCenter]
                removeObserver: self
                name: PSEnclosureDownloadStateDidChangeNotification
                object: enclosure];
            break;

        case default:
            break;
    }
}
```


Many feeds may also contain extension XML elements. If additional namespaces are used in a feed, use the `extensionXMLElementsUsingNamespace:` method to return an array of `NSXMLElement` objects. Pass the namespace URL, not the prefix, to the `extensionXMLElementsUsingNamespace:` method. If your feed had an entry like that in [Listing 1-3](Understanding%20Feeds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsnbvfvbuqmznknlte), `extensionXMLElementsUsingNamespace:` returns an array of four `NSXMLElement` objects.

Listing 4-5 shows how to find a specific element in a particular namespace in an entry. In this example, the namespace is the iTunes Podcast.

__Listing 4-5__  Retrieving extension XML from an entry

```
// Find each element using the iTunes Podcast namespace
for( NSXMLElement *elem in [entry extensionXMLElementsUsingNamespace: @"http://www.itunes.com/dtds/podcast-1.0.dtd"] ) {

    // Check if the element is called "keywords"
    if (NSOrderedSame == [[elem localName] isEqualToString:@"keywords"]) {

        // If it is, print the data from the element to the log
        NSLog(@"keywords:%@", [elem stringValue]);
    }
}
```

[Next](Glossary.md)[Previous](Subscribing%20to%20a%20Feed.md)

