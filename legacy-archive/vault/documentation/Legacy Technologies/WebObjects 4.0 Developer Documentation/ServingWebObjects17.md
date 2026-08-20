---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects17.html
archived_at: '2026-07-18T01:23:38.551627Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects16.md)

### Instance Configuration Options

With the options of the Instance Configuration page you can override global application settings for particular instances.
__To Access__: From the Detail View for an application, click the Config button next to the desired instance.

##### Application Start-Up / Command Line Arguments

This section allows you to change the command-line arguments that are used when the instance is started. See "[Setting Command-Line Arguments in Monitor](ServingWebObjects22.md#apple-gy3tmoa)" for details.

For convenience, the entire set of command-line arguments passed to the instance are displayed in the blue box at the bottom of this section.

##### Graceful Shutdown

This section allows you to change the minimum active session threshold for an instance. This threshold is used when the instance begins refusing new sessions. The default is zero. If your application is usually under heavy traffic, you might not want to wait for all sessions to time-out before terminating the application.

##### Scheduling

This section allows you to configure the scheduling settings for a given instance. Normally you should use the Application level scheduling to create a staggered schedule of starting and stopping instances. Use the instance-specific section to create your own schedule intervals. See "[Automatic Scheduling](ServingWebObjects30.md#apple-guytana)" for the scheduling procedure.

Monitor computes from the desired instance lifespan or from the desired instance downtime a series of shutdown dates The scheduling algorithm causes the instance to begin refusing new sessions on regular intervals based on these two variables.

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](Administrative%20Tasks.md)
