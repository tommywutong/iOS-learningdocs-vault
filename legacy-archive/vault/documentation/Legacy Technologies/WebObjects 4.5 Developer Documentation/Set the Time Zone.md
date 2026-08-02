---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.f.html
archived_at: '2026-07-15T08:09:50.921561Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Solaris%20Post-Installation%20Steps.md) [!](Setting%20the%20LDLIBRARYPATH.md) [!](Install%20the%20Java%20Native%20Threads%20Pack.md)

---

#   Set the Time Zone

As part of the installation process, you're told how to manually set the time zone. If you haven't yet done so, you should do it now. The instructions for setting the time zone are repeated here:

Certain WebObjects APIs depend upon this system's local time zone being set. To set the local time zone:

1. 

   `su' to root.
2. 

   `cd' to
   /usr/share/lib/zoneinfo
3. 

   Create the symbolic link
   localtime
   which points to the appropriate time zone. For example:
   ln -s US/Pacific localtime

Note that creating a symbol link isn't your only option for setting the system time zone. The algorithm that the
systemTimeZone
method (in the NSTimeZone class) uses to determine the time zone is as follows:

1. 

   systemTimeZone
   first checks for an environment variable named "TZFILE". If it exists and its value is a path to a valid time zone file,
   systemTimeZone
   returns the indicated time zone. If the environment variable doesn't exist, or the path is nonexistent or otherwise invalid, proceed to the next step.
2. 

   systemTimeZone
   next checks the "TZ" environment variable. If it exists and its value, when used as a path relative to
   /usr/share/lib/zoneinfo,
   indicates a valid time zone file,
   systemTimeZone
   returns the indicated time zone. If the "TZ" environment variable doesn't exist or doesn't identify a valid time zone file, proceed to the next step.
3. 

   systemTimeZone
   finally checks for the existence of a "localtime" symbolic link within
   /usr/share/lib/zoneinfo
   . If the link doesn't exist or doesn't point to a valid time zone file, NSTimeZone throws an exception and sets the time zone to GMT. Otherwise, the indicated time zone is returned from
   systemTimeZone
   .

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Solaris%20Post-Installation%20Steps.md) [!](Setting%20the%20LDLIBRARYPATH.md) [!](Install%20the%20Java%20Native%20Threads%20Pack.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
