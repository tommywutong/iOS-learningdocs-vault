---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-45.html
archived_at: '2026-07-15T08:05:01.417866Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Administrative%20Tasks.md) [!](Improving%20Performance.md) [!](Load%20Balancing.md)

---

# Automatic Scheduling

You can use Monitor to start and stop instances automatically at regular intervals. Typically, WebObjects applications can run for long periods of time, even months. If your application caches data or has memory leaks, you can schedule it to recycle its instances without interrupting service to your customers.

Use the Scheduling form of the Application Configuration page to configure a pool of instances. This form allows you establish a staggered schedule for stopping and restarting the instances. Here is an example of the Scheduling Instances form:

!

Either specify the instance lifespan or the frequency of shutdown (both in minutes) and then click the appropriate Use Option button. Each instance runs for a specified period before it begins refusing new sessions, and then it shuts down when the minimum active session threshold is reached. The diagram below displays an example schedule for four instances.

!

Do not set the frequency of shutdowns too low. If the session time-out for your application is 30 minutes, then the frequency of application shutdowns should not be less than 30 minutes. It should probably be several times higher than that. These settings are configurable because each application may have different needs.

You can also schedule instances individually with the Scheduling option of the Instance Configuration page (to go to this page, click Config next to an instance on the Detail View page):

!

Specify the start date (in the recommended format) and the lifespan of the instance in minutes, then click Save Changes

If you have set up scheduling for an application and then add a new instance, the new instance does not have a schedule that is synchronized with the other instances. To insert this new instance into the schedule you need to go to the Application Configuration page and reset the schedule, or you must manually create the schedule in the Instance's Configuration page.

You can programmatically set up an application to shut down in addition to scheduling shutdowns using the Monitor. If you want to use internal scheduling algorithms in your instance, it is not recommended that you also use Monitor's scheduling features. Instead, just use Monitor to recover failures of your instances and to access statistics.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Administrative%20Tasks.md) [!](Improving%20Performance.md) [!](Load%20Balancing.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
