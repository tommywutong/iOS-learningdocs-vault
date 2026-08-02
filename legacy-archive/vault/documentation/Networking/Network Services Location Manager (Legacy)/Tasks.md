---
title: Network Services Location Manager (Legacy)
apple_id: TP40000914
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSL/NSL2/NSL2.html
archived_at: '2026-07-15T08:18:16.872259Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Network Services Location Manager (Legacy)](Introduction.md)


[Next](Introduction%20to%20Network%20Services%20Location%20Manager.md)[Previous](Introduction.md)

# Tasks

The Network Services Location Manager provides high-level and low-level functions for searching for network services:

- The high-level functions are `NSLStandardRegisterURL` and `NSLStandardDeregisterURL` for registering and deregistering services and `NSLStandardGetURL`, which searches for services, displays a dialog box that lists the search results, and allows the user to choose a URL. If the user selects a URL from the search results, the `NSLStandardGetURL` function returns that URL to the calling application. Calling the high-level functions can be done without opening a session with the Network Services Location Manager or calling any other Network Services Location Manager function. For example, the NSLStandardGetURL function opens a session with the Network Services Location Manager and takes care of all of the details required to create request parameter blocks and search requests.
- Your application can call Network Services Location Manager low-level functions that open a session with the Network Services Location Manager, create request parameter blocks and search requests, and start searches.

This chapter describes the high-level Network Services Location Manager functions as well as the low-level Network Services Location Manager functions.

If your application only needs to register a network service, it can call the following Network Services Location Manager functions `NSLHexEncodeText` and without `NSLStandardRegisterURL` without having to call any other Network Services Location Manager functions.

The `NSLHexEncodeText` utility function encodes any characters that are not allowed in URLs that may occur in a URL that will be passed as a parameter to `NSLStandardRegisterURL`. For example, the space character in `http://myserver.com/`User Path is not allowed in URLs, and it needs to be encoded as `%20`. The parameters for calling `NSLHexEncodeText` are

```
OSStatus NSLHexEncodeText (
    char* rawText,
    UInt16 rawTextLen,
    char* newTextBuffer,
    UInt16* newTextBufferLen,
    Boolean* textChanged);
```

The `rawText` parameter points to the string containing the portion of a URL that is to be encoded. For example, when passed a string consisting of `User Path`, `NSLHexEncodeText`  will return a string consisting of `User%20Path`. The `rawTextLen` parameter contains the length of the string pointed to by `rawText`.

When `NSLHexEncode` returns, the `newTextBuffer` parameter points to the encoded string, and the `newTextBufferLen` parameter contains the length of that string. The `textChanged` parameter indicates whether any encoding was done and is `TRUE` if the string pointed to by `newTextBuffer contains encoded characters.`

The `NSLStandardRegisterURL` function registers network services. The parameters for calling `NSLStandardRegisterURL are`

```
OSStatus NSLStandardRegisterURL (
    NSLPath urlToRegister;
    NSLNeighborhood neighborhoodToRegisterIn);
```

The `urlToRegister` parameter is a null-terminated character string containing the URL to register.

The `neighborhoodToRegisterIn` parameter specifies the neighborhood in which the service is to be registered. If the `neighborhoodToRegisterIn` parameter is `NULL`, the Network Services Location Manager determines the neighborhoods in which to register the service. For this version of the Network Services Location Manager, applications almost always pass `NULL` as the value of this parameter, thereby allowing the Network Services Location Manager to determine the appropriate local neighborhood in which to register the service.

The `NSLStandardDeregisterURL` function deregisters services that have been registered and is typically called when the system is shutting down. The parameters for calling `NSLStandardDeregisterURL` are

```
OSStatus NSLStandardDeregisterURL (
    NSLPath urlToDeregister;
    NSLNeighborhood neighborhoodToDeregisterIn);
```

The `urlToDeregister` parameter is a null-terminated string containing the URL to deregister.

The `NSLStandardGetURL` function searches for neighborhoods and services, and displays a movable modal dialog box that lists the services and URLs that were found. The user can select a URL, and that URL is returned to the calling application.

[Figure 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydemjvfu2dimzzgq) shows the dialog box that `NSLStandardGetURL` displays.

__Figure 2-1__  Expanded dialog box displayed by `NSLStandardGetURL`

!

Clicking the up and down arrows of the At pop-up menu displays a list of favorite servers, recent servers, and neighborhoods from which users can make a selection.

The left column lists the available neighborhoods and the right column lists the servers in the selected neighborhood. The selected item in each column reflects the current selection in the At pop-up menu.

The current selection of the Show pop-up menu determines the type of service that is displayed in the At pop-up menu and the two columns. Users can use the Show pop-up menu to choose other service types (HTTP, AFP, WebDav, or FTP servers). If only one service is specified, the Show pop-up menu does not appear.

Clicking the “Add to Favorites” button adds the URL for the server that is selected in the right column to the user’s Favorites folder in the Finder and causes the server to appear in the At pop-up menu. To remove a Favorite, the user selects the “Remove from Favorites” item in the At pop-up menu, which causes a dialog box to appear. The dialog box lists all of the favorites and allows the user to select a favorite and remove it by clicking the Remove button.

The user can also type a URL in the Address text field. If the Address field is not empty when the user clicks the Connect button, the content of the Address field overrides the selection in the At pop-up menu.

To connect to the selected server or to connect to the URL specified in the Address text field, the user clicks the Connect button, which causes the dialog box to be dismissed and the selected URL to be returned to the calling application.

If the user clicks the Cancel button, the dialog box is dismissed and no URL is returned to the calling application.

Applications that call `NSLStandardGetURL` can control the following features of the dialog box that `NSLStandardGetURL` displays:

- the instructional text that appears in Small System font at the top of the dialog box
- the title of the dialog box; the default title is “Connect to Server”
- the button labels whose default values are “Cancel” and “Connect”
- the list of service types that appear in the Show pop-up menu
- the service type that appears at the top of the Show pop-up menu when the dialog box is first displayed
- whether the Address field is displayed

The parameters for calling `NSLStandardGetURL` are

```
OSStatus NSLStandardGetURL (
    NSLDialogOptions* dialogOptions,
    NSLEventUPP eventProc,
    void* eventProcContextPtr,
    NSLURLFilterUPP filterProc,
    char* serviceTypeList,
    char** userSelectedURL);
```

The `dialogOptions` parameter is pointer to an `NSLDialogOptions` structure whose fields specify the appearance of the dialog box, including the title of the dialog box, button names, whether instructional text is displayed, and whether the Address field is displayed. Call the `NSLGetDefaultDialogOptions` utility function to set your `NSLDialogOptions` structure to the default values; then modify your `NSLDialogOptions` structure as desired.

The `eventProc` parameter points to an application-defined system event callback function that the Network Services Location Manager calls so that your application can handle events that may occur while the `NSLStandardGetURL` dialog box is displayed. If `eventProc` is `NULL`, your application will not receive update events.

The `eventProcContextPtr` parameter points to a value that the Network Services Location Manager passes to your system event callback function so that your application can associate any particular call of `NSLStandardGetURL` with any particular call of its system event callback function.

The `filterProc` parameter is a value of type `NSLURLFilterUPP` that points to an application-defined callback function that your application can use to filter the results that the `NSLStandardGetURL` dialog box displays.

The `serviceTypeList` is a null-terminated string of tuples that specifies the services that are to be searched for. You can use the `serviceTypeList` parameter to specify custom icons that are displayed for each service that is found. If you do not specify custom icons, default icons are displayed.

The `userSelectedURL` parameter points to a address in memory. When `NSLStandardGetURL` returns, `userSelectedURL` points to the URL of the service that was selected when the user clicked the button that by default is labeled “Connect” or points to the URL specified in the Address field. If the user clicks the button that by default is labeled “Cancel,” the value of the `userSelectedURL` parameter is a null pointer when `NSLStandardGetURL` returns. Be sure to deallocate the memory allocated for the URL by calling NSLFreeURL when you no longer need the URL.

If a error occurs, the Network Services Location Manager calls `NSLErrorToString` to get a description of the error and a solution string and then displays a dialog box containing the error description and solution string.

Call `NSLOpenNavigationAPI` to open a session with the Network Services Location Manager. The `NSLOpenNavigationAPI` function returns a client reference that you use to prepare a search request.

Call `NSLMakeNewServicesList` to prepare a comma-delimited list of services that you want to search for, such as `http,ftp`. If you prepare a services list and later want to add another service to it, call `NSLAddServiceToServicesList`.

Call `NSLPrepareRequest` to create a search request. The following must be provided as parameters to `NSLPrepareRequest`:

- the client reference you received when you opened the Network Services Location Manager session
- a pointer to your application’s notification routine, which will be called when search results have been collected
- a pointer to an `NSLClientAsyncInfo` structure, which has fields you can use to change the conduct of searches that use the resulting search request

On output, `NSLPrepareRequest` provides a pointer to an `NSLClientAsyncInfo` structure. You can use the following fields in the `NSLClientAsyncInfo` structure to control the way in which searches are conducted:

- `maxSearchTime`, the maximum time in ticks that is to be spent on the search; zero means that the search time is not limited
- `alertInterval`, the time in ticks at which your application’s notification routine is to be called even if the search is still in progress; zero means that there is no interval
- `alertThreshold`, the number of items placed in the result buffer at which your application’s notification routine is to be called even if the search is still in progress; most applications set `alertThreshold` to 1

To search for neighborhoods, call `NSLStartNeighborhoodLookup`. The parameters for calling `NSLStartNeighborhoodLookup` are:

- the request reference created by calling `NSLPrepareRequest`
- `NULL` to get default neighborhoods or a neighborhood value created by calling `NSLMakeNewNeighborhood` to get the names of neighborhoods related to the name specified in the neighborhood value
- a pointer to the `NSLClientAsyncInfo` structure that was provided as a parameter to `NSLPrepareRequest`

To search for services, call `NSLStartServicesLookup`. The parameters for calling `NSLStartServicesLookup` are:

- the request reference created by calling `NSLPrepareRequest`
- `NULL` to search for top-level services or a neighborhood value created by calling `NSLMakeNewNeighborhood` to search for services in the neighborhood specified by the neighborhood value
- a request parameter block created by calling `NSLMakeServicesRequestPB`; before calling `NSLMakeNewServicesPB`, you must call `NSLMakeNewServicesList` to make a services list, which specifies the services, such as `http` or `ftp`, that you want to search for
- a pointer to the `NSLClientAsyncInfo` structure that was provided as a parameter to `NSLPrepareRequest`

If you set the `maxSearchTime`, `alertInterval`, and `alertThreshold` fields of your `NSLClientAsyncInfo` structure to 0, 0, and 1, respectively, your application’s notification routine is called whenever a search result is placed in the `resultBuffer` field of the `NSLClientAsyncInfo` structure.

Certain fields in the `NSLClientAsyncInfo` structure are used when a search is in progress. The fields are:

- `resultBuffer`, which points to the buffer in which the Network Services Location Manager places search results
- `bufferLen`, which reflects the number of bytes of valid data currently stored in `resultBuffer`
- `maxBufferSize`, which contains the maximum length in bytes of `resultBuffer`
- `totalItems`, which contains the number of individual search results currently stored in `resultBuffer`
- `searchState`, which describes the state of the search. The state can be that the result buffer is full, the search is ongoing, the search is complete, or the search is stalled
- `searchResult`, which consists of an `NSLError` structure whose `theErr` field may contain a result code that, depending on the state of the search, can help you decide whether to continue the search
- `searchDataType`, whose value is `kNSLNeighborhoodLookupDataEvent` if your notification routine was called as a result of a neighborhood search or `kNSLServicesLookupDataEvent` if your notification routine was called as a result of a neighborhood search

Your notification routine can use the `searchDataType` field to determine whether it should call `NSLGetNextNeighbor` or `NSLGetNextUrl` to process the result buffer.

If there are more search results to get, the search is continued when your notification routine returns. Depending on the contents of the result buffer, the value of the `searchState` and `searchResult` fields, you may decide to cancel the search by calling `NSLCancelRequest`. Note that you should not cancel the request from your notification routine.

When you no longer need a request reference, free the memory associated with it by calling `NSLDeleteRequest`, which also deallocates the `NSLClientAsyncInfo` structure associated with the deleted request reference. You’ll also want to deallocate memory for any neighborhood values, services lists, and parameter blocks. The utility functions for deallocating memory are described in the next section, `[“Using the Network Services Location Manager Utility Functions.”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydemjvfu2dsobsga)`

In addition to `NSLMakeNewNeighborhood`, there are several Network Services Location Manager utility functions for working with neighborhood values. The utility functions that work with neighborhood values are

- `NSLCopyNeighborhood`, which makes a copy of a neighborhood value
- `NSLGetNextNeighborhood`, which obtains a pointer to the next neighborhood in a result buffer and the length of that neighborhood
- `NSLGetNameFromNeighborhood` gets the name from a neighborhood value
- `NSLGetNeighborhoodLength` gets the length of a neighborhood value

In addition to `NSLMakeServicesRequestPB` and `NSLMakeNewServicesList`, there are several utility functions for working with request parameter blocks and services lists. The utility functions that work with request parameter blocks are

- `NSLServiceIsInServiceList`, which determines whether a service is in a service list
- `NSLAddServiceToServicesList`, which adds a service to a services list

There are several Network Services Location Manager utility functions for working with URLs. The utility functions that work with URLs are

- `NSLGetServiceFromURL`, which gets the service portion of a URL
- `NSLGetNextUrl`, which obtains a pointer to the next neighborhood in a result buffer and the length of that neighborhood

Before closing a Network Services Location Manager session, you should free memory allocated for neighborhood values, services lists, request parameter blocks, and request references. The functions and utility functions for deallocating memory are

- `NSLFreeNeighborhood`, which disposes a neighborhood value
- `NSLDisposeServicesList`, which deallocates the memory associated with a services list
- `NSLFreeTypedDataPtr`, which deallocates the memory associated with a request parameter block
- `NSLDeleteRequest`, which deallocates the memory associated with a request reference, as well as the `NSLClientAsyncInfo` structure associated with the request reference

To close a Network Services Location Manager session, call `NSLCloseNavigationAPI`.

[Next](Introduction%20to%20Network%20Services%20Location%20Manager.md)[Previous](Introduction.md)

