---
title: 'SeismicXML: Using NSXMLParser to parse XML documents'
apple_id: DTS40007323
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2016-01-08'
source_url: https://developer.apple.com/library/archive/samplecode/SeismicXML/History/History.html
archived_at: '2026-07-18T03:23:38.952112Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SeismicXML: Using NSXMLParser to parse XML documents](SeismicXML-%20Using%20NSXMLParser%20to%20parse%20XML%20documents.md)


[Previous](SeismicXML-APLEarthQuakeSource.m.md)

# Document Revision History

This table describes the changes to _SeismicXML: Using NSXMLParser to parse XML documents_.

| __Date__ | __Notes__ |
| 2016-01-08 | Upgraded to the iOS 9.0 SDK, now uses NSURLSession, changed to a newer xml feed and updated the parser. |
| 2014-06-17 | Fixed 64-bit bug - earthquake magnitude now draws correctly. |
| 2013-09-17 | Now uses NSURLConnection's sendAsynchronousRequest API, also uses NSCurrentLocaleDidChangeNotification to detect for locale changes. |
| 2013-05-13 | Updated to use ARC and storyboards. |
| 2010-08-18 | Now using NSOperation to perform the XML parsing. |
| 2010-06-25 | Updated for and tested with iOS 4.0 SDK. Also updated artwork and added NSXMLParserDelegate protocol. |
| 2010-04-28 | Proper formatting of dates, fixed earthquake reporting URLs due to changes in USGS page, removed unused frameworks, improved error reporting, now using KVO for table view updates. |
| 2009-05-13 | Switched NSXMLParser to use initWithData: instead of initWithContentsOfURL: and implemented asynchronous NSURLConnection for download to give better control of network error handling. Consolidated parsing into app delegate for better handling of parse error callbacks and to avoid the design pattern of using the app delegate as a singleton for data access. Switched from custom UITableViewCell subclass to managing the layout with view tags to meet documented best practices. Modified Earthquake class to model numeric and date properties as numbers and dates instead of strings and merged string parsing code into the XML parsing code. Added use of the lat/lon data for opening Maps link. |
| 2008-07-03 | First public release. |
| 2008-06-08 | -Updated for Beta 7. -Fixed memory leaks in XMLReader.m. -Now uses the SystemConfiguration framework to determine if the RSS feed provider is available and displays a message in the table view if it's not. |
| 2008-05-28 | Updated for Beta 6. The custom table view cell add subviews to its content view rather than drawing them directly. |
| 2008-05-06 | -Updated for Beta 5. -Removed the XML-to-Objective-C object mapping to simplify the sample. -Moved the XML parsing to a background thread. |
| 2008-04-23 | Updated for Beta 4. Now uses NSXMLParser to parse XML. |
| 2008-04-08 | Updated for Beta 3. Revised to use new table cell API. Removed unnecessary frameworks and files. |
| 2008-03-15 | New sample that demonstrates how to use libxml SAX and DOM APIs to parse XML. |

[Previous](SeismicXML-APLEarthQuakeSource.m.md)

