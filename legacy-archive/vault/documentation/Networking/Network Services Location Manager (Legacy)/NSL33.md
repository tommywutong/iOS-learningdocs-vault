---
title: Network Services Location Manager (Legacy)
apple_id: TP40000914
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSL/NSL3/NSL33.html
archived_at: '2026-07-15T08:18:17.615465Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Network Services Location Manager (Legacy)](Introduction.md)


[Next](Network%20Services%20Location%20Manager%20Data%20Types.md)[Previous](NSL32.md)

Network Services Location Manager Callback Functions

### Network Services Location Manager Miscellaneous Callbacks

- 

  Defines a pointer to a filter callback function. Your filter callback function determines if a URL should be displayed in the `NSLStandardGetURL` dialog box.

  ```
  typedef Boolean (*NSLURLFilterProcPtr)(
  char *url,
  Str255 displayString);
  ```

  If you name your function `MyNSLFilterProcPtr`, you would declare it like this:

  ```
  Boolean MyNSLURLFilterProcPtr (
  char* url,
  Str255 displayString);
  ```

  ```
  Parameters
  url
  A pointer to a string containing the URL to filter. Any data in a URL that follows the tag “?NAME=” has been removed from the URL.
  displayString
  A value of type
  Str255
  . If your filter callback returns
  TRUE
  , the URL pointed to by
  url
  will be listed in the dialog box displayed by
  NSLStandardGetURL
  . If you want to change the text of the URL, set
  displayString
  to the value you want.
  ```

  ```
  Discussion
  When calling
  NSLStandardGetURL
  , you can provide an
  NSLURLFilterProcPtr
  callback function for filtering the search results before they are displayed in the
  NSLStandardGetURL
  dialog box. Only those URLs for which your
  NSLURLFilterProcPtr
  callback function returns
  TRUE
  will appear in the right column of the dialog box displayed by
  NSLStandardGetURL
  . You can use the
  displayString
  parameter to modify the text of each URL that appears in the
  NSLStandardGetURL
  dialog box.
  ```
- 

  Defines a pointer to a system event callback function.

  ```
  typedef void (*NSLEventFilterProcPtr)(
  EventRecord *newEvent,
  void *userContext);
  ```

  If you name your function `MyNSLEventProcPtr`, you would declare it like this:

  ```
  void MyNSLEventProcPtr (
  EventRecord *newEvent,
  void *userContext);
  ```

  ```
  Parameters
  newEvent
  A pointer to a structure of type
  EventRecord
  that describes the event that triggered the execution of this callback function.
  displayString
  An untyped pointer to arbitrary data that your application previously passed to
  NSLStandardGetURL
  .
  ```

  ```
  Discussion
  When calling
  NSLStandardGetURL
  , you can provide an
  NSLEventProcPtr
  callback function for receiving system events while
  NSLStandardGetURL
  displays its dialog box. Your system event callback function will receive events while the
  NSLStandardGetURL
  dialog box is being displayed. If you do not provide an
  NSLEventProcPtr
  callback function, your application will not receive events.
  When your
  NSLEventProcPtr
  callback function is called, it should process the event immediately and return.
  ```

[Next](Network%20Services%20Location%20Manager%20Data%20Types.md)[Previous](NSL32.md)

