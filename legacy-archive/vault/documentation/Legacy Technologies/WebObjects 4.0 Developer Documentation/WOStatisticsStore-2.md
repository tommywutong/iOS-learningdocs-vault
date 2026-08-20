---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/WOStatisticsStore.html
archived_at: '2026-07-18T01:28:54.672376Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WOSessionStore-2.md)
[!](EOEditingContext%20Additions.md)

---

# WOStatisticsStore

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
WebObjects/WOStatisticsStore.h

---

## Class Description

The WOStatisticsStore object records statistics about a WebObjects application while that application runs. All WebObjects applications have a WOStatisticsStore object, which you can access by sending [__statisticsStore__](WOApplication-2.md#apple-haytmna) to the WOApplication object.

---

## Recording Information

The WOStatisticsStore object records the bulk of its statistics at the end of each cycle of the request-response loop. Specifically, at the end of WOSession's [__appendToResponse:inContext:__](WOSession-2.md#apple-gyyq) method, the WOSession sends the [__recordStatisticsForResponse:inContext:__](#apple-ha3a) message to the WOStatisticsStore. This message tells the WOStatisticsStore to begin recording statistics. Then, WOSession sends it a [__descriptionForResponse:inContext:__](#apple-gyza) message. This method sends the response component a [__descriptionForResponse:inContext:__](WOComponent-2.md#apple-ha4q) message. The default implementation of __descriptionForResponse:inContext:__  in WOComponent returns the component's name.

You can override __descriptionForResponse:inContext:__  in each of your components if you want to record more information. For example, you might want to record the values of all of the component's variables or perhaps just one or two key variables.

If you want to record extra information about the session, you can override WOStatisticsStore's __recordStatisticsForResponse:inContext:__  method.

---

## Maintaining a Log File

You can maintain an application log file by sending the message [__setLogFile:rotationFrequencyInDays:__](#apple-heya) to the WOStatisticsStore object. When a log file has been specified, each session records information in the log file about the pages it accessed.

The log is maintained in Common Log File Format (CLFF) so that it can be analyzed by any standard CLFF-analysis tool. (For more information about the statistics recorded in the log file, see the [__formatDescription:forResponse:inContext:__](#apple-gy3a) method description.) If a log file has been specified, the WOSession object keeps its own statistics about which pages it has accessed. When the session terminates, it writes this information to the log file.

---

## Method Types

**Recording information**

**[- recordStatisticsForResponse:inContext:](#apple-ha3a)

**[- descriptionForResponse:inContext:](#apple-gyza)

**[- setSessionMovingAverageSampleSize:](#apple-he2a)

**[- transactionMovingAverageSampleSize](#apple-gm3tsmy)********

**Retrieving information**

**[- statistics](#apple-gizdqmq)**

**Maintaining a CLFF log file**

**[- setLogFile:rotationFrequencyInDays:](#apple-heya)

**[- logFileRotationFrequencyInDays](#apple-g42a)

**[- logFile](#apple-g4ya)******

**Recording information in the CLFF log file**

**[- formatDescription:forResponse:inContext:](#apple-gy3a)

**[- logString:](#apple-g44a)****

**Securing access to the WOStats page**

**[- setPassword:](#apple-he4a)

**[- validateLogin:forSession:](#apple-geydm)****

---

## Instance Methods

---

### descriptionForResponse:inContext:

- (NSString \*)`descriptionForResponse:`(WOResponse \*)_aResponse_`inContext:`(WOContext \*)_aContext_

Records information about the current response by sending the [__descriptionForResponse:inContext:__](WOComponent-2.md#apple-ha4q) message to the response page and returning the result. This method is invoked at the end of the request-response loop in WOSession's [__appendToResponse:inContext:__](WOSession-2.md#apple-gyyq) method, after the [__recordStatisticsForResponse:inContext:__](#apple-ha3a) method.

---

### formatDescription:forResponse:inContext:

- (NSString \*)`formatDescription:`(NSString \*)_responseDescription_`forResponse:`(WOResponse \*)_aResponse_`inContext:`(WOContext \*)_aContext_

If log file recording is enabled, this method formats the string _responseDescription_ in using Common Log File Format (CLFF). The resulting string contains:

- The host from which the HTTP request was received
- The name of the user that performed the request
- The current date
- The request's HTTP method (GET or PUT)
- The WebObjects application name
- The result of the [__descriptionForResponse:inContext:__](#apple-gyza) method (by default, this method returns the response component's name)
- The request's HTTP version
- The HTTP status of the response
- The size of the response

You enable log file recording by setting a log file using the [__setLogFile:rotationFrequencyInDays:__](#apple-heya) method.

This method is used by WOSession to record information about the current transaction when log file recording is enabled.

__See also:__
[- __logFile__](#apple-g4ya), [- __logString:__](#apple-g44a)

---

### logFile

- (NSString \*)`logFile`

Returns the full path to the CLFF log file. This log file does not exist unless you send [__setLogFile:rotationFrequencyInDays:__](#apple-heya) to the WOStatisticsStore.

__See also:__
[- __formatDescription:forResponse:inContext:__](#apple-gy3a), [- __logFileRotationFrequencyInDays__](#apple-g42a),
[- __logString:__](#apple-g44a)

---

### logFileRotationFrequencyInDays

- (double)`logFileRotationFrequencyInDays`

The number of days a log file lasts. That is, a log file's contents are flushed after a certain time interval to ensure that it does not grow too large and a new log file is started. This method returns that time interval.

Before a new log file is started, the contents of the current log file are saved to a backup file. You can then inspect this log file and/or remove it when its data has grown stale.

__See also:__
[- __setLogFile:rotationFrequencyInDays:__](#apple-heya)

---

### logString:

- (void)`logString:`(NSString \*)_aString_

Writes the string _aString_ to the CLFF log file specified by [__logFile__](#apple-g4ya). The method is used to record a session's statistics when that session ends. You can also use it to record any string to the log file that might be helpful to you.

__See also:__
[- __formatDescription:forResponse:inContext:__](#apple-gy3a)

---

### sessionMovingAverageSampleSize

- (int)`sessionMovingAverageSampleSize`

Returns the sample size used to compute moving average statistics for each session. The WOStatisticsStore object uses this sample size to compute the response time for the last _n_ transactions and the idle time between the last _n_ transactions, where _n_ is the number returned by this method. The default sample size is 10.

__See also:__
[- __setSessionMovingAverageSampleSize:__](#apple-he2a)

---

### recordStatisticsForResponse:inContext:

- (void)`recordStatisticsForResponse:`(WOResponse \*)_aResponse_ `inContext:`(WOContext \*)_aContext_

Records statistics for the current cycle of the request-response loop. This method is invoked at the end of WOSession's [__appendToResponse:inContext:__](WOSession-2.md#apple-gyyq) method, immediately before the [__descriptionForResponse:inContext:__](#apple-gyza) method. By default, this method records the name of the response page for later use by __descriptionForResponse:inContext:__ . You can override it if you want to record more information about the session before the current request and response are deallocated. You must begin your implementation by invoking the superclass method.

---

### setLogFile:rotationFrequencyInDays:

- (void)`setLogFile:`(NSString \*)_filePath_ `rotationFrequencyInDays:`(double)_logRotation_

Sets the full path of the log file to which CLFF statistics will be recorded to _filePath_. The _logRotation_ argument specifies the number of days statistics will be recorded to this log file. Every _logRotation_ days, the contents of the current log file are saved to a backup file and a new log file is started.

The default is not to record information to a log file.

__See also:__
[- __logFile__](#apple-g4ya), [- __logFileRotationFrequencyInDays__](#apple-g42a)

---

### setSessionMovingAverageSampleSize:

- (void)`setSessionMovingAverageSampleSize:`(int)_aSize_

Sets the moving average sample size for each session to _aSize_. The WOStatisticsStore object uses this sample size to compute the response time for the last _aSize_ transactions and the idle time between the last _aSize_ transactions.

The default moving average session sample size is 10 transactions.

__See also:__
[- __sessionMovingAverageSampleSize__](#apple-haza)

---

### setPassword:

- (void)`setPassword:`(NSString \*)_aPassword_

Implements security for the WOStats page by setting its password to _aPassword_. By default, there is no password, so any user can access the WOStats page (provided they know the URL). If you implement this method, when you enter the WOStats URL, a login panel appears. You can leave the User name field blank; as long as you type the appropriate password in the password field, the WOStats page will appear.

__See also:__
[- __validateLogin:forSession:__](#apple-geydm)

---

### setTransactionMovingAverageSampleSize:

- (void)`setTransactionMovingAverageSampleSize:`(int)_aSize_

Sets the moving average sample size for each transaction to _aSize_. The WOStatisticsStore object uses this sample size to compute the response time for the last _aSize_ transactions and the idle time between the last _aSize_ transactions.

The default moving average transaction sample size is 100 transactions.

__See also:__
[- __transactionMovingAverageSampleSize__](#apple-gm3tsmy)

---

### statistics

- (NSDictionary \*)`statistics`

Returns a dictionary containing the statistics that the WOStatisticsStore records. See the section "The Statistics Dictionary" in the class description for more information on the type of information recorded as well as the keys to this dictionary.

The averages that are displayed by this method are not computed until this method is invoked. Therefore, invoking this method is costly and should not be done at every request.

---

### transactionMovingAverageSampleSize

- (int)`transactionMovingAverageSampleSize`

Returns the sample size used to compute moving average statistics for each transaction. The WOStatisticsStore object uses this sample size to compute the response time for the last _n_ transactions and the idle time between the last _n_ transactions, where _n_ is the number returned by this method. The default sample size is 100.

__See also:__
[- __setTransactionMovingAverageSampleSize:__](#apple-gm3tmoi)

---

### validateLogin:forSession:

- (BOOL)`validateLogin:`(NSString \*)_string_ `forSession:`(WOSession \*)_aSession_

Returns YES if _string_ is the password set by [__setPassword:__](#apple-he4a), and NO otherwise. The password controls if the user can see the WOStats page.

****

---

[!](WOSessionStore-2.md)
[!](EOEditingContext%20Additions.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
