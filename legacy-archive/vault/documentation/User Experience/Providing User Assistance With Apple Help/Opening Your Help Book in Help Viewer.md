---
title: Providing User Assistance With Apple Help
apple_id: TP40006563
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LegacyAppleHelpConcepts/using_ah_functions/using_ah_functions.html
archived_at: '2026-07-18T02:11:51.865227Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Providing User Assistance With Apple Help](Introduction%20to%20Providing%20User%20Assistance%20With%20Apple%20Help.md)


[Next](Apple%20Help%20Meta%20Tag%20Properties.md)[Previous](Registering%20Your%20Help%20Book.md)

# Opening Your Help Book in Help Viewer

This chapter describes how to use Apple Help functions to load content from your help book in Help Viewer. If you are providing contextually sensitive help, or if you have help books in addition to your primary application help book, you need to know how to access your help book using the Apple Help API.

When users choose an item from the Help menu, click a help button, or choose help from a contextual menu, your application must display the pertinent help book content in Help Viewer. To open your help book in Help Viewer, use one of the following Apple Help functions:

- `AHLookupAnchor` opens a location in your help book identified by an anchor.
- `AHSearch` searches your help book for a term or phrase.
- `AHGotoPage` opens a help book page in Help Viewer.

If you specify anchor locations in your help book, as described in [Indexing Your Help Book](Authoring%20User%20Help.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dknrtfvbuqmrqgywugskijbdeqqkg), you can use the Apple Help function `AHLookupAnchor` to find and display help content by anchor name. `AHLookupAnchor` allows you to search for a particular help topic without knowing the path to the page that it is on. If you are implementing contextually sensitive help, you can load it by anchor, without having to track the path to every help page you may access.

If an anchor name appears more than once in your help book, Help Viewer displays all of the content associated with that anchor in your help book in a search results table. To use `AHLookupAnchor`, you must index your help book with anchor indexing turned on.

Listing 4-1 shows a function that uses `AHLookupAnchor` to find and display the text associated with a help book anchor.

__Listing 4-1__  Displaying an anchor location

```
OSStatus MyGotoHelpAnchor( CFStringRef anchorName)
{
    CFBundleRef myApplicationBundle = NULL;
    CFTypeRef myBookName = NULL;
    OSStatus err = noErr;

    myApplicationBundle = CFBundleGetMainBundle();// 1
    if (myApplicationBundle == NULL) {err = fnfErr; goto bail;}

    myBookName = CFBundleGetValueForInfoDictionaryKey(// 2
                    myApplicationBundle,
                    CFSTR("CFBundleHelpBookName"));
    if (myBookName == NULL) {err = fnfErr; goto bail;}

    if (CFGetTypeID(myBookName) != CFStringGetTypeID()) {// 3
        err = paramErr;
    }

    if (err == noErr) err = AHLookupAnchor (myBookName, anchorName);// 4
    return err;

}
```

Here is what the function in Listing 4-1 does:

1. Calls the Core Foundation function `CFBundleGetMainBundle` to retrieve a reference to the application’s main bundle.
2. Calls the Core Foundation function `CFBundleGetValueForInfoDictionaryKey` to find the name of the application’s help book. When you register your help book, you store your help book’s name in the `Info.plist` file with the key `CFBundleHelpBookName`. Rather than hard code your help book name—which can change as the help book content is updated—in your application, use Core Foundation functions to retrieve the help book name from the property list file.
3. Checks that the value returned in step 3 was of type CFString.
4. Calls the Apple Help function `AHLookupAnchor` to look up the anchor in the application’s help book.

Here is an example of how you could call the `MyGotoHelpAnchor` function described in [Listing 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dknrtfvbuqmrqhawugsceivdeiqsb):

```
err = MyGotoHelpAnchor(CFSTR("surfing"));
```


Apple Help also offers a way for you to send Help Viewer a search query to execute on your help book. Using the `AHSearch` function, you can search your help book for a term or phrase. For example, if you are implementing contextually sensitive help for a user interface element that is referenced in numerous help pages, you can call `AHSearch` to find and display those pages in a search results table. Listing 4-2 shows a function that searches your help book for a search term or query using the `AHSearch` function.

__Listing 4-2__  A function that searches your help book

```
OSStatus MySearchHelpBook(CFStringRef theQuery)
{
    CFBundleRef myApplicationBundle = NULL;
    CFStringRef myBookName = NULL;
    OSStatus err = noErr;

    myApplicationBundle = CFBundleGetMainBundle();// 1
    if (myApplicationBundle != NULL) {
        myBookName = CFBundleGetValueForInfoDictionaryKey(// 2
                        myApplicationBundle,
                        CFSTR("CFBundleHelpBookName"));
    } else err = fnfErr;

    if (myBookName != NULL) {
            err = AHSearch(myBookName, theQuery);// 3
    } else err = fnfErr;

    return err;
}
```

Here is what the function in Listing 4-2 does:

1. Calls `CFBundleGetMainBundle` to retrieve a reference to the application’s main bundle.
2. Calls `CFBundleGetValueForInfoDictionaryKey` to retrieve the help book name associated with the application bundle.
3. Calls `AHSearch` to search the help book for the string passed to `MySearchHelpBook` in the `theQuery` parameter.

Here is an example of how you could call the function shown in [Listing 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dknrtfvbuqmrqhawugscejfceqssb) to search your help book for information on printing. You can use a full question for your query, such as “How do I print a document?” or you can search for a term, such as “print”.

```
err = SearchHelpBook(CFSTR("How do I print a document?"));
err = SearchHelpBook(CFSTR("Print"));
```


The Apple Help function `AHGotoPage` allows you to open a help book page at a known location and display it in Help Viewer. If you know the path to the information you want to display, or if you simply wish to open your help book to its title page, use `AHGotoPage`.

You can specify the location of the page using either a full `file://` URL or a combination of a relative path and the help book name. Relative paths should be specified relative to the help book’s folder. In addition, you can specify an anchor within the given help page; when you specify an anchor, Help Viewer scrolls directly to the location of that anchor on the help page before displaying the page.

Table 4-1 shows the arguments you can pass to `AHGotoPage` and what Help Viewer displays in response.

__Table 4-1__  Arguments to `AHGotoPage`

| Arguments provided to AHGotoPage | Results |
| help book name | Help Viewer opens the help book to its title page |
| help book name, relative path | Help Viewer opens the page at the given path in the help book |
| help book name, relative path, anchor name | Help Viewer opens the page at the path and scrolls to the section identified by the anchor |
| `file://` URL | Help Viewer opens the page at that path |

The function shown in Listing 4-3 takes a path and an anchor name as arguments and calls `AHGotoPage` to open a help book page in Help Viewer.

__Listing 4-3__  A function that loads a help book page

```
OSStatus MyGotoHelpPage (CFStringRef pagePath, CFStringRef anchorName)
{
    CFBundleRef myApplicationBundle = NULL;
    CFStringRef myBookName = NULL;
    OSStatus err = noErr;

    myApplicationBundle = CFBundleGetMainBundle();// 1
    if (myApplicationBundle == NULL) {err = fnfErr; goto bail;}// 2

    myBookName = CFBundleGetValueForInfoDictionaryKey(// 3
                    myApplicationBundle,
                    CFSTR("CFBundleHelpBookName"));
    if (myBookName == NULL) {err = fnfErr; goto bail;}

    if (CFGetTypeID(myBookName) != CFStringGetTypeID()) {// 4
        err = paramErr;
    }

    if (err == noErr) err = AHGotoPage (myBookName, pagePath, anchorName);// 5
    return err;

}
```

Here is what the code does:

1. Calls the Core Foundation function `CFBundleGetMainBundle` to retrieve the application’s bundle.
2. If `CFBundleGetMainBundle` cannot find the application’s main bundle, returns an error specifying that the file was not found.
3. Calls the Core Foundation function `CFBundleGetValueForInfoDictionaryKey` to retrieve the name of the help book associated with the application’s main bundle.
4. Checks that the value returned in step 3 is of type CFString. The Core Foundation function `CFGetTypeID` returns the type ID of the value returned in step 3; the function `CFStringGetTypeID` returns the type ID of a CFString. If the type IDs do not match, `MyGotoHelpPage` returns a parameter error.
5. Calls the Apple Help function `AHGotoPage` to open the application’s help book to the page and anchor passed in as arguments to the `MyGotoHelpPage` function. If the `pagePath` and `anchorName` arguments are both `NULL`, `AHGotoPage` opens the application’s help book to its title page.

Here are three examples of how you could call the `MyGotoHelpPage` function described in [Listing 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dknrtfvbuqmrqhawugsceivdumrki):

```
err = MyGotoHelpPage(CFSTR("pages/howto.html"), CFSTR("surfing"));
err = MyGotoHelpPage(CFSTR("pages/howto.html"), NULL);
err = MyGotoHelpPage(NULL, NULL);
```

[Next](Apple%20Help%20Meta%20Tag%20Properties.md)[Previous](Registering%20Your%20Help%20Book.md)

