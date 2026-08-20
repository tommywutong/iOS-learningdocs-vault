---
title: Date and Time Programming Guide for Core Foundation
apple_id: 10000125i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2005-08-11'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDatesAndTimes/Concepts/TimeZones.html
archived_at: '2026-07-15T07:22:18.152984Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Date and Time Programming Guide for Core Foundation](Introduction%20to%20Dates%20and%20Times%20Programming%20Guide%20for%20Core%20Foundation.md)


[Next](Using%20Dates.md)[Previous](Date%20Representations.md)

# Time Zones

CFDate objects are all expressed as Greenwich
Mean Time, or GMT. In order to convert a GMT date to your local
time you must use a CFTimeZone object. A CFTimeZone represents a
geopolitical region that has some temporal offset, either plus or
minus, from GMT as well as an abbreviation—such as “PST”.
In addition to familiar abbreviations, time zones are also named
by country and region. For example the United States spans these times
zones:

- USA Eastern: -5 hours GMT
- USA Indiana East: -5 hours GMT
- USA Central: -6 hours GMT
- USA Mountain: -7 hours GMT
- USA Arizona: -7 hours GMT
- USA Pacific: -8 hours GMT
- USA Alaska: -9 hours GMT
- USA Aleutian: -10 hours GMT
- USA Hawaii: -10 hours GMT

To make matters even more complex, any region may or may not
be on Daylight Savings Time (DST).

In order to properly convert GMT to local time, you have to
know which time zone you are in and if DST is in effect. Core Foundation
uses time zone names, abbreviations, GMT offset, and DST information
for a particular time zone obtained from a public-domain database
maintained at `ftp://elsie.nci.nih.gov//pub/`.
This database contains information representing the history of local
time for many representative locations around the globe. The database
is updated periodically to reflect changes made to GMT offsets and
daylight-saving rules by political entities.

For examples of how to use CFDate and CFTimeZone, see the [Using Dates](Using%20Dates.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge2dclkdjjbekscbifdq).

[Next](Using%20Dates.md)[Previous](Date%20Representations.md)

