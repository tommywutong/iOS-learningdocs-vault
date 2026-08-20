---
title: Quartz Composer SQLiteQuery
apple_id: DTS40009327
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2009-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/SQLiteQuery/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:22:45.109050Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Quartz Composer SQLiteQuery](Quartz%20Composer%20SQLiteQuery.md)


[Next](SQLiteQueryPlugIn.h.md)[Previous](Quartz%20Composer%20SQLiteQuery.md)

# ReadMe.txt

```
Copyright © 2007-2009 by Apple Inc.  All Rights Reserved.

Quartz Composer Plugin

SQLiteQuery                 A Quartz Composer plug-in that performs a query on a 
                        local SQLite database.

Sample Requirements             The plugin was created using the Xcode editor running 
                        under Mac OS X 10.6.x or later. 

About the sample                A Quartz Composer plug-in that queries synchronously a 
                        SQLite 3 database on disk and outputs the results as a 
                        structure. SQLite is a self-contained, serverless,
                        zero-configuration, and transactional SQL database
                        engine. SQLite reads and writes a complete SQL database
                        to a single disk file. It is a popular database engine
                        choice on memory constrained gadgets. This plug-in 
                        retrieves information from a SQLite database.
                        Given a SQLite database and a SQL query, the result 
                        will be returned. The default database path is set to 
                        Database.db which can be found in this sample.

Using the Sample                Open the project using the Xcode editor which can be found 
                        in /Developer/Applications. From the main menu, 
                        choose "Project", set "Active Configuration" to "Release", 
                        and "Active Target" to "Build & Copy".  These settings are
                        also available from the top left corner of the 'Overview' 
                        pull-down window. Build the project. Once the build has 
                        completed successfully, the plug-in can be used as a 
                        regular QC patch in the Quartz Composer editor (also 
                        installed under /Developer/Applications), by selecting it 
                        from the Library - Plugin panel.

                        This plug-in requires the query and the database path in 
                        the input ports. The results are returned in the output 
                        port "Result Structure".

Installation                    n/a

Changes from Previous Versions          n/a

Feedback and Bug Reports            Please send all feedback about this sample to:
                        http://developer.apple.com/contact/feedback.html

                        Please submit any bug reports about this example to 
                        http://developer.apple.com/bugreport
```

[Next](SQLiteQueryPlugIn.h.md)[Previous](Quartz%20Composer%20SQLiteQuery.md)

