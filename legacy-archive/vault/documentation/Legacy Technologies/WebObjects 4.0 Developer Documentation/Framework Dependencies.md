---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/EOFClasses5.html
archived_at: '2026-07-18T01:19:38.741673Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](Enterprise%20Objects%20Framework%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](Classes%20in%20a%20Web%20Application%20with%20a%20Java%20Client.md)

# Framework Dependencies

The architectural depictions of Enterprise Objects Framework in the previous sections present the ordering of the Framework components in terms of the conceptual data flow in the system. Another way to look at Enterprise Objects Framework is in terms of the structural dependencies of the components on one another.
[Figure 19](#apple-geydinbr) shows the relationships between the Framework's Objective-C frameworks (and also for the corresponding Java versions).

!

Figure 19. Objective-C Framework Dependencies

The control layer is the lowest layer in the Framework. It can be thought of as an extension of Foundation in that it defines generic core functionality, such as key-value access and object change notification. The control layer centers around EOEditingContext, a subclass of EOObjectStore that manages enterprise objects in memory.
The access layer extends the control layer by implementing an EOObjectStore for relational databases, EODatabaseContext. WebObjects framework too depends on EOControl, because it provides an EOEditingContext with each WOSession object.
The interface layer extends the control layer and the Application Kit by adding bindings between enterprise objects and the user interface. This keeps the values of enterprise objects in sync with their display in the user interface.
Each concrete adaptor (ODBCAdaptor and OracleAdaptor, for example) extends the access layer by implementing concrete subclasses of the access layer's adaptor level classes (EOAdaptor, EOAdaptorContext, and EOAdaptorChannel).
Finally, the server-side EOJavaClient framework extends WebObjects by providing a WOComponent for displaying Java interfaces.
[Figure 20](#apple-geydinjv) shows the relationships between the Framework's pure Java packages (for writing Java client applications).

!

Figure 20. Java Package Dependencies

Again the control layer is the lowest layer in the Framework. The interface layer extends the control layer and Swing (the presentation layer of Sun's JDK). Finally, the distribution layer extends the control layer by implementing an EOObjectStore for communicating to an application server through a channel.
[!Table of Contents](Enterprise%20Objects%20Framework%20Viewed%20Through%20Its%20Classes.md) [!Next Section](Designing%20Enterprise%20Objects.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
