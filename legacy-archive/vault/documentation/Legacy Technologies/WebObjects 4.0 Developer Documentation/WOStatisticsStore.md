---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/WOStatisticsStore.html
archived_at: '2026-07-18T01:28:52.665591Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](WOSessionStore.md)
[!](WOActionResults.md)

---

# WOStatisticsStore

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.webobjects

---

## Class Description

The WOStatisticsStore object records statistics about a WebObjects application while that application runs. All WebObjects applications have a WOStatisticsStore object, which you can access by sending [statisticsStore](WOApplication.md#apple-haytmna) to the WOApplication object.

---

## Recording Information

The WOStatisticsStore object records the bulk of its statistics at the end of each cycle of the request-response loop. Specifically, at the end of WOSession's [`appendToResponse`](WOSession.md#apple-gyyq) method, the WOSession sends the [`recordStatisticsForResponse`](#apple-ha3a) message to the WOStatisticsStore. This message tells the WOStatisticsStore to begin recording statistics. Then, WOSession sends it a [`descriptionForResponse`](#apple-gyza) message. This method sends the response component a [`descriptionForResponse`](WOComponent.md#apple-ha4q) message. The default implementation of `descriptionForResponse` in WOComponent returns the component's name.

You can override `descriptionForResponse` in each of your components if you want to record more information. For example, you might want to record the values of all of the component's variables or perhaps just one or two key variables.

If you want to record extra information about the session, you can override WOStatisticsStore's `recordStatisticsForResponse:inContext:` method.

---

## Maintaining a Log File

You can maintain an application log file by sending the message [`setLogFile`](#apple-heya) to the WOStatisticsStore object. When a log file has been specified, each session records information in the log file about the pages it accessed.

The log is maintained in Common Log File Format (CLFF) so that it can be analyzed by any standard CLFF-analysis tool. (For more information about the statistics recorded in the log file, see the [`formatDescription`](#apple-gy3a) method description.) If a log file has been specified, the WOSession object keeps its own statistics about which pages it has accessed. When the session terminates, it writes this information to the log file.

---

## Method Types

**Constructor**

**[WOStatisticsStore](#apple-haydooi)**

**Recording information**

**[recordStatisticsForResponse](#apple-ha3a)

**[descriptionForResponse](#apple-gyza)

**[setSessionMovingAverageSampleSize](#apple-he2a)

**[transactionMovingAverageSampleSize](#apple-gm3tsmy)********

**Retrieving information**

**[statistics](#apple-gizdqmq)**

**Maintaining a CLFF log file**

**[setLogFile](#apple-heya)

**[logFileRotationFrequencyInDays](#apple-g42a)

**[logFile](#apple-g4ya)******

**Recording information in the CLFF log file**

**[formatDescription](#apple-gy3a)

**[logString](#apple-g44a)****

**Securing access to the WOStats page**

**[setPassword](#apple-he4a)

**[validateLogin](#apple-geydm)****

---

## Constructors

---

### WOStatisticsStore

public `WOStatisticsStore`()

Returns an initialized WOStatisticsStore.

---

## Instance Methods

---

### descriptionForResponse

public java.lang.String `descriptionForResponse`(WOResponse _aResponse_, WOContext _aContext_)

Records information about the current response by sending the [`descriptionForResponse`](WOComponent.md#apple-ha4q) message to the response page and returning the result. This method is invoked at the end of the request-response loop in WOSession's [`appendToResponse`](WOSession.md#apple-gyyq) method, after the [`recordStatisticsForResponse`](#apple-ha3a) method.

---

### formatDescription

public java.lang.String `formatDescription`(java.lang.String _responseDescription_, WOResponse _aResponse_,
WOContext _aContext_)

If log file recording is enabled, this method formats the string _responseDescription_ in using Common Log File Format (CLFF). The resulting string contains:

- The host from which the HTTP request was received
- The name of the user that performed the request
- The current date
- The request's HTTP method (GET or PUT)
- The WebObjects application name
- The result of the [`descriptionForResponse`](#apple-gyza) method (by default, this method returns the response component's name)
- The request's HTTP version
- The HTTP status of the response
- The size of the response

You enable log file recording by setting a log file using the [`setLogFile`](#apple-heya) method.

This method is used by WOSession to record information about the current transaction when log file recording is enabled.

__See also:__
[`logFile`](#apple-g4ya), [`logString`](#apple-g44a)

---

### logFile

public java.lang.String `logFile`()

Returns the full path to the CLFF log file. This log file does not exist unless you send [`setLogFile`](#apple-heya) to the WOStatisticsStore.

__See also:__
[`formatDescription`](#apple-gy3a), [`logFileRotationFrequencyInDays`](#apple-g42a), [`logString`](#apple-g44a)

---

### logFileRotationFrequencyInDays

public double `logFileRotationFrequencyInDays`()

The number of days a log file lasts. That is, a log file's contents are flushed after a certain time interval to ensure that it does not grow too large and a new log file is started. This method returns that time interval.

Before a new log file is started, the contents of the current log file are saved to a backup file. You can then inspect this log file and/or remove it when its data has grown stale.

__See also:__
[`setLogFile`](#apple-heya)

---

### logString

public void `logString`(java.lang.String _aString_)

Writes the string _aString_ to the CLFF log file specified by [`logFile`](#apple-g4ya). The method is used to record a session's statistics when that session ends. You can also use it to record any string to the log file that might be helpful to you.

__See also:__
[`formatDescription`](#apple-gy3a)

---

### sessionMovingAverageSampleSize

public int `sessionMovingAverageSampleSiz`e()

Returns the sample size used to compute moving average statistics for each session. The WOStatisticsStore object uses this sample size to compute the response time for the last _n_ transactions and the idle time between the last _n_ transactions, where _n_ is the number returned by this method. The default sample size is 10.

__See also:__
[`setSessionMovingAverageSampleSize`](#apple-he2a)

---

### recordStatisticsForResponse

public void `recordStatisticsForResponse`(WOResponse _aResponse_, WOContext _aContext_)

Records statistics for the current cycle of the request-response loop. This method is invoked at the end of WOSession's [`appendToResponse`](WOSession.md#apple-gyyq) method, immediately before the [`descriptionForResponse`](#apple-gyza) method. By default, this method records the name of the response page for later use by `descriptionForResponse:inContext:`. You can override it if you want to record more information about the session before the current request and response are deallocated. You must begin your implementation by invoking the superclass method.

---

### setLogFile

public void `setLogFile`(java.lang.String _filePath_, double _logRotation_)

Sets the full path of the log file to which CLFF statistics will be recorded to _filePath_. The _logRotation_ argument specifies the number of days statistics will be recorded to this log file. Every _logRotation_ days, the contents of the current log file are saved to a backup file and a new log file is started.

The default is not to record information to a log file.

__See also:__
[`logFile`](#apple-g4ya), [`logFileRotationFrequencyInDays`](#apple-g42a)

---

### setSessionMovingAverageSampleSize

public void `setSessionMovingAverageSampleSize`(int _aSize_)

Sets the moving average sample size for each session to _aSize_. The WOStatisticsStore object uses this sample size to compute the response time for the last _aSize_ transactions and the idle time between the last _aSize_ transactions.

The default moving average session sample size is 10 transactions.

__See also:__
[`sessionMovingAverageSampleSize`](#apple-haza)

---

### setPassword

public void `setPassword`(java.lang.String _aPassword_)

Implements security for the WOStats page by setting its password to _aPassword_. By default, there is no password, so any user can access the WOStats page (provided they know the URL). If you implement this method, when you enter the WOStats URL, a login panel appears. You can leave the User name field blank; as long as you type the appropriate password in the password field, the WOStats page will appear.

__See also:__
[`validateLogin`](#apple-geydm)

---

### setTransactionMovingAverageSampleSize

public void `setTransactionMovingAverageSampleSize`(int _aSize_)

Sets the moving average sample size for each transaction to _aSize_. The WOStatisticsStore object uses this sample size to compute the response time for the last _aSize_ transactions and the idle time between the last _aSize_ transactions.

The default moving average transaction sample size is 100 transactions.

__See also:__
[`transactionMovingAverageSampleSize`](#apple-gm3tsmy)

---

### statistics

public NSDictionary `statistics`()

Returns a dictionary containing the statistics that the WOStatisticsStore records.

The averages that are displayed by this method are not computed until this method is invoked. Therefore, invoking this method is costly and should not be done at every request.

---

### transactionMovingAverageSampleSize

public int `transactionMovingAverageSampleSiz`e()

Returns the sample size used to compute moving average statistics for each transaction. The WOStatisticsStore object uses this sample size to compute the response time for the last _n_ transactions and the idle time between the last _n_ transactions, where _n_ is the number returned by this method. The default sample size is 100.

__See also:__
[`setTransactionMovingAverageSampleSize`](#apple-gm3tmoi)

---

### validateLogin

public boolean `validateLogin`(java.lang.String _string_, WOSession _aSession_)

Returns `true` if _string_ is the password set by [`setPassword`](#apple-he4a), and `false` otherwise. The password controls if the user can see the WOStats page.

****

---

[!](WOSessionStore.md)
[!](WOActionResults.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
