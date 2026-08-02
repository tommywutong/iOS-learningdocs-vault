---
title: Carbon Event Manager Programming Guide
apple_id: TP30000989
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Carbon_Event_Manager/Glossary/CarbonEventsGloss.html
archived_at: '2026-07-15T05:22:33.363513Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Carbon Event Manager Programming Guide](Introduction%20to%20Carbon%20Event%20Manager%20Programming%20Guide.md)


[Next](Index.md)[Previous](Control%20Events%20Versus%20Classic%20Control%20Messages.md)

# Glossary

- __blocked__

  The state where an application or thread is waiting for some event or action to occur. While blocked, that particular code path uses no processor time.

- __Classic Event Manager__

  The event handling interface used in Mac OS applications before the Carbon Event Manager. The Classic Event Manager often required a certain amount of polling of the event queue.

- __containment hierarchy__

  A hierarchy of event targets that determines which handler is to be called to process an event. Events are initially sent to the innermost (or lowest) relevant target in the hierarchy. If the handler associated with that event target does not handle the event (or if no handler exists), then the event is propagated to the next target in the hierarchy. If no handler in the hierarchy processes the event, the default handler is called.

- __event__

  A constant that notifies an application that some action is occurring, or has occurred.

- __event class__

  The general category an event belongs to, typically associated with an particular action or user-interface element. Example classes are window events and volume events. Compare [event kind](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqg4wueqkci5beir2k).

- __event handler__

  A callback procedure that processes one or more events.

- __event kind__

  A specific type of event within an event class (for example, a mouse-down event). Compare [event class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqg4wueqkcinceircb).

- __event loop__

  In the Carbon Event Manager, an execution loop that obtains events from the Window Server and places them in an event queue. The event loop also fires timers.

- __event queue__

  A first-in-first-out stack where events pertaining to a thread are stored. Each preemptively-scheduled thread has its own event queue.

- __event target__

  An object to which an event is sent. An event target is typically a user-interface element, such as a control or a window.

- __event timer__

  A timer mechanism that fires once, or at periodic intervals, calling a callback procedure when doing so.

- __event type__

  The combination of event class and event kind that uniquely identifies an event to the Carbon Event Manager. _See also_[event class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqg4wueqkcinceircb), [event kind](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqg4wueqkci5beir2k).

- __main event loop__

  The code loop where the application spends most of its time. The application is blocked while waiting for events. When an event occurs, the application processes it and then returns to the blocked state.

- __one-shot timer__

  A Carbon event timer that fires only once. _See also_[event timer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqg4wueqkcineumrkk).

- __peek__

  To examine an event in an event queue (obtaining its class, kind, parameters and so on) without removing it from the queue. Compare [pull](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqg4wueqkcjfdugq2e).

- __pull__

  To remove an event from an event queue. Compare [peek](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqg4wueqkcirbekqsj).

- __queue-synchronized state__

  The state of an input device accordiing to the events that have been dispatched from the event queue. This state may differ from the actual physical state of the input device.

- __standard event handler__

  The event handler that processes an event if the application did not install one for it.

- __standard toolbox dispatcher__

  In the Carbon Event Manager, the default event target for events when running under `RunApplicationEventLoop`. Events sent to the standard toolbox dispatcher are automatically routed to the appropriate event targets.

- __timer__

  _See_[event timer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqg4wueqkcineumrkk).

- __toolbox dispatcher__

  _See_[standard toolbox dispatcher](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqg4wueqkcjbfeoskj).

- __universal procedure pointer (UPP)__

  A generalized procedure pointer that allows code with different calling conventions to call each other. Some Carbon functions require you to pass UPPs for callbacks because the calling routine doesn't know in advance if your code is Mach-O based or CFM-based.

- __user focus__

  The window or text field control to which keyboard input is directed. The user can change the user focus by using the mouse or (sometimes) the Tab key.

- __user focus event target__

  Events sent to this target are automatically sent to the event target that has the current user focus. You can also install a handler on this target to intercept events before they get sent to the current user focus.

- __WaitNextEvent__

  The function that drove the event loop in older versions of the Mac OS. _See also_[Classic Event Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqg4wueqkcjjbecqkg).

[Next](Index.md)[Previous](Control%20Events%20Versus%20Classic%20Control%20Messages.md)

