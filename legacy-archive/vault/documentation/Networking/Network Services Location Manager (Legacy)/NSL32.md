---
title: Network Services Location Manager (Legacy)
apple_id: TP40000914
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSL/NSL3/NSL32.html
archived_at: '2026-07-15T08:18:17.581868Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Network Services Location Manager (Legacy)](Introduction.md)


[Next](NSL33.md)[Previous](Introduction%20to%20Network%20Services%20Location%20Manager.md)

Network Services Location Manager Functions

### Network Services Location Manager Miscellaneous Functions

- 

  Adds a service to a services list.

  ```
  NSLError NSLAddServiceToServicesList (
  NSLServicesList serviceList,
  NSLServiceType serviceType);
  ```

  ```
  Parameters
  serviceList
  On input, a value of type
  NSLServicesList
  previously created by calling
  NSLMakeNewServicesList
  .
  serviceType
  On input, a value of type
  NSLServiceType
  containing the name of the service, such as
  http
  or
  ftp
  that is to be added to the services list.
  function result
  An
  NSLError
  structure whose
  theErr
  field contains the result code. If the value of
  NSLError.theErr
  is
  noErr
  , the service was added to the list. Other possible values are
  kNSLNotInitialized
  ,
  kNSLBadServiceTypeErr
  , and
  kNSLNullListPtr
  . Call
  NSLErrorToString
  to get a problem and a solution string.
  ```

  ```
  Discussion
  This function adds the name of the specified service to a services list. If you need to add more than one service to the services list, call this function once for each service that you want to add.
  ```

  ```
  Special Considerations
  You must create
  serviceList
  by calling
  NSLMakeNewServicesList
  before calling this function.
  ```
- 

  Cancels an ongoing search.

  ```
  NSLError NSLCancelRequest (NSLRequestRef ref);
  ```

  ```
  Parameters
  ref
  On input, a value of type
  NSLRequestRef
  , obtained by previously calling
  NSLPrepareRequest
  , for the search that is to be canceled.
  function result
  An
  NSLError
  structure whose
  theErr
  field contains the result code. A value of
  noErr
  indicates that the request was canceled successfully. Other possible values are
  kNSLNotInitialized
  and
  kNSLBadReferenceErr
  . Call
  NSLErrorToString
  to get a problem and a solution string.
  ```

  ```
  Discussion
  This function cancels an ongoing search. Any outstanding I/O is also canceled.
  ```
- 

  Closes a session with the Network Services Location Manager.

  ```
  void NSLCloseNavigationAPI (NSLClientRef theClient);
  ```

  ```
  Parameters
  theClient
  On input, a value of type
  NSLClientRef
  , obtained by previously calling
  NSLOpenNavigationAPI
  , that identifies the session that is to be closed.
  ```

  ```
  Discussion
  This function closes the Network Services Location Manager session identified by
  theClient
  . If your application calls this function while a search is in progress, any data that would have been returned is lost.
  ```

  ```
  Special Considerations
  Your application is responsible for reclaiming memory that it allocates for services lists, parameter blocks, and search request references. Your application should reclaim memory by calling
  NSLDisposeServicesList
  ,
  NSLDeleteRequest
  , and
  NSLFreeTypedDataPtr
  , respectively.
  ```
- 

  Continues a search.

  ```
  NSLError NSLContinueLookup (
  NSLClientAsyncInfo *asyncInfo);
  ```

  ```
  Parameters
  asyncInfo
  On input, a pointer to the
  NSLClientAsyncInfo
  structure for this search.
  function result
  An
  NSLError
  structure whose
  theErr
  field contains the result code. If the value of
  NSLError.theErr
  is
  noErr
  ,
  NSLContinueLookip
  returned successfully. Possible errors include
  kNSLNotInitialized
  ,
  kNSLNoContextAvailable
  ,
  kNSLBadClientInfoPtr
  ,
  kNSLCannotContinueLookup
  , and
  kNSLBufferTooSmallForData
  . Call
  NSLErrorToString
  to get a problem and a solution string.
  ```

  ```
  Discussion
  This function is deprecated in Mac OS X and returns without performing any work. In Mac OS X, asynchronous searches continue automatically when the application’s notification routine returns. For compatibility with earlier versions of the Network Services Location Manager, applications can continue to call this function, but doing so is not necessary.
  ```
- 

  Copies a neighborhood.

  ```
  NSLNeighborhood NSLCopyNeighborhood (
  NSLNeighborhood neighborhood);
  ```

  ```
  Parameters
  neighborhood
  On input, the neighborhood that is to be copied.
  result
  An
  NSLNeighborhood
  value. If this function can’t copy the neighborhood specified by the
  neighborhood
  parameter, it returns
  NULL
  . This might happen, for example, if there is not enough memory.
  ```

  ```
  Discussion
  This utility function creates a copy of the specified neighborhood. A neighborhood is guaranteed to exist only during the execution of an application’s notification routine, so you may want to call this utility function from your application’s notification routine in order to keep a copy of the neighborhood.
  When you have no further use for an
  NSLNeighborhood
  value, you should reclaim the memory allocated to it by calling
  NSLFreeNeighborhood
  .
  ```
- 

  Deletes a request reference.

  ```
  NSLError NSLDeleteRequest (
  NSLRequestRef ref);
  ```

  ```
  Parameters
  ref
  On input, the value of type
  NSLRequestRef
  , obtained by previously calling
  NSLPrepareRequest
  , that is to be deleted.
  function result
  An
  NSLError
  structure whose
  theErr
  field contains the result code. If the value of the
  theErr
  field is
  noErr
  , the request reference was deleted. Other possible values are
  kNSLNotInitialized
  and
  kNSLBadReferenceErr
  . Call
  NSLErrorToString
  to get a problem and a solution string.
  ```

  ```
  Discussion
  This function deletes the specified request reference and deallocates memory associated with it, including the
  NSLClientAsyncInfo
  structure associated with the request reference. If a search using the specified request reference is in progress when this function is called, the search is canceled and any outstanding  I/O is lost.
  This function does not deallocate memory associated with services lists or request parameter blocks. To deallocate memory for services lists, call
  NSLDisposeServicesList
  ; to deallocate memory for parameter blocks, call
  NSLFreeTypedDataPtr
  .
  ```
- 

  Disposes of a services list.

  ```
  void NSLDisposeServicesList (
  NSLServicesList theList);
  ```

  ```
  Parameters
  theList
  On input, a value of type
  NSLServicesList
  , previously created by calling
  NSLMakeNewServicesList
  , that is to be disposed of.
  ```

  ```
  Discussion
  This utility function reclaims memory by disposing of a services list. Once you’ve incorporated the information in a services list into a request parameter block by passing the services list to
  NSLMakeServicesRequestPB
  , you can dispose of the services list.
  Calling
  NSLCloseNavigationAPI
  does not reclaim memory allocated for services lists, so your application should dispose of services lists before it closes a Network Services Location Manager session.
  ```
- 

  Obtains information about an error.

  ```
  OSStatus NSLErrorToString (
  NSLError theErr,
  char * errorString,
  char * solutionString);
  ```

  ```
  Parameters
  theErr
  On input, an
  NSLError
  structure whose
  theErr
  field contains a Network Services Location Manager result code.
  errorString
  On input, a pointer to the buffer in which this function is to place a null-terminated string containing a description of the problem that caused the error. The length of
  errorString
  should be 256 bytes.
  solutionString
  On input, a pointer to the buffer in which this function is to place a null-terminated string containing a possible solution to the problem. The length of
  solutionString
  should be 256 bytes.
  function result
  A value of
  noErr
  indicates that this function returned successfully. If the value of the
  theContext
  field of the
  NSLError
  structure that was passed to this function is zero and the
  theErr
  field contains a result code that is not within the range of Network Services Location Manager result codes, this function returns
  kNSLBadReferenceErr
  .
  ```

  ```
  Discussion
  This function obtains the error and solution strings for the result code stored in the
  theErr
  field of an
  NSLError
  structure.Your application can use the strings to display an appropriate error message.
  ```
- 

  Disposes of an `NSLNeighborhood` value.

  ```
  NSLNeighborhood NSLFreeNeighborhood (NSLNeighborhood neighborhood);
  ```

  ```
  Parameters
  neighborhood
  On input, the
  NSLNeighborhood
  value, obtained by previously calling
  NSLMakeNewNeighborhood
  , that is to be disposed of.
  function result
  An
  NSLNeighborhood
  whose value is
  NULL
  .
  ```

  ```
  Discussion
  This utility function disposes of an
  NSLNeighborhood
  value and reclaims the memory that was allocated to it.
  ```
- 

  Frees memory allocated for a request parameter block.

  ```
  NSLTypedDataPtr NSLFreeTypedDataPtr (
  NSLTypedDataPtr nslTypeData);
  ```

  ```
  Parameters
  nslTypeData
  On input, a value of type
  NSLTypedDataPtr
  , obtained by previously calling
  NSLMakeServicesRequestPB
  .
  function result
  A value of type
  NSLTypedDataPtr
  whose value is
  NULL
  .
  ```

  ```
  Discussion
  This utility function frees memory that was allocated when your application previously called
  NSLMakeServicesRequestPB
  . Your application should free the memory allocated for a request parameter block when it has no further use for the parameter block.
  ```
- 

  Frees memory allocated for a URL.

  ```
  (char *) NSLFreeURL (
  char * URL);
  ```

  ```
  Parameters
  URL
  On input, a pointer to a character string obtained by previously calling
  NSLStandardGetURL
  .
  result
  NULL
  .
  ```

  ```
  Discussion
  This utility function frees the memory that was allocated for
  URL
  when
  NSLStandardGetURL
  was called. Your application should call this utility function when it has no further use for the URL.
  ```
- 

  Assigns the default values to an `NSLDialogOptions` structure.

  ```
  OSStatus NSLGetDefaultDialogOptions (
  NSLDialogOptions * dialogOptions);
  ```

  ```
  Parameters
  dialogOptions
  On input, a pointer to an
  NSLDialogOptions
  structure. On output, the fields of the structure are filled in with the default values.
  function result
  A value of
  noErr
  indicates that the fields were filled in with the default values. See
  “Network Services Location Manager Result Codes”
  for other possible result codes.
  ```

  ```
  Discussion
  This utility function assigns default values to the
  NSLDialogOptions
  structure pointed to by the dialogOptions parameter. Assigning default values prepares the structure for use when calling
  NSLStandardGetURL
  . After the default values are assigned, you can modify the structure as desired. For the default values, see
  NSLDialogOptions
  .
  ```
- 

  Locates the name in a neighborhood.

  ```
  void NSLGetNameFromNeighborhood (
  NSLNeighborhood neighborhood,
  char ** name,
  long * length);
  ```

  ```
  Parameters
  neighborhood
  On input, a value of type
  NSLNeighborhood
  containing the name that is to be located.
  name
  On input, the address of a pointer. On output,
  name
  contains the address of a pointer to the name in the
  neighborhood
  parameter.
  length
  On input, a pointer to a location in memory. On output,
  length
  points to the length in bytes of the name in the
  neighborhood
  parameter.
  ```

  ```
  Discussion
  This utility function locates the null-terminated name in the neighborhood specified by the
  neighborhood
  parameter so that your application can, for example, display the name. Use the value pointed to by
  length
  to determine the length of the name.
  ```
- 

  Gets the length of a neighborhood.

  ```
  long NSLGetNeighborhoodLength (
  NSLNeighborhood neighborhood);
  ```

  ```
  Parameters
  neighborhood
  On input, the value of type
  NSLNeighborhood
  whose length is to be obtained.
  function result
  The length in bytes of the specified neighborhood.
  ```

  ```
  Discussion
  This utility function gets the length of the specified neighborhood, which you would need in order to make a copy of a neighborhood. Instead of calling this utility function, call
  NSLCopyNeighborhood
  to make a copy of a neighborhood.
  ```

  ```
  Special Considerations
  This utility function may be deprecated in the future.
  ```
- 

  Gets the position of the next neighborhood in a result buffer.

  ```
  Boolean NSLGetNextNeighborhood (
  NSLClientAsyncInfoPtr infoPtr,
  NSLNeighborhood * neighborhood,
  long * neighborhoodLength);
  ```

  ```
  Parameters
  infoPtr
  On input, a pointer to an
  NSLClientAsyncInfo
  structure whose resultBuffer field may contain another neighborhood.
  neighborhood
  On input, a pointer to a value of type
  NSLNeighborhood
  . On output,
  neighborhood
  points to the next neighborhood in the
  resultBuffer
  field of the
  NSLClientAsyncInfo
  structure pointed to by
  infoPtr
  .
  neighborhoodLength
  On output, the length of the neighborhood pointed to by
  neighborhood
  .
  function result
  A Boolean value. A value of
  TRUE
  indicates that
  neighborhood
  points to the next neighborhood in the
  resultBuffer
  field pointed to by
  infoPtr
  . A value of
  FALSE
  indicates that there are no more neighborhoods in the
  resultBuffer field
  .
  ```

  ```
  Discussion
  This utility function provides the starting position and the length of the next neighborhood in a result buffer. Typically, the neighborhoods were placed in the result buffer by a previous call to
  NSLStartNeighborhoodLookup
  .
  If you want to get a copy of the neighborhood, call
  NSLCopyNeighborhood
  . If you want to get the name from the neighborhood, call
  NSLGetNameFromNeighborhood
  .
  ```
- 

  Gets the position of the next URL in a result buffer.

  ```
  Boolean NSLGetNextUrl (
  NSLClientAsyncInfoPtr infoPtr,
  char ** urlPtr,
  long * urlLength);
  ```

  ```
  Parameters
  infoPtr
  On input, a pointer to an
  NSLClientAsyncInfo
  structure whose
  resultBuffer
  field may contain another URL.
  urlPtr
  On output, if another URL was found in the
  resultBuffer
  field, a pointer to the beginning of the URL.
  urlLength
  On output, the length of the URL pointed to by
  urlPtr
  .
  function result
  A Boolean value. A value of
  TRUE
  indicates that
  urlPtr
  points to the next URL in the
  resultBuffer
  field pointed to by
  infoPtr
  . A value of
  FALSE
  indicates that there are no more URLs in the
  resultBuffer
  field.
  ```

  ```
  Discussion
  This utility function obtains the starting position and the length of the next URL in a result buffer. Typically, the URLs were placed in the result buffer by a previous call to
  NSLStartServicesLookup
  .
  ```
- 

  Gets the service portion of a URL.

  ```
  OSStatus NSLGetServiceFromURL (
  char* theURL,
  char** svcString,
  UInt16* svcLen);
  ```

  ```
  Parameters
  theURL
  On input, a pointer to a null-terminated string containing a URL.
  svcString
  On input, a pointer to the address of a string in memory. On output,
  svcString
  points to the service portion of the URL specified by
  theURL
  .
  svcLen
  On input, a pointer to an unsigned 16-bit value. On output,
  svcLen
  points to the length in bytes of
  svcString
  .
  function result
  A value of
  noErr
  indicates that
  svcString
  points to the service portion of the URL specified by
  theURL
  .
  ```

  ```
  Discussion
  This utility function gets the service portion of a URL. For example, if the URL is
  http://www.apple.com
  , the service portion of that URL is
  http
  .
  ```
- 

  Decodes the encoded portion of a URL.

  ```
  OSStatus NSLHexDecodeText (
  char* encodedText,
  UInt16 encodedTextLen,
  char* decodedTextBuffer,
  UInt16* decodedTextBufferLen,
  Boolean* textChanged);
  ```

  ```
  Parameters
  encodedText
  On input, a pointer to a buffer containing the portion of a URL that has been encoded.
  encodedTextLen
  On input, a value of type
  UInt16
  that specifies the length of the buffer pointed to by encodedText.
  decodedTextBuffer
  On input, a pointer to a buffer in which the decoded text is to be stored. On output, the buffer contains the decoded text.
  decodedTextBufferLen
  On input, a pointer to a value of type
  UInt16
  containing the maximum length of
  decodedTextBuffer
  . On output,
  decodedTextBufferLen
  points to the length of the decoded text pointed to by
  decodedTextBuffer
  .
  textChanged
  On input, a pointer to a Boolean value. On output,
  textChanged
  points to a value that is
  TRUE
  if decoding occurred or that is
  FALSE
  if no decoding was required.
  function result
  A value of
  noErr
  indicates that this utility function returned successfully. See
  “Network Services Location Manager Result Codes”
  for other possible result codes.
  ```

  ```
  Discussion
  This utility function decodes the portion of a URL that was previously encoded by
  NSLHexEncodeText
  . If this utility function returns
  noErr
  , the buffer pointed to by
  decodedTextBuffer
  contains the decoded copy of the buffer pointed to by
  encodedTextBuffer
  , or it contains an exact copy of the buffer pointed to by
  encodedTextBuffer
  . Use the
  textChanged
  parameter to determine whether any decoding actually took place.
  ```
- 

  Encodes a portion of a URL.

  ```
  OSStatus NSLHexEncodeText (
  char* rawText,
  UInt16 rawTextLen,
  char* newTextBuffer,
  UInt16* newTextBufferLen,
  Boolean* textChanged);
  ```

  ```
  Parameters
  rawText
  On input, a pointer to a character array containing the portion of a URL that is to be encoded. For example, if the URL is
  afp://17.221.40.66?NAME=Kevs G3
  , the portion of the URL that contains a character that is not allowed is
  Kevs G3
  . In this example, the space character is not allowed.
  rawTextLen
  On input, a value of type
  UInt16
  containing the length in bytes of the
  rawText
  parameter.
  newTextBuffer
  On input, a pointer to a buffer. On output, the buffer contains the encoded text.
  newTextBufferLen
  On input, a pointer to a value of type
  UInt16
  . On output,
  newTextBufferLen
  points to the length of the encoded text in the buffer pointed to by
  newTextBuffer
  .
  textChanged
  On input, a pointer to a Boolean value. On output,
  textChanged
  points to a value that is
  TRUE
  if encoding occurred or that is
  FALSE
  if no encoding was required.
  function result
  A value of
  noErr
  indicates that this utility function returned successfully. See
  “Network Services Location Manager Result Codes”
  for other possible result codes.
  ```

  ```
  Discussion
  This utility function uses the US ASCII character set to encode characters that are not allowed in URLs. Hexadecimal values from 01 to 1F, from 80 to FF, and 7F are not allowed. In addition, the following characters are not allowed:
  < > " # { } | \ ^ ~ [ ]
  This utility function also encodes the following characters that are reserved for URL syntax:
  ; / ? : @ = % &
  If this utility function returns
  noErr
  , the buffer pointed to by
  newTextBuffer
  contains the encoded copy of the buffer pointed to by
  rawText
  , or it contains an exact copy of the buffer pointed to by
  rawText
  . Use the
  textChanged
  parameter to determine whether any encoding actually took place.
  Call
  NSLHexDecodeText
  to decode a string that has been encoded.
  ```

  ```
  Special Considerations
  The
  NSLStandardRegisterURL
  function returns an error if a URL you try to register contains characters that need to be encoded.
  ```
- 

  Determines whether the Network Services Location Manager is present.

  ```
  Boolean NSLLibraryPresent (void);
  ```

  ```
  Parameters
  function result
  TRUE
  if the Network Services Location Manager is present.
  ```

  ```
  Discussion
  This utility function returns
  TRUE
  when the Network Services Location Manager is available. The Network Services Location Manager is always present in Mac OS X, so for applications that only run on Mac OS X do not need to call this function.
  ```
- 

  Gets the Network Services Location Manager’s version.

  ```
  UInt32 NSLLibraryVersion (void);
  ```

  ```
  Parameters
  function result
  The Network Services Location Manager’s version number in hexadecimal format, where the first two bytes represent the version number, the second two bytes represent the revision number, and the third two bytes represent the subrevision number.
  ```

  ```
  Discussion
  This utility function gets the version of the Network Services Location Manager installed on the system.
  ```
- 

  Creates a neighborhood for use in searches.

  ```
  NSLNeighborhood NSLMakeNewNeighborhood (
  char * name,
  char * protocolList);
  ```

  ```
  Parameters
  name
  On input,
  NULL
  to create a neighborhood that can be used to obtain a list of default neighborhoods when calling
  NSLStartNeighborhoodLookup
  , or a pointer to a null-terminated string containing the name of a neighborhood in which searches are to be conducted.
  protocolList
  On input,
  NULL
  , which creates a neighborhood that will cause all available protocols to participate in any search that uses it. For compatibility with earlier versions of the Network Services Location Manager,
  protocolList
  can be a pointer to a comma-separated, null-terminated list of protocols (such as
  NBP,SLP
  ) that are to participate in a search conducted with the resulting neighborhood. The constants
  kDSProtocolType
  ,
  kNBPProtocolType
  , and
  kSLPProtocolType
  can be used to build a protocol list. However, searches conducted using the resulting neighborhood will not be limited to the protocols that were specified.
  function result
  An
  NSLNeighborhood
  value that can be used in subsequent calls to Network Services Location Manager functions, or
  NULL
  if a neighborhood value could not be created. This might happen, for example, if there is not enough memory.
  ```

  ```
  Discussion
  This utility function creates a neighborhood that can be provided as a parameter to other Network Services Location Manager functions such as
  NSLStartNeighborhoodLookup
  ,
  NSLStartServicesLookup
  ,
  NSLStandardRegisterURL
  , and
  NSLStandardDeregisterURL
  .
  When you have no further use for a neighborhood, you can reclaim the memory allocated to it by calling
  NSLFreeNeighborhood
  .
  ```

  ```
  Special Considerations
  Specifying protocols in the
  protocolList
  parameter is deprecated. If you specify protocols when other protocols are available, any use of the resulting neighborhood will not be limited to the protocols you specified.
  ```
- 

  Creates a request parameter block.

  ```
  OSStatus NSLMakeServicesRequestPB (
  NSLServicesList serviceList,
  NSLTypedDataPtr * newDataPtr);
  ```

  ```
  Parameters
  serviceList
  On input, a value of type
  NSLServicesList
  created by previously calling
  NSLMakeNewServicesList
  .
  newDataPtr
  On input, the address of the
  NSLTypedDataPtr
  at which the resulting parameter block is to be placed.
  function result
  A value of
  noErr
  indicates that the parameter block was created successfully. Possible errors include
  kNSLBadDomainErr
  .
  ```

  ```
  Discussion
  This utility function creates a parameter block formatted properly for use with subsequent calls to
  NSLStartServicesLookup
  .
  ```
- 

  Creates a services list.

  ```
  NSLServicesList NSLMakeNewServicesList (
  char* initialServiceList);
  ```

  ```
  Parameters
  initialServiceList
  On input, a pointer to a comma-delimited, null-terminated string of service names, such as
  http,ftp
  .
  function result
  A value of type
  NSLServicesList
  . This function returns
  NULL
  if it can’t create the services list because, for example, there is not enough memory or because the Network Services Location Manager is not initialized.
  ```

  ```
  Discussion
  This function creates a services list and fills it with the names of the services specified by the
  initialServiceList
  parameter. After creating the services list, you can add the names of additional services by calling
  NSLAddServiceToServicesList
  .
  ```

  ```
  Special Considerations
  When you have no further use for the services list, you should reclaim the memory allocated to it by calling
  NSLDisposeServicesList
  .
  ```
- 

  Opens a session with the Network Services Location Manager.

  ```
  OSStatus NSLOpenNavigationAPI (
  NSLClientRef * newRef);
  ```

  ```
  Parameters
  newRef
  On input, a pointer to a value of type
  NSLClientRef
  in which the Network Services Location Manager places a client reference. Pass the client reference to
  NSLPrepareRequest
  and
  NSLCloseNavigationAPI
  .
  function result
  A value of
  noErr
  indicates that the session was opened successfully. If
  NSLOpenNavigationAPI
  returns any of the following error codes, your application should not call any other Network Services Location Manager functions:
  kNSLNotInitialized
  ,
  kNSLInsufficientSysVer
  ,
  kNSLInsufficientOTVer
  ,
  kNSLPluginLoadFailed
  , or
  kNSL68kContextNotSupported
  .
  ```

  ```
  Discussion
  This function opens a session with the Network Services Location Manager and returns a client reference that your application later uses to prepare search requests and to close the Network Services Location Manager session. You must call
  NSLOpenNavigationAPI
  before calling any other Network Services Location Manager functions.
  ```
- 

  Creates a search request.

  ```
  NSLError NSLPrepareRequest (
  NSLClientNotifyUPP notifier,
  void * contextPtr,
  NSLClientRef theClient,
  NSLRequestRef * ref,
  char * bufPtr,
  unsigned long bufLen,
  NSLClientAsyncInfoPtr * infoPtr);
  ```

  ```
  Parameters
  notifier
  On input, a value of type
  NSLClientNotifyUPP
  that points to your application’s notification routine, or
  NULL
  . Your notification routine will be called when data is available, when the search is complete, or when an error occurs.
  contextPtr
  On input, an untyped pointer to arbitrary data that the Network Services Location Manager will pass to your application’s notification routine when that routine is called. Your application can use
  contextPtr
  to associate any particular execution of your notification routine with any particular search request.
  theClient
  On input, a value of type
  NSLClientRef
  obtained by previously calling
  NSLOpenNavigationAPI
  that identifies the Network Services Location Manager session for which this request is being prepared.
  ref
  On input, a pointer to a value of type
  NSLRequestRef
  in which the resulting search request reference is to be placed.
  bufPtr
  On input, a pointer to the buffer in which search results are to be placed.
  bufLen
  On input, the length of the buffer pointed to by
  bufPtr
  .
  infoPtr
  On output, the
  NSLClientAsyncInfo
  structure pointed to by
  infoPtr
  contains default instructions for how the search is to be conducted. Your application can change the defaults before it starts the search.
  function result
  An
  NSLError
  structure whose
  theErr
  field contains the result code. If the value of
  NSLError.theErr
  is
  noErr
  , the request was created. Other possible values include
  kNSLNotInitialized
  ,
  kNSLDuplicateSearchInProgress
  ,
  kNSLBadClientInfoPtr
  , and
  kNSLErrNullPtrError
  (if the value of
  infoPtr
  is
  NULL
  ). Call
  NSLErrorToString
  to get a problem and a solution string.
  ```

  ```
  Discussion
  This function creates a search request that your application later provides as a parameter when it calls
  NSLStartNeighborhoodLookup
  or
  NSLStartServicesLookup
  . Searches are conducted asynchronously.
  Your application’s notification routine will be called when the result buffer contains data, the result buffer is full, when the search is complete, or when an error occurs. Your application can cause your application’s notification routine to be called at a specified interval, when a specified number of items is in the result buffer, or when a specified amount of time has elapsed by modifying the value of the
  alertInterval
  ,
  alertThreshold
  , and
  maxSearchTime
  fields, respectively, of the
  NSLClientAsyncInfo
  structure pointed to by
  infoPtr
  .
  If this function returns a result code of
  kNSLDuplicateSearchInProgress
  , a search is in progress that is using a request reference that is identical to the newly created request reference. Your application can ignore this warning and use the newly created request reference, delete the newly created request reference, or cancel the search that is using the identical request reference.
  ```

  ```
  Special Considerations
  When your application no longer needs the request reference, it should call
  NSLDeleteRequest
  to reclaim memory associated with it.
  ```
- 

  Deregisters a service.

  ```
  OSStatus NSLStandardDeregisterURL (
  NSLPath urlToDeregister,
  NSLNeighborhood neighborhoodToDeregisterIn);
  ```

  ```
  Parameters
  urlToDeregister
  On input, a value of type
  NSLPath
  specifying the URL that is to be deregistered.
  neighborhoodToDeregisterIn
  On input, a value of type
  NSLNeighborhood
  specifying the neighborhood in which to deregister the service, or
  NULL
  . If
  NULL
  is specified, the Network Services Location Manager determines the neighborhood from which the service is deregistered.
  function result
  A value of
  noErr
  indicates that the service was deregistered. A value of
  kNSLBadURLSyntax
  indicates that the URL contains characters that are not allowed, such as spaces. To encode characters that are not allowed, call
  NSLHexEncodeText
  .
  ```

  ```
  Discussion
  This function deregisters the service specified by
  urlToDeregister
  . An application that registers services by calling
  NSLStandardRegisterURL
  should call this function as part of its standard shutdown procedure.
  ```

  ```
  Special Considerations
  You do not have to call
  NSLOpenNavigationAPI
  before calling this function.
  This function is available in version 1.1 of the Network Services Location Manager and later, and supersedes the
  NSLDeRegisterService
  function, which was provided in version 1.0.
  ```
- 

  Displays a dialog box that searches for services and allows the selection of a URL.

  ```
  OSStatus NSLStandardGetURL (
  NSLDialogOptions * dialogOptions,
  NSLEventUPP eventProc,
  void * eventProcContextPtr,
  NSLURLFilterUPP filterProc,
  char * serviceTypeList,
  char ** userSelectedURL);
  ```

  ```
  Parameters
  dialogOptions
  On input, a pointer to an
  NSLDialogOptions
  whose fields control the appearance of the dialog box. Before calling this function, call
  NSLGetDefaultDialogOptions
  to fill the fields of your
  NSLDialogOptions
  structure with the default values. Then customize the values of the fields of the
  NSLDialogOptions
  structure as desired.
  eventProc
  On input, a value of type
  NSLEventUPP
  that points to an application-defined system event callback,
  NSLEventProcPtr
  , or
  NULL
  . If
  eventProc
  is
  NULL
  , your application will not receive update events while the
  NSLStandardGetURL
  dialog box is displayed.
  eventProcContextPtr
  On input, an untyped pointer to arbitrary data that the Network Services Location Manager passes to the system event callback specified by
  eventProc
  . Your application can use
  eventProcContextPtr
  to associate any particular execution of your system event callback function with any particular call to this function.
  filterProc
  On input, a value of type
  NSLURLFilterUPP
  that specifies your filter callback function,
  NSLFilterProcPtr
  , or
  NULL
  if you do not have a filter callback function. If specified, your filter callback function will be called for each URL that is about to be displayed in the dialog box. If your filter callback function returns
  TRUE
  , the URL is displayed in the
  NSLStandardGetURL
  dialog box. If your filter callback function returns
  FALSE
  , the URL is not displayed.
  userSelectedURL
  On input, the address of a pointer to a string that will receive the URL that the user may select or enter. On output, if this function returns
  noErr
  ,
  userSelectedURL
  contains the null-terminated URL the user selected. When your application no longer needs
  userSelectedURL
  , it should call
  NSLFreeURL
  to reclaim the memory associated with it.
  serviceTypeList
  On input, a null-terminated string of tuples that describes the services that are to be searched for. See the Discussion section for a description of the format and for information on how to use
  serviceTypeList
  to control the icon that is displayed for each service type.
  function result
  A value of
  noErr
  indicates that the user selected a URL, which is stored in the
  userSelectedURL
  parameter. A value of
  kNSLUserCanceled
  indicates that the user clicked the Cancel button in the dialog box; the
  userSelectedURL
  parameter is empty.
  ```

  ```
  Discussion
  This function displays a dialog box that allows the user to select the type of service that is to be searched for and the neighborhood in which the search is to be conducted. The calling application is responsible for specifying the list of services types, and the Network Services Location Manager is responsible for displaying the neighborhoods, which it obtains by querying Open Directory.
  The
  serviceTypeList
  parameter consists of service names and service descriptor lists in the following format:
  service-name
  ,
  service-descriptor-list
  ;
  where
  service-descriptor-list
  is a comma-delimited list of services. For example, if you want to search for HTTP, HTTPS, and FTP services, the value of
  serviceTypeList
  would be
  Web Servers,http,https;FTP Servers,ftp
  Setting
  serviceTypeList
  in this way would cause the Show pop-up menu in the dialog box displayed by this function to contain two items: “Web Servers” and “FTP Servers”. The result of a search performed on these two items would consist of the list of HTTP and HTTPS services that were found, followed by the list of FTP services that were found.
  This function displays a unique icon for each of the http, https, ftp, afp, lpr, LaserWriter, and AFPServer service descriptors and the same generic icon for any other service descriptor. You can have your own icon displayed by specifying an icon suite resource ID in the
  serviceTypeList
  parameter. For example, if the value of
  serviceTypeList
  is
  Web Servers,http,https;Telnet Servers,telnet;NFS Servers,nfs,129
  the Network Services Location Manager’s unique icons will be displayed for HTTP and HTTPS services, the Network Services Location Manager’s generic icon will be displayed for Telnet services, and the icon suite at resource ID 129 in your application’s resource fork will be displayed for NFS services.
  ```

  ```
  Special Considerations
  Be sure to dispose of the
  userSelectedURL
  parameter by calling
  NSLFreeURL
  when
  userSelectedURL
  is no longer needed.
  ```
- 

  Registers the URL of a service.

  ```
  OSStatus NSLStandardRegisterURL (
  NSLPath urlToRegister,
  NSLNeighborhood neighborhoodToRegisterIn);
  ```

  ```
  Parameters
  urlToRegister
  On input, a value of type
  NSLPath
  specifying the URL to register.
  neighborhoodToRegisterIn
  On input, a value of type
  NSLNeighborhood
  specifying the neighborhood in which to register the service, or
  NULL
  . If
  NULL
  is specified, the Network Services Location Manager determines the neighborhood in which the URL is registered.
  function result
  A value of
  noErr
  indicates that the service was registered. A value of
  kNSLBadURLSyntax
  indicates that the URL contains characters that are not allowed, such as spaces. To encode characters that are not allowed, call
  NSLHexEncodeText
  .
  ```

  ```
  Discussion
  This function registers the specified URL with the Network Services Location Manager.
  Applications that provide a network service typically call this function as part of their startup procedure. They also call
  NSLStandardDeregisterURL
  as part of their shutdown procedure.
  ```

  ```
  Special Considerations
  You do not have to call
  NSLOpenNavigationAPI
  before calling this function.
  This function is available in version 1.1 and later of the Network Services Location Manager, and supersedes the
  NSLRegisterService
  function, which was provided in version 1.0.
  ```
- 

  Starts a search for neighborhoods.

  ```
  NSLError NSLStartNeighborhoodLookup (
  NSLRequestRef ref,
  NSLNeighborhood neighborhood,
  NSLClientAsyncInfo *asyncInfo);
  ```

  ```
  Parameters
  ref
  On input, a value of type
  NSLRequestRef
  created by previously calling
  NSLPrepareRequest
  .
  neighborhood
  On input,
  NULL
  or an
  NSLNeighborhood
  value created by previously calling
  NSLMakeNewNeighborhood
  . Passing
  NULL
  or a
  neighborhood
  parameter that was created with a
  name
  parameter whose value was
  NULL
  causes this function to get the default neighborhoods. If
  neighborhood
  was created with a value of
  name
  that is the name of a neighborhood, this function gets names related to that neighborhood. For example, if
  neighborhood
  was created with
  name
  set to “apple.com”, this function gets the subdomains of apple.com.
  asyncInfo
  On input, a pointer to an
  NSLClientAsyncInfo
  structure. Neighborhoods that are found will be stored in the structure’s
  resultBuffer
  field.
  function result
  An
  NSLError
  structure whose
  theErr
  field contains the result code. If the value of
  NSLError.theErr
  is
  noErr
  , this function successfully started a neighborhood search. Possible errors are
  kNSLNotInitialized
  ,
  kNSLSearchAlreadyInProgress
  ,
  kNSLNoPluginsForSearch
  ,
  kNSLBufferTooSmallForData
  , and
  kNSLNullNeighborhoodPtr
  . Call
  NSLErrorToString
  to get a problem and a solution string.
  ```

  ```
  Discussion
  This function starts a search for neighborhoods that your application can use to define the scope of a subsequent service search. The result of the search is returned to your application in the
  resultBuffer
  field of the
  NSLClientAsyncInfo
  structure pointed to by the
  asyncInfo
  parameter when the Network Services Location Manager calls your application’s notification routine. Call
  NSLGetNextNeighborhood
  to process the data in the result buffer. To cancel an ongoing search, call
  NSLCancelRequest
  . To delete a search request reference, call
  NSLDeleteRequest
  .
  When the Network Services Location Manager calls your application’s notification routine, it should check the value of the
  searchState
  field of the
  NSLClientAsyncInfo
  structure pointed to by the
  asyncInfo
  parameter. The
  searchState
  field will contain one of these values:
  kNSLSearchStateBufferFull
  ,
  kNSLSearchStateOnGoing
  ,
  kNSLSearchStateComplete
  , or
  kNSLSearchStateStalled
  .
  If the value of the searchState field is
  kNSLSearchStatausBufferFull
  , your application’s notification routine should process the data returned in the
  resultBuffer
  field of the
  NSLClientAsyncInfo
  structure and return.
  If the value of the
  searchState
  field is
  kNSLSearchStateOnGoing
  , the threshold set by the value of the
  alertInterval
  field or the
  alertThreshold
  field of the
  NSLClientAsyncInfo
  structure has been reached. Your application’s notification routine should process the data returned in the
  resultBuffer
  field of the
  NSLClientAsyncInfo
  structure and return.
  If the value of the
  searchState
  field is
  kNSLSearchStateComplete
  and the value of
  NSLError.theErr
  returned by
  NSLStartNeighborhoodLookup
  is
  noErr
  , the search is complete. Your application’s notification routine should process the data returned in
  resultBuffer
  and return. If the value of the
  searchState
  field is
  kNSLSearchStateComplete
  and the value of
  NSLError.theErr
  returned by
  NSLStartNeighborhoodLookup
  is not
  noErr
  , the error is a fatal error and the search has ended.
  If the value of the
  searchState
  field is
  kNSLSearchStateStalled
  , the threshold set by the value of the
  alertInterval
  field or the
  maxSearchTime
  field of the
  NSLClientAsyncInfo
  structure has been reached and there is no data in the result buffer. The Network Services Location Manager plug-ins that are processing this neighborhood search request are waiting to receive data from a server and may eventually time out. You can cancel the request by calling
  NSLCancelRequest
  .
  If the value of
  NSLError.theErr
  returned by this function is
  kNSLBufferTooSmallForData
  , the value of the
  maxBufferSize
  field of the
  NSLClientAsyncInfo
  structure is too small to hold data that would otherwise have been returned. Your notification routine can cancel the search, modify the size of the buffer, and restart the search, or it can ignore the error and return, thereby resuming the search even though some data has been lost.
  ```

  ```
  Special Considerations
  For any request reference, only one neighborhood or service search can be in progress at any one time.
  If this function returns an error, the
  resultBuffer
  field of the
  NSLClientAsyncInfo
  structure may still contain valid data that was collected before the error occurred. Your notification routine should process the data in the result buffer and return, thereby continuing the search.
  ```
- 

  Starts a search for services.

  ```
  NSLError NSLStartServicesLookup (
  NSLRequestRef ref,
  NSLNeighborhood neighborhood,
  NSLTypedDataPtr requestData,
  NSLClientAsyncInfo *asyncInfo);
  ```

  ```
  Parameters
  ref
  On input, a value of type
  NSLRequestRef
  containing a request reference obtained by previously calling
  NSLPrepareRequest
  .
  neighborhood
  On input,
  NULL
  or an
  NSLNeighborhood
  value created by previously calling
  NSLMakeNewNeighborhood
  . Passing
  NULL
  or a neighborhood created with a
  name
  parameter whose value was
  NULL
  causes this function to start a search for top-level services.
  requestData
  On input, a value of type
  NSLTypedDataPtr
  that describes the search parameters. To format
  requestData
  properly, call
  NSLMakeServicesRequestPB
  .
  asyncInfo
  On input, a pointer to a
  NSLClientAsyncInfo
  structure obtained by previously calling
  NSLPrepareRequest
  .
  function result
  An
  NSLError
  structure whose
  theErr
  field contains the result code. If the value of
  NSLError.theErr
  is
  noErr
  , this function successfully started a service search. Other possible values are
  kNSLNotInitialized
  ,
  kNSLSearchAlreadyInProgress
  ,
  kNSLNoPluginsForSearch
  ,
  kNSLNullNeighborhoodPtr
  , and
  kNSLBufferTooSmallForData
  . Call
  NSLErrorToString
  to get a problem and a solution string.
  ```

  ```
  Discussion
  This function starts a service search. The result of the search is returned to your application in the
  resultBuffer
  field of the
  NSLClientAsyncInfo
  structure pointed to by the
  asyncInfo
  parameter when the Network Services Location Manager calls your application’s notification routine. Call
  NSLGetNextURL
  to process the data in the result buffer. To cancel an ongoing search, call
  NSLCancelRequest
  . To delete a search request reference, call
  NSLDeleteRequest
  .
  When the Network Services Location Manager calls your application’s notification routine, it should check the value of the
  searchState
  field of the
  NSLClientAsyncInfo
  structure pointed to by the
  asyncInfo
  parameter. The
  searchState
  field will contain one of these values:
  kNSLSearchStateBufferFull
  ,
  kNSLSearchStateOnGoing
  ,
  kNSLSearchStateComplete
  , or
  kNSLSearchStateStalled
  .
  If the value of the
  searchState
  field is
  kNSLSearchStatausBufferFull
  , your application’s notification routine should process the data in the
  resultBuffer
  field of the
  NSLClientAsyncInfo
  structure and return.
  If the value of the
  searchState
  field is
  kNSLSearchStateOnGoing
  , the threshold set by the value of the
  alertInterval
  field or the
  alertThreshold
  field of the
  NSLClientAsyncInfo
  structure has been reached. Your application’s notification routine should process the data in the
  resultBuffer
  field and return.
  If the value of the
  searchState
  field is
  kNSLSearchStateComplete
  and the value of
  NSLError.theErr
  returned by
  NSLStartServicesLookup
  is
  noErr
  , the search is complete. Your application’s notification routine should process the data returned in
  resultBuffer
  and return. If the value of the
  searchState
  field is
  kNSLSearchStateComplete
  and the value of
  NSLError.theErr
  returned by
  NSLStartServicesLookup
  is not
  noErr
  , the error is a fatal error and the search has ended.
  If the value of the
  searchState
  field is
  kNSLSearchStateStalled
  , the threshold set by the value of the
  alertInterval
  field or the
  maxSearchTime
  field of the
  NSLClientAsyncInfo
  structure has been reached and there is no data in the result buffer. The Network Services Location Manager plug-ins that are processing this request are waiting to receive data from a server and may eventually time out. You can cancel the request by calling
  NSLCancelRequest
  . If the value of the
  searchState
  field is
  noErr
  , your application’s notification routine should ignore the notification and return immediately, thereby resuming the search.
  If the value of
  NSLError.theErr
  returned by this function is
  kNSLBufferTooSmallForData
  , the value of the
  maxBufferSize
  field of the
  NSLClientAsyncInfo
  structure is too small to hold data that would otherwise have been placed in the result buffer. Your application’s notification routine can cancel the search, modify the size of the buffer, and start the lookup again, or it can ignore the error and return, thereby resuming the search even though some data has been lost.
  ```

  ```
  Special Considerations
  For any request reference, only one neighborhood or service search can be ongoing at any one time.
  If this function returns an error, the
  resultBuffer
  field of the
  NSLClientAsyncInfo
  structure may still contain valid data that was collected before the error occurred. Your notification routine should process the data in the result buffer and return, thereby continuing the search.
  ```
- 

  Determines whether a service is in a services list.

  ```
  Boolean NSLServiceIsInServiceList (
  NSLServicesList serviceList,
  NSLServiceType svcToFind);
  ```

  ```
  Parameters
  serviceList
  On input, a value of type
  NSLServicesList
  created by previously calling
  NSLMakeNewServicesList
  .
  svcToFind
  On input, a value of type
  NSLServiceType
  specifying the service that is to be checked.
  function result
  A value of
  TRUE
  indicates that the service specified by
  svcToFind
  is in the services list specified by
  serviceList
  ; otherwise, the value returned is
  FALSE
  .
  ```

  ```
  Discussion
  This utility function determines whether the service specified by
  svcToFind
  is in the services list specified by
  serviceList
  .
  ```

[Next](NSL33.md)[Previous](Introduction%20to%20Network%20Services%20Location%20Manager.md)

