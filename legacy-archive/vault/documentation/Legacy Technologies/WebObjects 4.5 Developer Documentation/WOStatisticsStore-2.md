---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WOStatisticsStore.html
archived_at: '2026-07-15T08:11:47.808378Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WOStatisticsStore

> __Inherits
> from:__  NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  WebObjects/WOStatisticsStore.h

---

## Class Description

---

The WOStatisticsStore object records statistics about a WebObjects
application while that application runs. All WebObjects applications
have a WOStatisticsStore object, which you can access by sending [statisticsStore](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zxiylunfzxi2ldonjxi33smu) to the WOApplication
object.

## Recording Information

The WOStatisticsStore object records the bulk of its statistics
at the end of each cycle of the request-response loop. Specifically,
at the end of WOSession's [appendToResponse:inContext:](WOSession-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnyxwc4dqmvxgivdpkjsxg4dpnzzwkotjnzbw63tumv4hioq) method, the
WOSession sends the [recordStatisticsForResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpojswg33smrjxiylunfzxi2ldondg64ssmvzxa33oonstu2loinxw45dfpb2du) message
to the WOStatisticsStore. This message tells the WOStatisticsStore
to begin recording statistics. Then, WOSession sends it a [descriptionForResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpmrsxgy3snfyhi2lpnzdg64ssmvzxa33oonstu2loinxw45dfpb2du) message.
This method sends the response component a [descriptionForResponse:inContext:](WOComponent-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3emvzwg4tjob2gs33oizxxeutfonyg63ttmu5gs3sdn5xhizlyoq5a) message.
The default implementation of __descriptionForResponse:inContext:__ in
WOComponent returns the component's name.

You can override __descriptionForResponse:inContext:__ in
each of your components if you want to record more information.
For example, you might want to record the values of all of the component's
variables or perhaps just one or two key variables.

If you want to record extra information about the session,
you can override WOStatisticsStore's __recordStatisticsForResponse:inContext:__ method.

## Maintaining a Log File

You can maintain an application log file by sending the message [setLogFile:rotationFrequencyInDays:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjponsxitdpm5dgs3dfhjzg65dboruw63sgojsxc5lfnzrxssloirqxs4z2) to
the WOStatisticsStore object. When a log file has been specified,
each session records information in the log file about the pages
it accessed.

The log is maintained in Common Log File Format (CLFF) so
that it can be analyzed by any standard CLFF-analysis tool. (For
more information about the statistics recorded in the log file,
see the [formatDescription:forResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpmzxxe3lborcgk43dojuxa5djn5xduztpojjgk43qn5xhgzj2nfxeg33oorsxq5b2) method
description.) If a log file has been specified, the WOSession object
keeps its own statistics about which pages it has accessed. When
the session terminates, it writes this information to the log file.

## Adopted Protocols

---

> NSLocking: - lock
> : - unlock

## Method Types

---

> **Recording information**
> : [- recordStatisticsForResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpojswg33smrjxiylunfzxi2ldondg64ssmvzxa33oonstu2loinxw45dfpb2du)
> : [- descriptionForResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpmrsxgy3snfyhi2lpnzdg64ssmvzxa33oonstu2loinxw45dfpb2du)
> : [- setSessionMovingAverageSampleSize:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjponsxiu3fonzws33ojvxxm2lom5axmzlsmftwku3bnvygyzktnf5gkoq)
> : [- transactionMovingAverageSampleSize](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjporzgc3ttmfrxi2lpnzgw65tjnztuc5tfojqwozktmfwxa3dfknuxuzi)
>
> **Retrieving information**
> : [- statistics](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpon2gc5djon2gsy3t)
>
> **Maintaining a CLFF log
> file**
> : [- setLogFile:rotationFrequencyInDays:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjponsxitdpm5dgs3dfhjzg65dboruw63sgojsxc5lfnzrxssloirqxs4z2)
> : [- logFileRotationFrequencyInDays](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpnrxwortjnrsve33umf2gs33oizzgk4lvmvxgg6kjnzcgc6lt)
> : [- logFile](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpnrxwortjnrsq)
>
> **Recording information
> in the CLFF log file**
> : [- formatDescription:forResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpmzxxe3lborcgk43dojuxa5djn5xduztpojjgk43qn5xhgzj2nfxeg33oorsxq5b2)
> : [- logString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpnrxwou3uojuw4zz2)
>
> **Securing access to the
> WOStats page**
> : [- setPassword:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjponsxiudbonzxo33smq5a)
> : [- validateLogin:forSession:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpozqwy2lemf2gktdpm5uw4otgn5zfgzltonuw63r2)

## Instance Methods

---

### descriptionForResponse:inContext:

`- (NSString *)descriptionForResponse:(WOResponse
*)aResponse
inContext:(WOContext *)aContext`

Records information about the current response
by sending the [descriptionForResponse:inContext:](WOComponent-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3emvzwg4tjob2gs33oizxxeutfonyg63ttmu5gs3sdn5xhizlyoq5a) message
to the response page and returning the result. This method is invoked
at the end of the request-response loop in WOSession's [appendToResponse:inContext:](WOSession-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnyxwc4dqmvxgivdpkjsxg4dpnzzwkotjnzbw63tumv4hioq) method,
after the [recordStatisticsForResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpojswg33smrjxiylunfzxi2ldondg64ssmvzxa33oonstu2loinxw45dfpb2du) method.

---

### formatDescription:forResponse:inContext:

`- (NSString *)formatDescription:(NSString
*)responseDescription
forResponse:(WOResponse *)aResponse
inContext:(WOContext *)aContext`

If log file recording is enabled, this method
formats the string responseDescription in using Common Log File
Format (CLFF). The resulting string contains:

- The
  host from which the HTTP request was received
- The name of the user that performed the request
- The current date
- The request's HTTP method (GET or PUT)
- The WebObjects application name
- The result of the [descriptionForResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpmrsxgy3snfyhi2lpnzdg64ssmvzxa33oonstu2loinxw45dfpb2du) method
  (by default, this method returns the response component's name)
- The request's HTTP version
- The HTTP status of the response
- The size of the response

You enable
log file recording by setting a log file using the [setLogFile:rotationFrequencyInDays:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjponsxitdpm5dgs3dfhjzg65dboruw63sgojsxc5lfnzrxssloirqxs4z2) method.

This method is used by WOSession to record information
about the current transaction when log file recording is enabled.

__See
Also:__  [- logFile](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpnrxwortjnrsq), [- logString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpnrxwou3uojuw4zz2)

---

### logFile

`- (NSString *)logFile`

Returns the full path to the CLFF log file.
This log file does not exist unless you send [setLogFile:rotationFrequencyInDays:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjponsxitdpm5dgs3dfhjzg65dboruw63sgojsxc5lfnzrxssloirqxs4z2) to
the WOStatisticsStore.

__See Also:__  [- formatDescription:forResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpmzxxe3lborcgk43dojuxa5djn5xduztpojjgk43qn5xhgzj2nfxeg33oorsxq5b2), [- logFileRotationFrequencyInDays](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpnrxwortjnrsve33umf2gs33oizzgk4lvmvxgg6kjnzcgc6lt), [- logString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpnrxwou3uojuw4zz2)

---

### logFileRotationFrequencyInDays

`- (double)logFileRotationFrequencyInDays`

The number of days a log file lasts. That is,
a log file's contents are flushed after a certain time interval to
ensure that it does not grow too large and a new log file is started.
This method returns that time interval.

Before a new log
file is started, the contents of the current log file are saved
to a backup file. You can then inspect this log file and/or remove
it when its data has grown stale.

__See
Also:__  [- setLogFile:rotationFrequencyInDays:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjponsxitdpm5dgs3dfhjzg65dboruw63sgojsxc5lfnzrxssloirqxs4z2)

---

### logString:

`- (void)logString:(NSString
*)aString`

Writes the string _aString_ to
the CLFF log file specified by [logFile](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpnrxwortjnrsq). The method is used to record
a session's statistics when that session ends. You can also use
it to record any string to the log file that might be helpful to
you.

__See Also:__  [- formatDescription:forResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpmzxxe3lborcgk43dojuxa5djn5xduztpojjgk43qn5xhgzj2nfxeg33oorsxq5b2)

---

### recordStatisticsForResponse:inContext:

`- (void)recordStatisticsForResponse:(WOResponse
*)aResponse
inContext:(WOContext *)aContext`

Records statistics for the current cycle of
the request-response loop. This method is invoked at the end of
WOSession's [appendToResponse:inContext:](WOSession-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnyxwc4dqmvxgivdpkjsxg4dpnzzwkotjnzbw63tumv4hioq) method,
immediately before the [descriptionForResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpmrsxgy3snfyhi2lpnzdg64ssmvzxa33oonstu2loinxw45dfpb2du) method.
By default, this method records the name of the response page for
later use by __descriptionForResponse:inContext:__.
You can override it if you want to record more information about
the session before the current request and response are deallocated.
You must begin your implementation by invoking the superclass method.

---

### sessionMovingAverageSampleSize

`- (int)sessionMovingAverageSampleSize`

Returns the sample size used to compute moving
average statistics for each session. The WOStatisticsStore object
uses this sample size to compute the response time for the last
n transactions and the idle time between the last n transactions,
where n is the number returned by this method. The default sample
size is 10.

__See Also:__  [- setSessionMovingAverageSampleSize:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjponsxiu3fonzws33ojvxxm2lom5axmzlsmftwku3bnvygyzktnf5gkoq)

---

### setLogFile:rotationFrequencyInDays:

`- (void)setLogFile:(NSString
*)filePath
rotationFrequencyInDays:(double)logRotation`

Sets the full path of the log file to which
CLFF statistics will be recorded to _filePath_.
The _logRotation_ argument specifies
the number of days statistics will be recorded to this log file.
Every _logRotation_ days, the contents
of the current log file are saved to a backup file and a new log
file is started.

The default is not to record information
to a log file.

__See Also:__  [- logFile](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpnrxwortjnrsq), [- logFileRotationFrequencyInDays](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpnrxwortjnrsve33umf2gs33oizzgk4lvmvxgg6kjnzcgc6lt)

---

### setPassword:

`- (void)setPassword:(NSString
*)aPassword`

Implements security for the WOStats page by
setting its password to _aPassword_.
By default, there is no password, so any user can access the WOStats
page (provided they know the URL). If you implement this method,
when you enter the WOStats URL, a login panel appears. You can leave
the User name field blank; as long as you type the appropriate password
in the password field, the WOStats page will appear.

__See
Also:__  [- validateLogin:forSession:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjpozqwy2lemf2gktdpm5uw4otgn5zfgzltonuw63r2)

---

### setSessionMovingAverageSampleSize:

`- (void)setSessionMovingAverageSampleSize:(int)aSize`

Sets the moving average sample size for each
session to _aSize_. The WOStatisticsStore
object uses this sample size to compute the response time for the
last aSize transactions and the idle time between the last _aSize_ transactions.

The default moving average session sample size is 10 transactions.

__See
Also:__  [- sessionMovingAverageSampleSize](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjponsxg43jn5xe233wnfxgoqlwmvzgcz3fknqw24dmmvjws6tf)

---

### setTransactionMovingAverageSampleSize:

`- (void)setTransactionMovingAverageSampleSize:(int)aSize`

Sets the moving average sample size for each
transaction to _aSize_. The WOStatisticsStore
object uses this sample size to compute the response time for the
last _aSize_ transactions and the idle
time between the last _aSize_ transactions.

The default moving average transaction sample size is 100
transactions.

__See Also:__  [- transactionMovingAverageSampleSize](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjporzgc3ttmfrxi2lpnzgw65tjnztuc5tfojqwozktmfwxa3dfknuxuzi)

---

### statistics

`- (NSDictionary *)statistics`

Returns a dictionary containing the statistics
that the WOStatisticsStore records.

The averages that are displayed
by this method are not computed until this method is invoked. Therefore,
invoking this method is costly and should not be done at every request.

---

### transactionMovingAverageSampleSize

`- (int)transactionMovingAverageSampleSize`

Returns the sample size used to compute moving
average statistics for each transaction. The WOStatisticsStore object
uses this sample size to compute the response time for the last
n transactions and the idle time between the last n transactions,
where n is the number returned by this method. The default sample
size is 100.

__See Also:__  [- setTransactionMovingAverageSampleSize:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjponsxivdsmfxhgyldoruw63snn53gs3thif3gk4tbm5svgylnobwgku3jpjstu)

---

### validateLogin:forSession:

`- (BOOL)validateLogin:(NSString
*)string
forSession:(WOSession *)aSession`

Returns YES if string is the password set by [setPassword:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2torqxi2ltoruwg42torxxezjponsxiudbonzxo33smq5a), and NO otherwise.
The password controls if the user can see the WOStats page.

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
