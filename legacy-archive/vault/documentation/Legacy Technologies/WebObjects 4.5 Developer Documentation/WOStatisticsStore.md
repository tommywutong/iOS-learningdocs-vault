---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/Java/Classes/WOStatisticsStore.html
archived_at: '2026-07-15T08:11:47.188692Z'
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

> __Package:__ com.apple.yellow.webobjects

---

## Class Description

---

The WOStatisticsStore object records statistics about a WebObjects
application while that application runs. All WebObjects applications
have a WOStatisticsStore object, which you can access by sending [statisticsStore](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxg5dboruxg5djmnzvg5dpojsq) to the WOApplication
object.

## Recording Information

The WOStatisticsStore object records the bulk of its statistics
at the end of each cycle of the request-response loop. Specifically,
at the end of WOSession's [appendToResponse](WOSession.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylqobsw4zcun5jgk43qn5xhgzi) method,
the WOSession sends the [recordStatisticsForResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5zgky3pojsfg5dboruxg5djmnzum33skjsxg4dpnzzwk) message
to the WOStatisticsStore. This message tells the WOStatisticsStore
to begin recording statistics. Then, WOSession sends it a [descriptionForResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5sgk43dojuxa5djn5xem33skjsxg4dpnzzwk) message. This
method sends the response component a [descriptionForResponse](WOComponent.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmrsxgy3snfyhi2lpnzdg64ssmvzxa33oonsq) message.
The default implementation of __descriptionForResponse__ in WOComponent
returns the component's name.

You can override __descriptionForResponse__ in
each of your components if you want to record more information.
For example, you might want to record the values of all of the component's
variables or perhaps just one or two key variables.

If you want to record extra information about the session,
you can override WOStatisticsStore's __recordStatisticsForResponse__ method.

## Maintaining a Log File

You can maintain an application log file by sending the message [setLogFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5zwk5cmn5tum2lmmu) to the WOStatisticsStore object.
When a log file has been specified, each session records information
in the log file about the pages it accessed.

The log is maintained in Common Log File Format (CLFF) so
that it can be analyzed by any standard CLFF-analysis tool. (For
more information about the statistics recorded in the log file,
see the [formatDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5tg64tnmf2eizltmnzgs4dunfxw4) method
description.) If a log file has been specified, the WOSession object
keeps its own statistics about which pages it has accessed. When
the session terminates, it writes this information to the log file.

## Method Types

---

> **Constructor**
> : [WOStatisticsStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5lu6u3umf2gs43unfrxgu3un5zgk)
>
> **Recording information**
> : [recordStatisticsForResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5zgky3pojsfg5dboruxg5djmnzum33skjsxg4dpnzzwk)
> : [descriptionForResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5sgk43dojuxa5djn5xem33skjsxg4dpnzzwk)
> : [setSessionMovingAverageSampleSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5zwk5ctmvzxg2lpnzgw65tjnztuc5tfojqwozktmfwxa3dfknuxuzi)
> : [transactionMovingAverageSampleSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff52heyloonqwg5djn5xe233wnfxgoqlwmvzgcz3fknqw24dmmvjws6tf)
>
> **Retrieving information**
> : [statistics](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5zxiylunfzxi2ldom)
>
> **Maintaining a CLFF log
> file**
> : [setLogFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5zwk5cmn5tum2lmmu)
> : [logFileRotationFrequencyInDays](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5wg6z2gnfwgkutporqxi2lpnzdhezlrovsw4y3zjfxeiylzom)
> : [logFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5wg6z2gnfwgk)
>
> **Recording information
> in the CLFF log file**
> : [formatDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5tg64tnmf2eizltmnzgs4dunfxw4)
> : [logString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5wg6z2torzgs3th)
>
> **Securing access to the
> WOStats page**
> : [setPassword](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5zwk5cqmfzxg53pojsa)
> : [validateLogin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff53gc3djmrqxizkmn5tws3q)

## Constructors

---

### WOStatisticsStore

`public WOStatisticsStore()`

Returns an initialized WOStatisticsStore.

---

## Instance Methods

---

### descriptionForResponse

`public String descriptionForResponse(
WOResponse aResponse,
WOContext aContext)`

Records information about the current response
by sending the [descriptionForResponse](WOComponent.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmrsxgy3snfyhi2lpnzdg64ssmvzxa33oonsq) message
to the response page and returning the result. This method is invoked
at the end of the request-response loop in WOSession's [appendToResponse](WOSession.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylqobsw4zcun5jgk43qn5xhgzi) method,
after the [recordStatisticsForResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5zgky3pojsfg5dboruxg5djmnzum33skjsxg4dpnzzwk) method.

---

### formatDescription

`public String formatDescription(
String responseDescription,
WOResponse aResponse,
WOContext aContext)`

If log file recording is enabled, this method
formats the string responseDescription in using Common Log File
Format (CLFF). The resulting string contains:

- The
  host from which the HTTP request was received
- The name of the user that performed the request
- The current date
- The request's HTTP method (GET or PUT)
- The WebObjects application name
- The result of the [descriptionForResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5sgk43dojuxa5djn5xem33skjsxg4dpnzzwk) method (by
  default, this method returns the response component's name)
- The request's HTTP version
- The HTTP status of the response
- The size of the response

You enable
log file recording by setting a log file using the [setLogFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5zwk5cmn5tum2lmmu) method.

This
method is used by WOSession to record information about the current
transaction when log file recording is enabled.

__See
Also:__  [logFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5wg6z2gnfwgk), [logString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5wg6z2torzgs3th)

---

### lock

`public void lock()`

Locks access to the WOStatisticsStore
object.

---

### logFile

`public String logFile()`

Returns the full path to the CLFF log file.
This log file does not exist unless you send [setLogFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5zwk5cmn5tum2lmmu) to the WOStatisticsStore.

__See
Also:__  [formatDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5tg64tnmf2eizltmnzgs4dunfxw4), [logFileRotationFrequencyInDays](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5wg6z2gnfwgkutporqxi2lpnzdhezlrovsw4y3zjfxeiylzom), [logString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5wg6z2torzgs3th)

---

### logFileRotationFrequencyInDays

`public double logFileRotationFrequencyInDays()`

The number of days a log file lasts. That is,
a log file's contents are flushed after a certain time interval to
ensure that it does not grow too large and a new log file is started.
This method returns that time interval.

Before a new log
file is started, the contents of the current log file are saved
to a backup file. You can then inspect this log file and/or remove
it when its data has grown stale.

__See
Also:__  [setLogFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5zwk5cmn5tum2lmmu)

---

### logString

`public void logString(String aString)`

Writes the string _aString_ to
the CLFF log file specified by [logFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5wg6z2gnfwgk). The method is used to record
a session's statistics when that session ends. You can also use
it to record any string to the log file that might be helpful to
you.

__See Also:__  [formatDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5tg64tnmf2eizltmnzgs4dunfxw4)

---

### recordStatisticsForResponse

`public void recordStatisticsForResponse(
WOResponse aResponse,
WOContext aContext)`

Records statistics for the current cycle of
the request-response loop. This method is invoked at the end of
WOSession's [appendToResponse](WOSession.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylqobsw4zcun5jgk43qn5xhgzi) method,
immediately before the [descriptionForResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5sgk43dojuxa5djn5xem33skjsxg4dpnzzwk) method.
By default, this method records the name of the response page for
later use by __descriptionForResponse__. You
can override it if you want to record more information about the
session before the current request and response are deallocated.
You must begin your implementation by invoking the superclass method.

---

### sessionMovingAverageSampleSize

`public int sessionMovingAverageSampleSize()`

Returns the sample size used to compute moving
average statistics for each session. The WOStatisticsStore object
uses this sample size to compute the response time for the last
n transactions and the idle time between the last n transactions,
where n is the number returned by this method. The default sample
size is 10.

__See Also:__  [setSessionMovingAverageSampleSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5zwk5ctmvzxg2lpnzgw65tjnztuc5tfojqwozktmfwxa3dfknuxuzi)

---

### setLogFile

`public void setLogFile(
String filePath,
double logRotation)`

Sets the full path of the log file to which
CLFF statistics will be recorded to _filePath_.
The _logRotation_ argument specifies
the number of days statistics will be recorded to this log file.
Every _logRotation_ days, the contents
of the current log file are saved to a backup file and a new log
file is started.

The default is not to record information
to a log file.

__See Also:__  [logFile](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5wg6z2gnfwgk), [logFileRotationFrequencyInDays](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5wg6z2gnfwgkutporqxi2lpnzdhezlrovsw4y3zjfxeiylzom)

---

### setPassword

`public void setPassword(String aPassword)`

Implements security for the WOStats page by
setting its password to _aPassword_.
By default, there is no password, so any user can access the WOStats
page (provided they know the URL). If you implement this method,
when you enter the WOStats URL, a login panel appears. You can leave
the User name field blank; as long as you type the appropriate password
in the password field, the WOStats page will appear.

__See
Also:__  [validateLogin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff53gc3djmrqxizkmn5tws3q)

---

### setSessionMovingAverageSampleSize

`public void setSessionMovingAverageSampleSize(int aSize)`

Sets the moving average sample size for each
session to _aSize_. The WOStatisticsStore
object uses this sample size to compute the response time for the
last aSize transactions and the idle time between the last _aSize_ transactions.

The default moving average session sample size is 10 transactions.

__See
Also:__  [sessionMovingAverageSampleSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5zwk43tnfxw4tlpozuw4z2bozsxeylhmvjwc3lqnrsvg2l2mu)

---

### setTransactionMovingAverageSampleSize

`public void setTransactionMovingAverageSampleSize(int aSize)`

Sets the moving average sample size for each
transaction to _aSize_. The WOStatisticsStore
object uses this sample size to compute the response time for the
last _aSize_ transactions and the idle
time between the last _aSize_ transactions.

The default moving average transaction sample size is 100
transactions.

__See Also:__  [transactionMovingAverageSampleSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff52heyloonqwg5djn5xe233wnfxgoqlwmvzgcz3fknqw24dmmvjws6tf)

---

### statistics

`public NSDictionary statistics()`

Returns a dictionary containing the statistics
that the WOStatisticsStore records.

The averages that are displayed
by this method are not computed until this method is invoked. Therefore,
invoking this method is costly and should not be done at every request.

---

### transactionMovingAverageSampleSize

`public int transactionMovingAverageSampleSize()`

Returns the sample size used to compute moving
average statistics for each transaction. The WOStatisticsStore object
uses this sample size to compute the response time for the last
n transactions and the idle time between the last n transactions,
where n is the number returned by this method. The default sample
size is 100.

__See Also:__  [setTransactionMovingAverageSampleSize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5zwk5cuojqw443bmn2gs33ojvxxm2lom5axmzlsmftwku3bnvygyzktnf5gk)

---

### unlock

`public void unlock()`

Unlocks access to the WOStatisticsStore
object.

---

### validateLogin

`public boolean validateLogin(
String string,
WOSession aSession)`

Returns true if string is the password set by [setPassword](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5zwk5cqmfzxg53pojsa), and false otherwise.
The password controls if the user can see the WOStats page.

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
