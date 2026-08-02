---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/DeltaDoc/NewInEOF3.01.html
archived_at: '2026-07-15T07:57:52.070347Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in EOF 3.0](Table%20of%20Contents-2.md)

[!Table of Contents](Table%20of%20Contents-2.md) [!Previous Section](What%27s%20New%20in%20Enterprise%20Objects%20Framework%203.0.md)

# Compatibility With Earlier Releases

Enterprise Objects Framework 3.0 is backward compatible with Enterprise Objects Framework 2.2; however, you must keep in mind the following:

- Release 3.0 is the first release of Enterprise Objects Framework that runs on Rhapsody and on Yellow Box for Windows NT. It does not run on OpenStep 4.2. Because of this change, the locations of Enterprise Objects Framework files have changed (see the section "[File Location Changes](File%20Location%20Changes-2.md#apple-ge4dqnbr)").
- The file location changes require some changes to your Project Builder projects.
- Yellow Box uses a different version of the Java-wrapped APIs. The package names, class names, and some method names have changed. There is a script to help you convert your Java code.

If you have an existing application that uses both WebObjects and Enterprise Objects Framework (or that uses any of the Java APIs) and if you want to convert that application to the latest release, see the section "Converting an Existing WebObjects Application" in the document "[What's New in WebObjects 4.0](What%27s%20New%20in%20WebObjects%204.0.md)".

If you want to convert an application that doesn't use WebObjects, all you need to do is convert the project in Project Builder so that it points to the new locations for build tools. On Rhapsody systems, see the online document __/System/Developer/Makefiles/Conversion/DirectoryLayout/ConvertMakefilesReadMe.rtf__. On NT, see __NEXT_ROOT/Developer/Makefiles/Conversion/DirectoryLayout/ConvertMakefilesReadMe.rtf__.

[!Table of Contents](Table%20of%20Contents-2.md) [!Next Section](File%20Location%20Changes-2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
