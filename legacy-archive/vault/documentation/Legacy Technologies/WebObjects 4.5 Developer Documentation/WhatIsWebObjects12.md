---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WhatIsWebObjects12.html
archived_at: '2026-07-15T08:06:40.710495Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Previous Section](WhatIsWebObjects11.md)

### Code or Script File

You use the _code file_ to define your component's attributes and actions. The attributes are called _instance variables_, and the actions are called _methods_. Files containing your code can be found in Project Builder's Classes suitcase, as previously discussed.
Action Methods
Your component code contains _action methods_. An action method is a method you associate with a user action-for instance, clicking a submit button or a hyperlink. There are two types of action methods you can implement: those for _component action_ requests and those for _direct action_ requests.

- Elements bound to a component action pass the action message to the session object and on to the request component. State is restored by the session object.
- Elements bound to a direct action send their action message directly to the object that can handle it. Direct actions aren't required to use session objects and thus can be stateless.

Your components can contain a mix of direct and component actions.
For a more detailed discussion of action methods, see ["Action Methods"](Action%20Methods.md#apple-g44daoa).

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Next Section](WhatIsWebObjects13.md)
